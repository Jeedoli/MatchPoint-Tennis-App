# Generated by Django 5.0.6 on 2024-06-11 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0008_match_total_sets_alter_match_competition'),
        ('set', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='match_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='set_list', to='match.match'),
        ),
    ]
