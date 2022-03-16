from django.contrib import admin
from .models import *

class SpnPictureAdmin(admin.ModelAdmin):
	list_display = ('filename', 'sort_order', 'description', 'source')


class SpnPictureSetAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'get_pictures')

	def get_pictures(self, obj):
		return ', '.join(p.filename for p in obj.pictures.all())


class SpnResponseAdmin(admin.ModelAdmin):
	list_display = ('img', 'user', 'response_type')

admin.site.register(SpnPicture, SpnPictureAdmin)
admin.site.register(SpnPictureSet, SpnPictureSetAdmin)
admin.site.register(SpnResponse, SpnResponseAdmin)