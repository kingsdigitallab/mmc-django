from django.conf import settings
from django.utils.html import format_html, format_html_join
from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule, check_url
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

    except Exception, e:
        print e


hooks.register('after_create_page',
               populate_entity_relationships)
hooks.register('after_edit_page',
               populate_entity_relationships)


def editor_js():
    js_files = [
        'js/hallo_plugin_caption_image.js',
        'js/hallo_plugin_references.js',
    ]

    js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
                                   ((settings.STATIC_URL, filename)
                                    for filename in js_files)
                                   )

    return js_includes + format_html("""
        <script>
            registerHalloPlugin('imageCaptionButton');
            registerHalloPlugin('referenceButton');
        </script>
        """)


hooks.register('insert_editor_js', editor_js)


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
        'small': attribute_rule({'class': True})
    }


hooks.register('construct_whitelister_element_rules',
               whitelister_element_rules)
