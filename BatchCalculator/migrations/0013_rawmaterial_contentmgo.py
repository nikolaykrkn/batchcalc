# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BatchCalculator', '0012_auto_20161114_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterial',
            name='contentMgO',
            field=models.FloatField(default=0.0),
        ),
    ]