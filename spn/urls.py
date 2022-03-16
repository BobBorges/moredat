from django.urls import path, include
from . import views as spn_views





urlpatterns = [
	path('', spn_views.home_view, name='spn-home'),
	path('<str:pic_set>/finish/', spn_views.finish_view, name='spn-finish'),
	path('<str:pic_set>/<str:picnr>/', spn_views.pic_view, name='spn-pic'),
	path('<str:pic_set>/', spn_views.welcome_view, name='spn-welcome')
]