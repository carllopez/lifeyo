"""
Users app URLs
"""
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = patterns('lifeyo.users.views',
    url(r'^$', views.UsersListView.as_view(), name='users-list'),
    url(r'^(?P<pk>[\d]+)/$', views.UserInstanceView.as_view(), name='user-instance'),
)

urlpatterns += staticfiles_urlpatterns()
