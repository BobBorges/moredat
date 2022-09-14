from .forms import RegisterUser, UserDetailsForm
from .models import AssignedTasks, UserDetails, DefaultAssignedTasksByGroup
from .task_checker import complete_checker
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from main.models import Tasks








def register(request):
	context = {
		'title': 'MoReDaT Register'
	}
	if request.method == 'POST':
		registerform = RegisterUser(request.POST)
		context['registerform'] = registerform
		if registerform.is_valid():
			registerform.save()
			username = registerform.cleaned_data.get('username')
			messages.success(request, _(f'Account created for {username}'))
			user = User.objects.get(username=username)
			last = AssignedTasks.objects.order_by('-pk')[0].id
			consent_assignment = AssignedTasks.objects.create(id=last+1, user=user, task_id=Tasks.objects.get(task='Consent').id)
			consent_assignment.save()
			userdetails_assignment = AssignedTasks.objects.create(id=last+2, user=user, task_id=Tasks.objects.get(task="User Details").id)
			userdetails_assignment.save()
			return redirect('login')
	else:
		context['registerform'] = RegisterUser()
	return render(request, 'users/register.html', context)




@login_required
def get_user_details(request):
	context = {"title": "MoReDaT User Details"}
	try:
		already_details = UserDetails.objects.get(user=request.user)
		messages.warning(request, _("This user already did that. The form is shown because this is an example project, but you could perform some action –for instance redirect to the user profile– instead of seeing this message and form that has already been completed. Edit lines 48 and 49 of `users/views.py` to customize this behavior. Ticking the form again will do nothing to the database and the redirects are now disabled – the form is visible here for demonstration purposes only."))
		userdetailsform = UserDetailsForm()
	except:	
		if request.method == 'POST':
			userdetailsform = UserDetailsForm(request.POST)
			if userdetailsform.is_valid():
				userdetailsform.instance.user = request.user
				userdetailsform.save()
				usergroup = userdetailsform.cleaned_data.get('research_group')
				## assign default tasks by research group
				d_tasks = DefaultAssignedTasksByGroup.objects.filter(group_name=usergroup)
				for dt in d_tasks:
					T = AssignedTasks.objects.create(user=request.user, task=dt.task, complete=False)

				messages.success(request, _("Success! Thanks, now you can get started with the research tasks."))
				return redirect('profile')
		else:
			userdetailsform = UserDetailsForm()
	context['userdetailsform'] = userdetailsform
	return render(request, 'users/user-details.html', context)



@login_required
def profile(request):
	complete_checker(request.user)
	context = {
		'title': 'MoReDaT Profile'
	}
        # no database calls are made because all UD and assigned tasks is made available to the logged-in user throughout the site with the custom_contect_processor
	return render(request, 'users/profile.html', context)
