from django.db import models
from django.contrib.auth.models import User




class RanOrder(models.Model):
	user = models.OneToOneField(
		User, 
		on_delete=models.CASCADE, 
		blank=True, 
		null=True
	)
	practice_block_1 = models.CharField(max_length=200)
	practice_block_2 = models.CharField(max_length=200)
	block_1 = models.CharField(max_length=200)
	block_2 = models.CharField(max_length=200)
	block_3 = models.CharField(max_length=200)
	block_4 = models.CharField(max_length=200)
	block_5 = models.CharField(max_length=200)
	block_6 = models.CharField(max_length=200)
	ran_ready = models.BooleanField()

	def __str__(self):
		return self.user.username