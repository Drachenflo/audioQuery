# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20170630_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='preset',
            field=models.CharField(default=0, max_length=1),
        ),
    ]
