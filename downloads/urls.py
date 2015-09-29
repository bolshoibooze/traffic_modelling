from django.conf.urls import *
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views
#from .views import *
from .models import *



urlpatterns = [
    url(r'^downloads/$',login_required(TemplateView.as_view(template_name='downloads.html')),
        name='downloads'),
    
    url(r'^road-bs-cs-sl-excel/$',views.road_bs_cs_section_loading,name='road-bs-cs-sl-excel'),   
    url(r'^road-bs-cs-sl-csv/$',views.road_bs_cs_section_loading_csv,name='road-bs-cs-sl-csv'),
        
    url(r'^road-bs-cs-pjs-excel/$',views.road_bs_cs_projections,name='road-bs-cs-pjs-excel'),
    url(r'^road-bs-cs-pjs-csv/$',views.road_bs_cs_projections_csv,name='road-bs-cs-pjs-csv'),
    
    
    
    
    url(r'^pipeline-excel/$',views.pipeline_section_loading , name='pipeline-excel'),
    url(r'^pipeline-csv/$',views.pipeline_section_loading_csv , name='pipeline-csv'),
    
    
    url(r'^rail-bs-cs-excel/$',views.rail_bs_cs_section_loading , name='rail-bs-cs-excel'),
    url(r'^rail-bs-cs-csv/$',views.rail_bs_cs_section_loading_csv , name='rail-bs-cs-csv'),
    
    
    
    url(r'^rl-final-excel/$',views.rl_final_section_loading , name='rl-final-excel'),
    url(r'^rl-final-csv/$',views.rl_final_section_loading_csv , name='rl-final-csv'),
    
    
    url(r'^rltf-wrking-excel/$',views.rltfc_working_section_loading , name='rltf-wrking-excel'),
    url(r'^rltf-wrking-csv/$',views.rltfc_working_section_loading_csv , name='rltf-wrking-csv'),
    
    
    
    url(r'^bwf-sl-excel/$',views.bwf_section_loading , name='bwf-sl-excel'),
    url(r'^bwf-sl-csv/$',views.bwf_section_loading_csv , name='bwf-sl-csv'),
    url(r'^bwf-pjs-excel/$',views.bwf_projections , name='bwf-pjs-excel'),
    url(r'^bwf-pjs-csv/$',views.bwf_projections_csv , name='bwf-pjs-csv'),
    
    
    url(r'^rd-final-sl-excel/$',views.rd_final_section_loading , name='rd-final-sl-excel'),
    url(r'^rd-final-sl-csv/$',views.rd_final_section_loading_csv , name='rd-final-sl-csv'),
    url(r'^rd-final-pjs-excel/$',views.rd_final_projections , name='rd-final-pjs-excel'),
    url(r'^rd-final-pjs-csv/$',views.rd_final_projections_csv , name='rd-final-pjs-csv'),
    
    
    #to be checked later
    url(r'^bcsp-sl-excel/$',views.bcsp_section_loading , name='bcsp-sl-excel'),
    url(r'^bcsp-sl-csv/$',views.bcsp_section_loading_csv , name='bcsp-sl-csv'),
    url(r'^bcsp-pjs-excel/$',views.bcsp_projections , name='bcsp-pjs-excel'),
    url(r'^bcsp-pjs-csv/$',views.bcsp_projections_csv , name='bcsp-pjs-csv'),
    
    
    
    url(r'^xpol-sl-excel/$',views.xpol_section_loading , name='xpol-sl-excel'),
    url(r'^xpol-sl-csv/$',views.xpol_section_loading_csv , name='xpol-sl-csv'),
    url(r'^xpol-pjs-excel/$',views.xpol_projections , name='xpol-pjs-excel'),
    url(r'^xpol-pjs-csv/$',views.xpol_projections_csv , name='xpol-pjs-csv'),
    
    
    
    url(r'^lpw-sl-excel/$',views.lpw_section_loading , name='lpw-sl-excel'),
    url(r'^lpw-sl-csv/$',views.lpw_section_loading_csv , name='lpw-sl-csv'),
    url(r'^lpw-pjs-excel/$',views.lpw_projections , name='lpw-pjs-excel'),
    url(r'^lpw-pjs-csv/$',views.lpw_projections_csv , name='lpw-pjs-csv'),
    
    
    url(r'^ltfc-sl-excel/$',views.ltfc_section_loading , name='ltfc-sl-excel'),
    url(r'^ltfc-sl-csv/$',views.ltf_section_loading_csv , name='ltfc-sl-csv'),
    url(r'^ltfc-pjs-excel/$',views.ltfc_projections , name='ltfc-pjs-excel'),
    url(r'^ltfc-pjs-csv/$',views.ltfc_projections_csv , name='ltfc-pjs-csv'),
    
    
    url(r'^lpcu-sl-excel/$',views.lpcu_section_loading , name='lpcu-sl-excel'),
    url(r'^lpcu-sl-csv/$',views.lpcu_section_loading_csv , name='lpcu-sl-csv'),
    url(r'^lpcu-pjs-excel/$',views.lpcu_projections , name='lpcu-pjs-excel'),
    url(r'^lpcu-pjs-csv/$',views.lpcu_projections_csv , name='lpcu-pjs-csv'),
    
    
    
    url(r'^pls-ls-excel/$',views.pls_section_loading , name='pls-ls-excel'),
    url(r'^pls-ls-csv/$',views.pls_section_loading_csv , name='pls-ls-csv'),
    url(r'^pls-pjs-excel/$',views.pls_projections , name='pls-pjs-excel'),
    url(r'^pls-pjs-csv/$',views.pls_projections_csv , name='pls-pjs-csv'),
    
    
    
    url(r'^ttl-tfc-sl-excel/$',views.ttl_tfc_section_loading , name='ttl-tfc-sl-excel'),
    url(r'^ttl-tfc-sl-csv/$',views.ttl_tfc_section_loading_csv , name='ttl-tfc-sl-csv'),
    url(r'^ttl-tfc-pjs-excel/$',views.ttl_tfc_projections , name='ttl-tfc-pjs-excel'),
    url(r'^ttl-tfc-pjs-csv/$',views.ttl_tfc_projections_csv , name='ttl-tfc-pjs-csv'),
    
    
    
    
    #url(r'^/$',views. , name=''),
    #url(r'^/$',views. , name=''),
    #url(r'^/$',views. , name=''),
    #url(r'^/$',views. , name=''),
    
    #url(r'^datasets/$',login_required(TemplateView.as_view(template_name='datasets.html')),name='datasets'),
    
    
]
