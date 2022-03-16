from .models import *
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import random






RANReady_label = _('Are you ready to start the Picture-naming Task?')
class RanWelcomeForm(forms.ModelForm):
	ran_ready = forms.BooleanField(required=True, label=RANReady_label)

	class Meta:
		model = RanOrder
		fields = ('ran_ready',)




class RanFinishForm(forms.Form):
	ran_complete = forms.BooleanField(widget=forms.HiddenInput(), required=True, initial=True)
