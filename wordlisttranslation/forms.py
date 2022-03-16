from django import forms
from .models import WordlistResponse




class WordlistResponseForm(forms.ModelForm):

	class Meta:
		model = WordlistResponse
		fields = ['response_type', 'written_response', 'commentary']



class WordlistFinishForm(forms.Form):
	vidnar_complete = forms.BooleanField(widget=forms.HiddenInput(), required=True, initial=True)