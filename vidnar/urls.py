from django.urls import path, include
from . import views as vidnar_views





urlpatterns = [
	path('', vidnar_views.vidnar_home, name='vidnar-home'),
	path('savetrialdata/', vidnar_views.save_trial_data, name='vidnar-save-trial-data'),
	path('<str:vid_set>/finish/', vidnar_views.vidnar_finish, name='vidnar-finish'),
	path('<str:vid_set>/<str:vidnr>/', vidnar_views.vidnar_trial, name='vidnar-trial'),
	path('<str:vid_set>/', vidnar_views.vidnar_welcome, name='vidnar-welcome'),

]