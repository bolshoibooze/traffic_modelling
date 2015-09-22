
from django.conf.urls import include, url
from accounts.admin import admin_site
from django.contrib import admin

#from batchimport import urls as batch_urls
from gis_data.views import *

urlpatterns = [
    url(r'^batchimport/',include('batchimport.urls')),
    #url(r'^gis_data/',include('gis_data.urls')),
    
    #url(r'^section_loading/', include('section_loading.urls')),
    url(r'^myadmin/', include(admin_site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^kml/', all_kml)
]
