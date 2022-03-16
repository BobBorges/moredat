from django.urls import path
from . import views as ran_views








urlpatterns = [
	path('postpractice/', ran_views.ran_post_practice, name='ran-postpractice'),
	path('finish/', ran_views.ran_finish, name='ran-finish'),
	path('', ran_views.ran_welcome, name='ran-welcome'),
	path('savetrialdata/', ran_views.save_trial_data, name='save-trial-data'),	
	path('trialblock/<str:block>/', ran_views.ran_trial_block, name='ran-trialblock')
]