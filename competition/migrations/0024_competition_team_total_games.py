# Generated by Django 5.0.6 on 2024-06-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0023_competitionteammatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='team_total_games',
            field=models.IntegerField(blank=True, help_text='팀 시합 경기수', null=True),
        ),
    ]
