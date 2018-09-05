# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-02 03:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_shippingagent_is_active_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        )
    ]