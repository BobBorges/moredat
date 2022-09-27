from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from main.models import Tasks
from users.decorators import user_consented
from users.models import UserDetails, AssignedTasks
from .forms import VidnarFinishForm
from .models import *
import os








@login_required
@user_consented
def vidnar_home(request):

	context = {'title': 'MoReDaT Video Narration'}
	context['video_sets'] = VidnarVideoSet.objects.all() 

	return render(request, 'vidnar/vidnar-home.html', context)




@login_required
@user_consented
def vidnar_welcome(request, vid_set):
	UD_object = UserDetails.objects.get(user=request.user)
	context = {"title": "MoReDaT Video Narration"}
	current_set = VidnarVideoSet.objects.get(slug=vid_set)
	context['vid_set_obj'] = current_set
	vids = current_set.videos.all().order_by('sort_order')	
	vids_fn_desc = {}
	for idx, vid in enumerate(vids, start=1):
		vids_fn_desc[idx] = (vid.filename, vid.description)
	context['vids_fn_desc'] =  vids_fn_desc

	return render(request, 'vidnar/vidnar-welcome.html', context)




@login_required
@user_consented
def vidnar_trial(request, vid_set, vidnr):
	UD_object = UserDetails.objects.get(user=request.user)
	context = {"title": "MoReDaT Video Narration"}
	current_set = VidnarVideoSet.objects.get(slug=vid_set)
	context['vid_set_obj'] = current_set

	current_task = Tasks.objects.get(url_name='vidnar-welcome', url_arg=vid_set)
	
	vids = current_set.videos.all().order_by('sort_order')
	context['num_vids'] = len(vids)

	vids_d = {}
	for idx, vid in enumerate(vids, start=1):
		vids_d[idx] = vid

	current_vid = vids_d[int(vidnr)]

	context['current_vid'] = current_vid
	context['vidnr'] = vidnr	
	next_vid_nr = None
	if int(vidnr) < len(vids_d):
		next_vid_nr = int(vidnr) + 1
	context['next_vid_nr'] = next_vid_nr

	return render(request, 'vidnar/vidnar-trial.html', context)




@login_required
def vidnar_finish(request, vid_set):
	context = {"title": "MoReDaT VidNar"}
	current_task = Tasks.objects.get(url_name='vidnar-welcome', url_arg=vid_set)
	if request.method == 'POST':
		form = VidnarFinishForm(request.POST)
		context['form'] = form
		if form.is_valid():
			try:
				inst = AssignedTasks.objects.get(user=request.user, task=current_task)
				inst.complete = True
				inst.save()
			except:
				inst = AssignedTasks.objects.create(user=request.user, task=current_task, complete=True)
				inst.save()
			message = messages.success(request, _('Thanks for finishing this Video Narration Task.'))
			return redirect('profile')
	else:
		form = VidnarFinishForm()
		context['form'] = form

	return render(request, 'vidnar/vidnar-finish.html', context)




@login_required
@user_consented
def save_trial_data(request):
	with open(
		os.path.join(settings.MEDIA_ROOT, 'recorded-audio/VIDNAR-{}-{}_{}_{}_{:%Y-%m-%d-%H-%M-%S}.wav'.format(
			request.headers['trialBlock'],
			request.headers['stimid'],
			request.headers['researchGroup'], 
			request.user.id, datetime.now()
		)), 
		'wb') as trialAudio:
		trialAudio.write(request.body)

	return HttpResponse('audio received')
