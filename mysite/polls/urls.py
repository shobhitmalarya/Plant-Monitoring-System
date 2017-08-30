from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [

    url(r'^ch/$', views.exp.as_view(), name = 'expview'),
    url(r'^$', views.index, name='index'),
]
