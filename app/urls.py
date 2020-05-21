from django.conf.urls import url, include
from django.conf import settings
from .views import *

urlpatterns = [
    url(r'^$', AppListView.as_view(), name='list'),
    url(r'^create/$', AppCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', AppDetailView.as_view(), name='detail'),
]