# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-10 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0011_auto_20190210_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeappointment',
            name='availabletime',
            field=models.CharField(max_length=100),
        ),
    ]
