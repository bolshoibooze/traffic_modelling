from __future__ import absolute_import

import math
import decimal
import datetime
from celery import Celery
from celery import shared_task
from django.conf import settings
from celery.utils.log import get_task_logger
from django.utils.translation import ugettext as _
from socket import error as socket_error
from celery.contrib.methods import *
from django.utils import timezone
#from django.db.models import *
#from django.db import *


from django.core import urlresolvers
from django.db.models.query import QuerySet
from decimal import Decimal

from .models import *
from mashup.models import *
D = decimal.Decimal


mashup = Mashup.objects.filter(data__icontains='Road Traffic').order_by('id')

#for dropping down to raw sql
from django.db import connection,transaction

#app = Celery('cardpesr',default_retry_delay=30, max_retries=5)

# celery -A traffic_modelling  worker --loglevel=INFO


road_tcf_qs = RoadTraffic.objects.all().order_by('id')

final_tfc_qs = FinalTraffic.objects.all().order_by('id')

projection_qs = Projection.objects.all().order_by('id')

expol_qs = ExcPOL.objects.all().order_by('id')

lamu_working_qs = LamuPortWorking.objects.all().order_by('id')

#road_tfc_loading_qs = RailTfcWrking.objects.all().order_by('id')

lamu_tcf_qs = LamuTraffic.objects.all().order_by('id')

road_tfc_loading_qs = RdTfcLoading.objects.all().order_by('id')

base_working_file_qs = BaseWorkingFile.objects.all().order_by('id')

lamu_proportionate_qs = LamuProportinateShare.objects.all().order_by('id')

total_projections_qs = TotalTfcProjections.objects.all().order_by('id')

# ---- loading summation for each route & section ---------
base_scenario_qs = mashup.filter(scenario__icontains='Base Case')
base_working_file_scenario_qs = mashup.filter(scenario__icontains='Base Working File')
road_tfc_final_scenario_qs =  mashup.filter(scenario__icontains='Road Traffic Final')
projections_scenario_qs = mashup.filter(scenario__icontains='Projections BS CS')
expol_scenario_qs = mashup.filter(scenario__icontains='Without POL Imports')
lamu_port_working_scenario_qs = mashup.filter(scenario__icontains='Lamu Port Working')

rtfc_loading_scenario_qs = mashup.filter(scenario__icontains='RdTfcLoading PCUs')
prop_lamu_share_scenario_qs = mashup.filter(scenario__icontains='Prop. Lamu Share')
#_scenario_qs = mashup.filter(secanrio__icontains='')
total_combined_tfc_scenario_qs = Mashup.objects.filter(Q(data__icontains='All:Total Tfc')& Q(scenario__icontains='All:Total Tfc'))
# ---------- end of summation qs ---------------------------#

@shared_task
def get_mashup_duplicates():
    pass 
    """
    last_seen = float('-Inf')
    for obj in base_scenario_qs.iterator():
        if not obj.id ==last_seen:
           duplicate_list= base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_county=obj.terminating_county)& Q(terminating_centriod=obj.terminating_centriod))
           for item in duplicate_list.iterator():
               d = Duplicate(
               origin_county=item.origin_county,origin_centriod=item.origin_centriod,
               terminating_county=item.terminating_county,terminating_centriod=item.terminating_county
               )
               d.save()
    """               
              
              
def get_unique_routes():
    last_seen = float('-Inf')
    for obj in mashup.iterator():
        if obj.id == last_seen:#then  it's unique
           #write_to_a_csv_file/excel_file_maybe
           pass
    
               
               

"""
#smarter implementation
@shared_task
def base_scenario_summation():
    for obj in dupes.iterator():
        qs_list =  base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
        for route in qs_list.iterator():
            route.stage_0 = round(D(qs_list.aggregate(Sum('stage_0')).values()[0]),2)
            route.stage_1 = round(D(qs_list.aggregate(Sum('stage_1')).values()[0]),2)
            route.stage_2 = round(D(qs_list.aggregate(Sum('stage_2')).values()[0]),2)
            route.stage_3 = round(D(qs_list.aggregate(Sum('stage_3')).values()[0]),2)
            route.stage_4 = round(D(qs_list.aggregate(Sum('stage_4')).values()[0]),2)
            route.stage_5 = round(D(qs_list.aggregate(Sum('stage_5')).values()[0]),2)
            route.stage_6 = round(D(qs_list.aggregate(Sum('stage_6')).values()[0]),2)
            route.stage_7 = round(D(qs_list.aggregate(Sum('stage_7')).values()[0]),2)
            route.stage_8 = round(D(qs_list.aggregate(Sum('stage_8')).values()[0]),2)
            route.save()
"""            

