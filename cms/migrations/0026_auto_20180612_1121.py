# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-12 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0025_auto_20180501_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitytype',
            name='colour',
            field=models.CharField(help_text='You            can use the following colours:            purple, lightgreen, darkgreen, orange,            lightblue, darkblue, teal, yellow, lightgray            pink, red.', max_length=128),
        ),
    ]