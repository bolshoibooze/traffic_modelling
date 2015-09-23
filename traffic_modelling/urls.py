"""traffic_modelling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
#from accounts.admin import admin_site
from django.contrib import admin

#from batchimport import urls as batch_urls
from section_loading.views import IndexView
from gis_data.views import *

admin.site.site_header = 'Master Plan-KE Site Admin'

urlpatterns = [
    url(r'^$',IndexView.as_view()),
    url(r'^batchimport/',include('batchimport.urls')),
    url(r'^section_loading/',include('section_loading.urls')),
    url(r'^gis_data/',include('gis_data.urls')),
    
    
    #url(r'^section_loading/', include('section_loading.urls')),
    #url(r'^myadmin/', include(admin_site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^kml/', all_kml)
]
