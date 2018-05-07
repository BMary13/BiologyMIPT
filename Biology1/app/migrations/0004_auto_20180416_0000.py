# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-15 21:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180415_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 0, 0, 50, 701839), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 4, 16, 0, 0, 50, 701839), verbose_name='Дата'),
        ),
    ]