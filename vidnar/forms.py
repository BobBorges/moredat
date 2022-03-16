from django import forms


class VidnarFinishForm(forms.Form):
	vidnar_complete = forms.BooleanField(widget=forms.HiddenInput(), required=True, initial=True)