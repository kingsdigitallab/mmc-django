# Generated by Django 3.2.8 on 2021-10-14 15:43

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.contrib.routable_page.models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("wagtailimages", "0023_add_choose_permissions"),
        ("taggit", "0003_taggeditem_add_unique_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ]
                    ),
                ),
                ("date", models.DateField()),
                (
                    "feed_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="Entity",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ],
                        verbose_name="Description",
                    ),
                ),
                (
                    "creator_text",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        verbose_name="Author/Creator (Text)",
                    ),
                ),
                (
                    "subtype",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        verbose_name="Category/Role",
                    ),
                ),
                (
                    "date_from",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="Date 1"
                    ),
                ),
                (
                    "date_to",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="Date 2"
                    ),
                ),
                (
                    "date_mozart",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        verbose_name="Date related to mozart",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=256, null=True, verbose_name="Location"
                    ),
                ),
                (
                    "sublocation",
                    models.CharField(
                        blank=True,
                        max_length=256,
                        null=True,
                        verbose_name="Sublocation",
                    ),
                ),
                (
                    "location_mozart",
                    models.CharField(
                        blank=True,
                        max_length=256,
                        null=True,
                        verbose_name="Location Related to Mozart",
                    ),
                ),
                (
                    "mozart_relevence",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                        verbose_name="Mozart Relevance",
                    ),
                ),
                (
                    "location_purchase",
                    models.CharField(
                        blank=True,
                        max_length=256,
                        null=True,
                        verbose_name="Place of Purchase",
                    ),
                ),
                (
                    "bibliog",
                    models.TextField(
                        blank=True, null=True, verbose_name="Bibliographic Reference"
                    ),
                ),
                (
                    "comments",
                    models.TextField(blank=True, null=True, verbose_name="Comments"),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="entity_creator",
                        to="cms.entity",
                        verbose_name="Author/Creator",
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="entity_recipient",
                        to="cms.entity",
                        verbose_name="Recipient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Entity",
                "verbose_name_plural": "Entities",
                "ordering": ["title"],
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="EntityIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="EntityType",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ]
                    ),
                ),
                (
                    "colour",
                    models.CharField(
                        help_text="You            can use the following colours:            purple, lightgreen, darkgreen, orange,            lightblue, darkblue, teal, yellow, lightgray            pink, red.",
                        max_length=128,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="IndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="ObjectIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="RichTextPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="ObjectPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ]
                    ),
                ),
                ("homepage_text", models.TextField(blank=True, null=True)),
                (
                    "homepage_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="pilcrow", required=False
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail.core.blocks.RichTextBlock(
                                    icon="openquote", required=False
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    required=False
                                ),
                            ),
                            (
                                "footnote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("numeral", wagtail.core.blocks.TextBlock()),
                                        ("reference", wagtail.core.blocks.TextBlock()),
                                    ],
                                    required=False,
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(
                                    icon="doc-full-inverse", required=False
                                ),
                            ),
                        ]
                    ),
                ),
                (
                    "mozart_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="EntityThrough",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="throughentity",
                        to="cms.entity",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="throughpage",
                        to="wagtailcore.page",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BlogPostTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="cms.blogpost",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cms_blogposttag_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="blogpost",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="cms.BlogPostTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
