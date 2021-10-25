# Generated by Django 3.1.2 on 2021-10-22 15:32

import analytics.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20211022_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[analytics.validators.LessThanNowValidator()]),
        ),
    ]
