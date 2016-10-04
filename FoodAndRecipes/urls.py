from django.conf.urls import url, include

from . import views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

urlpatterns = [
    url(r'^$', views.recipe_list, name='recipe_list'),
    url(r'^recipe/(?P<pk>[0-9]+)/$', views.recipe_detail, name='recipe_detail'),
    url(r'^recipe/new/$', views.recipe_new, name='recipe_new'),
    url(r'^recipe/(?P<pk>[0-9]+)/edit/$', views.recipe_edit, name='recipe_edit'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search-form/$', views.search_form, name='search-form')
]

if settings.DEBUG:

    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL,

            document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

