from .forms import *
from .models import Questionnaire, Question, Answer, ChoiceSet
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render, redirect
from django.template import Template, Context
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from users.decorators import user_consented
from users.models import UserDetails









def CompileQuestion(UD_object, qtext):
	question_context = Context({
		"language": UD_object.research_group.target_language,
		"language2": UD_object.research_group.other_language
	})
	question_text = Template(qtext)
	return question_text.render(question_context)




def MakeQuestionForm(UD_object, Q, idx, RP=None):
	multianswer = False
	otherField = False
	horizontalRadio = False


	QT = Q.q_type
	if RP:
		form = QuestionForm(RP, prefix=idx)
	else:
		form = QuestionForm(prefix=idx)


	if QT == 'ShortText':
		form.fields['answer'].widget = forms.TextInput(
			attrs={"id": f'{idx}_answer', "name": f"{idx}_answer"}
		)
		form.fields['answer'].label = CompileQuestion(UD_object, Q.subtext)

	if QT == "RadioSelect":
		opts = []
		for choice_obj in Q.choices.choices.all():
			opts.append((choice_obj.short_val, choice_obj.text))
		opts = tuple(opts)
		form.fields['answer'].widget = forms.RadioSelect(
			choices=opts, attrs={"id": f'{idx}_answer', "name": f"{idx}_answer"}
		)
		form.fields['answer'].label = CompileQuestion(UD_object, Q.subtext)

	if QT == "RadioSelectMulti":
		opts = []
		for choice_obj in Q.choices.choices.all():
			opts.append((
				CompileQuestion(UD_object, choice_obj.short_val), 
				CompileQuestion(UD_object, choice_obj.text)
			))
		opts = tuple(opts)
		form.fields['answer'].widget = forms.CheckboxSelectMultiple(
			choices=opts, 
			attrs={"id": f'{idx}_answer', "name": f"{idx}_answer"}
		)
		form.fields['answer'].label = CompileQuestion(UD_object, Q.subtext)
		multianswer = True

	if QT == "RadioSelectOther":
		opts = []
		for choice_obj in Q.choices.choices.all().order_by('sort_order'):
			opts.append((
				CompileQuestion(UD_object, choice_obj.short_val), 
				CompileQuestion(UD_object, choice_obj.text)
			))
		opts = tuple(opts)
		form.fields['answer'].widget = forms.RadioSelect(
			choices=opts, 
			attrs={"id": f'{idx}_answer', "name": f"{idx}_answer"}
		)
		form.fields['answer'].label = CompileQuestion(UD_object, Q.subtext)
		otherField = True

	if QT == "RadioSelectOtherMulti":
		opts = []
		for choice_obj in Q.choices.choices.all().order_by('sort_order'):
			opts.append((
				CompileQuestion(UD_object, choice_obj.short_val), 
				CompileQuestion(UD_object, choice_obj.text)
			))
		opts = tuple(opts)
		form.fields['answer'].widget = forms.CheckboxSelectMultiple(
			choices=opts, 
			attrs={"id": f'{idx}_answer', "name": f"{idx}_answer"}
		)
		form.fields['answer'].label = CompileQuestion(UD_object, Q.subtext)
		otherField = True
		multianswer = True

	if QT == "TextLong":
		form.fields['answer'].widget = forms.Textarea(attrs={"id": f"{idx}_answer"})
		form.fields['answer'].label = CompileQuestion(UD_object, Q.subtext)

	if QT == "HorizontalGrid":
		opts = []
		for choice_obj in Q.choices.choices.all().order_by('sort_order'):
			opts.append((
				CompileQuestion(UD_object, choice_obj.short_val), 
				CompileQuestion(UD_object, choice_obj.text)
			))
		opts = tuple(opts)
		form.fields['answer'].widget = forms.RadioSelect(
			choices=opts, 
			attrs={"id": f'{idx}_answer', "name": f"{idx}_answer"}
		)
		form.fields['answer'].label = CompileQuestion(UD_object, Q.subtext)
		horizontalRadio = True

	return form, multianswer, otherField, horizontalRadio




def get_next_slug(questionnaire, question):
	current_questionnaire = Questionnaire.objects.get(slug=questionnaire)
	questiones = current_questionnaire.questions.all().order_by('sort_order')
	slugs = []
	for q in questiones:
		if q.slug not in slugs:
			slugs.append(q.slug)
	qidx = slugs.index(question)
	if qidx + 1 < len(slugs):
		return slugs[qidx+1], qidx+1, len(slugs) 
	else:
		return 'questionnaire-finish', qidx+1, len(slugs) 




@login_required
@user_consented
def home_view(request):
	context = {"title": "MoReDaT Questionnaire"}
	questionnaires = Questionnaire.objects.all()
	context['questionnaires'] = questionnaires
	return render(request, 'questionnaire/questionnaire-home.html', context)



