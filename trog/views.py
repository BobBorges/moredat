from .forms import *
from .models import *
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from main.models import Tasks
from users.models import UserDetails, AssignedTasks
import random








img_stimuli = {
	"A0": ["A0_1_t.jpg", "A0_2_d.jpg", "A0_3_d.jpg", "A0_4_d.jpg"],
	"A1": ["A1_1_d.jpg", "A1_2_t.jpg", "A1_3_d.jpg", "A1_4_d.jpg"],
	"A2": ["A2_1_d.jpg", "A2_2_t.jpg", "A2_3_d.jpg", "A2_4_d.jpg"],
	"A3": ["A3_1_d.jpg", "A3_2_t.jpg", "A3_3_d.jpg", "A3_4_d.jpg"],
	"A4": ["A4_1_d.jpg", "A4_2_t.jpg", "A4_3_d.jpg", "A4_4_d.jpg"],
	"B1": ["B1_1_d.jpg", "B1_2_t.jpg", "B1_3_d.jpg", "B1_4_d.jpg"],
	"B2": ["B2_1_d.jpg", "B2_2_t.jpg", "B2_3_d.jpg", "B2_4_d.jpg"],
	"B3": ["B3_1_d.jpg", "B3_2_t.jpg", "B3_3_d.jpg", "B3_4_d.jpg"],
	"B4": ["B4_1_d.jpg", "B4_2_t.jpg", "B4_3_d.jpg", "B4_4_d.jpg"],
	"C1": ["C1_1_d.jpg", "C1_2_t.jpg", "C1_3_d.jpg", "C1_4_d.jpg"],
	"C2": ["C2_1_d.jpg", "C2_2_t.jpg", "C2_3_d.jpg", "C2_4_d.jpg"],
	"C3": ["C3_1_d.jpg", "C3_2_t.jpg", "C3_3_d.jpg", "C3_4_d.jpg"],
	"C4": ["C4_1_d.jpg", "C4_2_t.jpg", "C4_3_d.jpg", "C4_4_d.jpg"],
	"D1": ["D1_1_d.jpg", "D1_2_t.jpg", "D1_3_d.jpg", "D1_4_d.jpg"],
	"D2": ["D2_1_d.jpg", "D2_2_t.jpg", "D2_3_d.jpg", "D2_4_d.jpg"],
	"D3": ["D3_1_d.jpg", "D3_2_t.jpg", "D3_3_d.jpg", "D3_4_d.jpg"],
	"D4": ["D4_1_d.jpg", "D4_2_t.jpg", "D4_3_d.jpg", "D4_4_d.jpg"],
	"E1": ["E1_1_d.jpg", "E1_2_t.jpg", "E1_3_d.jpg", "E1_4_d.jpg"],
	"E2": ["E2_1_d.jpg", "E2_2_t.jpg", "E2_3_d.jpg", "E2_4_d.jpg"],
	"E3": ["E3_1_d.jpg", "E3_2_t.jpg", "E3_3_d.jpg", "E3_4_d.jpg"],
	"E4": ["E4_1_d.jpg", "E4_2_t.jpg", "E4_3_d.jpg", "E4_4_d.jpg"],
	"F1": ["F1_1_d.jpg", "F1_2_t.jpg", "F1_3_d.jpg", "F1_4_d.jpg"],
	"F2": ["F2_1_d.jpg", "F2_2_t.jpg", "F2_3_d.jpg", "F2_4_d.jpg"],
	"F3": ["F3_1_d.jpg", "F3_2_t.jpg", "F3_3_d.jpg", "F3_4_d.jpg"],
	"F4": ["F4_1_d.jpg", "F4_2_t.jpg", "F4_3_d.jpg", "F4_4_d.jpg"],
	"G1": ["G1_1_d.jpg", "G1_2_t.jpg", "G1_3_d.jpg", "G1_4_d.jpg"],
	"G2": ["G2_1_d.jpg", "G2_2_t.jpg", "G2_3_d.jpg", "G2_4_d.jpg"],
	"G3": ["G3_1_d.jpg", "G3_2_t.jpg", "G3_3_d.jpg", "G3_4_d.jpg"],
	"G4": ["G4_1_d.jpg", "G4_2_t.jpg", "G4_3_d.jpg", "G4_4_d.jpg"],
	"H1": ["H1_1_d.jpg", "H1_2_t.jpg", "H1_3_d.jpg", "H1_4_d.jpg"],
	"H2": ["H2_1_d.jpg", "H2_2_t.jpg", "H2_3_d.jpg", "H2_4_d.jpg"],
	"H3": ["H3_1_d.jpg", "H3_2_t.jpg", "H3_3_d.jpg", "H3_4_d.jpg"],
	"H4": ["H4_1_d.jpg", "H4_2_t.jpg", "H4_3_d.jpg", "H4_4_d.jpg"],
	"I1": ["I1_1_d.jpg", "I1_2_t.jpg", "I1_3_d.jpg", "I1_4_d.jpg"],
	"I2": ["I2_1_d.jpg", "I2_2_t.jpg", "I2_3_d.jpg", "I2_4_d.jpg"],
	"I3": ["I3_1_d.jpg", "I3_2_t.jpg", "I3_3_d.jpg", "I3_4_d.jpg"],
	"I4": ["I4_1_d.jpg", "I4_2_t.jpg", "I4_3_d.jpg", "I4_4_d.jpg"],
	"J1": ["J1_1_d.jpg", "J1_2_t.jpg", "J1_3_d.jpg", "J1_4_d.jpg"],
	"J2": ["J2_1_d.jpg", "J2_2_t.jpg", "J2_3_d.jpg", "J2_4_d.jpg"],
	"J3": ["J3_1_d.jpg", "J3_2_t.jpg", "J3_3_d.jpg", "J3_4_d.jpg"],
	"J4": ["J4_1_d.jpg", "J4_2_t.jpg", "J4_3_d.jpg", "J4_4_d.jpg"],
	"K1": ["K1_1_d.jpg", "K1_2_t.jpg", "K1_3_d.jpg", "K1_4_d.jpg"],
	"K2": ["K2_1_d.jpg", "K2_2_t.jpg", "K2_3_d.jpg", "K2_4_d.jpg"],
	"K3": ["K3_1_d.jpg", "K3_2_t.jpg", "K3_3_d.jpg", "K3_4_d.jpg"],
	"K4": ["K4_1_d.jpg", "K4_2_t.jpg", "K4_3_d.jpg", "K4_4_d.jpg"],
	"L1": ["L1_1_d.jpg", "L1_2_t.jpg", "L1_3_d.jpg", "L1_4_d.jpg"],
	"L2": ["L2_1_d.jpg", "L2_2_t.jpg", "L2_3_d.jpg", "L2_4_d.jpg"],
	"L3": ["L3_1_d.jpg", "L3_2_t.jpg", "L3_3_d.jpg", "L3_4_d.jpg"],
	"L4": ["L4_1_d.jpg", "L4_2_t.jpg", "L4_3_d.jpg", "L4_4_d.jpg"],
	"M1": ["M1_1_d.jpg", "M1_2_t.jpg", "M1_3_d.jpg", "M1_4_d.jpg"],
	"M2": ["M2_1_d.jpg", "M2_2_t.jpg", "M2_3_d.jpg", "M2_4_d.jpg"],
	"M3": ["M3_1_d.jpg", "M3_2_t.jpg", "M3_3_d.jpg", "M3_4_d.jpg"],
	"M4": ["M4_1_d.jpg", "M4_2_t.jpg", "M4_3_d.jpg", "M4_4_d.jpg"],
	"N1": ["N1_1_d.jpg", "N1_2_t.jpg", "N1_3_d.jpg", "N1_4_d.jpg"],
	"N2": ["N2_1_d.jpg", "N2_2_t.jpg", "N2_3_d.jpg", "N2_4_d.jpg"],
	"N3": ["N3_1_d.jpg", "N3_2_t.jpg", "N3_3_d.jpg", "N3_4_d.jpg"],
	"N4": ["N4_1_d.jpg", "N4_2_t.jpg", "N4_3_d.jpg", "N4_4_d.jpg"],
	"O1": ["O1_1_d.jpg", "O1_2_t.jpg", "O1_3_d.jpg", "O1_4_d.jpg"],
	"O2": ["O2_1_d.jpg", "O2_2_t.jpg", "O2_3_d.jpg", "O2_4_d.jpg"],
	"O3": ["O3_1_d.jpg", "O3_2_t.jpg", "O3_3_d.jpg", "O3_4_d.jpg"],
	"O4": ["O4_1_d.jpg", "O4_2_t.jpg", "O4_3_d.jpg", "O4_4_d.jpg"],
	"P1": ["P1_1_d.jpg", "P1_2_t.jpg", "P1_3_d.jpg", "P1_4_d.jpg"],
	"P2": ["P2_1_d.jpg", "P2_2_t.jpg", "P2_3_d.jpg", "P2_4_d.jpg"],
	"P3": ["P3_1_d.jpg", "P3_2_t.jpg", "P3_3_d.jpg", "P3_4_d.jpg"],
	"P4": ["P4_1_d.jpg", "P4_2_t.jpg", "P4_3_d.jpg", "P4_4_d.jpg"],
	"Q1": ["Q1_1_d.jpg", "Q1_2_t.jpg", "Q1_3_d.jpg", "Q1_4_d.jpg"],
	"Q2": ["Q2_1_t.jpg", "Q2_2_t.jpg", "Q2_3_d.jpg", "Q2_4_d.jpg"],
	"Q3": ["Q3_1_d.jpg", "Q3_2_t.jpg", "Q3_3_d.jpg", "Q3_4_d.jpg"],
	"Q4": ["Q4_1_d.jpg", "Q4_2_t.jpg", "Q4_3_d.jpg", "Q4_4_d.jpg"],
	"R1": ["R1_1_d.jpg", "R1_2_t.jpg", "R1_3_d.jpg", "R1_4_d.jpg"],
	"R2": ["R2_1_d.jpg", "R2_2_t.jpg", "R2_3_d.jpg", "R2_4_d.jpg"],
	"R3": ["R3_1_d.jpg", "R3_2_t.jpg", "R3_3_d.jpg", "R3_4_d.jpg"],
	"R4": ["R4_1_d.jpg", "R4_2_t.jpg", "R4_3_d.jpg", "R4_4_d.jpg"],
	"S1": ["S1_1_d.jpg", "S1_2_t.jpg", "S1_3_d.jpg", "S1_4_d.jpg"],
	"S2": ["S2_1_d.jpg", "S2_2_t.jpg", "S2_3_d.jpg", "S2_4_d.jpg"],
	"S3": ["S3_1_d.jpg", "S3_2_t.jpg", "S3_3_d.jpg", "S3_4_d.jpg"],
	"S4": ["S4_1_d.jpg", "S4_2_t.jpg", "S4_3_d.jpg", "S4_4_d.jpg"],
	"T1": ["T1_1_d.jpg", "T1_2_t.jpg", "T1_3_d.jpg", "T1_4_d.jpg"],
	"T2": ["T2_1_d.jpg", "T2_2_t.jpg", "T2_3_d.jpg", "T2_4_d.jpg"],
	"T3": ["T3_1_d.jpg", "T3_2_t.jpg", "T3_3_d.jpg", "T3_4_d.jpg"],
	"T4": ["T4_1_d.jpg", "T4_2_t.jpg", "T4_3_d.jpg", "T4_4_d.jpg"]
}

