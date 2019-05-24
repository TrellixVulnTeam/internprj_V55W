# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-13 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
