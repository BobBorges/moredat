from django.contrib.auth.models import User
from django.db import models




class TrogOrder(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
	trog_ready = models.BooleanField()
	practice_block = models.CharField(max_length=500)
	block_1 = models.CharField(max_length=500)
	block_2 = models.CharField(max_length=500)
	block_3 = models.CharField(max_length=500)
	block_4 = models.CharField(max_length=500)
	block_5 = models.CharField(max_length=500)
	block_6 = models.CharField(max_length=500)
	block_7 = models.CharField(max_length=500)
	block_8 = models.CharField(max_length=500)





class TrogResponse(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	click_quadrant = models.CharField(max_length=3)
	selected_stimulus = models.CharField(max_length=10)
	audio_repeats = models.IntegerField()
	render_time = models.CharField(max_length=255)
	click_time = models.CharField(max_length=255)
