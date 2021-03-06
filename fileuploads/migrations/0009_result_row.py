# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-06-05 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploads', '0008_auto_20160604_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signal_name', models.CharField(max_length=200)),
                ('op_name', models.CharField(max_length=20)),
                ('cut_off_number', models.IntegerField(default=0)),
                ('display_order', models.IntegerField(default=0)),
                ('result_number', models.IntegerField(default=0)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileuploads.Result')),
            ],
        ),
    ]
