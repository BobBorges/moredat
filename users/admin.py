from django.contrib import admin
from .models import *






class ResearchGroupsAdmin(admin.ModelAdmin):
	list_display = ['group_name','slug', 'description']




class AssignedTasksAdmin(admin.ModelAdmin):
	list_display = ['user', 'task', 'complete']




class DefaultAssignments(admin.ModelAdmin):
	list_display = ['group_name', 'task']




class UserDetailsAdmin(admin.ModelAdmin):
	list_display = ['user', 'research_group', 'gender']




admin.site.register(ResearchGroups, ResearchGroupsAdmin)
admin.site.register(AssignedTasks, AssignedTasksAdmin)
admin.site.register(DefaultAssignedTasksByGroup, DefaultAssignments)
admin.site.register(UserDetails, UserDetailsAdmin) 