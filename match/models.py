from django.db import models
from core.models import TimeStampedModel, SoftDeleteModel
from competition.models import Competition
from participant_info.models import ParticipantInfo

class Match(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    matchround = models.IntegerField(db_column='matchRound', blank=True, null=True)  # Field name made lowercase.
    matchnumber = models.IntegerField(db_column='matchNumber', blank=True, null=True)  # Field name made lowercase.
    courtnumber = models.IntegerField(db_column='courtNumber', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)  
    winner_id = models.ForeignKey(ParticipantInfo, models.DO_NOTHING, related_name='winner_user', blank=True, null=True)
    competition = models.ForeignKey(Competition, models.DO_NOTHING, related_name='matches')
    a_team = models.ForeignKey(ParticipantInfo, models.DO_NOTHING, related_name='match_a_team_set', blank=True, null=True)
    b_team = models.ForeignKey(ParticipantInfo, models.DO_NOTHING, related_name='match_b_team_set', blank=True, null=True)

    class Meta: 
        db_table = 'match'