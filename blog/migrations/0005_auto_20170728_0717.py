# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-28 11:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170728_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 11, 17, 56, 5819, tzinfo=utc)),
        ),
    ]
