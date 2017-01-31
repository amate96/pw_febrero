from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.inicio, name='inicio'),
	url(r'^circun_list/$', views.CircunList.as_view(), name='circun_list'),
	url(r'^circun/detail/(?P<pk>\d+)/$', views.CircunDetail.as_view(), name='circun_detail'),
	url(r'^circun/create/$', views.CircunCreate.as_view(), name='circun_create'),
	url(r'^circun/delete/(?P<pk>\d+)/$', views.CircunDelete.as_view(), name='circun_delete'),
	url(r'^circun/update/(?P<pk>\d+)/$', views.CircunUpdate.as_view(), name='circun_update'),
	url(r'^circun/mesas/(?P<id>\d+)/$', views.mesa_list, name='mesa_list'),
	url(r'^circun/mesas/detail/(?P<id>\d+)/$', views.mesa_detail, name='mesa_detail'),
	url(r'^circun/mesas/create/$', views.mesa_create, name='mesa_create'),
	url(r'^circun/mesas/update/(?P<id>\d+)/$', views.mesa_update, name='mesa_update'),
    
]