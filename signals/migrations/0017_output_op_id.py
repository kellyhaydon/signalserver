# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2017-01-12 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0016_process_file_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='op_id',
            field=models.IntegerField(default=0),
        ),
    ]
