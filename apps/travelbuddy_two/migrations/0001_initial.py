# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-07 03:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travelbuddy_one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('end_date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('plan', models.CharField(max_length=255)),
                ('joiner_id', models.ManyToManyField(related_name='jointrips', to='travelbuddy_one.User')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='travelbuddy_one.User')),
            ],
        ),
    ]
