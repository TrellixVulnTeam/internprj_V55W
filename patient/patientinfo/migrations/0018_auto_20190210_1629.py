# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-10 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0017_auto_20190210_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='end_date',
            field=models.CharField(max_length=50),
        ),
    ]
