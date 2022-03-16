from .models import *
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User 
from django.utils.translation import ugettext_lazy as _








class QuestionForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['answer']
		widgets = {}



class OtherFieldForm(forms.Form):

	def init(self, *args, **kwargs):
		super(OtherFieldForm, self).__init__(*args, **kwargs)
	
	other_field = forms.CharField(
		max_length=999, 
		required=False, 
		label='Please specify:'
	)

	class Meta:
		fields = ['other_field']
