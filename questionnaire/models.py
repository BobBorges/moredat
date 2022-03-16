from django.contrib.auth.models import User
from django.db import models






class Choice(models.Model):
	sort_order = models.IntegerField(blank=True, null=True)
	short_val = models.CharField(max_length=100, blank=True, null=True) #stored in DB
	text = models.TextField(blank=True, null=True) # what user sees

	def __str__(self):
		return self.text



class ChoiceSet(models.Model):
	name = models.CharField(max_length=255)
	choices = models.ManyToManyField(Choice)

	def __str__(self):
		return self.name



QUESTION_TYPES =(
	("ShortText", "Short -one line- free text answer"),
	("RadioSelect", "Options are presented, user selects one"),
	("RadioSelectMulti", "Options are presented, user selects multiple"),
	("RadioSelectOther", "Select predefined options or \'other\' with text input"),
	("RadioSelectOtherMulti", "Select predefined options and / or \'other\' with text input"),
	("TextLong", "Long(ger) -multi line- free text answer"),
	("HorizontalGrid", "Mutliple checkbox-select subquestions in a grid"),

)

class Question(models.Model):
	slug = models.CharField(max_length=255)
	q_type = models.CharField(max_length=255, choices=QUESTION_TYPES)
	text = models.TextField()
	subtext = models.TextField(blank=True, null=True)
	help_text = models.TextField(blank=True, null=True)
	choices = models.ForeignKey(ChoiceSet, on_delete=models.CASCADE, blank=True, null=True)
	sort_order = models.IntegerField()

	def __str__(self):
		return self.slug



class Questionnaire(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	welcome_instructions = models.TextField()
	slug = models.CharField(max_length=255)
	questions = models.ManyToManyField(Question)

	def __str__(self):
		return self.name



class Answer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.TextField()
