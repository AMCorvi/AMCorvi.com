# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-28 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20170728_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]