from django.contrib import admin
from .models import AcknowledgedContribution, CitedReference, Tasks






class TasksAdmin(admin.ModelAdmin):
	list_display = ['task', 'url_name', 'url_arg', 'model_name', 'app_name']



admin.site.register(AcknowledgedContribution)
admin.site.register(CitedReference)
admin.site.register(Tasks, TasksAdmin)