# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20170727_0427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='link_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='link_url',
            new_name='url',
        ),
        migrations.AddField(
            model_name='link',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
