from club.models import Club
from coach.models import Coach
from custom_admin.club.serializers import ApplicationSerializer, ClubListSerializer, ClubSerializer, MemberSerializer, TeamSerializer, User
from custom_admin.pagination import StandardResultsSetPagination
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action, permission_classes, authentication_classes
from custom_admin.permissions import IsAdmin, IsCoach
from custom_admin.service.club_service import ClubService
from custom_admin.service.image_service import ImageService
from rest_framework.response import Response
from django.db.models import Count, Prefetch
from club_applicant.models import ClubApplicant
from tier.models import Tier


from team.models import Team


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().select_related(
        'image_url').order_by('-created_at')
    pagination_class = StandardResultsSetPagination
    image_service = ImageService()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated or IsAdminUser or IsCoach]

    def get_serializer_class(self):
        if self.action == 'list':
            return ClubListSerializer
        return ClubSerializer

    @swagger_auto_schema(
        operation_summary='클럽 목록 조회',
        operation_description='클럽 목록을 조회합니다.',
        responses={
            200: ClubSerializer(many=True),
            401: 'Authentication Error',
            403: 'Permission Denied',
            404: 'Not Found'
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='클럽 상세 조회',
        operation_description='클럽 상세 정보를 조회합니다.',
        responses={
            200: ClubSerializer,
            401: 'Authentication Error',
            403: 'Permission Denied',
            404: 'Not Found'
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='클럽 생성',
        operation_description='클럽을 생성합니다.',
        responses={
            201: ClubSerializer,
            401: 'Authentication Error',
            403: 'Permission Denied',
            400: 'Bad Request'
        }
    )
    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_staff and user.club is not None:
            return Response({'message': '이미 관리하는 클럽이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        club = Club.objects.create(
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            address=serializer.validated_data['address'],
            phone=serializer.validated_data['phone']
        )

        if user.is_staff:
            user.club = club
            user.save()
            Coach.objects.create(club=club, user=user)

        image_data = request.data.get('image_file')
        if image_data:
            self.image_service.upload_image(club, image_data)

        return Response(ClubSerializer(club).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='클럽 수정',
        operation_description='클럽 정보를 수정합니다.',
        responses={
            200: ClubSerializer,
            401: 'Authentication Error',
            403: 'Permission Denied',
            400: 'Bad Request'
        }
    )
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        for attr, value in serializer.validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        image_data = request.data.get('image_file')
        delete_image = request.data.get('delete_image', False)

        if delete_image:
            self.image_service.delete_image(instance)

        if image_data and hasattr(image_data, 'size') and image_data.size > 0:
            self.image_service.upload_image(instance, image_data)

        return Response(ClubSerializer(instance).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='클럽 삭제',
        operation_description='클럽을 삭제합니다.',
        responses={
            204: 'No Content',
            401: 'Authentication Error',
            403: 'Permission Denied',
            404: 'Not Found'
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        method='get',
        operation_summary='팀 목록 조회',
        operation_description='클럽에 속한 팀 목록을 조회합니다.',
        responses={
            200: TeamSerializer(many=True),
            401: 'Authentication Error',
            403: 'Permission Denied',
            404: 'Not Found'
        }
    )
    @swagger_auto_schema(
        method='post',
        operation_summary='팀 생성',
        operation_description='클럽에 속한 팀을 생성합니다.',
        request_body=TeamSerializer,
        responses={
            201: TeamSerializer,
            400: 'Bad Request',
            401: 'Authentication Error',
            403: 'Permission Denied',
        }
    )
    @action(detail=True, methods=['get', 'post'], url_name='teams', url_path='teams')
    def teams(self, request, *args, **kwargs):
        club = self.get_object()

        if request.method == 'GET':
            teams = club.teams.annotate(users_count=Count('users')).select_related(
                'image_url').all()

            return Response(TeamSerializer(teams, many=True).data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            return self._create_team(request, club)

    def _create_team(self, request, club):
        try:
            request.data['club'] = club.id
            serializer = TeamSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            team = Team.objects.create(
                name=serializer.validated_data['name'],
                club=club,
                description=serializer.validated_data['description']
            )

            image_data = request.data.get('image_file')
            if image_data:
                self.image_service.upload_image(team, image_data)

            return Response(TeamSerializer(team).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e.with_traceback())
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        method='get',
        operation_summary='멤버 목록 조회',
        operation_description='클럽에 속한 멤버 목록을 조회합니다.',
        responses={
            200: MemberSerializer(many=True),
            401: 'Authentication Error',
            403: 'Permission Denied',
            404: 'Not Found'
        }
    )
    @action(detail=True, methods=['get'], url_name='members', url_path='members')
    def members(self, request, *args, **kwargs):
        club = self.get_object()
        members = User.objects.filter(club=club).select_related('team').prefetch_related(
            Prefetch(
                'tiers', queryset=Tier.objects.select_related('match_type'))
        )
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        method='put',
        operation_summary='멤버 수정',
        operation_description='클럽 멤버의 팀과 부를 수정합니다.',
        responses={
            200: MemberSerializer,
            400: 'Bad Request',
            401: 'Authentication Error',
            403: 'Permission Denied',
        }
    )
    @action(detail=True, methods=['put'], url_name='update_member', url_path=r'members/(?P<user_id>\d+)')
    def update_member(self, request, *args, **kwargs):
        club_service = ClubService()
        try:
            user_id = kwargs.get('user_id')
            user = User.objects.get(id=user_id)
            club_service.update_member(user, request.data)
            return Response(MemberSerializer(user).data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': '멤버 정보가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        method='get',
        operation_summary='클럽 가입 신청 목록 조회',
        operation_description='클럽 가입 신청 목록을 조회합니다.',
        responses={
            200: ApplicationSerializer(many=True),
            401: 'Authentication Error',
            403: 'Permission Denied',
            404: 'Not Found'
        }
    )
    @action(detail=True, methods=['get'], url_name='applications', url_path='applications')
    def applications(self, request, *args, **kwargs):
        club = self.get_object()

        if request.method == 'GET':
            applications = club.applicants.filter(
                status='pending').select_related('user', 'club')
            return Response(ApplicationSerializer(applications, many=True).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        method='post',
        operation_summary='클럽 가입 신청 승인',
        operation_description='클럽 가입 신청을 승인합니다.',
        responses={
            200: 'Success',
            400: 'Bad Request',
            401: 'Authentication Error',
            403: 'Permission Denied',
            404: 'Not Found'
        }
    )
    @action(detail=True, methods=['post'], url_name='accept_application', url_path='applications/(?P<application_id>\d+)/accept')
    def accept_application(self, request, *args, **kwargs):
        club_service = ClubService()
        try:
            application_id = kwargs.get('application_id')
            application = ClubApplicant.objects.get(
                id=application_id, status='pending')
            club_service.accept_club_application(application)
            return Response({'detail': '가입 신청이 수락되었습니다.'}, status=status.HTTP_200_OK)
        except ClubApplicant.DoesNotExist:
            return Response({'error': '가입 신청 정보가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        method='post',
        operation_summary='클럽 가입 신청 거부',
        operation_description='클럽 가입 신청을 거부합니다.',
        responses={
            200: 'Success',
            400: 'Bad Request',
            401: 'Authentication Error',
            403: 'Permission Denied',
            404: 'Not Found'
        }
    )
    @action(detail=True, methods=['post'], url_name='reject_application', url_path='applications/(?P<application_id>\d+)/reject')
    def reject_application(self, request, *args, **kwargs):
        club_service = ClubService()
        try:
            application_id = kwargs.get('application_id')
            application = ClubApplicant.objects.get(
                id=application_id, status='pending')
            club_service.reject_club_application(application)
            return Response({'detail': '가입 신청이 거절되었습니다.'}, status=status.HTTP_200_OK)
        except ClubApplicant.DoesNotExist:
            return Response({'error': '가입 신청 정보가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
