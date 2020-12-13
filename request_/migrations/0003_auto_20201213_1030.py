# Generated by Django 2.2.17 on 2020-12-13 06:30

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_', '0002_auto_20201213_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalrequest',
            old_name='payload',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='payload',
            new_name='data',
        ),
        migrations.AddField(
            model_name='historicalrequest',
            name='params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='request',
            name='params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='historicalrequest',
            name='status',
            field=models.CharField(choices=[('INIT', 'Initial'), ('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('SUCCESSFUL', 'Successful'), ('FAILED', 'Failed'), ('CANCELED', 'Canceled')], default='INIT', max_length=10),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('INIT', 'Initial'), ('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('SUCCESSFUL', 'Successful'), ('FAILED', 'Failed'), ('CANCELED', 'Canceled')], default='INIT', max_length=10),
        ),
    ]
