from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField
from main.models import Tasks
from tinymce import models as tinymce_models
from tinymce.models import HTMLField








class ResearchGroups(models.Model):
	group_name = models.CharField(max_length=255)
	target_language = models.CharField(max_length=255)
	other_language = models.CharField(max_length=255, blank=True, null=True)
	target_lang_short_name = models.CharField(max_length=10)
	other_langauge_short_name = models.CharField(max_length=10) #langAUge spelled wrong, but ALL references across the project will need to be fixed :|
	description = models.TextField()
	slug = models.SlugField()

	def __str__(self):
		return self.group_name




GENDER_OPTIONS = [
	('male', 'Male'),
	('female', 'Female'),
	('other', 'Other / Rather not say.')
]

class UserDetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	research_group = models.ForeignKey(ResearchGroups, on_delete=models.CASCADE)
	birth_date = models.DateField()
	gender = models.CharField(max_length=100, choices=GENDER_OPTIONS)
	user_bio = tinymce_models.HTMLField(blank=True, default='.')
	profile_pic = ResizedImageField(size=[300,400], quality=100, upload_to="static/users/profile_pictures/", default="static/users/profile_pictures/default.png")

	def __str__(self):
		return self.user.username



class AssignedTasks(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
	complete = models.BooleanField(default=False)




class DefaultAssignedTasksByGroup(models.Model):
	group_name = models.ForeignKey(ResearchGroups, on_delete=models.CASCADE)
	task = models.ForeignKey(Tasks, on_delete=models.CASCADE)