from django.conf.urls import patterns, include, url

from polls.views import index

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^tutorial/', include('tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^polls/$', 'poll.views.index'),
    url(r'^polls/$', index),
    url(r'^polls/(?P<poll_id>\d+)/$','polls.views.detail',name="detail"),
    url(r'^polls/(?P<poll_id>\d+)/results/$','polls.views.results', name="results"),
    url(r'^polls/(?P<poll_id>\d+)/vote/$','polls.views.vote',name="vote"),
)
