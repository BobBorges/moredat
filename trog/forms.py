from .models import *
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import random


trogReady_label = _('Are you ready to start the listening task?')
class TrogWelcomeForm(forms.ModelForm):
	trog_ready = forms.BooleanField(required=True, label=trogReady_label)

	class Meta:
		model = TrogOrder
		fields = ('trog_ready',)


class TrogFinishForm(forms.Form):
	trog_complete = forms.BooleanField(widget=forms.HiddenInput(), required=True, initial=True)