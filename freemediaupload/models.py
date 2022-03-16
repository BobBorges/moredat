from django.contrib.auth.models import User
from django.db import models





class UploadMetaData(models.Model):
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=510)
	creator = models.CharField(max_length=510)
	date_created = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField()
	filename = models.FileField(upload_to="user-uploads")

	def __str__(self):
		return self.title
