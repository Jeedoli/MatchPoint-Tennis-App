import re
from rest_framework import serializers
from applicant.models import Applicant
from applicant_info.models import ApplicantInfo, TeamApplicantInfo
from competition.models import Competition, CompetitionTeamMatch
from matchtype.models import MatchType
from participant.models import Participant
from participant_info.models import ParticipantInfo, TeamParticipantInfo
from point.models import Point
from team.models import Team
from tier.models import Tier
from users.models import CustomUser
from match.models import Match
from set.models import Set


class CompetitionListSerializer(serializers.ModelSerializer):
    tier = serializers.SerializerMethodField()
    match_type = serializers.SerializerMethodField()

    class Meta:
        model = Competition
        fields = ('id', 'name', 'tier', 'match_type', 'start_date', 'status', 'competition_type',
                  'total_rounds', 'location', 'phone', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at', 'status')
        ref_name = "CustomAdminCompetitionList"

    def get_tier(self, obj):
        return {'id': obj.tier.id, 'name': obj.tier.name} if obj.tier else None

    def get_match_type(self, obj):
        return {'id': obj.match_type.id,
                'gender': obj.match_type.gender,
                'type': obj.match_type.type} if obj.match_type else None


class TeamGameSerializer(serializers.Serializer):
    tier_id = serializers.IntegerField(required=False)
    match_type_id = serializers.IntegerField(required=False)


class TeamMatchListSerializer(serializers.ModelSerializer):
    tier = serializers.SerializerMethodField()
    match_type = serializers.SerializerMethodField()

    class Meta:
        model = CompetitionTeamMatch
        fields = ('id', 'tier', 'match_type', 'game_number')
        read_only_fields = ('id', 'tier', 'match_type', 'game_number')

    def get_tier(self, obj):
        return {'id': obj.tier.id, 'name': obj.tier.name} if obj.tier else None

    def get_match_type(self, obj):
        return {'id': obj.match_type.id,
                'gender': obj.match_type.gender,
                'type': obj.match_type.type} if obj.match_type else None


class CompetitionSerializer(serializers.ModelSerializer):
    tier = serializers.SerializerMethodField()
    tier_id = serializers.PrimaryKeyRelatedField(
        queryset=Tier.objects.all(), write_only=True, source='tier', required=False)
    match_type = serializers.SerializerMethodField()
    match_type_id = serializers.PrimaryKeyRelatedField(
        queryset=MatchType.objects.all(), write_only=True, source='match_type')
    image_file = serializers.ImageField(write_only=True, required=False)
    image_url = serializers.SerializerMethodField(read_only=True)
    delete_image = serializers.BooleanField(
        write_only=True, required=False, default=False)
    team_games = TeamGameSerializer(many=True, write_only=True, required=False)
    team_match_list = TeamMatchListSerializer(
        read_only=True, many=True)

    def get_image_url(self, obj):
        return obj.image_url.image_url if obj.image_url else None

    def get_tier(self, obj):
        return {'id': obj.tier.id, 'name': obj.tier.name} if obj.tier else None

    def get_match_type(self, obj):
        return {'id': obj.match_type.id,
                'gender': obj.match_type.gender,
                'type': obj.match_type.type} if obj.match_type else None

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        team_games_data = []
        team_games_pattern = re.compile(r'^team_games\[(\d+)\]\[(\w+)\]$')

        for key, value in data.items():
            match = team_games_pattern.match(key)
            if match:
                index, field = match.groups()
                index = int(index)
                while len(team_games_data) <= index:
                    team_games_data.append({})
                team_games_data[index][field] = value

        internal_value['team_games'] = team_games_data
        return internal_value

    class Meta:
        model = Competition
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'status',
                  'total_rounds', 'total_sets', 'rule', 'address', 'location', 'code',
                  'phone', 'fee', 'bank_name', 'bank_account_number', 'bank_account_name',
                  'site_link', 'image_file', 'image_url', 'match_type', 'match_type_id',
                  'tier', 'tier_id', 'max_participants', 'competition_type', 'team_games',
                  'team_total_games', 'team_match_list', 'created_at', 'updated_at', 'delete_image')
        read_only_fields = ('id', 'created_at', 'updated_at', 'status', 'code')
        extra_kwargs = {
            'description': {'required': False, 'allow_blank': True},
            'end_date': {'required': False},
            'total_rounds': {'required': False},
            'rule': {'required': False, 'allow_blank': True},
            'address': {'required': False, 'allow_blank': True},
            'location': {'required': False, 'allow_blank': True},
            'phone': {'required': False, 'allow_blank': True},
            'fee': {'required': False},
            'bank_name': {'required': False, 'allow_blank': True},
            'bank_account_number': {'required': False, 'allow_blank': True},
            'bank_account_name': {'required': False, 'allow_blank': True},
            'site_link': {'required': False, 'allow_blank': True},
            'max_participants': {'required': False},
            'delete_image': {'write_only': True},
            'tier': {'required': False},
            'tier_id': {'required': False},
            'team_total_games': {'required': False},
        }


class CompetitionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')


