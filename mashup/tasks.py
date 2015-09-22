from __future__ import absolute_import


import math
import decimal
import datetime
from celery import Celery
from celery import shared_task
from django.conf import settings
from celery.utils.log import get_task_logger
from bulk_update.helper import bulk_update
from django.utils.translation import ugettext as _
from socket import error as socket_error
from celery.contrib.methods import *
from django.utils import timezone
from django.db.models import *

from django.core import urlresolvers

from django.db.models.query import QuerySet

from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from .models import *
from rail.models import *
from pipeline.models import *
from gis_data.models import *
from road.models import *

D = decimal.Decimal

year = D('365')
pcu_converter = D('2.5773')

m = Mashup.objects.all()

roads = Mashup.objects.raw("SELECT id,surfacecla FROM mashup_mashup WHERE data='Road Traffic' ")
mashup_qs = Mashup.objects.raw(
"SELECT id,surfacecla,period,stage_0,stage_1,stage_2,stage_3,stage_4,stage_5,stage_6,stage_7,stage_8 FROM mashup_mashup"
)  

routes = Mashup.objects.raw("SELECT id,optimal_pcus,origin_county,origin_centriod,terminating_county,terminating_centriod FROM mashup_mashup")

objs = Stretch.objects.filter(Q(road_class__exact='A')| Q(road_class__exact='B')| Q(road_class__exact='C'))

# Mashup.objects.filter(Q(data__icontains='Road Traffic') & Q(scenario__icontains=''))


# Divide all values by 365 excluding PCU Data, then bulk update results
#normal_road_tonnes_qs = Mashup.objects.filter(Q(data__icontains='Road Traffic')& Q(scenario__icontains='') Q(scenario__icontains='') Q(scenario__icontains='') Q() Q())

#--------------------------- independent dataset -------------------------#
ttl_traffic_qs = Mashup.objects.filter(Q(data__icontains='Ttl Combined Tfc'))
#--------------------------- independent dataset -------------------------#

road_data_qs = Mashup.objects.filter(Q(data__icontains='Road Traffic') & Q(scenario__icontains='Base Case'))
rd_tfc_final_qs = Mashup.objects.filter(Q(data__icontains='Road Traffic') & Q(scenario__icontains='Road Traffic Final'))
bs_cs_projections_qs = Mashup.objects.filter(Q(data__icontains='Road Traffic') & Q(scenario__icontains='Projections BS CS'))
expol_data_qs = Mashup.objects.filter(Q(data__icontains='Road Traffic') & Q(scenario__icontains='Without POL Imports'))
road_tfc_final_qs = Mashup.objects.filter(Q(data__icontains='Road Traffic') & Q(scenario__icontains='Road Traffic Final'))

regular_road_data_qs = Mashup.objects.filter(Q(data__icontains='Road Traffic') & Q(scenario__icontains='Road Traffic Final')| Q(scenario__icontains='Without POL Imports')| Q(scenario__icontains='Projections BS CS')| Q(scenario__icontains='Road Traffic Final')| Q(scenario__icontains='Base Working File'))

#rail-data-analysis
rail_data_qs = Mashup.objects.filter(Q(data__icontains='Rail Traffic') & Q(scenario__icontains='Base Case'))
rail_final_qs = Mashup.objects.filter(Q(data__icontains='Rail Traffic') & Q(scenario__icontains='RL Final'))
rail_tfc_working_qs = Mashup.objects.filter(Q(data__icontains='Rail Traffic') & Q(scenario__icontains='Rail Traffic Working'))


#pipeline-data-analysis
pipeline_data_qs = Pipeline.objects.all()

#replace border points with road ids
namanga_terminal_qs=Mashup.objects.filter(Q(terminating_county__icontains='Malawi')| Q(terminating_county__icontains='Tanzania')| Q(terminating_county__icontains='Zambia')| Q(terminating_county__icontains='Zimbabwe')| Q(origin_county__icontains='South Africa')| Q(origin_county__icontains='Botswana'))

