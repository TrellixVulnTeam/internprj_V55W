# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-09 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0009_auto_20190205_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]