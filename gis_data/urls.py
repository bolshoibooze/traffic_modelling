from django.conf.urls import *
from django.views.generic import TemplateView
from djgeojson.views import *
from .views import *
from .models import *



urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Town), name='data'),
    
     url(r'^sections/$', TemplateView.as_view(template_name='section.html'), name='sections'),
    url(r'^section.geojson$', GeoJSONLayerView.as_view(model=Section), name='section'),
    
    url(r'^roads/$', TemplateView.as_view(template_name='roads.html'), name='roads'),
    url(r'^road_data.geojson$', GeoJSONLayerView.as_view(model=MajorRoad), name='road_data'),
    
    url(r'^road_stretch/$', TemplateView.as_view(template_name='road_stretch.html'), name='road_stretch'),
    url(r'^stretch.geojson$', GeoJSONLayerView.as_view(model=StretchData), name='stretch'),
    
    url(r'^groad/$', TemplateView.as_view(template_name='google_roads.html'), name='groad'),
    url(r'^google.geojson$', GeoJSONLayerView.as_view(model=GoogleRoads), name='google'),
    
    url(r'^kml/', all_kml),
    url(r'^map/$',TemplateView.as_view(template_name='map.html'),name='map'),
    
    url(r'^layer/$',TemplateView.as_view(template_name='openlayers.html'),name='layer'),
    
    url(r'^test/$',TemplateView.as_view(template_name='qgis_to_leaflet.html'),name='test'),
    
    #url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Stretch), name='data'),
    
    #url(r'^test/$',TemplateView.as_view(template_name='gis_test.html'),name='test'),
    
    
    
    #url(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).json$',GeoJSONTile(Town, geometry_field='geom', trim_to_boundary=True), name='tiled_data')
    #url(r'^mushrooms.geojson$', MapLayer.as_view(model=MushroomSpot, properties=('name',)), name='mushrooms')
]