namanga_terminal_centriod_qs=Mashup.objects.filter(Q(terminating_centriod__icontains='Malawi')| Q(terminating_centriod__icontains='Tanzania')| Q(terminating_centriod__icontains='Zambia')| Q(terminating_centriod__icontains='Zimbabwe')| Q(terminating_centriod__icontains='South Africa')| Q(terminating_centriod__icontains='Botswana'))

namanga_origin_qs=Mashup.objects.filter(Q(origin_county__icontains='Malawi')| Q(origin_county__icontains='Tanzania')| Q(origin_county__icontains='Zambia')| Q(origin_county__icontains='Zimbabwe')| Q(origin_county__icontains='South Africa')| Q(origin_county__icontains='Botswana'))

namanga_centriod_qs=Mashup.objects.filter(Q(origin_centriod__icontains='Malawi')| Q(origin_centriod__icontains='Tanzania')| Q(origin_centriod__icontains='Zambia')| Q(origin_centriod__icontains='Zimbabwe')| Q(origin_county__icontains='South Africa')| Q(origin_county__icontains='Botswana'))


# ------ end of namanga ------#


#------ busia data -----#
busia_centriod_qs=Mashup.objects.filter(Q(origin_centriod__icontains='Uganda')| Q(origin_centriod__icontains='Rwanda')| Q(origin_centriod__icontains='CONGO')| Q(terminating_county__icontains='BURUNDI'))

busia_origin_qs =  Mashup.objects.filter(Q(origin_county__icontains='Uganda')| Q(origin_county__icontains='Rwanda')| Q(origin_county__icontains='CONGO')| Q(terminating_county__icontains='BURUNDI')) 

busia_terminal_qs =  Mashup.objects.filter(Q(terminating_county__icontains='Uganda')| Q(terminating_county__icontains='Rwanda')| Q(terminating_county__icontains='CONGO')| Q(terminating_county__icontains='BURUNDI'))

busia_terminal_centriod_qs =  Mashup.objects.filter(Q(terminating_centriod__icontains='Uganda')| Q(terminating_centriod__icontains='Rwanda')| Q(terminating_centriod__icontains='CONGO')| Q(terminating_centriod__icontains='BURUNDI'))
# ------- end of busia data ---------#


# -------- south sudan ------# 
sudan_centriod_qs = Mashup.objects.filter(Q(origin_centriod__icontains='SUDAN'))
sudan_origin_qs =  Mashup.objects.filter(Q(origin_county__icontains='SUDAN')) 
sudan_terminal_qs =  Mashup.objects.filter(Q(terminating_county__icontains='SUDAN'))
sudan_terminal_centriod_qs = Mashup.objects.filter(Q(terminating_centriod__icontains='SUDAN'))
#  ----end for south sudan ------#


# -------- ethiopia ------# 
ethiopia_centriod_qs = Mashup.objects.filter(Q(origin_centriod__icontains='ETHIOPIA'))
ethiopia_origin_qs =  Mashup.objects.filter(Q(origin_county__icontains='ETHIOPIA')) 
ethiopia_terminal_qs =  Mashup.objects.filter(Q(terminating_county__icontains='ETHIOPIA'))
ethiopia_terminal_centriod_qs = Mashup.objects.filter(Q(terminating_centriod__icontains='ETHIOPIA'))
#  ----end for ethiopia------#

# -------- SOMALI ------# 
somalia_centriod_qs = Mashup.objects.filter(Q(origin_centriod__icontains='SOMALI'))
somalia_origin_qs =  Mashup.objects.filter(Q(origin_county__icontains='SOMALI')) 
somalia_terminal_qs =  Mashup.objects.filter(Q(terminating_county__icontains='SOMALI'))
somalia_terminal_centriod_qs = Mashup.objects.filter(Q(terminating_centriod__icontains='SOMALI'))
#  ----end for SOMALI ------#

