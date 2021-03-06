# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 17:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passenger', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('isActive', models.BooleanField(default=False)),
                ('isBusy', models.BooleanField(default=False)),
                ('zoneFrom', models.CharField(blank=True, max_length=100)),
                ('zoneTo', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=16)),
                ('requests', models.CharField(blank=True, max_length=1000)),
                ('dumdum', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            field=models.ManyToManyField(to='driver.Driver'),
        ),
        migrations.AddField(
            model_name='request',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passenger.Passenger'),
        ),
    ]
