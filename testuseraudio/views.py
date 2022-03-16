from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render








@login_required
def voice_request(request):
	with open('recorded_data/testfile_{}_{:%Y-%m-%d-%H-%M}.wav'.format(request.user.id, datetime.now()),'wb') as tf:
		tf.write(request.body)
	return HttpResponse('audio received')




@login_required
def test_audio(request):
	context = {
		'title': 'MoReDaT Audio Test'
	}
	return render(request, 'testuseraudio/audiotest.html', context)