from django.db import models
from core.models import TimeStampedModel

class Team(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    club = models.ForeignKey('club.Club', models.DO_NOTHING)
    image_url = models.ForeignKey('image_url.ImageUrl', on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'team'