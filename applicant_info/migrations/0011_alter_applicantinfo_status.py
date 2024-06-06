# Generated by Django 5.0.6 on 2024-06-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant_info', '0010_alter_applicantinfo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantinfo',
            name='status',
            field=models.CharField(choices=[('unpaid', '입금 대기'), ('pending_participation', '참가 대기중'), ('confirmed_participation', '참가 완료'), ('user_canceled', '사용자 취소'), ('admin_canceled', '관리자 취소')], default='unpaid', max_length=50),
        ),
    ]
