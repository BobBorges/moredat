from django.contrib import admin

from .models import Revision, WikiPage


class RevisionInlines(admin.TabularInline):
    model = Revision
    extra = 1


class WikiPageAdmin(admin.ModelAdmin):
    inlines = [RevisionInlines]
    list_display = ('slug', 'title')

class RevisionAdmin(admin.ModelAdmin):
    pass


admin.site.register(WikiPage, WikiPageAdmin)
admin.site.register(Revision, RevisionAdmin)
