from django.http import Http404
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, parsers
from rest_framework_simplejwt.views import TokenObtainPairView
from djangorestframework_camel_case.parser import CamelCaseFormParser, CamelCaseMultiPartParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import (CreateUserSerializer,
                          PhoneCheckSerializer,
                          CustomTokenObtainPairSerializer,
                          UserInfoSerializer,
                          UpdateMyProfileSerializer,
                          ChangePasswordSerializer,
) 


User = get_user_model()


# 회원가입 view ##
class CreateUserView(APIView):
    """
    회원가입 API
    """
    parser_classes = (CamelCaseFormParser, CamelCaseMultiPartParser) 
    @swagger_auto_schema(
        operation_summary='유저 회원가입',
        operation_description='회원가입 API',
        request_body=CreateUserSerializer,
        responses={
            200: openapi.Response('회원가입이 완료 되었습니다'),
            400: openapi.Response('입력값을 확인해주세요')
        }
        
    )
    
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)  # request.data를 직접 사용
        
        if serializer.is_valid():
            user = serializer.save()
            token = CustomTokenObtainPairSerializer.get_token(user)  # 사용자를 위한 토큰 생성
            response = Response({
                'message': '회원가입이 완료 되었습니다',
                'access': str(token.access_token)
            }, status=status.HTTP_201_CREATED)
            
            # 생성된 리프레시 토큰을 쿠키에 설정
            response.set_cookie('refresh',value=str(token), httponly= True)
            return response

        return Response({
            'code': 400,
            'message': '입력값을 확인해주세요',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



class PhoneCheckView(APIView):
    """
    휴대폰번호 중복 확인 API
    """
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    @swagger_auto_schema(
        operation_summary='휴대폰번호 중복확인',
        operation_description='휴대폰번호 중복 확인 API',
        request_body=PhoneCheckSerializer,
        responses={
            200: openapi.Response('사용 가능한 휴대폰 번호 입니다'),
            400: openapi.Response('유효성 검사 실패', PhoneCheckSerializer)
        }
    )
    
    def post(self, request, *args, **kwargs):
        serializer = PhoneCheckSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response({
                'message': '사용 가능한 휴대폰 번호 입니다'
            }, status=status.HTTP_200_OK)
        
        return Response({
            'code': 400,
            'message': '유효성 검사 실패',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)







## 로그인 ##
class LoginView(TokenObtainPairView):
    """
    유저 로그인 API
    """
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    @swagger_auto_schema(
        operation_summary='유저 로그인',
        operation_description='유저 로그인 API',
        request_body=CustomTokenObtainPairSerializer,
        responses={
            200: openapi.Response('로그인 완료'),
            400: openapi.Response('로그인에 실패하였습니다. 전화번호와 비밀번호를 확인해 주세요')
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        res = super().post(request, *args, **kwargs)
        
        response = Response({
            "message": "로그인 완료",
            "access": str(res.data.get('access', None))
            }, status= status.HTTP_200_OK)
        
        response.set_cookie("refresh", res.data.get('refresh', None), httponly= True)
        
        return response
    
    
     
    
## 로그아웃 ##
class LogoutView(APIView):
    @swagger_auto_schema(
        operation_summary='유저 로그아웃',
        operation_description='유저 로그아웃 API',
    )
    
    def post(self, request, *args, **kwargs):
        response = Response({
            'detail': '로그아웃되었습니다'
            }, status=status.HTTP_200_OK)
        
        response.delete_cookie('refresh')
        
        return response



## 액세스 토큰 리프레시 ##
from rest_framework.permissions import AllowAny

class RefreshAccessTokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')

        if refresh_token is None:
            return Response({"error": "리프레시 토큰이 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            new_access_token = str(token.access_token)

            # 필요하다면 새 리프레시 토큰도 생성하여 반환할 수 있습니다. 
            # new_refresh_token = str(token)

            response = Response()
            response.data = {
                'access': new_access_token,
                # 'refresh': new_refresh_token,
            }

            return response
        except Exception as e:
            return Response({"error": "인증되지 않은 리프레시 토큰입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
            

class UpdateMyProfileAPIView(APIView):
    """
     내 프로필을 업데이트하는 API
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    parser_classes = (CamelCaseFormParser, CamelCaseMultiPartParser)
    @swagger_auto_schema(
        operation_summary='내 프로필 편집',
        operation_description='내 프로필을 업데이트하는 API',
        request_body=UpdateMyProfileSerializer,
        responses={
            200: openapi.Response(''),
            400: openapi.Response('')
        }
    )

    def put(self, request, format=None):
        user = request.user  # Use the currently authenticated user's information.
        serializer = UpdateMyProfileSerializer(user, data=request.data, partial=True)  # 부분 업데이트를 위해 partial=True를 추가합니다.
        if serializer.is_valid():
            serializer.save()
            # 업데이트가 성공적으로 완료되면, serializer의 데이터와 함께 200 OK 응답을 반환합니다.
            return Response(serializer.data, status=status.HTTP_200_OK)
        # 유효성 검사에 실패한 경우, 오류 메시지와 함께 400 Bad Request 응답을 반환합니다.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# 유저 비밀번호 변경 시리얼라이저
class ChangePasswordView(APIView):
    """
    유저 비밀번호 변경 api
    """
    permission_classes = [IsAuthenticated]
    
    parser_classes = (CamelCaseFormParser, CamelCaseMultiPartParser)
    @swagger_auto_schema(
        operation_summary='유저 비밀번호 변경',
        operation_description='유저 비밀번호 변경 API',
        request_body=ChangePasswordSerializer,
        responses={
            200: openapi.Response('비밀번호가 변경되었습니다'),
            400: openapi.Response('기존 비밀번호가 일치하지 않습니다')
        }
    )

    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        
     
        if serializer.is_valid():
            # 기존 비밀번호
            if not user.check_password(serializer.validated_data['prev_password']):
                return Response({'prev_password': ['기존 비밀번호가 일치하지 않습니다.']}, status=status.HTTP_400_BAD_REQUEST)
            
            # 새로운 비밀번호
            user.set_password(serializer.validated_data['changed_password'])
            user.save()
            return Response({'message': '비밀번호가 변경되었습니다.'}, status=status.HTTP_200_OK)





        
        
class UserDetailView(APIView):
    """
    유저 상세 정보를 제공하는 API
    """
    @swagger_auto_schema(
        operation_summary='유저 상세 정보 조회',
        operation_description='유저 상세 정보를 제공하는 API',
    )

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': '해당 유저가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)      
        



class MyProfileView(APIView):
    """
    로그인한 유저 정보를 제공하는 API
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary='로그인한 유저 정보 조회',
        operation_description='로그인한 유저 정보를 제공하는 API',
    )

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
        
        # request.user에는 JWT 토큰을 통해 인증된 사용자의 인스턴스가 포함되어 있습니다.
        user = request.user
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)