# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-05 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0005_auto_20161105_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='value',
            field=models.IntegerField(),
        ),
    ]