from django.db import models






class AcknowledgedContribution(models.Model):
	person = models.CharField(max_length=255)
	reason = models.CharField(max_length=510)



class CitedReference(models.Model):
	item_title = models.CharField(max_length=510)
	creators = models.TextField(blank=True)
	production_date = models.CharField(max_length=11)
	persistent_id = models.CharField(max_length=510, blank=True)
	full_reference = models.TextField()



class Tasks(models.Model):
	task = models.CharField(max_length=255)
	url_name = models.CharField(max_length=255)
	app_name = models.CharField(max_length=255)
	model_name = models.CharField(max_length=255)
	url_arg = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.task