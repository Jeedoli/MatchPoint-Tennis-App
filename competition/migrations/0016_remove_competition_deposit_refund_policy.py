# Generated by Django 5.0.6 on 2024-05-27 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0015_rename_round_competition_total_rounds_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='deposit_refund_policy',
        ),
    ]
