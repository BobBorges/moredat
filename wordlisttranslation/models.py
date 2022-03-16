from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from main.models import Tasks



class WordlistWord(models.Model):
	word = models.CharField(max_length=510)
	sort_order = models.IntegerField()

	def __str__(self):
		return self.word


class WordlistWordSet(models.Model):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	words = models.ManyToManyField(WordlistWord)
	description = models.TextField(blank=True)
	source = models.TextField(blank=True, null=True)
	special_instructions = models.TextField(blank=True)

	def __str__(self):
		return self.name




WL_RESPONSE_TYPE = (
	("Record response", _('Record response')),
	("I don't remember", _("I don't remember")),
	("I don't know", _("I don't know"))
)
class WordlistResponse(models.Model):
	task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
	word = models.ForeignKey(WordlistWord, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	response_type = models.CharField(max_length=255, choices=WL_RESPONSE_TYPE)
	audio_response = models.CharField(max_length=255, blank=True, null=True)
	written_response = models.CharField(max_length=255, blank=True, null=True)
	commentary = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.word.word