#Alternate implementation
@shared_task
def _summation():
    for obj in base_scenario_qs.iterator():
    
	base_match_points = base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
	
	if obj.stage_0:
           obj.stage_0 = round(D(base_match_points.aggregate(Sum('stage_0')).values()[0]),2)
           obj.save()
           
        elif obj.stage_1:
             obj.stage_1 = round(base_match_points.aggregate(Sum('stage_1')).values()[0],2)
             obj.save()
             
        elif obj.stage_2: 
             obj.stage_2 = round(base_match_points.aggregate(Sum('stage_2')).values()[0],2)
             obj.save()
             
        elif obj.stage_3:
             obj.stage_3 = round(base_match_points.aggregate(Sum('stage_3')).values()[0],2)
             obj.save()
             
        elif obj.stage_4:     
             obj.stage_4 = round(base_match_points.aggregate(Sum('stage_4')).values()[0],2)
             obj.save()
             
        elif obj.stage_5:
             obj.stage_5 = round(base_match_points.aggregate(Sum('stage_5')).values()[0],2)
             obj.save()
             
        elif obj.stage_6:
             obj.stage_6 = round(base_match_points.aggregate(Sum('stage_6')).values()[0],2)
             obj.save()
             
        elif obj.stage_7:
             obj.stage_7 = round(base_match_points.aggregate(Sum('stage_7')).values()[0],2)
             obj.save()
             
        elif obj.stage_8:
             obj.stage_8 = round(base_match_points.aggregate(Sum('stage_8')).values()[0],2)
	     obj.save()
             break
        
        
        
@shared_task
def base_working_file_scenario_summation():
    for obj in base_working_file_scenario_qs.iterator():
    
	bwf_match_points = base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
	
        obj.stage_0 = bwf_match_points.aggregate(Sum('stage_0')).values()[0]
        obj.stage_1 = bwf_match_points.aggregate(Sum('stage_1')).values()[0]
        obj.stage_2 = bwf_match_points.aggregate(Sum('stage_2')).values()[0]
        obj.stage_3 = bwf_match_points.aggregate(Sum('stage_3')).values()[0]
        obj.stage_4 = bwf_match_points.aggregate(Sum('stage_4')).values()[0]
        obj.stage_5 = bwf_match_points.aggregate(Sum('stage_5')).values()[0]
        obj.stage_6 = bwf_match_points.aggregate(Sum('stage_6')).values()[0]
        obj.stage_7 = bwf_match_points.aggregate(Sum('stage_7')).values()[0]
        obj.stage_8 = bwf_match_points.aggregate(Sum('stage_8')).values()[0]
	obj.save()
        break
        
        
@shared_task
def road_tfc_final_scenario_summation():
    for obj in road_tfc_final_scenario_qs.iterator():
    
	road_tfc_match_points = base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
	
        obj.stage_0 = road_tfc_match_points.aggregate(Sum('stage_0')).values()[0]
        obj.stage_1 = road_tfc_match_points.aggregate(Sum('stage_1')).values()[0]
        obj.stage_2 = road_tfc_match_points.aggregate(Sum('stage_2')).values()[0]
        obj.stage_3 = road_tfc_match_points.aggregate(Sum('stage_3')).values()[0]
        obj.stage_4 = road_tfc_match_points.aggregate(Sum('stage_4')).values()[0]
        obj.stage_5 = road_tfc_match_points.aggregate(Sum('stage_5')).values()[0]
        obj.stage_6 = road_tfc_match_points.aggregate(Sum('stage_6')).values()[0]
        obj.stage_7 = road_tfc_match_points.aggregate(Sum('stage_7')).values()[0]
        obj.stage_8 = road_tfc_match_points.aggregate(Sum('stage_8')).values()[0]
	obj.save()
        break
        

