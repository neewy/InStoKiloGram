from django.conf.urls import url, include

from . import views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

urlpatterns = [
    url(r'^$', views.food_list, name='food_list'),
    url(r'^food/(?P<pk>[0-9]+)/$', views.food_detail, name='food_detail'),
    url(r'^food/new/$', views.food_new, name='food_new'),
    url(r'^food/(?P<pk>[0-9]+)/edit/$', views.food_edit, name='food_edit'),
]

if settings.DEBUG:

    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL,

            document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

