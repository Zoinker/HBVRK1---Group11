# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 21:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_remove_driver_dumdum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='user',
        ),
    ]
