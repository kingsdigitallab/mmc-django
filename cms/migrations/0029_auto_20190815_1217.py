# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-15 11:17
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0028_homepage_mozart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='mozart_relevence',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow', required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow', required=False)), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote', required=False)), (b'table', wagtail.contrib.table_block.blocks.TableBlock(required=False)), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())], required=False)), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))], blank=True, null=True, verbose_name='Mozart Relevance'),
        ),
    ]
