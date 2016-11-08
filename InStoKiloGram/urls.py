"""InStoKiloGram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from Users import views
from Weight import views as wviews

urlpatterns = [
    url(r'^weight/add/$',wviews.wadd, name='wadd'),
    url(r'^weight/delete/$',wviews.wdelete, name='wdelete'),
    url(r'^weight/stat/$',wviews.wstat, name='wstat'),
    url(r'^weight/$',wviews.wview, name='wview'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('Blog.urls')),
    url(r'', include('Diets.urls')),
    url(r'^users/', include('Users.urls')),
    url(r'^login/$',views.customlogin, name='login'),
    url(r'^logout/$',views.customlogout, name='logout'),
    url(r'^vklogin/$',views.vklogin, name='vklogin'),
    url(r'^vkoauth/$',views.vkoauth, name='vkoauth'),
    url(r'^vkoauthcb/$',views.vkoauthcb, name='vkoauthcb'),
    url(r'^accounts/profile/$',views.accountsprofile, name='accountsprofile'),
    url(r'^register/$',views.customregister, name='register'),
    url(r'^exercises/', include('Exercises.urls')),
    url(r'^food/', include('Food.urls')),
]
