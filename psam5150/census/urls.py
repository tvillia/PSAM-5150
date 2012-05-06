from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^dolaicensus/$', 'census.views.dolai_census', name='dolaicensus'),
	url(r'^received/$', 'census.views.received', name='received'),
	)