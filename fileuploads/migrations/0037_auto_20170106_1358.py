# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2017-01-06 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20161209_2103'),
        ('fileuploads', '0036_auto_20170106_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='results',
        ),
        migrations.AddField(
            model_name='video',
            name='processes',
            field=models.ManyToManyField(to='groups.Process'),
        ),
    ]
