from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
import logging




logger = logging.getLogger(__name__)




#####################################
## scaffolding site view functions ##
#####################################
def about_django_view(request):
	context = {
		"title":"MoReDaT"
	}
	return render(request, 'main/AboutDjango.html', context)




def apps_list_short_descriptions(request):
	context = {
		"title": "MoReDaT Apps"
	}
	return render(request, 'main/apps-short_descrs.html', context)




def credits_view(request):
	context = {
		"title": "MoReDaT Credits"
	}
	return render(request, 'main/credits.html', context)




def home_view(request):
	context = {
		"title": "MoReDaT Home"
	}
	return render(request, 'main/home.html', context)




def how_to_cite_view(request):
	context = {
		"title":"MoReDaT Cite"
	}
	return render(request, 'main/HowToCite.html', context)




def quickstart_view(request):
	context = {
		"title": "MoReDaT Quick Start"
	}
	return render(request, 'main/QuickStartGuide.html', context)




#####################################
## app descriptions view funvtions ##
#####################################
def check_user_audio_descr(request):
	context = {
		"title": "MoReDaT User Audio Test"
	}
	return render(request, 'main/test-user-audio_descr.html', context)




def documentation_descr(request):
	context = {
		"title":"MoReDaT Documentation"
	}
	return render(request, 'main/documentation_descr.html', context)




def free_media_upload_descr(request):
	context = {
		"title": "MoReDaT Free Media Upload"
	}
	return render(request, 'main/free-media-upload_descr.html', context)




def informed_consent_descr(request):
	context = {
		"title": "MoReDaT Consent"
	}
	return render(request, 'main/consent-form_descr.html', context)




def questionnaires_descr(request):
	context = {
		"title":"MoReDaT Questionnaires"
	}
	return render(request, 'main/questionnaires_descr.html', context)




def ran_descr(request):
	context = {
		"title": "MoReDaT RAN Task"
	}
	return render(request, 'main/ran_descr.html', context)




def spn_descr(request):
	context = {
		"title": "MoReDaT SPN Task"
	}
	return render(request, 'main/spn_descr.html', context)




def trog_descr(request):
	context = {
		"title": "MoReDaT TROG Task"
	}
	return render(request, 'main/trog_descr.html', context)




def users_descr(request):
	context = {
		"title":"MoReDaT Users"
	}
	return render(request, 'main/users_descr.html', context)




def vidnar_descr(request):
	context = {
		"title": "MoReDaT VIDNAR Task"
	}
	return render(request, 'main/vidnar_descr.html', context)




def wordlist_translation_descr(request):
	context = {
		"title": "MoReDaT Wordlist Translation"
	}
	return render(request, 'main/wordlist-translation_descr.html', context)

