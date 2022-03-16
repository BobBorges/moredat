from django.urls import path
from . import views as consent_views






urlpatterns = [
	path('', consent_views.get_user_consent, name='get-consent'),
	path('download/', consent_views.dl_consent_form, name='download-consent-form')
]