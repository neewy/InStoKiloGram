from django.conf.urls import url, include

from . import views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

urlpatterns = [
    url(r'^$', views.exercise_list, name='exercise_list'),
    url(r'^exercise/(?P<pk>[0-9]+)/$', views.exercise_detail, name='exercise_detail'),
    url(r'^exercise/new/$', views.exercise_new, name='exercise_new'),
    url(r'^exercise/(?P<pk>[0-9]+)/edit/$', views.exercise_edit, name='exercise_edit'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search-form/$', views.search_form, name='search-form')
]

if settings.DEBUG:

    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL,

            document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

