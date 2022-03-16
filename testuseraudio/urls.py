from django.urls import path
from . import views








urlpatterns = [
	path('', views.test_audio, name='test-user-audio'),
	path('voice_request/', views.voice_request, name='voice-request')
]