@shared_task
def projections_scenario_summation():
    for obj in projections_scenario_qs.iterator():
    
	prjctn_match_points = base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
	
        obj.stage_0 = prjctn_match_points.aggregate(Sum('stage_0')).values()[0]
        obj.stage_1 = prjctn_match_points.aggregate(Sum('stage_1')).values()[0]
        obj.stage_2 = prjctn_match_points.aggregate(Sum('stage_2')).values()[0]
        obj.stage_3 = prjctn_match_points.aggregate(Sum('stage_3')).values()[0]
        obj.stage_4 = prjctn_match_points.aggregate(Sum('stage_4')).values()[0]
        obj.stage_5 = prjctn_match_points.aggregate(Sum('stage_5')).values()[0]
        obj.stage_6 = prjctn_match_points.aggregate(Sum('stage_6')).values()[0]
        obj.stage_7 = prjctn_match_points.aggregate(Sum('stage_7')).values()[0]
        obj.stage_8 = prjctn_match_points.aggregate(Sum('stage_8')).values()[0]
	obj.save()
        break
        
        
@shared_task
def expol_scenario_summation():
    for obj in expol_scenario_qs.iterator():
    
	expol_match_points = base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
	
        obj.stage_0 = expol_match_points.aggregate(Sum('stage_0')).values()[0]
        obj.stage_1 = expol_match_points.aggregate(Sum('stage_1')).values()[0]
        obj.stage_2 = expol_match_points.aggregate(Sum('stage_2')).values()[0]
        obj.stage_3 = expol_match_points.aggregate(Sum('stage_3')).values()[0]
        obj.stage_4 = expol_match_points.aggregate(Sum('stage_4')).values()[0]
        obj.stage_5 = expol_match_points.aggregate(Sum('stage_5')).values()[0]
        obj.stage_6 = expol_match_points.aggregate(Sum('stage_6')).values()[0]
        obj.stage_7 = expol_match_points.aggregate(Sum('stage_7')).values()[0]
        obj.stage_8 = expol_match_points.aggregate(Sum('stage_8')).values()[0]
	obj.save()
        break
        
        
        
@shared_task
def lamu_port_working_scenario_summation():
    for obj in lamu_port_working_scenario_qs.iterator():
    
	lamu_match_points = base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
	
        obj.stage_0 = lamu_match_points.aggregate(Sum('stage_0')).values()[0]
        obj.stage_1 = lamu_match_points.aggregate(Sum('stage_1')).values()[0]
        obj.stage_2 = lamu_match_points.aggregate(Sum('stage_2')).values()[0]
        obj.stage_3 = lamu_match_points.aggregate(Sum('stage_3')).values()[0]
        obj.stage_4 = lamu_match_points.aggregate(Sum('stage_4')).values()[0]
        obj.stage_5 = lamu_match_points.aggregate(Sum('stage_5')).values()[0]
        obj.stage_6 = lamu_match_points.aggregate(Sum('stage_6')).values()[0]
        obj.stage_7 = lamu_match_points.aggregate(Sum('stage_7')).values()[0]
        obj.stage_8 = lamu_match_points.aggregate(Sum('stage_8')).values()[0]
	obj.save()
        break
        
        
@shared_task
def rtfc_loading_scenario_summation():
    for obj in rtfc_loading_scenario_qs.iterator():
    
	rtfc_match_points = base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
	
        obj.stage_0 = rtfc_match_points.aggregate(Sum('stage_0')).values()[0]
        obj.stage_1 = rtfc_match_points.aggregate(Sum('stage_1')).values()[0]
        obj.stage_2 = rtfc_match_points.aggregate(Sum('stage_2')).values()[0]
        obj.stage_3 = rtfc_match_points.aggregate(Sum('stage_3')).values()[0]
        obj.stage_4 = rtfc_match_points.aggregate(Sum('stage_4')).values()[0]
        obj.stage_5 = rtfc_match_points.aggregate(Sum('stage_5')).values()[0]
        obj.stage_6 = rtfc_match_points.aggregate(Sum('stage_6')).values()[0]
        obj.stage_7 = rtfc_match_points.aggregate(Sum('stage_7')).values()[0]
        obj.stage_8 = rtfc_match_points.aggregate(Sum('stage_8')).values()[0]
	obj.save()
        break
        

@shared_task
def prop_lamu_share_scenario_summation():
    for obj in prop_lamu_share_scenario_qs.iterator():
    
	prop_match_points = base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
	
        obj.stage_0 = prop_match_points.aggregate(Sum('stage_0')).values()[0]
        obj.stage_1 = prop_match_points.aggregate(Sum('stage_1')).values()[0]
        obj.stage_2 = prop_match_points.aggregate(Sum('stage_2')).values()[0]
        obj.stage_3 = prop_match_points.aggregate(Sum('stage_3')).values()[0]
        obj.stage_4 = prop_match_points.aggregate(Sum('stage_4')).values()[0]
        obj.stage_5 = prop_match_points.aggregate(Sum('stage_5')).values()[0]
        obj.stage_6 = prop_match_points.aggregate(Sum('stage_6')).values()[0]
        obj.stage_7 = prop_match_points.aggregate(Sum('stage_7')).values()[0]
        obj.stage_8 = prop_match_points.aggregate(Sum('stage_8')).values()[0]
	obj.save()
        break
        
        
