# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-19 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorinfo', '0010_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
