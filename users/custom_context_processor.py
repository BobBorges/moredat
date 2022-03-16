from users.models import UserDetails, AssignedTasks
from consent.models import UserConsent






def get_user_details(request):

	user_details = None 
	assigned_tasks = None
	user_consented = False
	num_assigned_tasks = None 
	num_completed_tasks = None 


	try:
		user_consented = UserConsent.objects.get(user=request.user)
	except:
		print('Failed at consent')

	try:
		user_details = UserDetails.objects.get(user=request.user)
	except:
		print('Failed at UD')

	try:
		assigned_tasks = AssignedTasks.objects.filter(user=request.user)
		num_assigned_tasks = len(assigned_tasks)
	except:
		print('Failed at AT')

	try:
		completed_tasks = AssignedTasks.objects.filter(user_id=request.user.id, complete=True)
		num_completed_tasks = len(completed_tasks)
	except:
		print('Failed at CT')		
	

	context =  {
		"assigned_tasks": assigned_tasks,
		"user_details": user_details, 
		"user_consented": user_consented,
		"num_completed_tasks": num_completed_tasks,
		"num_assigned_tasks": num_assigned_tasks
	}

	return context

