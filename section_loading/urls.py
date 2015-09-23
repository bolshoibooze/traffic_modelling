from django.conf.urls import *
from django.views.generic import TemplateView
from djgeojson.views import *
from section_loading.views import *
from .models import *



urlpatterns = [
    url(r'^index/$',IndexView.as_view(),name='index'),
    
    url(r'^datasets/$',TemplateView.as_view(template_name='datasets.html'),name='datasets'),
    
    url(r'^road-base-case-section-loading/$',RoadBaseSectionLoadingListView.as_view(),name='rdbase'),
    url(r'^road-base-case-projections/$',RoadBaseProjectionsListView.as_view(),name='rdbaseprojctns'),
    
    url(r'^total-traffic/$',TTFCPSectionLoadingListView.as_view(),name='total-traffic'),
    url(r'^total-traffic-projections/$',TTFCPProjectionsListView.as_view(),name='total-traffic-projections'),
    
    url(r'^pls/$',PLSSectionLoadingListView.as_view(),name='pls'),
    url(r'^pls-projections/$',PLSProjectionsListView.as_view(),name='pls-projections'),
    
    url(r'^lpcu/$',LPCUSectionLoadingListView.as_view(),name='lpcu'),
    url(r'^lpcu-projections/$',LPCUProjectionsListView.as_view(),name='lpcu-projections'),
    
    url(r'^ltfc/$',LTFCSectionLoadingListView.as_view(),name='ltfc'),
    url(r'^ltfc-projections/$',LTFCProjectionsListView.as_view(),name='ltfc-projections'),
    
    url(r'^lpw/$',LPWSectionLoadingListView.as_view(),name='lpw'),
    url(r'^lpw-projections/$',LPWProjectionsListView.as_view(),name='lpw-projections'),
    
    url(r'^expol/$',xPOLSectionLoadingListView.as_view(),name='expol'),
    url(r'^expol-projections/$',xPOLProjectionsListView.as_view(),name='expol-projections'),
    
    url(r'^bcsp/$',BCSPSectionLoadingListView.as_view(),name='bcsp'),
    url(r'^bcsp-projections/$',BCSPProjectionsListView.as_view(),name='bcsp-projections'),
    
    url(r'^rdfinal/$',RoadFinalSectionLoadingListView.as_view(),name='rdfinal'),
    url(r'^rdfinal-projections/$',RoadFinalProjectionsListView.as_view(),name='rdfinal-projections'),
    
    url(r'^bwf/$',BWFSectionLoadingListView.as_view(),name='bwf'),
    url(r'^bwf-projections/$',BWFProjectionsListView.as_view(),name='bwf-projections'),
    
   
    
    url(r'^pipeline/$',PipelineSectionLoadingListView.as_view(),name='pipeline'),
    url(r'^rail-base/$',RailBaseSectionLoadingListView.as_view(),name='rail-base'),
    url(r'^rail-final/$',RailFinalSectionLoadingListView.as_view(),name='rail-final'),
    url(r'^rltfc/$',RtfcWSectionLoadingListView.as_view(),name='rltfc'),
    
    
    
    
    
    #url(r'^test/$',TemplateView.as_view(template_name='gis_test.html'),name='test'),
   
    
    #url(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).json$',GeoJSONTile(Town, geometry_field='geom', trim_to_boundary=True), name='tiled_data')
    #url(r'^mushrooms.geojson$', MapLayer.as_view(model=MushroomSpot, properties=('name',)), name='mushrooms')
]
