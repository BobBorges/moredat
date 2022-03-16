from django import forms
from .models import SpnResponse




class SpnResponseForm(forms.ModelForm):

	class Meta:
		model = SpnResponse
		fields = ['response_type', 'written_response', 'commentary']





class SpnFinishForm(forms.Form):
	spn_complete = forms.BooleanField(widget=forms.HiddenInput(), required=True, initial=True)