# ----------------------------------------------------- end of border point switch ----------------------------------------------------------------------------------#
#xl = pd.ExcelFile(obj)
#xl.sheet_names
#df = xl.parse('Duplicate Sections')
#grouped = df.groupby('origin_county','origin_centriod','terminating_county','terminating_centriod')
#index = [gp_keys[0] for gp_keys in grouped.groups.values()]
#unique_df = df.reindex(index)
# pivot = pd.pivot_table(df,index=['origin_county','origin_centriod','terminating_county','terminating_centriod'],values = ['stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'],aggfunc=[np.sum])
#changes = df.drop_duplicates(subset=['origin_county','origin_centriod','terminating_county','terminating_centriod'],take_last=True)
# dataset = df.drop_duplicates(subset=['data','scenario','road_class','origin_county','origin_centriod','terminating_county','terminating_centriod','period','easting','northing','length_km','surfacecla'],take_last=True)
# writer = pd.ExcelWriter('UniqueRoutes.xls',engine='xlsxwriter')
# changes.to_excel(writer,'Routes')
# writer.save()i


data_fields = ['stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',]

@shared_task
def clean_road_tfc_base_case():
    for obj in road_data_qs.filter(Q(stage_0__gt=0)& Q(stage_1__lt=1)& Q(stage_2__lt=1)& Q(stage_3__lt=1)& Q(stage_4__lt=1)& Q(stage_5__lt=1)& Q(stage_6__lt=1)& Q(stage_7__lt=1)& Q(stage_8__lt=1)).iterator():
        obj.stage_0 = D('0.00')
        obj.save()
    
            
            
@shared_task
def remove_mashup_dupes():
    pass
        
    
@shared_task
def road_daily_tfc_tonnes():
    for obj in regular_road_data_qs.iterator():
        obj.stage_0 = round((D(obj.stage_0)/year),2)
        obj.stage_1 = round((D(obj.stage_1)/year),2)
        obj.stage_2 = round((D(obj.stage_2)/year),2)
        obj.stage_3 = round((D(obj.stage_3)/year),2)
        obj.stage_4 = round((D(obj.stage_4)/year),2)
        obj.stage_5 = round((D(obj.stage_5)/year),2)
        obj.stage_6 = round((D(obj.stage_6)/year),2)
        obj.stage_7 = round((D(obj.stage_7)/year),2)
        obj.stage_8 = round((D(obj.stage_8)/year),2)
        obj.save()
 
        #return bulk_update(regular_road_data_qs)
        
        
@shared_task
def road_daily_tfc_pcus():
    for obj in regular_road_data_qs.iterator():
        obj.stage_0 = round((D(obj.stage_0)/pcu_converter),2)
        obj.stage_1 = round((D(obj.stage_1)/pcu_converter),2)
        obj.stage_2 = round((D(obj.stage_2)/pcu_converter),2)
        obj.stage_3 = round((D(obj.stage_3)/pcu_converter),2)
        obj.stage_4 = round((D(obj.stage_4)/pcu_converter),2)
        obj.stage_5 = round((D(obj.stage_5)/pcu_converter),2)
        obj.stage_6 = round((D(obj.stage_6)/pcu_converter),2)
        obj.stage_7 = round((D(obj.stage_7)/pcu_converter),2)
        obj.stage_8 = round((D(obj.stage_8)/pcu_converter),2)
        obj.save()

@shared_task        
def combined_total_tfc_tonnes():
    for obj in ttl_traffic_qs.iterator():
        obj.stage_0 = round((D(obj.stage_0)/year),2)
        obj.stage_1 = round((D(obj.stage_1)/year),2)
        obj.stage_2 = round((D(obj.stage_2)/year),2)
        obj.stage_3 = round((D(obj.stage_3)/year),2)
        obj.stage_4 = round((D(obj.stage_4)/year),2)
        obj.stage_5 = round((D(obj.stage_5)/year),2)
        obj.stage_6 = round((D(obj.stage_6)/year),2)
        obj.stage_7 = round((D(obj.stage_7)/year),2)
        obj.stage_8 = round((D(obj.stage_8)/year),2)
        obj.save()
 
        #return bulk_update(ttl_traffic_qs,update_fields = ['stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',])
        
        
