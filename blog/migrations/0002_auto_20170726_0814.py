# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-26 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_create',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]