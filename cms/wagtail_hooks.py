from wagtail.wagtailcore import hooks
import re


def populate_entity_relationships(request, page):
    # I know this shouldn't go here, but it's a bit of
    # trickery
    from cms.models import (Entity, ObjectPage) # noqa

    if isinstance(page, ObjectPage):

        # Clear existing relations
        page.entities.clear()

        # Our list of new potential entities:
        page_list = []

        # Regex to match:
        re1 = '.*?'
        re2 = '(\\d+)'

        rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)

        # Check for new entities
        for block in page.body.stream_data:
            q = None
            if type(block) is tuple:
                q = block[1].source
            else:
                if block['type'] == 'paragraph':
                    q = block['value']
            if q:
                search = rg.search(q)
                if search:
                    page_id = int(search.group(1))
                    if page_id not in page_list:
                        page_list.append(page_id)
        # We have our list:
        entities = Entity.objects.filter(id__in=page_list)
        for entity in entities.all():
            page.entities.add(entity)


hooks.register('after_create_page', populate_entity_relationships)
hooks.register('after_edit_page', populate_entity_relationships)
