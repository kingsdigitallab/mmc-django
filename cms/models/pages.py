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
from .streamfield import CMSStreamBlock
from wagtail.wagtailcore.fields import StreamField


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

    mozart_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = ['BlogIndexPage', 'ObjectIndexPage',
                     'EntityIndexPage', 'IndexPage',
                     'RichTextPage']


HomePage.content_panels = [
    FieldPanel('title', classname='full title'),
    ImageChooserPanel('mozart_image'),
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
            purple, lightgreen, darkgreen, orange,\
            lightblue, darkblue, teal, yellow, lightgray\
            pink, red.")
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = ['Entity']

    @property
    def entities(self):
        return self.get_children()


EntityType.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('colour', classname='full title'),
    StreamFieldPanel('body'),
]


# Entity
class Entity(Page):
    body = StreamField(CMSStreamBlock(), verbose_name="Description")
    creator = models.ForeignKey('self', null=True,
                                blank=True,
                                verbose_name='Author/Creator',
                                related_name='entity_creator',
                                on_delete=models.SET_NULL)
    recipient = models.ForeignKey('self', null=True,
                                  blank=True,
                                  verbose_name='Recipient',
                                  related_name='entity_recipient',
                                  on_delete=models.SET_NULL)

    creator_text = models.CharField(max_length=128, blank=True,
                                    null=True,
                                    verbose_name='Author/Creator (Text)')

    subtype = models.CharField(max_length=128, blank=True,
                               null=True,
                               verbose_name='Category/Role')
    date_from = models.CharField(max_length=128, blank=True, null=True,
                                 verbose_name='Date 1')
    date_to = models.CharField(max_length=128, blank=True, null=True,
                               verbose_name='Date 2')

    date_mozart = models.CharField(max_length=128, blank=True, null=True,
                                   verbose_name='Date related to mozart')

    # Normally wouldn't use a charfield for this, but
    # looking at the example data that's what's needed
    location = models.CharField(max_length=256, null=True,
                                blank=True,
                                verbose_name='Location')
    sublocation = models.CharField(max_length=256, null=True,
                                   blank=True,
                                   verbose_name='Sublocation')
    location_mozart = models.CharField(max_length=256, null=True,
                                       blank=True,
                                       verbose_name='Location\
                                       Related to Mozart')

    mozart_relevence = StreamField(CMSStreamBlock(required=False),
                                   verbose_name="Mozart Relevance",
                                   null=True, blank=True)

    location_purchase = models.CharField(max_length=256, null=True,
                                         blank=True,
                                         verbose_name='Place of Purchase')

    bibliog = models.TextField(null=True, blank=True,
                               verbose_name='Bibliographic Reference')

    comments = models.TextField(null=True, blank=True,
                                verbose_name='Comments')

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('subtype'),
        index.SearchField('mozart_relevence'),
        index.SearchField('comments'),
    ]

    subpage_types = []

    class Meta:
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'
        ordering = ['title', ]

    def get_entities(self):
        e = EntityThrough.objects.filter(entity=self)
        return e.all()


Entity.content_panels = [
    MultiFieldPanel(
        [
            FieldPanel('title', classname='full title',),
        ],
        heading="Title/Name",
    ),

    StreamFieldPanel('body'),

    MultiFieldPanel(
        [
            FieldPanel('subtype', classname='full'),
            PageChooserPanel('creator'),
            FieldPanel('creator_text'),
            PageChooserPanel('recipient'),

            FieldPanel('date_from'),
            FieldPanel('date_to'),

            FieldPanel('location', classname='full'),
            FieldPanel('sublocation', classname='full'),
            FieldPanel('location_mozart', classname='full'),

            FieldPanel('date_mozart', classname='full'),

            FieldPanel('location_purchase', classname='full'),
        ],
        heading="Entity Details",
        classname="collapsible"
    ),
    StreamFieldPanel('mozart_relevence'),

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
    homepage_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    homepage_text = models.TextField(blank=True, null=True)
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

    def parent_is_object_page(self):
        if type(self.get_parent().specific) == ObjectPage:

            return True
        else:
            return False

    def get_next(self):
        try:
            page = Page.objects.get(pk=self.pk)
            num = list(self.get_parent().get_children()).index(page) + 1

            if isinstance(self.get_parent().specific, ObjectIndexPage):
                return self.get_children()[0]
            else:
                if num < self.get_parent().get_children().count():
                    return self.get_parent().get_children()[num]
                else:
                    parent_page = self.get_parent()
                    parent_num = list(parent_page.get_parent()
                                      .get_children()).index(
                        parent_page) + 1

                    if parent_num < parent_page.get_parent()\
                            .get_children().count():
                        return parent_page.get_parent()\
                            .get_children()[parent_num]
                    else:
                        return None
        except: # noqa
            return None

    def get_prev(self):
        try:
            page = Page.objects.get(pk=self.pk)
            num = list(self.get_parent().get_children()).index(page)

            if isinstance(self.get_parent().specific, ObjectIndexPage):
                return self.get_parent().get_children()[num - 1]\
                    .get_children().last()
            else:
                if num > 0:
                    return self.get_parent().get_children()[num - 1]
                elif num == 0:
                    return self.get_parent()
                else:
                    parent_page = self.get_parent()
                    parent_num = list(parent_page.get_parent()
                                      .get_children()).index(
                        parent_page) - 1

                    if parent_num >= 0:
                        return parent_page.get_parent()\
                            .get_children()[parent_num]

                    else:
                        return None
        except: # noqa
            return None


ObjectPage.content_panels = [
    FieldPanel('title', classname='full title'),

    StreamFieldPanel('body'),

    MultiFieldPanel(
        [
            FieldPanel('homepage_text'),
            ImageChooserPanel('homepage_image'),
        ],
        heading="Homepage Promo Details",
    ),
]

ObjectPage.promote_panels = Page.promote_panels


class EntityThrough(models.Model):
    entity = models.ForeignKey(Entity, related_name="throughentity")
    page = models.ForeignKey(Page, related_name="throughpage")
