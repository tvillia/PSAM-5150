from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(''
	url(r'^dolaicontact/$', 'contact.views.my_contact', name='dolaicontact'),
	url(r'^received/$', 'contact.views.received', name='received'), 
)