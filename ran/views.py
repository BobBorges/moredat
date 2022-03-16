from .forms import RanWelcomeForm, RanFinishForm
from .models import RanOrder
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
import random, os
from users.models import AssignedTasks








trialbloc_fns = {
	'practice_block_1': 'p1',
	'practice_block_2': 'p2',
	'block_1': 'b1',
	'block_2': 'b2',
	'block_3': 'b3',
	'block_4': 'b4',
	'block_5': 'b5',
	'block_6': 'b6'
}

RAN_TRAJECTORY = {
	"practice_block_1" : "practice_block_2",
	"practice_block_2" : "postpractice",
	"block_1" : "block_2",
	"block_2" : "block_3",
	"block_3" : "block_4",
	"block_4" : "block_5",
	"block_5" : "block_6",
	"block_6" : "ranfinish"
}

RAN_BLOCKNAMES = {
	"practice_block_1" : _("Practice Block 1 of 2"),
	"practice_block_2" : _("Practice Block 2 of 2"),
	"block_1" : _("Block 1 of 6"),
	"block_2" : _("Block 2 of 6"),
	"block_3" : _("Block 3 of 6"),
	"block_4" : _("Block 4 of 6"),
	"block_5" : _("Block 5 of 6"),
	"block_6" : _("Block 6 of 6")
}




def ShuffleStumuli():
	stimuli = [
		'001',	'002',	'003',	'004',	'005',	'006',	'007',	
		'008',	'009',	'010',  '011',	'012',	'013',	'014',	
		'015',	'016',	'017',	'018',	'019',	'020',  '021',	
		'022',	'023',	'024',	'025',	'026',	'027',	'028',	
		'029',	'030',  '031',	'032',	'033',	'034',	'035',	
		'036',	'037',	'038',	'039',	'040',  '041',	'042',	
		'043',	'044',	'045',	'046',	'047',	'048',	'049',	
		'050',  '051',	'052',	'053',	'054',	'055',	'056',	
		'057',	'058',	'059',	'060',  '061',	'062',	'063',	
		'064',	'065',	'066',	'067',	'068',	'069',	'070',
		'071',	'072',	'073',	'074',	'075',	'076',	'077',	
		'078',	'079',	'080',  '081',	'082',	'083',	'084',	
		'085',	'086',	'087',	'088',	'089',	'090',  '091',	
		'092',	'093',	'094',	'095',	'096',	'097',	'098',	
		'099',	'100'
	]
	random.shuffle(stimuli) 
	pb1 = stimuli[:5]
	pb2 = stimuli[5:10]
	b1 = stimuli[10:25]
	b2 = stimuli[25:40]
	b3 = stimuli[40:55]
	b4 = stimuli[55:70]
	b5 = stimuli[70:85]
	b6 = stimuli[85:]
	
	return 	pb1, pb2, b1, b2, b3, b4, b5, b6




def consented(user):
	return True




@login_required
@user_passes_test(consented, login_url='profile')
def ran_welcome(request):
	context = {"title": "MoReDaT RAN"}
	Uobj = User.objects.get(id=request.user.id)

	try:
		ROobj = RanOrder.objects.get(user_id=Uobj.id)
		print(ROobj)
		message = messages.warning(request, _('You already did that. You still see the form, but you will not create another RAN Order object. Edit the lines where you find this message in ran/views.py, ran_welcome().'))
		context['form'] = RanWelcomeForm()
		#return redirect('profile')		

	except:
		if request.method == 'POST':
			form = RanWelcomeForm(request.POST)
			context['form'] = form
			if form.is_valid():
				shufft = ShuffleStumuli()
				mo = form.save(commit=False)
				mo.user_id = Uobj.id
				mo.practice_block_1 = shufft[0]
				mo.practice_block_2 = shufft[1]
				mo.block_1 = shufft[2]
				mo.block_2 = shufft[3]
				mo.block_3 = shufft[4]
				mo.block_4 = shufft[5]
				mo.block_5 = shufft[6]
				mo.block_6 = shufft[7]
				mo.save()
				return redirect('ran-trialblock', block='practice_block_1')
		else:
			context['form'] = RanWelcomeForm()

	return render(request, 'ran/ran-welcome.html', context)




@login_required
@user_passes_test(consented, login_url='profile')
def ran_trial_block(request, block):
	context = {"title": "MoReDaT RAN"}
	try:
	 	user_order = RanOrder.objects.get(user_id=request.user.id)
	except:
		return redirect('ran-welcome')
	block_order_raw = getattr(user_order, block)
	block_order_list = block_order_raw.strip('[]').split(', ')
	block_order = [item.strip("'") for item in block_order_list]
	context['next'] = RAN_TRAJECTORY[block]
	context['block_description'] = RAN_BLOCKNAMES[block]
	context['stimuli'] = block_order
	context['current_trial'] = block

	return render(request, 'ran/ran-trialblock.html', context)




@login_required
@user_passes_test(consented, login_url='profile')
def ran_post_practice(request):
	context = {"title": "MoReDaT RAN"}
	return render(request, 'ran/postpractice.html', context)




@login_required
@user_passes_test(consented, login_url='profile')
def ran_finish(request):
	context = {"title": "MoReDaT RAN"}
	if request.method == 'POST':
		form = RanFinishForm(request.POST)
		context['form'] = form
		if form.is_valid():
			try:
				inst = AssignedTasks.objects.get(user=request.user, task="Automated Picture Naming")
				inst.complete = True
				inst.save()
			except:
				inst = AssignedTasks.objects.create(user=request.user, task="Automated Picture Naming", complete=True)
				inst.save()
			message = messages.success(request, _('Thanks for finishing the Automated Picture-Naming Task.'))
			return redirect('profile')
	else:
		form = RanFinishForm()
		context['form'] = form

	return render(request, 'ran/finish.html', context)




@login_required
def save_trial_data(request):
	with open(
		os.path.join(settings.MEDIA_ROOT, 'recorded-audio/RAN-{}-{}_{}_{}_{:%Y-%m-%d-%H-%M-%S}.wav'.format(
			trialbloc_fns[request.headers['trialBlock']], 
			request.headers['stimid'], 
			request.headers['researchGroup'], 
			request.user.id, datetime.now()
		)), 
		'wb') as trialAudio:
		trialAudio.write(request.body)

	return HttpResponse('audio received')