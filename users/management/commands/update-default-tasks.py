from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from users.models import *




class Command(BaseCommand):

    help = """
    Run this command to update existing users' AssignedTasks to match the DefaultAssignedTasksByGroup. Since DefaultAssignedTasksByGroup are assigned on successful submission of the UserDetails form, adding default tasks to research groups will have no effect on existing users belonging to that group."""


    def handle(self, *args, **options):
        research_groups = ResearchGroups.objects.all()
        for rg in research_groups:
            rg_tasks = DefaultAssignedTasksByGroup.objects.filter(group_name=rg)
            rg_users = UserDetails.objects.filter(research_group=rg)
            for rg_user in rg_users:
                for rg_task in rg_tasks:
                    try:
                        T = AssignedTasks.objects.get(user=rg_user.user, task=rg_task.task)
                        self.stdout.write(f'{T.task} already exists for {rg_user.user}, moving on...')
                    except:
                        self.stdout.write(f'Assigning {rg_task.task} to {rg_user.user}.')
                        T = AssignedTasks.objects.create(user=rg_user.user, task=rg_task.task, complete=False)
                        T.save()
                        self.stdout.write(f'  ---> created {T.task} for {rg_user}.')
