# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-28 10:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20170728_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 6, 6, 36, 3099)),
        ),
    ]
