# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 12:41
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='pic',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]