from django.conf.urls import patterns, include, url
from . import views
from django.views.decorators.chache import cache_page



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appHidrica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^map/', views.MapView.as_view(), name="mape"),
    url(r'^map/', views.PrintView.as_view(), name="print"),
 	
 )