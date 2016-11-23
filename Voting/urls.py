from django.conf.urls import url
from Voting import views as vviews

urlpatterns = [
    url(r'^vote/(?P<poll_pk>\d+)/$', vviews.vote, name='poll_ajax_vote'),
    url(r'^poll/(?P<poll_pk>\d+)/$', vviews.poll, name='poll'),
    url(r'^result/(?P<poll_pk>\d+)/$', vviews.result, name='poll_result'),
]
