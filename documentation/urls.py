from .views import *
from django.conf.urls import url
from django.contrib.auth.decorators import login_required






# Wiki slugs must been CamelCase but slashes are fine, if each slug
# is also a CamelCase/OtherSide
WIKI_SLUG = r'((([A-Z]+[a-z]+){2,})(/([A-Z]+[a-z]+){2,})*)'
WIKI_SLUG = getattr(settings, 'DOCUMENTATION_SLUG_REGEX', WIKI_SLUG)

urlpatterns = [
    url(r'^$', index, name='documentation_index'),
    # Revision and Page list
    url(r'^history/$', revision_list, name='documentation_revision_list'),
    url(r'^index/$', page_list, name='documentation_page_list'),
    # Revision list for page
    url(
        r'^(?P<slug>%s)/history/$' % WIKI_SLUG,
        revisions,
        name='documentation_revision_list',
    ),
    # Changes between two revisions, revision id's come from GET
    url(r'^(?P<slug>%s)/changes/$' % WIKI_SLUG, changes, name='documentation_changes'),
    # Edit Form
    url(
        r'^(?P<slug>%s)/edit/(?P<rev_id>\d+)/$' % WIKI_SLUG,
        login_required(edit),
        name='documentation_edit',
    ),
    url(
        r'^(?P<slug>%s)/edit/$' % WIKI_SLUG, login_required(edit), name='documentation_edit',
    ),
    # Page
    url(r'^(?P<slug>%s)/rev(?P<rev_id>\d+)/$' % WIKI_SLUG, page, name='documentation_page',),
    url(r'^(?P<slug>%s)/$' % WIKI_SLUG, page, name='documentation_page'),
]
