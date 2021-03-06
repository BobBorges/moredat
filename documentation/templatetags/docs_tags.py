import re

from django.core.exceptions import ObjectDoesNotExist
from django.template import Library
from django.urls import reverse
from django.utils.safestring import mark_safe

from documentation.models import WikiPage
from documentation.urls import WIKI_SLUG

register = Library()

WIKI_WORDS_REGEX = re.compile(r'\b%s\b' % WIKI_SLUG, re.UNICODE)


def replace_wikiwords(value):
    def replace_wikiword(m):
        slug = m.group(1)
        try:
            page = WikiPage.objects.get(slug=slug)
            url = reverse('documentation_page', kwargs={'slug': slug})
            return r'<a href="%s">%s</a>' % (url, page.slug)
        except ObjectDoesNotExist:
            url = reverse('documentation_edit', kwargs={'slug': slug})
            return r'<a class="doesnotexist" href="%s">%s</a>' % (url, slug)

    return mark_safe(WIKI_WORDS_REGEX.sub(replace_wikiword, value))


@register.filter
def wikify(value):
    """Makes WikiWords"""
    return replace_wikiwords(value)
