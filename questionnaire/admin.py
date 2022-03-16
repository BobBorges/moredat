from django.contrib import admin
from .models import *



class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('text', 'short_val', 'sort_order')



class ChoiceSetAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_choices')

	def get_choices(self, obj):
		return ', '.join([c.short_val for c in obj.choices.all()])



class QuestionAdmin(admin.ModelAdmin):
	list_display = ('slug', 'q_type','text', 'subtext', 'choices', 'sort_order')



class QuestionnaireAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'get_questions')

	def get_questions(self, obj):
		return ', '.join([q.slug for q in obj.questions.all()])



class AnswerAdmin(admin.ModelAdmin):
	list_display = ('user', 'questionnaire', 'question', 'answer')



admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ChoiceSet, ChoiceSetAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)