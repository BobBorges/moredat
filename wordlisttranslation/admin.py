from django.contrib import admin
from .models import *

class WordlistWordAdmin(admin.ModelAdmin):
	list_display = ('word', 'sort_order')


class WordlistWordSetAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'get_words')

	def get_words(self, obj):
		return ', '.join(w.word for w in obj.words.all())


class WordlistResponseAdmin(admin.ModelAdmin):
	list_display = ('word', 'user', 'response_type', 'written_response', 'audio_response')

admin.site.register(WordlistWord, WordlistWordAdmin)
admin.site.register(WordlistWordSet, WordlistWordSetAdmin)
admin.site.register(WordlistResponse, WordlistResponseAdmin)