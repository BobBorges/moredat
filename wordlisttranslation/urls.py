from django.urls import path, include
from . import views as wlt_views




urlpatterns = [
	path('', wlt_views.wlt_home, name='wlt-home'),
	path('<str:word_set>/finish/', wlt_views.wlt_finish, name='wlt-finish'),
	path('<str:word_set>/<str:wordnr>/', wlt_views.wlt_trial, name='wlt-trial'),
	path('<str:word_set>/', wlt_views.wlt_welcome, name='wlt-welcome')
]