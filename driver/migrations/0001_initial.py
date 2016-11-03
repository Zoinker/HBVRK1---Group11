# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverID', models.BigIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('isActive', models.BooleanField(default=False)),
                ('isBusy', models.BooleanField(default=False)),
                ('zones', models.CharField(max_length=1000)),
                ('phone_number', models.CharField(max_length=16)),
                ('requests', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passengerID', models.BigIntegerField()),
                ('inTown', models.BooleanField(default=True)),
                ('arrivalTime', models.DateTimeField()),
                ('status', models.CharField(default='pending', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.Zone'),
        ),
        migrations.AddField(
            model_name='request',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.Driver'),
        ),
    ]
