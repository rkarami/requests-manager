# Generated by Django 2.2.17 on 2020-12-12 20:21

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrequest',
            name='response_body',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrequest',
            name='response_http_status',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(limit_value=999), django.core.validators.MinValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='request',
            name='response_body',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='response_http_status',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(limit_value=999), django.core.validators.MinValueValidator(100)]),
        ),
    ]
