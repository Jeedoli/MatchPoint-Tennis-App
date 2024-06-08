# Generated by Django 5.0.6 on 2024-06-08 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0007_remove_applicant_participant_info_and_more'),
        ('applicant_info', '0011_alter_applicantinfo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='applicant_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='applicant_info.applicantinfo'),
        ),
    ]
