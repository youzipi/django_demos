from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^p/(?P<post_id>[0-9]+)/$', views.post, name="post"),
    url(r'^u/(?P<user_id>[\w]+)/$', views.user, name="user"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
