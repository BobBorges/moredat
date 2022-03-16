from django.db import models




class VidnarVideo(models.Model):
	filename = models.CharField(max_length=255)
	sort_order = models.IntegerField()
	description = models.TextField(blank=True)
	source = models.TextField(blank=True)

	def __str__(self):
		return self.filename


LANG_CHOICES = [
	('target_language', "Target Language"),
	('other_language', "Other Language")
]
class VidnarVideoSet(models.Model):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	videos = models.ManyToManyField(VidnarVideo)
	description = models.TextField(blank=True)
	target_language = models.CharField(max_length=255, choices=LANG_CHOICES)
	special_instructions = models.TextField(blank=True)

	def __str__(self):
		return self.name