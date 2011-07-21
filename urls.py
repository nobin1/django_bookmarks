import os
from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from bookmarks.views import *

static = os.path.join(os.path.dirname(__file__), 'static')

urlpatterns = patterns('',
	# Browsing
	(r'^$', main_page),
	(r'^user/(\w+)/$', user_page),
	(r'^search/$', search_page),
	(r'^popular/$', popular_page),
	(r'^tag/([^\s]+)/$', tag_page),
	(r'^bookmark/(\d+)/$', bookmark_page),
	# Session management
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),
	(r'^register/$', register_page),
	(r'^register/success/$', direct_to_template,
	{'template': 'registration/register_success.html'}),
	# Account management
	(r'^save/$', bookmark_save_page),
	(r'^vote/$', bookmark_vote_page),
	# Site media
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': static}),
	# Comments
	#(r'^comments/',	include('django.contrib.comments.urls')),
	# i18n
	#(r'^i18n/', include('django.conf.urls.i18n')),
	# Ajax
	(r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),
	# Friends
	(r'^friends/(\w+)/$', friends_page),
	(r'^friend/add/$', friend_add),
	)
