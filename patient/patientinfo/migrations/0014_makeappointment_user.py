# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-10 09:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patientinfo', '0013_auto_20190210_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeappointment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
