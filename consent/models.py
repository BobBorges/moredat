from django.contrib.auth.models import User
from django.db import models








class UserConsent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
	consent = models.BooleanField()

	def __str__(self):
		return str(self.consent)