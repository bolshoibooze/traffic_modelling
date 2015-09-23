from django.shortcuts import *
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db.models import *


from ua_detector.views import *
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from traffic_modelling.settings import *
from ua_detector.generic_views import *
from ua_detector.model_views import *
from .models import *


class IndexView(TemplateView):
    template_name='index.html'


class PipelineSectionLoadingListView(ListView):
    model = Pipeline
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(PipelineSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = Pipeline.objects.all()
        return context
    
    

    
    
class RailBaseSectionLoadingListView(ListView):
    model = RBC
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(RailBaseSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = RBC.objects.all()
        return context
    

    
    
class RailFinalSectionLoadingListView(ListView):
    model = RailFinal
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(RailFinalSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = RailFinal.objects.all()
        return context
    

    
    
    
class RtfcWSectionLoadingListView(ListView):
    model = RailTrafficWorking
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(RtfcWSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = RailTrafficWorking.objects.all()
        return context
    

    
    
    
class RoadBaseSectionLoadingListView(ListView):
    model = RoadBaseCase
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(RoadBaseSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = RoadBaseCase.objects.all()
        return context
    
class RoadBaseProjectionsListView(ListView):
    model = RoadBaseCase
    template_name= 'projections_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(RoadBaseProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = RoadBaseCase.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context
    
    
    
class BWFSectionLoadingListView(ListView):
    model = BWF
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(BWFSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = BWF.objects.all()
        return context
    
class BWFProjectionsListView(ListView):
    model = BWF
    template_name= 'projections_list.html'
    context_object_name='obj'
    
    
    def get_context_data(self,**kwargs):
        context = super(BWFProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = BWF.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context
    
    
    
    
    
class RoadFinalSectionLoadingListView(ListView):
    model = RoadFinal
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(RoadFinalSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = RoadFinal.objects.all()
        return context
    
    
class RoadFinalProjectionsListView(ListView):
    model = RoadFinal
    template_name= 'projections_list.html'
    context_object_name='obj'
    
    def get_context_data(self,**kwargs):
        context = super(RoadFinalProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = RoadFinal.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context
    
    
    
class BCSPSectionLoadingListView(ModelListView):
    model = BCSP
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(BCSPSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = BCSP.objects.all()
        return context
    
class BCSPProjectionsListView(ListView):
    model = BCSP
    template_name= 'projections_list.html'
    context_object_name='obj'
    
    def get_context_data(self,**kwargs):
        context = super(BCSPProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = BCSP.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context
    
    
    
class xPOLSectionLoadingListView(ListView):
    model = xPOL
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(xPOLSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = xPOL.objects.all()
        return context
    
class xPOLProjectionsListView(ListView):
    model = xPOL
    template_name= 'projections_list.html'
    context_object_name='obj'
    
    def get_context_data(self,**kwargs):
        context = super(xPOLProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = xPOL.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context
    
    
    
class LPWSectionLoadingListView(ListView):
    model = LPW
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(LPWSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = LPW.objects.all()
        return context
    
class LPWProjectionsListView(ListView):
    model = LPW
    template_name= 'projections_list.html'
    context_object_name='obj'
    
    def get_context_data(self,**kwargs):
        context = super(LPWProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = LPW.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context
    
    
    
class LTFCSectionLoadingListView(ListView):
    model = LTFC
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(LTFCSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = LTFC.objects.all()
        return context
    
class LTFCProjectionsListView(ListView):
    model = LTFC
    template_name= 'projections_list.html'
    context_object_name='obj'
    
    def get_context_data(self,**kwargs):
        context = super(LTFCProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = LTFC.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context
    
    
    
class LPCUSectionLoadingListView(ListView):
    model = LPCU
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(LPCUSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = LPCU.objects.all()
        return context
    
class LPCUProjectionsListView(ListView):
    model = LPCU
    template_name= 'projections_list.html'
    context_object_name='obj'
    
    def get_context_data(self,**kwargs):
        context = super(LPCUProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = LPCU.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context
    
    
    
class PLSSectionLoadingListView(ListView):
    model = PLS
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(PLSSectionLoadingListView,self).get_context_data(**kwargs)
        context['obj_list'] = PLS.objects.all()
        return context
    
class PLSProjectionsListView(ListView):
    model = PLS
    template_name= 'projections_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(PLSProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = PLS.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context
    
    

class TTFCPSectionLoadingListView(ListView):
    model = TTFCP
    template_name= 'section_loading_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(TTFCPSectionLoadingListViewself).get_context_data(**kwargs)
        context['obj_list'] = TTFCP.objects.all()
        return context
    
class TTFCPProjectionsListView(ListView):
    model = TTFCP
    template_name= 'projections_list.html'
    context_object_name = 'obj'
    
    def get_context_data(self,**kwargs):
        context = super(TTFCPProjectionsListView,self).get_context_data(**kwargs)
        context['obj_list'] = TTFCP.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
        return context

"""
<!----
                                                                             <a href="{% url '' %}"> </a> |<a href="{% url '' %}"> </a> |
                                                                             <a href="{% url '' %}"> </a> |<a href="{% url '' %}"> </a> |
                                                                             <a href="{% url '' %}"> </a> |<a href="{% url '' %}"> </a> |
                                                                             --->         

"""   
    
 
