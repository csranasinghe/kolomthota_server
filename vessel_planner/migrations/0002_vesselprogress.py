# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-05 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_line', '0012_auto_20181205_1057'),
        ('vessel_planner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VesselProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis', models.IntegerField(default=0)),
                ('load', models.IntegerField(default=0)),
                ('vessel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shipping_line.VesselArrival')),
            ],
        ),
    ]
