from django.contrib import admin
from .models import *


class VidnarVideoAdmin(admin.ModelAdmin):
	list_display = ('filename', 'sort_order', 'description', 'source')


class VidnarVideoSetAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'target_language', 'description', 'get_videos')

	def get_videos(self, obj):
		return ', '.join(v.filename for v in obj.videos.all())


admin.site.register(VidnarVideo, VidnarVideoAdmin)
admin.site.register(VidnarVideoSet, VidnarVideoSetAdmin)