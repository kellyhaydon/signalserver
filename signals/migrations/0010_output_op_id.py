# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-08-22 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0009_signal_frame_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='op_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
