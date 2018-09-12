# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-09 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180909_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(choices=[('BP', 'Berth Planner'), ('SA', 'Shipping Agent'), ('ADMIN', 'System Admin')], max_length=10),
        ),
    ]