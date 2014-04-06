from django.conf.urls import patterns, include, url
from mysite.views import homepage
from mysite.view1 import rssreader1
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', homepage),
    url(r'^rssreader/$', rssreader1),
    url(r'^rssreader/?kodikos=(\d{1,2})$', rssreader1),
    url(r'^admin/', include(admin.site.urls)),
)
