from django.conf.urls import url

from . import views
from quan.views import AboutView, ArticleView, ArticlesView, DashBroadView, TagView

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^p/(?P<post_id>[0-9]+)/$', ArticleView.as_view(), name="article"),
    url(r'^p/$', ArticlesView.as_view(), name="articles"),
    # (?:/(?P<title>[a-zA-Z]+)/)?
    url(r'^u/(?P<user_id>[\w]+)/$', views.user, name="user"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^new/', views.new, name='new'),
    url(r'^about/', AboutView.as_view()),
    url(r'^dashbroad/$', DashBroadView.as_view()),
    url(r'^tag/(?P<tag>[0-9]+/$)', TagView.as_view()),
]
