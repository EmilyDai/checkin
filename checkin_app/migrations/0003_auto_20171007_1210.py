# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_app', '0002_auto_20171007_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
