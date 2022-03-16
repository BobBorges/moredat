from django.urls import path, include
from . import views as medupviews




urlpatterns = [
	path('', medupviews.freemediaupload_view, name='freemediaupload'),
	path('thx/', medupviews.thx_view, name='thx4upload')
]