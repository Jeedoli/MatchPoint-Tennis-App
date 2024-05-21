from django.utils.timezone import now
from rest_framework import serializers
from .models import Competition
from applicant_info.models import ApplicantInfo
from matchtype.serializers import MatchTypeSerializer
from image_url.serializers import ImageUrlSerializer




''' 대회 부분 '''

## 대회 리스트 조회
class CompetitionListSerializer(serializers.ModelSerializer):
    match_type_details = MatchTypeSerializer(source='match_type', read_only=True)
    image_url = serializers.SerializerMethodField()
    tier = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    waiting_count = serializers.SerializerMethodField()
    class Meta:
        model = Competition
        fields = ['id', 'name', 'start_date', 'end_date', 'match_type_details', 'tier', 'location', 'image_url', 'status', 'waiting_count']
        
    def get_image_url(self, obj):
        if obj.image_url:
            return obj.image_url.image_url
        return None

    def get_tier(self, obj):
        if obj.tier:
            return obj.tier.name
        return None
    
    def get_status(self, obj):
        user = self.context['request'].user
        current_applicants_count = obj.applicants.count()
        is_waiting = current_applicants_count >= obj.max_participants
        
        if obj.status == 'before' and not user.is_authenticated or user.gender != obj.match_type.gender or user.tier != obj.tier:
            return '신청 불가능'
        elif obj.status == 'before' and user.is_authenticated and current_applicants_count >= obj.max_participants:
            return '대기 가능'
        elif obj.status == 'before' and user.is_authenticated:
            return '신청 가능'
        elif obj.status == 'during':
            return '대회 진행중'
        else:
            return '대회 종료'
        
    def get_waiting_count(self, obj):
        current_applicants_count = obj.applicants.count()
        return current_applicants_count



## 대회 상세조회
class CompetitionSerializer(serializers.ModelSerializer):
    match_type_details = MatchTypeSerializer(source='match_type', read_only=True)
    image_url = serializers.SerializerMethodField()
    tier = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    waiting_count = serializers.SerializerMethodField()

    class Meta:
        model = Competition
        fields = ['id', 'name', 'start_date', 'tier', 'match_type_details', 'round', 'location', 'address', 
                  'description', 'rule', 'code', 'phone', 'site_link', 'feedback',
                  'image_url', 'status', 'is_waiting', 'waiting_count']
    
    
    def get_image_url(self, obj):
        if obj.image_url:
            return obj.image_url.image_url
        return None
    
    def get_tier(self, obj):
        if obj.tier:
            return obj.tier.name
        return None
    
    def get_status(self, obj):
        user = self.context['request'].user
        current_applicants_count = obj.applicants.count()
        is_waiting = current_applicants_count >= obj.max_participants
        
        if obj.status == 'before' and not user.is_authenticated or user.gender != obj.match_type.gender or user.tier != obj.tier:
            return '신청 불가능'
        elif obj.status == 'before' and user.is_authenticated and current_applicants_count >= obj.max_participants:
            return '대기 가능'
        elif obj.status == 'before' and user.is_authenticated:
            return '신청 가능'
        elif obj.status == 'during':
            return '대회 진행중'
        else:
            return '대회 종료'
        


## 대회신청 시리얼라이저 ##        
class CompetitionApplyInfoSerializer(serializers.ModelSerializer):
    match_type_details = MatchTypeSerializer(source='match_type', read_only=True)
    tier = serializers.SerializerMethodField()
    
    class Meta:
        model = Competition
        fields = ['id', 'name', 'start_date', 'match_type_details', 'tier', 'round', 'location', 'address', 'bank_account_name', 
                  'bank_name', 'bank_account_number', 'fee', 'deposit_refund_policy'
                  ]
        
        
    def get_tier(self, obj):
        if obj.tier:
            return obj.tier.name
        return None