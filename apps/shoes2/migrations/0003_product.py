# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-26 23:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shoes1', '0001_initial'),
        ('shoes2', '0002_auto_20180226_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_posted', models.DateField(default=datetime.datetime.today)),
                ('date_bought', models.DateField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sold', models.BooleanField(default=False)),
                ('buyer_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buy_products', to='shoes1.User')),
                ('seller_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sell_products', to='shoes1.User')),
            ],
        ),
    ]
