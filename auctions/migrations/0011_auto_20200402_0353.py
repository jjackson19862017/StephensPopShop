# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-02 03:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200402_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 9, 3, 53, 12, 178654, tzinfo=utc), null=True),
        ),
    ]
