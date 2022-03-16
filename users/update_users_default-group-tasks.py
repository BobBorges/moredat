from django.contrib.auth.models import User
from users.models import *




"""
WHEN TO USE THIS SCRIPT

	Use this script in the case when you already have established research groups with users assigned to it, after updating the DefaultAssignedTasksByGroup objects. In other words – DefaultAssignedTasksByGroup are assigned to users when assigning the user to the ResearchGroup. If you add default tasks to a research group, this action will have no effect on existing users. 

	Run this script to update existing users' AssignedTasks to match the DefaultAssignedTasksByGroup.

HOW TO USE THIS SCRIPT

1. enter the django shell
	--->	$ python manage.py shell

3. run the script in the shell
	--->	>>> exec(open('users/update_users_default-group-tasks.py').read())
"""




research_groups = ResearchGroups.objects.all()
for rg in research_groups:
	rg_tasks = DefaultAssignedTasksByGroup.objects.filter(group_name=rg)
	rg_users = UserDetails.objects.filter(research_group=rg)
	for rg_user in rg_users:
		for rg_task in rg_tasks:
			try:
				T = AssignedTasks.objects.get(user=rg_user.user, task=rg_task.task)
				print(f'{T.task} already exists for {rg_user.user}, moving on...')
			except:
				print(f'Assigning {rg_task.task} to {rg_user.user}.')
				T = AssignedTasks.objects.create(user=rg_user.user, task=rg_task.task, complete=False)
				T.save()
				print(f'  ---> created {T.task} for {rg_user}.')
