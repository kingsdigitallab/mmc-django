# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-25 19:30


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_auto_20180325_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpage',
            name='entities',
            field=models.ManyToManyField(related_name='entities', to='wagtailcore.Page'),
        ),
    ]
