# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 10:10
from __future__ import unicode_literals

import cms.models.streamfield
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('cms', '0010_auto_20170619_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock()), (b'affiliation', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'style', cms.models.streamfield.PullQuoteStyleChoiceBlock())], icon='openquote')), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
