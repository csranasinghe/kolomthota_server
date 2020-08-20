# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-02 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('max_length', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('max_across', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('max_draft', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'verbose_name': 'berth',
                'verbose_name_plural': 'berths',
            },
        ),
    ]
