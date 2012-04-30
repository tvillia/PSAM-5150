from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^dolaicontact/$', 'contact.views.dolai_contact', name='dolaicontact'),
	url(r'^received/$', 'contact.views.received', name='received'),
	)