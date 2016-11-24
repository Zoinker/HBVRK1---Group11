from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SearchFormView.as_view(), name='index'),
    url(r'^$', v)
    #url(r'^upgrade/$', views.becomeDriver.as_view(), name='upgrade'),
    #url(r'^logout/$', views.logout.as_view(), name='logout'),
]
