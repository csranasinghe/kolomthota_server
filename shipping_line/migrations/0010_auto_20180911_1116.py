# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-11 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_line', '0009_auto_20180911_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingline',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
