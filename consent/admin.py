from django.contrib import admin
from .models import UserConsent






class UserConsentAdmin(admin.ModelAdmin):
	list_display = ['user', 'consent']




admin.site.register(UserConsent, UserConsentAdmin)