# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BatchCalculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterialname',
            name='contentAl2O3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rawmaterialname',
            name='contentSiO2',
            field=models.FloatField(),
        ),
    ]
