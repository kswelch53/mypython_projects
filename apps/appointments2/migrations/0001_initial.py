# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-21 17:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('time', models.TimeField()),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('user_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appts', to='appointments1.User')),
            ],
        ),
    ]
