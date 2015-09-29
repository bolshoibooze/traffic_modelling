from django.shortcuts import *
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db.models import *



from django.views.generic.list import ListView
from pure_pagination.mixins import PaginationMixin
from django.views.generic import TemplateView
from traffic_modelling.settings import *
from .models import *

#deleted pesky ua_detector views

class IndexView(TemplateView):
    template_name='index.html'


class PipelineSectionLoadingListView(PaginationMixin, ListView):
    model = Pipeline
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   

    
    
class RailBaseSectionLoadingListView(PaginationMixin,ListView):
    model = RBC
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    

    
    
class RailFinalSectionLoadingListView(PaginationMixin,ListView):
    model = RailFinal
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
    
    
class RtfcWSectionLoadingListView(PaginationMixin,ListView):
    model = RailTrafficWorking
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   

    
    
    
class RoadBaseSectionLoadingListView(PaginationMixin,ListView):
    model = RoadBaseCase
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
   
        
class RoadBaseProjectionsListView(PaginationMixin,ListView):
    model = RoadBaseCase
    template_name= 'projections_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
    
    
class BWFSectionLoadingListView(PaginationMixin,ListView):
    model = BWF
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
        
class BWFProjectionsListView(PaginationMixin,ListView):
    model = BWF
    template_name= 'projections_list.html'
    context_object_name='obj'
    paginate_by = 10
   
    
    
    
    
class RoadFinalSectionLoadingListView(PaginationMixin,ListView):
    model = RoadFinal
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
  
    
class RoadFinalProjectionsListView(PaginationMixin,ListView):
    model = RoadFinal
    template_name= 'projections_list.html'
    context_object_name='obj'
    paginate_by = 10
    
   
    
    
class BCSPSectionLoadingListView(PaginationMixin,ListView):
    model = BCSP
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
        
class BCSPProjectionsListView(PaginationMixin,ListView):
    model = BCSP
    template_name= 'projections_list.html'
    context_object_name='obj'
    paginate_by = 10
   
    
    
class xPOLSectionLoadingListView(PaginationMixin,ListView):
    model = xPOL
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
        
class xPOLProjectionsListView(PaginationMixin,ListView):
    model = xPOL
    template_name= 'projections_list.html'
    context_object_name='obj'
    paginate_by = 10
    
   
    
    
class LPWSectionLoadingListView(PaginationMixin,ListView):
    model = LPW
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
        
class LPWProjectionsListView(PaginationMixin,ListView):
    model = LPW
    template_name= 'projections_list.html'
    context_object_name='obj'
    paginate_by = 10
    
   
    
    
class LTFCSectionLoadingListView(PaginationMixin,ListView):
    model = LTFC
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
    
class LTFCProjectionsListView(PaginationMixin,ListView):
    model = LTFC
    template_name= 'projections_list.html'
    context_object_name='obj'
    paginate_by = 10
    
    
    
    
class LPCUSectionLoadingListView(PaginationMixin,ListView):
    model = LPCU
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
  
        
class LPCUProjectionsListView(PaginationMixin,ListView):
    model = LPCU
    template_name= 'projections_list.html'
    context_object_name='obj'
    paginate_by = 10
    
    
    
    
class PLSSectionLoadingListView(PaginationMixin,ListView):
    model = PLS
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
        
class PLSProjectionsListView(PaginationMixin,ListView):
    model = PLS
    template_name= 'projections_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
    

class TTFCPSectionLoadingListView(PaginationMixin,ListView):
    model = TTFCP
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
class TTFCPProjectionsListView(PaginationMixin,ListView):
    model = TTFCP
    template_name= 'projections_list.html'
    context_object_name = 'obj'
    paginate_by = 10
    
   