@shared_task
def combined_total_tfc_pcus():
    for obj in ttl_traffic_qs.iterator():
        obj.stage_0 = round((D(obj.stage_0)/pcu_converter),2)
        obj.stage_1 = round((D(obj.stage_1)/pcu_converter),2)
        obj.stage_2 = round((D(obj.stage_2)/pcu_converter),2)
        obj.stage_3 = round((D(obj.stage_3)/pcu_converter),2)
        obj.stage_4 = round((D(obj.stage_4)/pcu_converter),2)
        obj.stage_5 = round((D(obj.stage_5)/pcu_converter),2)
        obj.stage_6 = round((D(obj.stage_6)/pcu_converter),2)
        obj.stage_7 = round((D(obj.stage_7)/pcu_converter),2)
        obj.stage_8 = round((D(obj.stage_8)/pcu_converter),2)
        obj.save()
        

@shared_task        
def road_tfc_data_tonnes():
    for obj in road_data_qs.iterator():
        obj.stage_0 = round((D(obj.stage_0)/year),2)
        obj.stage_1 = round((D(obj.stage_1)/year),2)
        obj.stage_2 = round((D(obj.stage_2)/year),2)
        obj.stage_3 = round((D(obj.stage_3)/year),2)
        obj.stage_4 = round((D(obj.stage_4)/year),2)
        obj.stage_5 = round((D(obj.stage_5)/year),2)
        obj.stage_6 = round((D(obj.stage_6)/year),2)
        obj.stage_7 = round((D(obj.stage_7)/year),2)
        obj.stage_8 = round((D(obj.stage_8)/year),2)
        obj.save()
 
        #return bulk_update(road_data_qs,update_fields = ['stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',])
        
        

@shared_task        
def road_tfc_data_pcus():
    for obj in road_data_qs.iterator():
        obj.stage_0 = round((D(obj.stage_0)/pcu_converter),2)
        obj.stage_1 = round((D(obj.stage_1)/pcu_converter),2)
        obj.stage_2 = round((D(obj.stage_2)/pcu_converter),2)
        obj.stage_3 = round((D(obj.stage_3)/pcu_converter),2)
        obj.stage_4 = round((D(obj.stage_4)/pcu_converter),2)
        obj.stage_5 = round((D(obj.stage_5)/pcu_converter),2)
        obj.stage_6 = round((D(obj.stage_6)/pcu_converter),2)
        obj.stage_7 = round((D(obj.stage_7)/pcu_converter),2)
        obj.stage_8 = round((D(obj.stage_8)/pcu_converter),2)
        obj.save()
        

@shared_task        
def rail_data_tonnes():
    for obj in rail_data_qs.iterator():
        obj.stage_0 = round((D(obj.stage_0)/year),2)
        obj.stage_1 = round((D(obj.stage_1)/year),2)
        obj.stage_2 = round((D(obj.stage_2)/year),2)
        obj.stage_3 = round((D(obj.stage_3)/year),2)
        obj.stage_4 = round((D(obj.stage_4)/year),2)
        obj.stage_5 = round((D(obj.stage_5)/year),2)
        obj.stage_6 = round((D(obj.stage_6)/year),2)
        obj.stage_7 = round((D(obj.stage_7)/year),2)
        obj.stage_8 = round((D(obj.stage_8)/year),2)
        obj.save()
 
        #return bulk_update(rail_data_qs,update_fields = ['stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',])
        
@shared_task        
def rail_final_tonnes():
    for obj in rail_final_qs.iterator():
        obj.stage_0 = round((D(obj.stage_0)/year),2)
        obj.stage_1 = round((D(obj.stage_1)/year),2)
        obj.stage_2 = round((D(obj.stage_2)/year),2)
        obj.stage_3 = round((D(obj.stage_3)/year),2)
        obj.stage_4 = round((D(obj.stage_4)/year),2)
        obj.stage_5 = round((D(obj.stage_5)/year),2)
        obj.stage_6 = round((D(obj.stage_6)/year),2)
        obj.stage_7 = round((D(obj.stage_7)/year),2)
        obj.stage_8 = round((D(obj.stage_8)/year),2)
        obj.save()
 
        #return bulk_update(rail_final_qs)
        
        
