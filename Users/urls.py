from django.conf.urls import url

from . import views
from Weight import views as wviews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^weight/$',wviews.wview, name='wview'),
    url(r'^accounts/profile/$',views.accountsprofile, name='accountsprofile'),
    url(r'^myprofile/$',views.myprofile, name='myprofile'),
]

