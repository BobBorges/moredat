from django.urls import path, include
from . import views as trog_views




urlpatterns = [
	path('', trog_views.welcome, name='trog-welcome'),
	path('block/<str:TROGblock>/', trog_views.block, name='trog-block'),
	path('postpractice/', trog_views.postpractice, name='trog-postpractice'),
	path('finish', trog_views.finish, name='trog-finish'),
	path('savedata/', trog_views.save_data, name='trog-savedata')
]