@shared_task        
def rail_tfc_working_tonnes():
    for obj in rail_tfc_working_qs.iterator():
        obj.stage_0 = round((D(obj.stage_0)/year),2)
        obj.stage_1 = round((D(obj.stage_1)/year),2)
        obj.stage_2 = round((D(obj.stage_2)/year),2)
        obj.stage_3 = round((D(obj.stage_3)/year),2)
        obj.stage_4 = round((D(obj.stage_4)/year),2)
        obj.stage_5 = round((D(obj.stage_5)/year),2)
        obj.stage_6 = round((D(obj.stage_6)/year),2)
        obj.stage_7 = round((D(obj.stage_7)/year),2)
        obj.stage_8 = round((D(obj.stage_8)/year),2)
        obj.save()
 
        #return bulk_update(rail_tfc_working_qs,update_fields = ['stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',])
        
 

# Namanga         
@shared_task
def namanga_centriod_updates():
    for obj in namanga_centriod_qs.iterator() :
         obj.origin_centriod = 'Namanga'
         obj.save()
         


@shared_task         
def namanga_origin_updates():
    for obj in namanga_origin_qs:
         obj.origin_county = 'Namanga'
         obj.save()
         
@shared_task         
def namanga_terminal_updates():
    for obj in namanga_terminal_qs:
         obj.terminating_county = 'Namanga'
         obj.save()
         
@shared_task
def namanga_terminal_centriod_updates():
    for obj in namanga_terminal_centriod_qs.iterator() :
         obj.terminating_centriod = 'Namanga'
         obj.save()

#busia         
@shared_task         
def busia_centriod_updates():
    for obj in busia_centriod_qs.iterator():
         obj.origin_centriod = 'Busia'
         obj.save()
    
@shared_task         
def busia_origin_updates():
    for obj in busia_origin_qs.iterator():
         obj.origin_county = 'Busia'
         obj.save() 
    
@shared_task         
def busia_terminal_updates():
    for obj in busia_terminal_qs.iterator():
         obj.terminating_county = 'Busia'
         obj.save() 
         
@shared_task         
def busia_terminal_centriod_updates():
    for obj in busia_terminal_centriod_qs.iterator():
         obj.terminating_centriod = 'Busia'
         obj.save() 

#sudan        
@shared_task        
def sudan_centriod_updates():
    for obj in sudan_centriod_qs.iterator():
        obj.origin_centriod = 'Lokichar'
        obj.save()
        
@shared_task        
def sudan_origin_updates():
    for obj in sudan_centriod_qs.iterator():
        obj.origin_county = 'Lokichar'
        obj.save()
        
@shared_task        
def sudan_terminal_updates():
    for obj in sudan_terminal_qs.iterator():
        obj.terminating_county = 'Lokichar'
        obj.save()
        
        
@shared_task        
def sudan_terminal_centriod_updates():
    for obj in sudan_terminal_centriod_qs.iterator():
        obj.terminating_centriod = 'Lokichar'
        obj.save()
        
#
@shared_task        
def somalia_centriod_updates():
    for obj in sudan_centriod_qs.iterator():
        obj.origin_centriod = 'Mandera'
        obj.save()
        
@shared_task        
def somalia_origin_updates():
    for obj in somalia_centriod_qs.iterator():
        obj.origin_county = 'Mandera'
        obj.save()
        
@shared_task        
def somalia_terminal_updates():
    for obj in somalia_terminal_qs.iterator():
        obj.terminating_county = 'Mandera'
        obj.save()
        
        
@shared_task        
def somalia_terminal_centriod_updates():
    for obj in somalia_terminal_centriod_qs.iterator():
        obj.terminating_centriod = 'Mandera'
        obj.save()
        

#ethiopia 
@shared_task        
def ethiopia_centriod_updates():
    for obj in ethiopia_centriod_qs.iterator():
        obj.origin_centriod = 'Moyale'
        obj.save()
        
