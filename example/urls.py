from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from crest_app.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(HomeView.as_view())),
    url(r'^login/$', 'example.crest_app.views.login', name='user_login'),
    url(r'^logout/$', 'example.crest_app.views.logout', name='user_logout'),
    #url(r'^done/$', 'example.crest_app.views.done', name='done'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
