from django import forms
from .models import UploadMetaData


class UploadForm(forms.ModelForm):

	class Meta:
			model = UploadMetaData
			fields = ['title', 'creator', 'date_created', 'description', 'filename']