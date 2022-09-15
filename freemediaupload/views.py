from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import UploadMetaData
from users.decorators import user_consented








@login_required
@user_consented
def freemediaupload_view(request):
	context = {'title': 'MoReDaT Free Media Upload'}

	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		context['form'] = form
		if form.is_valid():
			inst = form.save(commit=False)
			inst.uploader = request.user
			inst.save()
			return redirect('thx4upload')
		else:
			print(form.errors)
	else:
		context['form'] = UploadForm

	return render(request, 'freemediaupload/upload.html', context)




@login_required
def thx_view(request):
	context = {'title': 'MoReDaT thx for your upload'}
	return render(request, 'freemediaupload/thx.html', context)
