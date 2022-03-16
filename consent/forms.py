from .models import UserConsent
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _






consent_label= _("I have read and above information and agree to voluntarily participate in the research program.")
info_on_consent = _("Read the whole policy") + "<a target=\"_blank\" href=\"download/\">" + _(" here") + "</a>."

class GetUserConsent(forms.ModelForm):
	consent = forms.BooleanField(label=consent_label, help_text=info_on_consent, required=True)
	user = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = UserConsent
		fields = ('consent', )
