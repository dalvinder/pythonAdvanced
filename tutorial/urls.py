from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.list import ListView
from polls.models import Poll
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^tutorial/', include('tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',TemplateView.as_view(
        template_name='home.html'
    ),name='home'),
    url(r'^polls/$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date'),
            context_object_name = 'latest_poll_list',
            template_name='polls/index.html'
        ),
        name="polls_home"),
    url(r'^polls/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html'
        ),
        name="detail"),
    url(r'^polls/(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'
        ),
        name="results"),
    
    url(r'^polls/(?P<poll_id>\d+)/vote/$','polls.views.vote',name="vote"),
    url(r'',include('social_auth.urls')),
    url(r'logout/$',logout, {'next_page':'/'},name='logout'),
)
