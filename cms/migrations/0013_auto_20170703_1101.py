# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 10:01


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20170703_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpage',
            name='entities',
            field=models.ManyToManyField(to='cms.Entity'),
        ),
    ]
