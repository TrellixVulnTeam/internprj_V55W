# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-03 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0004_remove_userprofile_re_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='_is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