@shared_task
def total_combined_tfc_scenario_summation():
    for obj in total_combined_tfc_scenario_qs.iterator():
    
	ttl_match_points = base_scenario_qs.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_centriod__exact=obj.terminating_centriod)& Q(terminating_county__exact=obj.terminating_county))
	
        obj.stage_0 = ttl_match_points.aggregate(Sum('stage_0')).values()[0]
        obj.stage_1 = ttl_match_points.aggregate(Sum('stage_1')).values()[0]
        obj.stage_2 = ttl_match_points.aggregate(Sum('stage_2')).values()[0]
        obj.stage_3 = ttl_match_points.aggregate(Sum('stage_3')).values()[0]
        obj.stage_4 = ttl_match_points.aggregate(Sum('stage_4')).values()[0]
        obj.stage_5 = ttl_match_points.aggregate(Sum('stage_5')).values()[0]
        obj.stage_6 = ttl_match_points.aggregate(Sum('stage_6')).values()[0]
        obj.stage_7 = ttl_match_points.aggregate(Sum('stage_7')).values()[0]
        obj.stage_8 = ttl_match_points.aggregate(Sum('stage_8')).values()[0]
	obj.save()
        break
        
        

# ---------------------------- other regular tasks ------------------------#
@shared_task()
def road_tcf_mashup():
    for obj in road_tcf_qs.iterator():
        road_tcf = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8)
        road_tcf.save()
        
        
@shared_task()
def base_working_file_mashup():
    for obj in base_working_file_qs.iterator():
        base_working_file = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8,scenario='Base Working File')
        base_working_file.save()
        
        
@shared_task()
def final_tfc_mashup():
    for obj in final_tfc_qs.iterator():
        final_tfc = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8,scenario='Road Traffic Final',excl_road_pcus=obj.excl_road_tonnes)
        final_tfc.save()
        
        
@shared_task()
def projection_mashup():
    for obj in projection_qs.iterator():
        projection = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8,scenario='Projections BS CS',excl_road_pcus=obj.excl_road_tonnes)
        projection.save()
        
        
@shared_task()
def expol_mashup():
    for obj in expol_qs.iterator():
        expol = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8,scenario='Without POL Imports')
        expol.save()
        
        
@shared_task()
def lamu_working_mashup():
    for obj in lamu_working_qs.iterator():
        lamu_working = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,road_pcus=obj.road_pcus,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	excl_road_pcus=obj.excl_road_pcus,stage_8 = obj.stage_8,scenario='Lamu Port Working')
        lamu_working.save()
        
"""       
@shared_task()
def road_tfc_loading_mashup():
    for obj in .iterator():
        road_tfc_loading = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,road_pcus=obj.road_pcus,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	excl_road_pcus=obj.exc_road_pcus,stage_8 = obj.stage_8,scenario='Road Traffic Loading PCUs')
        road_tfc_loading.save()
"""        
        
@shared_task()
def lamu_tcf_mashup():
    for obj in lamu_tcf_qs.iterator():
        lamu_tcf = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,road_pcus=obj.road_pcus,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	excl_road_pcus=obj.excl_road_pcus,stage_8 = obj.stage_8,scenario='Lamu Traffic')
        lamu_tcf.save()
        
        
@shared_task()
def road_tfc_loading_mashup():
    for obj in road_tfc_loading_qs.iterator():
        road_tfc_loading = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,road_pcus=obj.road_pcus,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	excl_road_pcus=obj.excl_road_pcus,stage_8 = obj.stage_8,scenario='RdTfcLoading PCUs')
        road_tfc_loading.save()
        
        

@shared_task()
def lamu_proportionate_mashup():
    for obj in lamu_proportionate_qs.iterator():
        lamu_proportionate = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Road Traffic',
        	stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8,scenario='Prop. Lamu Share')
        lamu_proportionate.save()
        


@shared_task()
def total_projections_mashup():
    for obj in total_projections_qs.iterator():
        total_projections = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Ttl Combined Tfc',
        	stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8,scenario='All:Total Tfc')
        total_projections.save()