@login_required
@user_consented
def welcome_view(request, questionnaire):

	#check here if user already answered questionnaire ---> redirect profile

	UD_object = UserDetails.objects.get(user=request.user)
	context = {"title": "MoReDaT Questionnaire"}
	current_questionnaire = Questionnaire.objects.get(slug=questionnaire)
	context['questionnaire_obj'] = current_questionnaire
	QOs = current_questionnaire.questions.all().order_by('sort_order')
	
	qslugs = []
	for QO in QOs:
		if QO.slug not in qslugs:
			qslugs.append(QO.slug)
	
	Qs = []
	for qslug in qslugs:
		questions = QOs.filter(slug=qslug)
		if len(questions) == 1:
			for q in questions:
				subtxt = None
				if q.subtext:
					subtxt = q.subtext
				Qs.append((qslug, CompileQuestion(UD_object, q.text), [subtxt]))
		else:
			subtxts = []
			for q in questions:
				if q.subtext:
					subtxts.append(q.subtext)
			Qs.append((qslug, CompileQuestion(UD_object, questions[0].text), subtxts))

	context['Q_objs'] =  Qs
	return render(request, 'questionnaire/questionnaire-welcome.html', context)




@login_required
@user_consented
def question_view(request, questionnaire, question):
	if question == 'questionnaire-finish':
		return redirect('questionnaire-finish', questionnaire=questionnaire)

	UD_object = UserDetails.objects.get(user=request.user)
	next_slug, q_num, total_q = get_next_slug(questionnaire, question)
	context = {"title": "MoReDaT Questionnaire"}
	context['questionnaire_slug'] = questionnaire
	context['next_slug'] = next_slug
	context['q_num'] = q_num
	context['total_q'] = total_q

	#check here if user already answered question ---> redirect next_slug

	current_questions = Question.objects.filter(slug=question).order_by('sort_order')
	question_forms = {}
	POSTbool = False
	otherform = None
	all_true = []

	if current_questions[0].q_type == "HorizontalGrid":
		context['helptext'] = current_questions[0].help_text
		
	context['q_text'] = CompileQuestion(UD_object, current_questions[0].text)


	for qidx, current_question in enumerate(current_questions):
		if request.method == 'POST':
			POSTbool = True
			question_form, multianswer, otherField, horizontalRadio = MakeQuestionForm(
				UD_object, current_question, qidx, request.POST
			)
			if otherField:
				otherform = OtherFieldForm(request.POST, prefix=qidx)
				otherform.fields['other_field'].widget = forms.TextInput(
					attrs={"id": f'{qidx}_other_field',
						"class": "textinput textInput form-control"
					}
				)
			if horizontalRadio:
				context['horizontalRadio'] = True
			question_forms[f'form{qidx}'] = (question_form, multianswer, 
				otherform, current_question
			)

			if question_form.is_valid():
				if otherField:
					if otherform.is_valid():
						all_true.append(True)
					else:
						all_true.append(False)
				else:
					all_true.append(True)
			else:
				all_true.append(False)
		else:
			question_form, multianswer, otherField, horizontalRadio = MakeQuestionForm(
				UD_object, current_question, qidx
			)
			if otherField:
				otherform = OtherFieldForm(prefix=qidx)
				
				otherform.fields['other_field'].widget = forms.TextInput(
					attrs={"id": f'{qidx}_other_field',
						"class": "textinput textInput form-control"
					}
				)
			if horizontalRadio:
				context['horizontalRadio'] = True

			question_forms[f'form{qidx}'] = (question_form, multianswer, otherform)
	

	if POSTbool == True:
		if len(all_true) == len(current_questions) \
		and len(set(all_true)) == 1 \
		and all_true[0] == True:
			for k, v in question_forms.items():
				#print(k,v[0])
				if v[2]:
					if len(v[2].cleaned_data) > 0:
						print(v[2].cleaned_data)
						Answer.objects.create(
							answer = v[2].cleaned_data['other_field'],
							user = request.user,
							questionnaire = Questionnaire.objects.get(slug=questionnaire),
							question = v[3]
						)
				if v[1] == True: 
					if 'answer' in v[0].cleaned_data:
						print(v[0].cleaned_data)
						for a in v[0].cleaned_data['answer'].strip('[]').split(', '):
							Answer.objects.create(
								answer = a.strip("'"), 
								user = request.user, 
								questionnaire = Questionnaire.objects.get(slug=questionnaire),
								question = v[3]
							)
				else:
					print(v[0])
					v[0].instance.user = request.user
					v[0].instance.questionnaire = Questionnaire.objects.get(slug=questionnaire)
					v[0].instance.question = v[3]
					#print(v[0].cleaned_data)
					v[0].save()
		return redirect(
			'questionnaire-question', 
			questionnaire=questionnaire, 
			question=next_slug
		)

	context['question_forms'] = question_forms
	return render(request, 'questionnaire/questionnaire-question.html', context)




@login_required
@user_consented
def finish_view(request, questionnaire):
	context = {
		"title":"MoReDaT Questionnaire",
		"questionnaire": Questionnaire.objects.get(slug=questionnaire)
	}
	return render(request, 'questionnaire/questionnaire-finish.html', context)




@login_required
def file_download(request, trgtfile):
	file_path = f'static/questionnaire/docs/{trgtfile}'
	try:
		return FileResponse(open(file_path, 'rb'), content_type='contenttype/pdf')
	except FileNotFoundError:
		raise Http404()
