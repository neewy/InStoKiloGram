from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^diet/$', views.diet_list, name='diet_list'),
    url(r'^diet/(?P<pk>[0-9]+)/$', views.diet_detail, name='diet_detail'),
    url(r'^new_diet/$', views.new_diet, name='new_diet'),
    url(r'^edit_diet/(?P<pk>[0-9]+)$', views.diet_edit, name='edit_diet'),
    url(r'^new_review/$', views.new_review, name='new_review'),
    url(r'^edit_review/(?P<pk>[0-9]+)$', views.review_edit, name='edit_review'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()