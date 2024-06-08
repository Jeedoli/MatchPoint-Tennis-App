# Generated by Django 5.0.6 on 2024-06-07 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applicant_info', '0011_alter_applicantinfo_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('applicant_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='applicant_info.applicantinfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('refund_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='refund', to='payments.payment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
