from django.contrib import admin
from .models import *
# Register your models here.
class TrogOrderAdmin(admin.ModelAdmin):
	list_display = ('user', 'trog_ready')

class TrogResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'click_quadrant', 'selected_stimulus', 'audio_repeats', 'render_time', 'click_time')


admin.site.register(TrogOrder, TrogOrderAdmin)
admin.site.register(TrogResponse, TrogResponseAdmin)