# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-11 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_line', '0008_auto_20180911_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vessel',
            old_name='_loa',
            new_name='vessel_loa',
        ),
    ]
