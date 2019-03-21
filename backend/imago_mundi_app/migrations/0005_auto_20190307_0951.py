# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-07 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imago_mundi_app', '0004_auto_20190219_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagomundi',
            name='place_of_origin_country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='imagomundi',
            name='place_of_origin_town',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]