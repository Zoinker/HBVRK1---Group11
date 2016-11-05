from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^search/$', views.searchDrivers.as_view(), name='search'),
    #url(r'^upgrade/$', views.becomeDriver.as_view(), name='upgrade'),
    #url(r'^logout/$', views.logout.as_view(), name='logout'),
]