img_keys = [x for x in list(img_stimuli.keys()) if x != "A0"]

TROG_TRAJECTORY = {
	"practice_block": "post-practice",
	"block_1": "block_2",
	"block_2": "block_3",
	"block_3": "block_4",
	"block_4": "block_5",
	"block_5": "block_6",
	"block_6": "block_7",
	"block_7": "block_8",
	"block_8": "finish",
}

TROG_DESCR = {
	"practice_block": _('a practice trial.'),
	"block_1": _('block 1 of 8'),
	"block_2": _('block 2 of 8'),
	"block_3": _('block 3 of 8'),
	"block_4": _('block 4 of 8'),
	"block_5": _('block 5 of 8'),
	"block_6": _('block 6 of 8'),
	"block_7": _('block 7 of 8'),
	"block_8": _('block 8 of 8')	
}




def ShuffleStumuli():
	random.shuffle(img_keys)
	return img_keys




@login_required
def welcome(request):
	context = {
		"title": 'MoReDaT TROG welcome'
	}
	Uobj = User.objects.get(id=request.user.id)

	if request.method == 'POST':
		try:
			TOobj = TrogOrder.objects.get(user_id=Uobj.id)
			message = messages.warning(request, _('You already did that. You still see the form, but you will not create another TROG Order object. Edit the lines where you find this message in ran/views.py, ran_welcome().'))
			context['form'] = TrogWelcomeForm()
		except:
			form = TrogWelcomeForm(request.POST)
			context['form'] = form
			if form.is_valid():
				shuff = ShuffleStumuli()
				mo = form.save(commit=False)
				mo.user_id = Uobj.id
				mo.practice_block = ["A0"]
				mo.block_1 = shuff[:10]
				mo.block_2 = shuff[10:20]
				mo.block_3 = shuff[20:30]
				mo.block_4 = shuff[30:40]
				mo.block_5 = shuff[40:50]
				mo.block_6 = shuff[50:60]
				mo.block_7 = shuff[60:70]
				mo.block_8 = shuff[70:80]
				mo.save()
				return redirect('trog-block', TROGblock='practice_block')
	else:
		context['form'] = TrogWelcomeForm()
	return render(request, 'trog/welcome.html', context)




