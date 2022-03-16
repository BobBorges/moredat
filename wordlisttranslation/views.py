from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from main.models import Tasks
from users.models import UserDetails, AssignedTasks
from .forms import WordlistFinishForm, WordlistResponseForm
from .models import *
import os








@login_required
def wlt_home(request):
	context = {'title': 'MoReDaT Wordlist Translation'}
	context['wordlist_sets'] = WordlistWordSet.objects.all()

	return render(request, 'wordlisttranslation/wlt-home.html', context)




@login_required
def wlt_welcome(request, word_set):
	UD_object = UserDetails.objects.get(user=request.user)
	context = {"title": "MoReDaT Wordlist Translation"}
	current_set = WordlistWordSet.objects.get(slug=word_set)
	context['word_set_obj'] = current_set
	words = current_set.words.all().order_by('sort_order')	
	words_fn_desc = {}
	for idx, word in enumerate(words, start=1):
		words_fn_desc[idx] = word.word
	context['words_fn_desc'] =  words_fn_desc

	return render(request, 'wordlisttranslation/wlt-welcome.html', context)




@login_required
def wlt_trial(request, word_set, wordnr):
	UD_object = UserDetails.objects.get(user=request.user)
	context = {"title": "MoReDaT Word List Translation"}
	current_set = WordlistWordSet.objects.get(slug=word_set)
	context['pic_set_obj'] = current_set

	current_task = Tasks.objects.get(url_name='wlt-welcome', url_arg=word_set)
	
	words = current_set.words.all().order_by('sort_order')	
	words_d = {}
	for idx, word in enumerate(words, start=1):
		words_d[idx] = word

	current_word = words_d[int(wordnr)]
	context['current_word'] = current_word
	
	next_word_nr = None
	if int(wordnr) < len(words_d):
		next_word_nr = int(wordnr) + 1
	context['next_word_nr'] = next_word_nr

	if request.method == 'POST':

		form = WordlistResponseForm(request.POST)
		context['form'] = form
		if form.is_valid():
			if form.cleaned_data['response_type'] == 'Record response' and 'hidden_field' in request.FILES:
				word_filename = f'WLT-{current_set.slug}-{wordnr}_{UD_object.research_group.target_lang_short_name}_{request.user.id}_{datetime.now()}.wav'
				data = request.FILES['hidden_field']
				path = default_storage.save(f'recorded-audio/{word_filename}', ContentFile(data.read()))
				tmp_file = os.path.join(settings.MEDIA_ROOT, path)

				f_inst = form.save(commit=False)
				f_inst.task = current_task
				f_inst.word = current_word
				f_inst.user = request.user
				f_inst.audio_response = word_filename
				f_inst.save()
				if next_word_nr:
					return redirect('wlt-trial', word_set=word_set, wordnr=str(next_word_nr))
				else:
					return redirect('wlt-finish', word_set=word_set, wordnr='finish')
			else:
				f_inst = form.save(commit=False)
				f_inst.task = current_task
				f_inst.word = current_word
				f_inst.user = request.user
				f_inst.save()
				if next_word_nr:
					return redirect('wlt-trial', word_set=word_set, wordnr=str(next_word_nr))
				else:
					return redirect('wlt-trial', word_set=word_set, wordnr='finish')

	else:
		context['form'] = WordlistResponseForm()

	return render(request, 'wordlisttranslation/wlt-trial.html', context)




@login_required
def wlt_finish(request, word_set):
	context = {"title": "MoReDaT WLT"}
	current_task = Tasks.objects.get(url_name='wlt-welcome', url_arg=word_set)
	if request.method == 'POST':
		form = WordlistFinishForm(request.POST)
		context['form'] = form
		if form.is_valid():
			try:
				inst = AssignedTasks.objects.get(user=request.user, task=current_task)
				inst.complete = True
				inst.save()
			except:
				inst = AssignedTasks.objects.create(user=request.user, task=current_task, complete=True)
				inst.save()
			message = messages.success(request, _('Thanks for finishing this Translation Task.'))
			return redirect('profile')
	else:
		form = WordlistFinishForm()
		context['form'] = form

	return render(request, 'wordlisttranslation/wlt-finish.html', context)