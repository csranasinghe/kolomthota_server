# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-05 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180909_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(choices=[('BP', 'Berth Planner'), ('SA', 'Shipping Agent'), ('ADMIN', 'System Admin'), ('DM', 'Duty Manager'), ('VP', 'Vessel Planeer')], max_length=10),
        ),
    ]
