from django import template
from django.conf import settings
from cms.models import (HomePage, EntityType, ObjectIndexPage)
import re

register = template.Library()


@register.filter
def get_first_search_result_index(page):
    """ Calculates the start value for an OL containing
        search results based on the page number """
    return (int(settings.ITEMS_PER_PAGE) * (int(page) - 1)) + 1


@register.filter
def add_image_captions(block):
    text = str(block)
    return re.sub(r'<img class="(.*?)" .* alt="(.*?)">',
                  #  r'<div class="\1">\g<0> <p class="caption">\2</p></div>',
                  r'<div class="\1">\g<0></div>',

                  text)


@register.simple_tag
def are_comments_allowed():
    """Returns True if commenting on the site is allowed, False otherwise."""
    return getattr(settings, 'ALLOW_COMMENTS', False)


@register.assignment_tag
def get_entity_types():
    return EntityType.objects.all()


@register.assignment_tag
def get_menu_pages():
    root = HomePage.objects.first()
    return root.get_children().live().in_menu()


@register.assignment_tag
def get_chapters():
    return ObjectIndexPage.objects.live().first().get_children().live()


@register.simple_tag
def get_first_item():
    return ObjectIndexPage.objects.first().get_children().first().url


@register.simple_tag(takes_context=True)
def get_site_root(context):
    """Returns the site root Page, not the implementation-specific model used.
    Object-comparison to self will return false as objects would differ.

    :rtype: `wagtail.wagtailcore.models.Page`
    """
    return context['request'].site.root_page


@register.simple_tag
def has_view_restrictions(page):
    """Returns True if the page has view restrictions set up, False
    otherwise."""
    return page.view_restrictions.count() > 0


@register.inclusion_tag('cms/tags/main_menu.html', takes_context=True)
def main_menu(context, root, current_page=None):
    """Returns the main menu items, the children of the root page. Only live
    pages that have the show_in_menus setting on are returned."""
    menu_pages = root.get_children().live().in_menu()

    root.active = (current_page.url == root.url
                   if current_page else False)

    for page in menu_pages:
        page.active = (current_page.url.startswith(page.url)
                       if current_page else False)

    return {'request': context['request'], 'root': root,
            'current_page': current_page, 'menu_pages': menu_pages}


@register.inclusion_tag('cms/tags/entities.html', takes_context=True)
def get_entities(context):
    ''' Gets the entity index page and returns its children'''
    entities = EntityType.objects.all()

    return {'request': context['request'], 'entities': entities}


@register.inclusion_tag('cms/tags/sidenav.html', takes_context=True)
def get_sidenav(context, current_page=None):
    ''' Gets the entity index page and returns its children'''
    pages = ObjectIndexPage.objects.get(title="Souvenirs").get_children()
    if current_page:
        root_node = current_page.get_ancestors().type(
            ObjectIndexPage).first()
        if root_node:
            root_nodes = root_node.get_children()
            all_ancestors = current_page.get_ancestors(inclusive=True)
            current_section = (root_nodes & all_ancestors).first()

            return {'request': context['request'], 'pages': pages,
                    'current_section': current_section, 'current_page':
                    current_page}

    return {'request': context['request'], 'pages': pages}


@register.inclusion_tag('cms/tags/footer_menu.html', takes_context=True)
def footer_menu(context, root, current_page=None):
    """Returns the main menu items, the children of the root page. Only live
    pages that have the show_in_menus setting on are returned."""
    menu_pages = root.get_children().live().in_menu()

    root.active = (current_page.url == root.url
                   if current_page else False)

    for page in menu_pages:
        page.active = (current_page.url.startswith(page.url)
                       if current_page else False)

    return {'request': context['request'], 'root': root,
            'current_page': current_page, 'menu_pages': menu_pages}
