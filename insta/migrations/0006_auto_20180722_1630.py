# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 16:30
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20180722_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pic',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]