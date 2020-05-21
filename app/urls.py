from django.conf.urls import url
from .views import app_detail_view, app_list_view, AppListView, AppDetailView

urlpatterns = [
    url(r'^$', app_list_view, name='list'),
    url(r'^1/$', app_detail_view, name='detail'),
]