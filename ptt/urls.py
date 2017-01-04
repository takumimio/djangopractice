from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.post_list),
	url(r'^hire$', views.post_hire),
)