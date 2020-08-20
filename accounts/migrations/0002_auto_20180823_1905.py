# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-23 19:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAgent',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='sa_account', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='berthplanner',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='bp_account', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
