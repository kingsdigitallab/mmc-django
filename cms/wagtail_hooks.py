from django.conf import settings
from django.utils.html import format_html, format_html_join
from wagtail.core import hooks
from wagtail.core.whitelist import attribute_rule, check_url
from cms.models import EntityThrough
import re


def populate_entity_relationships(request, page):
    # I know this shouldn't go here, but it's a bit of
    # trickery
    from cms.models import (Entity, ObjectPage) # noqa
    try:
        if isinstance(page, ObjectPage):

            EntityThrough.objects.filter(page=page).delete()

            # Our list of new potential entities:
            page_list = []

            # Regex to match:
            rg = re.compile('<a(.*?)(\\d+)(.*)linktype=\\"page\\">')

            # Check for new entities
            for block in page.body.stream_data:
                q = None
                if type(block) is tuple:
                    q = block[1].source
                else:
                    if block['type'] == 'paragraph':
                        q = block['value']
                if q:

                    search = rg.findall(q)
                    if search:
                        for i in search:
                            page_id = int(i[1])
                            if page_id not in page_list:
                                page_list.append(page_id)

            # We have our list:
            entities = Entity.objects.filter(id__in=page_list)
            for entity in entities.all():
                e = EntityThrough()
                e.page = page
                e.entity = entity
                e.save()

    except Exception as e:
        print(e)


hooks.register('after_create_page',
               populate_entity_relationships)
hooks.register('after_edit_page',
               populate_entity_relationships)

from wagtail.admin.rich_text import HalloPlugin
from wagtail.core import hooks

@hooks.register('register_rich_text_features')
def register_embed_feature(features):


    features.register_editor_plugin(
        'hallo', 'bookmark-add',
        HalloPlugin(
            name='bookmarkAddButton',
            js=['js/hallo_bookmark_add.js'],
        )
    )

    features.register_editor_plugin(
        'hallo', 'bookmark-link',
        HalloPlugin(
            name='bookmarkLinkButton',
            js=['js/hallo_bookmark_link.js'],
        )
    )

    features.register_editor_plugin(
        'hallo', 'link-new',
        HalloPlugin(
            name='openLinkInNewWindow',
            js=['js/hallo_link_new_window.js'],
        )
    )
    features.register_editor_plugin(
        'hallo', 'caption-button',
        HalloPlugin(
            name='imageCaptionButton',
            js=['js/hallo_plugin_caption_image.js'],
        )
    )

    features.register_editor_plugin(
        'hallo', 'ref-button',
        HalloPlugin(
            name='referenceButton',
            js=['js/hallo_plugin_references.js'],
        )
    )

    features.register_editor_plugin(
        'hallo', 'html-edit',
        HalloPlugin(
            name='editHtmlButton',
            js=['js/hallo_source_editor.js'],
        )
    )
    

    features.default_features.append('bookmark-add')
    features.default_features.append('bookmark-link')
    features.default_features.append('link-new')
    features.default_features.append('caption-button')
    features.default_features.append('ref-button')
    features.default_features.append('html-edit')
    

def editor_js():
    js_files = [
       # 'js/hallo_plugin_caption_image.js',
       # 'js/hallo_plugin_references.js',
       # 'js/hallo_source_editor.js',
       # 'js/hallo_bookmark_add.js',
       # 'js/hallo_bookmark_link.js',
       # 'js/hallo_link_new_window.js'
    ]

    #js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
     #                              ((settings.STATIC_URL, filename)
     #                               for filename in js_files)
      #                             )

    #return js_includes + format_html("""
     #   <script>
     ##       registerHalloPlugin('imageCaptionButton');
      #      registerHalloPlugin('referenceButton');
      #      registerHalloPlugin('bookmarkAddButton');
      #      registerHalloPlugin('bookmarkLinkButton');
      #      registerHalloPlugin('openLinkInNewWindow');
      #      registerHalloPlugin('editHtmlButton');
      #  </script>
      #  """)


#hooks.register('insert_editor_js', editor_js)


def whitelister_element_rules():
    return {
        'p': attribute_rule({'class': True}),
        'a': attribute_rule({'href': check_url, 'id': True, 'class': True,
                             'target': True}),
        'span': attribute_rule({'class': True}),
        'i': attribute_rule({'class': True}),
        'iframe': attribute_rule(
            {'id': True, 'class': True, 'src': True, 'style': True,
             'frameborder': True, 'allowfullscreen': True, 'width': True,
             'height': True}),
        'small': attribute_rule({'class': True}),
        'div': attribute_rule({'class': True})
    }


hooks.register('construct_whitelister_element_rules',
               whitelister_element_rules)