@shared_task        
def ethiopia_origin_updates():
    for obj in ethiopia_centriod_qs.iterator():
        obj.origin_county = 'Moyale'
        obj.save()
        
@shared_task        
def ethiopia_terminal_updates():
    for obj in ethiopia_terminal_qs.iterator():
        obj.terminating_county = 'Moyale'
        obj.save()
        
        
@shared_task        
def ethiopia_terminal_centriod_updates():
    for obj in ethiopia_terminal_centriod_qs.iterator():
        obj.terminating_centriod = 'Moyale'
        obj.save()   
    
@shared_task 
def set_origin_road_markers():
    for obj in Stretch.objects.filter(Q(road_class__exact='A')| Q(road_class__exact='B')| Q(road_class__exact='C')).iterator(): 
        for p in Mashup.objects.filter(Q(origin_county__icontains=obj.from_field)& Q(origin_centriod__icontains=obj.to_field)).iterator():
            p.easting = obj.easting
            p.northing = obj.northing
            p.road_class = obj.road_class
            p.surfacecla = obj.surfacecla
            p.length_km = obj.length_km
            p.save() 
            break 
            
            
@shared_task 
def set_class_a_markers():
    for obj in Stretch.objects.filter(Q(road_class__exact='A')).iterator(): 
        for p in Mashup.objects.filter(Q(origin_county__icontains=obj.from_field)& Q(origin_centriod__icontains=obj.to_field)).iterator():
            p.easting = obj.easting
            p.northing = obj.northing
            p.road_class = obj.road_class
            p.surfacecla = obj.surfacecla
            p.length_km = obj.length_km
            p.save() 
            break 
            
            
@shared_task 
def set_class_b_markers():
    for obj in Stretch.objects.filter(Q(road_class__exact='B')).iterator(): 
        for p in Mashup.objects.filter(Q(origin_county__icontains=obj.from_field)& Q(origin_centriod__icontains=obj.to_field)).iterator():
            p.easting = obj.easting
            p.northing = obj.northing
            p.road_class = obj.road_class
            p.surfacecla = obj.surfacecla
            p.length_km = obj.length_km
            p.save() 
            break 
            
            
@shared_task 
def set_class_c_markers():
    for obj in Stretch.objects.filter(Q(road_class__exact='C')).iterator(): 
        for p in Mashup.objects.filter(Q(origin_county__icontains=obj.from_field)& Q(origin_centriod__icontains=obj.to_field)).iterator():
            p.easting = obj.easting
            p.northing = obj.northing
            p.road_class = obj.road_class
            p.surfacecla = obj.surfacecla
            p.length_km = obj.length_km
            p.save() 
            break 
            
            
@shared_task 
def set_terminating_road_markers():
    for obj in Stretch.objects.filter(Q(road_class__exact='A')| Q(road_class__exact='B')| Q(road_class__exact='C')).iterator(): 
        for p in Mashup.objects.filter(Q(terminating__icontains=obj.from_field)& Q(terminating_centriod__icontains=obj.to_field)).iterator():
            p.easting = obj.easting
            p.northing = obj.northing
            p.road_class = obj.road_class
            p.surfacecla = obj.surfacecla
            p.length_km = obj.length_km
            p.save()
            break  
             
              

       

     
@shared_task
def paved_optimal_pcus():
    for obj in Mashup.objects.filter(surfacecla__icontains='paved').iterator():
        obj.optimal_pcus = 15000
        obj.save()
        
@shared_task
def upaved_optimal_pcus():
    for obj in Mashup.objects.filter(surfacecla__icontains='unpaved').iterator():
        obj.optimal_pcus = 10000
        obj.save()
        
    
             
             

def total_traffic_summation():
    """for combined total traffic """
    #for obj in ttl.objects.filter(data__icontains='Ttl Combined').iterator():
    #for obj in TotalTraffic.objects.raw("SELECT id,origin_county,# FROM WHERE data='Ttl Traffic'")
    pass 
    
