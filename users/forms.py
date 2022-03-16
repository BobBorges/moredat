from .models import UserDetails, ResearchGroups
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _








class RegisterUser(UserCreationForm):
	first_name = forms.CharField(max_length=255)
	last_name = forms.CharField(max_length=255)
	username = forms.CharField(max_length=255)

	def clean(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')

		if User.objects.filter(email=email).exists():
			raise ValidationError(_("That email already exists."))
		if User.objects.filter(username=username).exists():
			raise ValidationError(_("That username already exists."))
		
		return self.cleaned_data

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')




GENDER_OPTIONS = (
	(None, "---------"),
	('male', 'Male'),
	('female', 'Female'),
	('other', 'Other / Rather not say.')
)

RESEARCH_GROUP_LABEL = "Select your research group. What language do you speak?"

class UserDetailsForm(forms.ModelForm):
	research_group = forms.ModelChoiceField(ResearchGroups.objects.all())
	birth_date = forms.DateField()
	gender = forms.ChoiceField(choices=GENDER_OPTIONS)

	class Meta:
		model = UserDetails
		fields = ('research_group', 'birth_date', 'gender')

