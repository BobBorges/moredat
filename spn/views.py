from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.urls import resolve
from django.utils.translation import gettext as _
from main.models import Tasks
from users.decorators import user_consented
from users.models import UserDetails, AssignedTasks
from .forms import SpnResponseForm, SpnFinishForm
from .models import SpnPicture, SpnPictureSet, SpnResponse
import os








@login_required
@user_consented
def home_view(request):
	context = {'title': 'MoReDaT Self-paced Picture Naming'}
	context['picture_sets'] = SpnPictureSet.objects.all() 
	return render(request, 'spn/spn-home.html', context)




@login_required
@user_consented
def welcome_view(request, pic_set):
	UD_object = UserDetails.objects.get(user=request.user)
	context = {"title": "MoReDaT Self-paced Picture Naming"}
	current_set = SpnPictureSet.objects.get(slug=pic_set)
	context['pic_set_obj'] = current_set

	pics = current_set.pictures.all().order_by('sort_order')	
	pics_fn_desc = {}
	for idx, pic in enumerate(pics, start=1):
		pics_fn_desc[idx] = (pic.filename, pic.description)
	
	context['pics_fn_desc'] =  pics_fn_desc

	return render(request, 'spn/spn-welcome.html', context)




@login_required
@user_consented
def pic_view(request, pic_set, picnr):
    UD_object = UserDetails.objects.get(user=request.user)
    context = {"title": "MoReDaT Self-paced Picture Naming"}
    current_set = SpnPictureSet.objects.get(slug=pic_set)
    context['pic_set_obj'] = current_set
    
    current_task = Tasks.objects.get(url_name='spn-welcome', url_arg=pic_set)
    
    pics = current_set.pictures.all().order_by('sort_order')	
    pics_d = {}
    for idx, pic in enumerate(pics, start=1):
        pics_d[idx] = pic

    current_pic = pics_d[int(picnr)]
    context['current_pic'] = current_pic
	
    next_pic_nr = None
    if int(picnr) < len(pics_d):
        next_pic_nr = int(picnr) + 1
    context['next_pic_nr'] = next_pic_nr

    if request.method == 'POST':

        form = SpnResponseForm(request.POST)
        context['form'] = form
        if form.is_valid():
            if form.cleaned_data['response_type'] == 'Record response' and 'hidden_field' in request.FILES:
                spn_filename = 'SPN-{}-{}_{}_{}_{:%Y-%m-%d-%H-%M-%S}.wav'.format(
                    current_set.slug,
                    picnr,
                    UD_object.research_group.target_lang_short_name,
                    request.user.id,
                    datetime.now()
                )
                data = request.FILES['hidden_field']
                path = default_storage.save(f'recorded-audio/{spn_filename}', ContentFile(data.read()))
                tmp_file = os.path.join(settings.MEDIA_ROOT, path)

                f_inst = form.save(commit=False)
                f_inst.task = current_task
                f_inst.img = current_pic
                f_inst.user = request.user
                f_inst.audio_response = spn_filename
                f_inst.save()

                if next_pic_nr:
                    return redirect('spn-pic', pic_set=pic_set, picnr=str(next_pic_nr))
                else:
                    return redirect('spn-pic', pic_set=pic_set, picnr='finish')
            else:
                f_inst = form.save(commit=False)
                f_inst.task = current_task
                f_inst.img = current_pic
                f_inst.user = request.user
                f_inst.save()
                if next_pic_nr:
                    return redirect('spn-pic', pic_set=pic_set, picnr=str(next_pic_nr))
                else:
                    return redirect('spn-pic', pic_set=pic_set, picnr='finish')

    else:
        context['form'] = SpnResponseForm()

    return render(request, 'spn/spn-pic.html', context)




@login_required
@user_consented
def finish_view(request, pic_set):
	context = {"title": "MoReDaT SPN"}
	current_task = Tasks.objects.get(url_name='spn-welcome', url_arg=pic_set)
	if request.method == 'POST':
		form = SpnFinishForm(request.POST)
		context['form'] = form
		if form.is_valid():
			try:
				inst = AssignedTasks.objects.get(user=request.user, task=current_task)
				inst.complete = True
				inst.save()
			except:
				inst = AssignedTasks.objects.create(user=request.user, task=current_task, complete=True)
				inst.save()
			message = messages.success(request, _('Thanks for finishing this Self-paced Picture-Naming Task.'))
			return redirect('profile')
	else:
		form = SpnFinishForm()
		context['form'] = form

	return render(request, 'spn/spn-finish.html', context)

