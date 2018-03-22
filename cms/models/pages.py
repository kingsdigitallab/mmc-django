from __future__ import unicode_literals

import logging

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.shortcuts import render, redirect
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                StreamFieldPanel,
                                                MultiFieldPanel,
                                                PageChooserPanel)
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from .behaviours import WithFeedImage, WithStreamField, int_to_roman

logger = logging.getLogger(__name__)


def _paginate(request, items):
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(items, settings.ITEMS_PER_PAGE)

    try:
        items = paginator.page(page)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        items = paginator.page(1)

    return items


class HomePage(Page, WithStreamField):
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = ['BlogIndexPage', 'ObjectIndexPage',
                     'EntityIndexPage', 'IndexPage',
                     'RichTextPage']


HomePage.content_panels = [
    FieldPanel('title', classname='full title'),
    StreamFieldPanel('body'),
]

HomePage.promote_panels = Page.promote_panels


class IndexPage(Page, WithStreamField):
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = ['IndexPage', 'RichTextPage']


IndexPage.content_panels = [
    FieldPanel('title', classname='full title'),
    StreamFieldPanel('body'),
]

IndexPage.promote_panels = Page.promote_panels


class RichTextPage(Page, WithStreamField):
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = []


RichTextPage.content_panels = [
    FieldPanel('title', classname='full title'),

    StreamFieldPanel('body'),
]

RichTextPage.promote_panels = Page.promote_panels


class BlogIndexPage(RoutablePageMixin, Page, WithStreamField):
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = ['BlogPost']

    @property
    def posts(self):
        posts = BlogPost.objects.live().descendant_of(self)

        posts = posts.order_by('-date')

        return posts

    @route(r'^$')
    def all_posts(self, request):
        posts = self.posts

        return render(request, self.get_template(request),
                      {'self': self, 'posts': _paginate(request, posts)})

    @route(r'^tag/(?P<tag>[\w\- ]+)/$')
    def tag(self, request, tag=None):
        if not tag:
            # Invalid tag filter
            logger.error('Invalid tag filter')
            return self.all_posts(request)

        posts = self.posts.filter(tags__name=tag)

        return render(
            request, self.get_template(request), {
                'self': self, 'posts': _paginate(request, posts),
                'filter_type': 'tag', 'filter': tag
            }
        )


BlogIndexPage.content_panels = [
    FieldPanel('title', classname='full title'),
    StreamFieldPanel('body'),
]

BlogIndexPage.promote_panels = Page.promote_panels


class BlogPostTag(TaggedItemBase):
    content_object = ParentalKey('BlogPost', related_name='tagged_items')


class BlogPost(Page, WithStreamField, WithFeedImage):
    date = models.DateField()
    tags = ClusterTaggableManager(through=BlogPostTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('date'),
        index.RelatedFields('tags', [
                            index.SearchField('name'),
                            index.SearchField('slug'),
                            ]),
    ]

    subpage_types = []

    def get_index_page(self):
        # Find closest ancestor which is a blog index
        return BlogIndexPage.objects.ancestor_of(self).last()


BlogPost.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('date'),
    StreamFieldPanel('body'),
]

BlogPost.promote_panels = Page.promote_panels + [
    FieldPanel('tags'),
    ImageChooserPanel('feed_image'),
]


# Entities Index Page
class EntityIndexPage(Page):
    subpage_types = ['EntityType']


# EntityType
class EntityType(Page, WithStreamField):
    colour = models.CharField(max_length=128, blank=False, help_text="You\
            can use the following colours:\
            lightgreen, darkgreen, lightpurple,\
            dark, purple, yellow, orange, red, lightblue,\
            darkblue, lightbrown, darkbrown and lightgray.")
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = ['Entity']


EntityType.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('colour', classname='full title'),
    StreamFieldPanel('body'),
]


# Entity
class Entity(Page, WithStreamField):
    creator = models.ForeignKey('self', null=True,
                                blank=True,
                                verbose_name='Creator',
                                related_name='entity_creator',
                                on_delete=models.SET_NULL)
    recipient = models.ForeignKey('self', null=True,
                                  blank=True,
                                  verbose_name='Recipient',
                                  related_name='entity_recipient',
                                  on_delete=models.SET_NULL)
    subtype = models.CharField(max_length=128, blank=True,
                               null=True,
                               verbose_name='Subtype/Role')
    date_from = models.DateField(blank=True, null=True,
                                 verbose_name='Start Date')
    date_to = models.DateField(blank=True, null=True,
                               verbose_name='End Date')

    # Normally wouldn't use a charfield for this, but
    # looking at the example data that's what's needed
    location = models.CharField(max_length=256, null=True,
                                blank=True,
                                verbose_name='Location')

    location_purchase = models.CharField(max_length=256, null=True,
                                         blank=True,
                                         verbose_name='Place of Purchase')

    bibliog = models.TextField(null=True, blank=True,
                               verbose_name='Bibliographic Details')

    comments = models.TextField(null=True, blank=True,
                                verbose_name='Comments')

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = []

    class Meta:
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'


Entity.content_panels = [
    FieldPanel('title', classname='full title'),

    MultiFieldPanel(
        [
            PageChooserPanel('creator'),
            PageChooserPanel('recipient'),
            FieldPanel('subtype', classname='full'),

            FieldPanel('date_from'),
            FieldPanel('date_to'),

            FieldPanel('location', classname='full'),
            FieldPanel('location_purchase', classname='full'),
        ],
        heading="Entity Details",
        classname="collapsible"
    ),

    StreamFieldPanel('body'),

    FieldPanel('comments', classname='full'),
    FieldPanel('bibliog', classname='full'),

]


class ObjectIndexPage(Page, WithStreamField):
    subpage_types = ['ObjectPage']

    def serve(self, request):
        return redirect('/', permanent=False)


ObjectIndexPage.content_panels = [
    FieldPanel('title', classname='full title'),
    StreamFieldPanel('body'),
]

ObjectIndexPage.promote_panels = Page.promote_panels


class ObjectPage(Page, WithStreamField):
    entities = models.ManyToManyField(Entity)
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = ['ObjectPage']

    def get_numeral(self):
        page = Page.objects.get(pk=self.pk)
        num = list(self.get_parent().get_children()).index(page) + 1
        if type(self.get_parent().specific) == ObjectPage:
            return int_to_roman(num)
        else:
            return num

    def get_next(self):
        page = Page.objects.get(pk=self.pk)
        num = list(self.get_parent().get_children()).index(page) + 1

        if num < self.get_parent().get_children().count():
            return self.get_parent().get_children()[num]
        else:
            parent_page = self.get_parent()
            parent_num = list(parent_page.get_parent().get_children()).index(
                parent_page) + 1

            if parent_num < parent_page.get_parent().get_children().count():
                return parent_page.get_parent().get_children()[parent_num]
            else:
                return None

    def get_prev(self):
        page = Page.objects.get(pk=self.pk)
        num = list(self.get_parent().get_children()).index(page) - 1

        if num >= 0:
            return self.get_parent().get_children()[num]
        else:
            parent_page = self.get_parent()
            parent_num = list(parent_page.get_parent().get_children()).index(
                parent_page) - 1

            if parent_num >= 0:
                return parent_page.get_parent().get_children()[parent_num]

            else:
                return None


ObjectPage.content_panels = [
    FieldPanel('title', classname='full title'),

    StreamFieldPanel('body'),
]

ObjectPage.promote_panels = Page.promote_panels
