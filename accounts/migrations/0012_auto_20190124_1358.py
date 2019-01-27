# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-24 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190124_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(choices=[('BP', 'Berth Planner'), ('SA', 'Shipping Agent'), ('ADMIN', 'System Admin'), ('DM', 'Duty Manager'), ('VP', 'Vessel Planner')], default='SA', max_length=10),
        ),
    ]