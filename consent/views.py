from .forms import GetUserConsent
from consent.models import UserConsent
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _








# SHORT VERSION OF CONSENT FORM 
RESEARCH_PROJECT_TITLE = _("DUMMY RESEARCH TITLE") 

RESEARCH_PURPOSE = _("""We're investigating
    * X
    * Y
    * Z
...because we hypothesize that X influences Y and Z is a mitigating factor that determines the extent to which Y is influenced.""")

RESEARCH_PROCEDURES = _("""As a participant we will ask you to tell use your experience with Z qdn we will measure your Y and Z using structured interrogative eyeballing and calibrated deterministic quantification. Collected data will be amalgamated and analyzed using conglomerated regressive retrogradation.""")

RESEARCH_FUNDING = _("""The project is funded by the National Science Philanthropers club with contributions from the Science-fairy godparents foundation.""")

RESEARCH_VOLUNTARY = _("""The research is voluntary and you may withdraw your consent at any time without consequence.""")

RESEARCH_PUBLICATION = _("""We the researchers will publish results of the research in scientific and popular-science outlets. Your data appearing in such a publication will be anonymized to the best of our ability.""")

RESEARCH_ARCHIVING = _("""At the end of our research project, data will be anonymized and dumped into the Norwegian Underground Seed Vault and kept under embargo for 300years, after which data will be available OA for other researchers to reuse.""")




@login_required
def get_user_consent(request):
	context = {"title":"MoReDaT Consent Form"} 
	context['research_project_title'] = RESEARCH_PROJECT_TITLE
	context['research_purpose'] = RESEARCH_PURPOSE
	context['research_procedures'] = RESEARCH_PROCEDURES
	context['research_funding'] = RESEARCH_FUNDING
	context['research_voluntary'] = RESEARCH_VOLUNTARY
	context['research_publication'] = RESEARCH_PUBLICATION
	context['research_archiving'] = RESEARCH_ARCHIVING
	try:
		already_consented = UserConsent.objects.get(user_id=request.user.id)
		messages.warning(request, _("This user already did that. The form is shown because this is an example project, but you could perform some action –for instance redirect to the user profile– instead of seeing this message and form that has already been completed. Edit lines 45 and 46 of `consent/views.py` to customize this behavior. Ticking the form again will do nothing to the database and the redirects are now disabled – the form is visible here for demonstration purposes only."))
		consentform = GetUserConsent()
	except:
		if request.method == 'POST':
			userobject = User.objects.get(id=request.user.id)
			consentform = GetUserConsent(request.POST)
			if consentform.is_valid():
				consentform.instance.user = request.user
				consentform.save()
				messages.success(request, _("Thanks for agreeing! Please tell us a bit about yourself."))
				return redirect('get-user-details')
			else:
				print(consentform.errors)
		else:
			consentform = GetUserConsent()
	context['consentform'] = consentform
	return render(request, 'consent/consent-form.html', context)




@login_required
def dl_consent_form(request):
	try:
		return FileResponse(open('static/consent/docs/consent-form.pdf', 'rb'), content_type='contenttype/pdf')
	except FileNotFoundError:
		raise Http404()