# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-28 11:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_auto_20170728_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 11, 17, 56, 8717, tzinfo=utc)),
        ),
    ]
