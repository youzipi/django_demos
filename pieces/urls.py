from django.conf.urls import url

from pieces.views import HomePageView, CardView

# URLS
URL_ID = "(?P<id>[0-9]+)"
URL_BLOG_ID = "(?P<blog_id>[0-9]+)"
URL_SLUG = "(?P<slug>[a-zA-Z0-9-]+)"

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^%s/$' % URL_ID, CardView.as_view(), name="card_detail"),
    # url(r'^p/$', ArticlesView.as_view(), name="articles"),
    # # (?:/(?P<title>[a-zA-Z]+)/)?
    # url(r'^u/(?P<user_id>[\w]+)/$', views.user, name="user"),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'^new/', views.new, name='new'),
    # url(r'^about/', AboutView.as_view()),
    # url(r'^dashbroad/$', DashBroadView.as_view()),
    # url(r'^py_posts/$', PyPostView.as_view()),
    # url(r'^tag/(?P<tag>[0-9]+/$)', TagView.as_view()),
]
