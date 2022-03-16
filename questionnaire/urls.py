from django.urls import path, include
from . import views as questionnaire_views






urlpatterns = [
	path('', questionnaire_views.home_view, name='questionnaire-home'),
	path('finish/<str:questionnaire>/', questionnaire_views.finish_view, name='questionnaire-finish'),
	path('download/<str:trgtfile>/', questionnaire_views.file_download, name='questionnaire-download'),
	path('<str:questionnaire>/', questionnaire_views.welcome_view, name='questionnaire-welcome'),
	path('<str:questionnaire>/<str:question>/', questionnaire_views.question_view, name='questionnaire-question'),
]
