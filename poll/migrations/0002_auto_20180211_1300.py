# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-11 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pais',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
