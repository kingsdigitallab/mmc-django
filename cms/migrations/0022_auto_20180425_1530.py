# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-25 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0021_auto_20180325_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'ordering': ['title'], 'verbose_name': 'Entity', 'verbose_name_plural': 'Entities'},
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())])), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())])), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
        migrations.AlterField(
            model_name='entity',
            name='bibliog',
            field=models.TextField(blank=True, null=True, verbose_name='Bibliographic Reference'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())])), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='date_from',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Date 1'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='date_to',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Date 2'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='location_mozart',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Location                                       Related to Mozart'),
        ),
        migrations.AlterField(
            model_name='entitytype',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())])), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())])), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())])), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
        migrations.AlterField(
            model_name='objectindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())])), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
        migrations.AlterField(
            model_name='objectpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())])), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
        migrations.AlterField(
            model_name='richtextpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'pull_quote', wagtail.wagtailcore.blocks.RichTextBlock(icon='openquote')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'footnote', wagtail.wagtailcore.blocks.StructBlock([(b'numeral', wagtail.wagtailcore.blocks.TextBlock()), (b'reference', wagtail.wagtailcore.blocks.TextBlock())])), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
    ]