class ApplicantSerializer(serializers.ModelSerializer):
    user = CompetitionUserSerializer(read_only=True)

    class Meta:
        model = Applicant
        fields = ['user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation['user']


class CompetitionTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class ApplicantInfoSerializer(serializers.ModelSerializer):
    applicants = ApplicantSerializer(many=True, read_only=True)
    has_payment = serializers.BooleanField()
    has_refund = serializers.BooleanField()

    class Meta:
        model = ApplicantInfo
        fields = ('id', 'status', 'expired_date',
                  'competition', 'waiting_number', 'applicants', 'created_at', 'updated_at', 'has_payment', 'has_refund')
        read_only_fields = ('id', 'waiting_number',
                            'competition', 'expired_date', 'status', 'applicants', 'created_at', 'updated_at')
        extra_kwargs = {
            'expired_date': {'required': False},
            'waiting_number': {'required': False},
        }


class TeamApplicantInfoSerializer(serializers.ModelSerializer):
    team = CompetitionTeamSerializer(read_only=True)
    has_payment = serializers.BooleanField()
    has_refund = serializers.BooleanField()

    class Meta:
        model = TeamApplicantInfo
        fields = ('id', 'status', 'expired_date',
                  'competition', 'waiting_number', 'team', 'created_at', 'updated_at', 'has_payment', 'has_refund')
        read_only_fields = ('id', 'waiting_number',
                            'competition', 'expired_date', 'status', 'team', 'created_at', 'updated_at', 'has_payment', 'has_refund')


class ParticipantSerializer(serializers.ModelSerializer):
    user = CompetitionUserSerializer()

    class Meta:
        model = Participant
        fields = ['user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation['user']


class ParticipantInfoSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = ParticipantInfo
        fields = ('id', 'participants', 'competition',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'competition', 'participants',
                            'created_at', 'updated_at')


class TeamParticipantInfoSerializer(serializers.ModelSerializer):
    team = CompetitionTeamSerializer(read_only=True)

    class Meta:
        model = TeamParticipantInfo
        fields = ('id', 'team', 'competition',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'competition', 'team',
                            'created_at', 'updated_at')


class ParticipantInfoSimpleSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = ParticipantInfo
        fields = ('id', 'participants')


class MatchSerializer(serializers.ModelSerializer):
    a_team = ParticipantInfoSimpleSerializer(read_only=True)
    b_team = ParticipantInfoSimpleSerializer(read_only=True)

    a_team_id = serializers.PrimaryKeyRelatedField(
        queryset=ParticipantInfo.objects.all(), write_only=True, source='a_team', required=False)
    b_team_id = serializers.PrimaryKeyRelatedField(
        queryset=ParticipantInfo.objects.all(), write_only=True, source='b_team', required=False)
    winner = serializers.PrimaryKeyRelatedField(
        queryset=ParticipantInfo.objects.all(), write_only=True, source='winner_id', required=False)

    class Meta:
        model = Match
        fields = ('id', 'match_round', 'match_number', 'court_number', 'description', 'total_sets',
                  'winner_id', 'competition', 'a_team', 'b_team', 'created_at', 'updated_at',
                  'a_team_id', 'b_team_id', 'winner')
        read_only_fields = ('id', 'created_at', 'updated_at')
        extra_kwargs = {
            'description': {'required': False, 'allow_blank': True},
            'winner_id': {'required': False},
            'a_team': {'required': False},
            'b_team': {'required': False},
            'match_round': {'required': False},
            'match_number': {'required': False},
            'court_number': {'required': False},
        }


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ['id', 'set_number', 'a_score', 'b_score']
        read_only_fields = ('id',)


class MatchResultSerializer(serializers.ModelSerializer):
    a_team = ParticipantInfoSimpleSerializer(read_only=True)
    b_team = ParticipantInfoSimpleSerializer(read_only=True)
    sets = SetSerializer(many=True, read_only=True, source='set_list')
    competition = CompetitionListSerializer(read_only=True)
    has_point = serializers.SerializerMethodField(read_only=True)

    a_team_id = serializers.PrimaryKeyRelatedField(
        queryset=ParticipantInfo.objects.all(), write_only=True, source='a_team', required=False)
    b_team_id = serializers.PrimaryKeyRelatedField(
        queryset=ParticipantInfo.objects.all(), write_only=True, source='b_team', required=False)
    winner = serializers.PrimaryKeyRelatedField(
        queryset=ParticipantInfo.objects.all(), write_only=True, source='winner_id', required=False)

    class Meta:
        model = Match
        fields = ('id', 'match_round', 'match_number', 'court_number', 'description', 'competition',
                  'winner_id', 'a_team', 'b_team', 'sets', 'total_sets', 'a_team_id', 'b_team_id', 'winner', 'has_point')
        read_only_fields = ['id']
        extra_kwargs = {
            'description': {'required': False, 'allow_blank': True},
            'winner_id': {'required': False},
            'a_team': {'required': False},
            'b_team': {'required': False},
            'match_round': {'required': False},
            'match_number': {'required': False},
            'court_number': {'required': False},
        }

    def get_has_point(self, obj):
        print('has_point', obj)
        return Point.objects.filter(match=obj).exists()


class TeamCompetitionListSerializer(serializers.ModelSerializer):
    team_match_list = TeamMatchListSerializer(read_only=True, many=True)
    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Competition
        fields = ('id', 'name', 'start_date', 'status', 'competition_type', 'team_match_list', 'address', 'description', 'total_sets',
                  'image_url', 'total_rounds', 'total_sets', 'location', 'phone', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at', 'status')

    def get_image_url(self, obj):
        return obj.image_url.image_url if obj.image_url else None


class TeamCompetitionApplicationUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()


class TeamCompetitionApplicationSerializer(serializers.Serializer):
    game_number = serializers.IntegerField()
    users = TeamCompetitionApplicationUserSerializer(many=True)


class TeamCompetitionApplySerializer(serializers.Serializer):
    applications = TeamCompetitionApplicationSerializer(many=True)
    team_id = serializers.IntegerField()