def total_with_lamu_port_working():
    pass
    
def total_regular_tfc():
    pass
    
def pipeline_stage_0():
    for obj in Mashup.objects.filter(data__icontains='Pipeline').iterator():
        sum_0 = m.aggregate(Sum('stage_0')).values()[0]
        #then do a bulk update
        #! but this will be the total for the whole column
        # we need a total for each road-section, for each, for each stage/period
        #is there a way to sort out the routes for easier filtering??????
    

    
def dataset_totals():
    """rail + road + traffic"""
    for obj in m.filter(data__icontains='').iterator():
        #get total_value_for_dataset & update
        pass
    
    


           
           

                    

 
             
@shared_task 
def set_dataset_period():# this works
    for obj in Mashup.objects.all().iterator():
        if obj.stage_0:
           obj.period = '2013 - 2014'
           obj.save()
           
           
        elif obj.stage_1:
             obj.period = '2014 - 2015'
             obj.save()
             
        elif obj.stage_2:
             obj.period = '2019 - 2020'
             obj.save()
             
        elif obj.stage_3:
             obj.period = '2024 - 2025'
             obj.save()
             
        elif obj.stage_4:
             obj.period = '2029 - 2030'
             obj.save()
             
        elif obj.stage_5:
             obj.period = '2034 - 2035'
             obj.save()
             
        elif obj.stage_6:
             obj.period = '2044 - 2045'
             obj.save()
             
        elif obj.stage_7:
             obj.period = '2054 - 2055'
             obj.save()
             
        elif obj.stage_8:
             obj.period = '2064 - 2065'
             obj.save() 
             break          
	

"""   
def update_to_mashup():
    for obj in objs.iterator():
        o_county = obj.origin_county
        o_centriod = obj.origin_centriod
        t_county = obj.terminating_county
        t_centriod = obj.terminating_centriod
        stage_0 = obj.stage_0 #decimal
        dataset = must_be_specified
        scenario = must_be_specified
        #once you get all that ---> do a bulk update to Mashup model
        
        
           
           
def set_period():
    # later on do an update on Mashup to match periods with data
        if obj.stage_0:
           return Mashup.update(period=1)
        elif obj.stage_1:
           continue
    
           
def set_optimal_pcus():
    for obj in objs.iterator():
        if obj.road_class == 'A':# _icontains='A'
           return Mashup.objects.filter(road_class__icontains='A').update(optimal_pcus = 0.5 )
        elif obj.road_class == 'B':
             return Mashup.objects.filter(road_class__icontains='B').update(optimal_pcus = 0.5 )
        elif obj.road_class == 'C':
             return Mashup.objects.filter(road_class__icontains='C').update(optimal_pcus = 0.5 )
             break
             
             
def mark_corridors_for_updgrade(): 
    for obj in objs.iterator():
        if obj.total_pcus > obj.optimal_pcus:
           #then calculate how many PCUS per lane viz. additional lanes/cpacity
           
           
def set_period():
    for obj in objs.iterator():
        if obj.stage_0:
           return m.filter(stage_0__exact=obj.stage_0).update(period=1)
           
        elif obj.stage_1:
             return m.filter(stage_0__exact=obj.stage_0).update(period=1)
             
        elif obj.stage_2:
             return m.filter(stage_2__exact=obj.stage_2).update(period=1)
        elif obj.stage_3:
             return m.filter(stage_3__exact=obj.stage_3).update(period=1)
        elif obj.stage_4:
             return m.filter(stage_4__exact=obj.stage_4).update(period=1)
             
        elif obj.stage_5:
             return m.filter(stage_5__exact=obj.stage_5).update(period=1)
        elif obj.stage_6:
             return m.filter(stage_6__exact=obj.stage_6).update(period=1)
        elif obj.stage_7:
             return m.filter(stage_7__exact=obj.stage_7).update(period=1)
        elif obj.stage_8:
             return m.filter(stage_8__exact=obj.stage_8).update(period=1)
             
             
              
    
    
    
"""           
        
