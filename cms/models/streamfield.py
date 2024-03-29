

from django import forms
from wagtail.core.blocks import (
    CharBlock, FieldBlock, PageChooserBlock, RawHTMLBlock, RichTextBlock,
    StreamBlock, StructBlock, TextBlock, URLBlock
)
from wagtail.documents.blocks import DocumentChooserBlock
# from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock


class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('default', 'Default'), ('full', 'Full width'),
    ))


class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()


class FootnoteBlock(StructBlock):
    numeral = TextBlock()
    reference = TextBlock()

    class Meta:
        template = 'cms/blocks/footnote_block.html'


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'),
        ('mid', 'Centred'), ('full-width', 'Full width'),
        ('hero', 'Hero'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()

    class Meta:
        template = 'cms/blocks/image_block.html'


class LinkStyleChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('default', 'Default'), ('button', 'Button'),
    ))


class LinkBlock(StructBlock):
    url = URLBlock(required=False)
    page = PageChooserBlock(required=False)
    label = CharBlock()
    style = LinkStyleChoiceBlock()

    class Meta:
        help_text = '''
        Use either URL or page, if both are filled in URL takes precedence.'''
        template = 'cms/blocks/link_block.html'


class PullQuoteStyleChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('default', 'Default'),
    ))


class PullQuoteBlock(StructBlock):
    quote = TextBlock('quote title')
    attribution = CharBlock()
    affiliation = CharBlock(required=False)
    style = PullQuoteStyleChoiceBlock()

    class Meta:
        template = 'cms/blocks/pull_quote_block.html'


class CMSStreamBlock(StreamBlock):

    # h2 = CharBlock(icon='title', classname='title')
    # h3 = CharBlock(icon='title', classname='title')
    # h4 = CharBlock(icon='title', classname='title')
    # h5 = CharBlock(icon='title', classname='title')

    intro = RichTextBlock(icon='pilcrow', required=False)
    paragraph = RichTextBlock(icon='pilcrow', required=False)
    pull_quote = RichTextBlock(icon='openquote', required=False)
    # pullquote = PullQuoteBlock(icon='openquote')
    table = TableBlock(required=False)
    footnote = FootnoteBlock(required=False)

    # image = ImageBlock(label='Aligned image', icon='image')
    document = DocumentChooserBlock(icon='doc-full-inverse', required=False)
    # link = LinkBlock(icon='link')
    # embed = EmbedBlock(icon='media')

    # html = AlignedHTMLBlock(icon='code', label='Raw HTML')
