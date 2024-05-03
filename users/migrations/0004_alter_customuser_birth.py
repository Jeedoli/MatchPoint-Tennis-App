# Generated by Django 5.0.4 on 2024-05-03 01:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_phone_number_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2050)]),
        ),
    ]
