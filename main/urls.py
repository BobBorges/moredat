from . import views as main_views
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include








urlpatterns = [
    path('i18n', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




urlpatterns += i18n_patterns(
    ###########################
    ## scaffolding site urls ##
    ###########################
    path('', main_views.home_view, name='HOME'),
    path('about-django/', main_views.about_django_view, name='about-django'),
    path('apps-list/', main_views.apps_list_short_descriptions, name='home-apps'),
    path('credits/', main_views.credits_view, name='credits'),
    path('how-to-cite/', main_views.how_to_cite_view, name='how-to-cite'),
    path('quickstart/', main_views.quickstart_view, name='quickstart'),

    ######################
    ## app descriptions ##
    ######################
    path('test-user-audio_descr/', main_views.check_user_audio_descr, name='test-user-audio-descr'),
    path('documentation_descr/', main_views.documentation_descr, name='documentation-descr'),
    path('free-media-upload_descr/', main_views.free_media_upload_descr, name='free-media-upload-descr'),
    path('informed-consent_descr/', main_views.informed_consent_descr, name='informed-consent-descr'),
    path('questionnaires_descr/', main_views.questionnaires_descr, name='questionnaires-descr'),
    path('ran_descr/', main_views.ran_descr, name='ran-descr'),
    path('spn_descr', main_views.spn_descr, name='spn-descr'),
    path('trog-descr/', main_views.trog_descr, name='trog-descr'),
    path('users_descr/', main_views.users_descr, name='users-descr'),
    path('vidnar_descr', main_views.vidnar_descr, name='vidnar-descr'),
    path('wordlist-translation_descr', main_views.wordlist_translation_descr, name='wordlist-translation-descr'),

    ##################
    ## paths to apps #
    ##################
    path('consent/', include('consent.urls')),
    path('documentation/',  include('documentation.urls')),
    path('free-media-upload/', include('freemediaupload.urls')),
    path('questionnaire/', include('questionnaire.urls')),
    path('ran/', include('ran.urls')),
    path('spn/', include('spn.urls')),
    path('trog/', include('trog.urls')),
    path('test-user-audio/', include('testuseraudio.urls')),
    path('users/', include('users.urls')),
    path('vidnar/', include('vidnar.urls')),
    path('wordlist-translation/', include('wordlisttranslation.urls'))
)
