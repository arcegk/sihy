from django.conf.urls import patterns, include, url
from django.contrib import admin
from map.views import MapView , PrintView
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appHidrica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   	url(r'^$', MapView.as_view() , name = "home"),
   	url(r'^print/$', PrintView.as_view() , name = "print"),
   	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
)
