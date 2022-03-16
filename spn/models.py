from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from main.models import Tasks





class SpnPicture(models.Model):
	filename = models.CharField(max_length=255)
	sort_order = models.IntegerField()
	description = models.TextField(blank=True)
	source = models.TextField(blank=True)

	def __str__(self):
		return self.filename




class SpnPictureSet(models.Model):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	pictures = models.ManyToManyField(SpnPicture)
	description = models.TextField(blank=True)
	special_instructions = models.TextField(blank=True)

	def __str__(self):
		return self.name



SPN_RESPONSE_TYPE = (
	("Record response", _('Record response')),
	("I don't remember", _("I don't remember")),
	("I don't know", _("I don't know"))
)
class SpnResponse(models.Model):
	task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
	img = models.ForeignKey(SpnPicture, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	response_type = models.CharField(max_length=255, choices=SPN_RESPONSE_TYPE)
	audio_response = models.CharField(max_length=255, blank=True, null=True)
	written_response = models.CharField(max_length=255, blank=True, null=True)
	commentary = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.img.filename