@login_required
def block(request, TROGblock):
	if TROGblock == 'post-practice':
		return redirect('trog-postpractice')
	elif TROGblock == 'finish':
		return redirect('trog-finish')
	else:
		context = {
			"title": f"MoReDaT TROG {TROGblock}",
			"blockvar": str(TROGblock)
		}

	try:
		user_order = TrogOrder.objects.get(user_id=request.user.id)
	except:
		return redirect('trog-welcome')

	block_order_raw = getattr(user_order, TROGblock)
	block_order_list = block_order_raw.strip('[]').split(', ')
	block_order = [x.strip("'") for x in block_order_list] 

	block_d = {}
	for x in block_order:
		block_d[x] = img_stimuli[x]
		random.shuffle(block_d[x])

	context["block_order"] = block_order
	context["block_d"] = block_d
	context["next"] = TROG_TRAJECTORY[TROGblock]
	context['block_desctiption'] = TROG_DESCR[TROGblock]

	return render(request, 'trog/block.html', context)




@login_required
def postpractice(request):
	context = {
		'title': "NESPOMILA TROG"
	}

	return render(request, 'trog/postpractice.html', context)




@login_required
def finish(request):
	context = {"title": "MoReDaT TROG"}

	if request.method == 'POST':
		form = TrogFinishForm(request.POST)
		context['form'] = form
		if form.is_valid():
			TROG = Tasks.objects.get(url_name='trog-welcome')
			try:
				inst = AssignedTasks.objects.get(user=request.user, url_name=TROG)
				inst.complete = True
				inst.save()
			except:
				inst = AssignedTasks.objects.create(user=request.user, task=TROG, complete=True)
				inst.save()
			message = messages.success(request, _('Thanks for finishing this TROG Task.'))
			return redirect('profile')
	else:
		form = TrogFinishForm()
		context['form'] = form

	return render(request, 'trog/finish.html', context)




@login_required
def save_data(request):
	TrogResponse.objects.create(
		user=request.user,
		click_quadrant=request.POST['clicked_quad'],
		selected_stimulus=request.POST['clicked_stim'],
		audio_repeats=request.POST['replays'],
		render_time= request.POST['renderTime'],
		click_time=request.POST['clickTime']
	)
	return HttpResponse("OK")