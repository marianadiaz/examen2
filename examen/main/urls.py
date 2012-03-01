from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
    url(r'^$', 'home', name='home'),
    url(r'^zombie/(?P<pk>\d+)$', 'show_zombie', name='show_zombie'),
   	url(r'^zombie/add/$', 'add_zombie',name='add_zombie'),
   	url(r'^tweet/add/$', 'add_tweet',name='add_tweet'),
	url(r'^zombie/(?P<pk>\d+)/edit$', 'edit_zombie', name='edit_zombie'),   
	url(r'^tweet/(?P<pk>\d+)/edit$', 'edit_tweet', name='edit_tweet'),   
	url(r'^zombie/(?P<pk>\d+)/delete$', 'delete_zombie', name='delete_zombie'),   
	url(r'^tweet/(?P<pk>\d+)/delete$', 'delete_tweet', name='delete_tweet'),   

)
