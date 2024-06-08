# Generated by Django 5.0.6 on 2024-06-08 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant_info', '0011_alter_applicantinfo_status'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='applicant_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='applicant_info.applicantinfo'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
