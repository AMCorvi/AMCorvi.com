# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 08:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20170726_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date published',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 27, 4, 23, 48, 457856)),
        ),
    ]
