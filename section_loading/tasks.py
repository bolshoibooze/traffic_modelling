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
from django.db.models import *
#from django.db import *


from django.core import urlresolvers
from django.db.models.query import QuerySet
from django_pandas.io import read_frame
from decimal import Decimal
import os,xlsxwriter
#import pandas as pd
#from pandas import *
#import numpy as np

from .models import *
from mashup.models import *
from bulk_update.helper import bulk_update
from gis_data.models import *

D = decimal.Decimal


mashup = Mashup.objects.filter(Q(data__icontains='Road Traffic')& Q(scenario__icontains='Base Working File'))

road_section_qs = mashup #SectionLoading.objects.filter(data__iexact='Road Traffic').order_by('id')
rail_section_qs = mashup #SectionLoading.objects.filter(data__iexact='Rail Traffic').order_by('id')

#base_section_qs = section_qs.filter(scenario__icontains='Base Working File')

rail_qs =  Mashup.objects.filter(data__iexact='Rail Traffic').order_by('id')
road_qs = Mashup.objects.filter(data__iexact='Road Traffic').order_by('id')
combined_tfc_qs = Mashup.objects.filter(Q(data__iexact='Ttl Combined Tfc')).order_by('id')

#rail_qs.filter(scenario__iexact='')

#stretch_qs = Stretch.objects.filter(Q(road_class___icontains='A')| Q(road_class___icontains='B')| Q(road_class___icontains='C'))


            
@shared_task 
def tag_road_sections():
    for obj in Stretch.objects.filter(Q(road_class__exact='A')| Q(road_class__exact='B')| Q(road_class__exact='C')).iterator(): 
        for item in Corridor.objects.filter(Q(origin_county__icontains=obj.from_field)| Q(origin_centriod__icontains=obj.to_field)| Q(terminating_county__icontains=obj.to_field)| Q(terminating_centriod__icontains=obj.from_field)).iterator():
            item.origin_county = obj.from_field
            item.origin_centriod = obj.to_field
            item.terminating_county = obj.from_field
            item.terminating_centriod = obj.to_field
            item.save()
           
            break 
           
    




@shared_task
def get_corridor_duplicates():
    last_seen = float('-Inf')
    for obj in mashup.iterator():
        if not obj.id ==last_seen:
           duplicate_list= mashup.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_county=obj.terminating_county)& Q(terminating_centriod=obj.terminating_centriod)& Q(scenario__exact=obj.scenario))
           for item in duplicate_list.iterator():
               d = Corridor(
               origin_county=item.origin_county,origin_centriod=item.origin_centriod,scenario=obj.scenario,
               terminating_county=item.terminating_county,terminating_centriod=item.terminating_county,
               data='Road Traffic'
               )
               d.save()
               


@shared_task 
def reset_projections():
    for obj in RoadBaseCase.objects.all().iterator():#filter(data__iexact='Rail Traffic'):
            
            obj.stage_0 = D('0.00')
            obj.stage_1 = D('0.00')
            obj.stage_2 = D('0.00')
            obj.stage_3 = D('0.00')
            obj.stage_4 = D('0.00')
            obj.stage_5 = D('0.00')
            obj.stage_6 = D('0.00')
            obj.stage_7 = D('0.00')
            obj.stage_8 = D('0.00')
            obj.save()

@shared_task            
def set_data_scenario():
    #data_qs = road_section_qs.filter(Q(scenarios=None)& Q(stage_8__gt=0.00)).iterator():
    for obj in road_section_qs.filter(Q(scenarios=None)& Q(stage_8__gt=0.00)).iterator():
        obj.scenario = s
        obj.save()
        
        
@shared_task        
def test_choice_field():
    nrb = Scenario.objects.filter(name='Base Working File')
    nmg = Scenario.objects.filter(name='Road Base Case')
    for obj in TestTable.objects.filter(Q(item__icontains='nairobi')& Q(choice__name__exact='Base Working File')):
        obj.value +=500
        obj.save()
        #obj.choice.add(s)
        
        
@shared_task 
def populate_road_section_loadings():
   
    for obj in road_qs.filter(scenario__iexact='Base Case').iterator():
    # Base Working File, Road Traffic Final, RdTfcLoading PCUs, Projections BS CS, Without POL Imports, Lamu Port Working, Prop. Lamu Share, Base Case
        #road_qs = BWF.objects.all() #RdBC,RoadFinal,BCSP, xPOL, LPW, LTFC, LPCU, PLS, TTFCP
        obj_list =  RoadBaseCase.objects.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_county__exact=obj.terminating_county)& Q(terminating_centriod__exact=obj.terminating_centriod))
        for item in obj_list.iterator():
            
            item.stage_0 += obj.stage_0 
            item.stage_1 += obj.stage_1 
            item.stage_2 += obj.stage_2
            item.stage_3 += obj.stage_3
            item.stage_4 += obj.stage_4
            item.stage_5 += obj.stage_5 
            item.stage_6 += obj.stage_6
            item.stage_7 += obj.stage_7
            item.stage_8 += obj.stage_8
      
            item.optimal_pcus = obj.optimal_pcus
            item.road_class = obj.road_class
            item.surfacecla = obj.surfacecla
            item.length_km = obj.length_km
            item.scenario = obj.scenario
            item.distance = obj.distance
            item.northing = obj.northing
            item.easting = obj.easting
            item.data = obj.data
            item.save()

@shared_task
def lamu_edge_case_dataset():  
    for obj in road_qs.filter(scenario__iexact='Lamu Port Working').iterator():
        obj_list =  LPW.objects.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_county__exact=obj.terminating_county)& Q(terminating_centriod__exact=obj.terminating_centriod))
        for item in obj_list.iterator():
            item.road_pcus += obj.road_pcus 
            item.excl_road_pcus += obj.excl_road_pcus 
            item.save()

@shared_task
def populate_combined_tfc():
    for obj in combined_tfc_qs.iterator():
        obj_list =  TTFCP.objects.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_county__exact=obj.terminating_county)& Q(terminating_centriod__exact=obj.terminating_centriod))
        for item in obj_list.iterator():
            
            item.stage_0 += obj.stage_0 
            item.stage_1 += obj.stage_1 
            item.stage_2 += obj.stage_2
            item.stage_3 += obj.stage_3
            item.stage_4 += obj.stage_4
            item.stage_5 += obj.stage_5 
            item.stage_6 += obj.stage_6
            item.stage_7 += obj.stage_7
            item.stage_8 += obj.stage_8
      
            item.optimal_pcus = obj.optimal_pcus
            item.road_class = obj.road_class
            item.surfacecla = obj.surfacecla
            item.length_km = obj.length_km
            item.scenario = obj.scenario
            item.distance = obj.distance
            item.northing = obj.northing
            item.easting = obj.easting
            item.data = obj.data
            item.save()
                  

@shared_task            
def populate_rail_section_loadings():
    for obj in rail_qs.filter(scenario__iexact='Rail Traffic Working').iterator():# Rail Traffic Working, RL Final
        #RBC, RailFinal, RailTrafficWorking
        obj_list =  RailTrafficWorking.objects.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_centriod)& Q(terminating_county__exact=obj.terminating_county)& Q(terminating_centriod__exact=obj.terminating_centriod))
        for item in obj_list.iterator():
            
            item.stage_0 += obj.stage_0 
            item.stage_1 += obj.stage_1 
            item.stage_2 += obj.stage_2
            item.stage_3 += obj.stage_3
            item.stage_4 += obj.stage_4
            item.stage_5 += obj.stage_5 
            item.stage_6 += obj.stage_6
            item.stage_7 += obj.stage_7
            item.stage_8 += obj.stage_8
            
            item.length_km = obj.length_km
            item.scenario = obj.scenario
            item.distance = obj.distance
            item.northing = obj.northing
            item.easting = obj.easting
            item.data=obj.data
            item.save()
            
@shared_task             
def pivot_mashup_data():
    pass
    """
    obj = os.path.abspath('BaseWorkingMashup.xls')
    xl = pd.ExcelFile(obj)
    df = xl.parse('Duplicate Sections')
    index = df.index=['origin_county','origin_centriod','terminating_county','terminating_centriod']
    pivot = pd.pivot_table(index,aggfunc=[np.sum])
    writer = pd.ExcelWriter('MashupPivotSample.xls',engine='xlsxwriter')
    pivot.to_excel(writer)
    writer.save()
    """      

@shared_task            
def base_case_section_loading():
    pass
    
@shared_task             
def stage_one():#Failed attempt
    for obj in SectionLoading.objects.all():
        m_list = mashup.filter(Q(origin_county__exact=obj.origin_county)& Q(origin_centriod__exact=obj.origin_county)& Q(terminating_county__exact=obj.terminating_county)& Q(terminating_centriod__exact=obj.terminating_centriod))
        for item in m_list.iterator():
            val = m_list.aggregate(Sum('stage_0')).values()[0]
            return SectionLoading.objects.filter(Q(origin_county__exact=item.origin_county)& Q(origin_centriod__exact=obj.item.centriod)& Q(terminating_county=item.terminating_county)& Q(terminating_centriod__exact=item.terminating_county)).update(stage_0=F('stage_0') + val)
        
            
        
            
            
            
@shared_task
def base_scenario_totals():
    for obj in base_section_qs.iterator():
            obj.stage_0 = round(D(base_section_qst.aggregate(Sum('commodity_data__stage_0')).values()[0]),2)
            obj.stage_1 = round(D(base_section_qst.aggregate(Sum('commodity_data__stage_1')).values()[0]),2)
            obj.stage_2 = round(D(base_section_qst.aggregate(Sum('commodity_data__stage_2')).values()[0]),2)
            obj.stage_3 = round(D(base_section_qst.aggregate(Sum('commodity_data__stage_3')).values()[0]),2)
            obj.stage_4 = round(D(base_section_qst.aggregate(Sum('commodity_data__stage_4')).values()[0]),2)
            obj.stage_5 = round(D(base_section_qst.aggregate(Sum('commodity_data__stage_5')).values()[0]),2)
            obj.stage_6 = round(D(base_section_qst.aggregate(Sum('commodity_data__stage_6')).values()[0]),2)
            obj.stage_7 = round(D(base_section_qst.aggregate(Sum('commodity_data__stage_7')).values()[0]),2)
            obj.stage_8 = round(D(base_section_qst.aggregate(Sum('commodity_data__stage_8')).values()[0]),2)
            bulk_update(base_section_qs)
                            
                   
     

@shared_task
def extract_road_corridors():#Write a full script to extract data from raw file
    pass
    """
    qs = mashup.filter(scenario__icontains='Base Working File')
    df = read_frame(
    qs,fieldnames=['origin_county','origin_centriod','terminating_county','terminating_centriod']
    )
    changes = df.drop_duplicates(
    subset=['origin_county','origin_centriod','terminating_county','terminating_centriod'],take_last=True
    )
    writer = pd.ExcelWriter('BaseRouteData.xls',engine='xlsxwriter')
    changes.to_excel(writer,'Routes')
    writer.save()
    """
    
    
@shared_task
def extract_rail_sections():#Write a full script to extract data from raw file
    #qs = mashup.filter(scenario__icontains='Base Working File')
    pass
    """
    qs = Mashup.objects.filter(Q(data__iexact='Rail Traffic')& Q(scenario__iexact='Rail Traffic Working'))
    df = read_frame(
    qs,fieldnames=['origin_county','origin_centriod','terminating_county','terminating_centriod']
    )
    changes = df.drop_duplicates(
    subset=['origin_county','origin_centriod','terminating_county','terminating_centriod'],take_last=True
    )
    writer = pd.ExcelWriter('RailTfcWrkngData.xls',engine='xlsxwriter')
    changes.to_excel(writer,'Routes')
    writer.save()
    """
    
@shared_task
def extract_combined_sections():#Write a full script to extract data from raw file
    #qs = mashup.filter(scenario__icontains='Base Working File')
    pass
    """
    qs = Mashup.objects.filter(Q(data__iexact='Ttl Combined Tfc'))
    df = read_frame(
    qs,fieldnames=['origin_county','origin_centriod','terminating_county','terminating_centriod']
    )
    changes = df.drop_duplicates(
    subset=['origin_county','origin_centriod','terminating_county','terminating_centriod'],take_last=True
    )
    writer = pd.ExcelWriter('CombinedSectionData.xls',engine='xlsxwriter')
    changes.to_excel(writer,'Routes')
    writer.save()
    """
    
    
@shared_task
def extract_all_section_upgrades():
    pass
    """
    qs = TTFCP.objects.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
    
    df = read_frame(
    qs,fieldnames=['origin_county','origin_centriod','terminating_county','terminating_centriod','road_class','surfacecla','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8']
    )
    
    writer = pd.ExcelWriter('TotalTrafficUpgrades.xls',engine='xlsxwriter')
    df.to_excel(writer,)
    writer.save()
    """
    
@shared_task
def extract_unpaved_section_upgrades():
    pass
    """
    unpaved_qs = BWF.objects.filter(surfacecla__iexact='unpaved')
    qs = unpaved_qs.filter(Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
    
    df = read_frame(
    qs,fieldnames=['origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8']
    )
    writer = pd.ExcelWriter('BaseWorkingUnPavedUpgrades.xls',engine='xlsxwriter')
    df.to_excel(writer,)
    writer.save()
    """

@shared_task
def extract_lamu_edge_case_projections():
    pass
    """
    lpw_qs = LPW.objects.filter(surfacecla__iexact='unpaved')
    qs = lpw_qs.filter(Q(road_pcus__gte=1)& Q(excl_road_pcus__gte=1)& Q(additional_capacity_0__gte=1)| Q(additional_capacity_1__gte=1)| Q(additional_capacity_2__gte=1)| Q(additional_capacity_3__gte=1)| Q(additional_capacity_4__gte=1)| Q(additional_capacity_5__gte=1)| Q(additional_capacity_6__gte=1)| Q(additional_capacity_7__gte=1)|Q(additional_capacity_8__gte=1))
    
    df = read_frame(
    qs,fieldnames=['origin_county','origin_centriod','terminating_county','terminating_centriod','road_pcus','excl_road_pcus','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8']
    )
    
    """

             
        

# Some thoughts:
# --------------------------------#
# 0:Reset all additional capacities
# 1:Compute additional capacity
# 2: If additional_capacity >= 1: #checks_if_int_is_+ve
#       mark_road_for_upgrade        
 

@shared_task
def clean_road_tfc_dataset():
    for obj in RoadBaseCase.objects.all().iterator():
        if len(str(obj.stage_0)) > 7:
           round_num =  round(obj.stage_0,-3)
           nomarlized = round_num/10000
           obj.stage_0 = D('0.00')
           obj.save()
@shared_task   
def reset_all_capacities():
    for obj in RoadBaseCase.objects.all().iterator():
        
        obj.additional_capacity_0 = 0
        obj.additional_capacity_1 = 0
        obj.additional_capacity_2 = 0
        obj.additional_capacity_3 = 0
        obj.additional_capacity_4 = 0
        obj.additional_capacity_5 = 0
        obj.additional_capacity_6 = 0
        obj.additional_capacity_7 = 0
        obj.additional_capacity_8 = 0
        obj.save()
        
@shared_task
def set_unpaved_lamu_capacity():
    for obj in LPW.objects.filter(Q(surfacecla__iexact='unpaved')).iterator():
        obj.road_pcus = int(round((obj.road_pcus - 10000)/5000))
        obj.excl_road_pcus = int(round((obj.excl_road_pcus - 10000)/5000))
        obj.save()
        
@shared_task
def set_paved_lamu_capacity():
    for obj in LPW.objects.filter(Q(surfacecla__iexact='paved')).iterator():
        obj.road_pcus = int(round((obj.road_pcus - 15000)/7500))
        obj.excl_road_pcus = int(round((obj.excl_road_pcus - 15000)/7500))
        obj.save()
        
# ---------------- end of lamu edge case -------------------------#   

@shared_task
def set_unpaved_capacity():
    #road_qs = BWF.objects.all() #RdBC,RoadFinal,BCSP, xPOL, LPW, LTFC, LPCU, PLS, TTFCP
    for obj in RoadFinal.objects.filter(Q(surfacecla__iexact='unpaved')).iterator():
        obj.additional_capacity_0 = int(round((obj.stage_0 - 10000)/5000))
        obj.additional_capacity_1 = int(round((obj.stage_1 - 10000)/5000))
        obj.additional_capacity_2 = int(round((obj.stage_2 - 10000)/5000))
        obj.additional_capacity_3 = int(round((obj.stage_3 - 10000)/5000))
        obj.additional_capacity_4 = int(round((obj.stage_4 - 10000)/5000))
        obj.additional_capacity_5 = int(round((obj.stage_5 - 10000)/5000))
        obj.additional_capacity_6 = int(round((obj.stage_6 - 10000)/5000))
        obj.additional_capacity_7 = int(round((obj.stage_7 - 10000)/5000))
        obj.additional_capacity_8 = int(round((obj.stage_8 - 10000)/5000))
        obj.save()
        
@shared_task        
def set_paved_capacity():
    #road_qs = BWF.objects.all() #RdBC,RoadFinal,BCSP, xPOL, LPW, LTFC, LPCU, PLS, TTFCP
    for obj in  RoadFinal.objects.filter(Q(surfacecla__iexact='paved')).iterator():
        obj.additional_capacity_0 = int(round((obj.stage_0 - 15000)/7500))
        obj.additional_capacity_1 = int(round((obj.stage_1 - 15000)/7500))
        obj.additional_capacity_2 = int(round((obj.stage_2 - 15000)/7500))
        obj.additional_capacity_3 = int(round((obj.stage_3 - 15000)/7500))
        obj.additional_capacity_4 = int(round((obj.stage_4 - 15000)/7500))
        obj.additional_capacity_5 = int(round((obj.stage_5 - 15000)/7500))
        obj.additional_capacity_6 = int(round((obj.stage_6 - 15000)/7500))
        obj.additional_capacity_7 = int(round((obj.stage_7 - 15000)/7500))
        obj.additional_capacity_8 = int(round((obj.stage_8 - 15000)/7500))
        obj.save()
     
@shared_task     
def normalize_rail_tonnes():
    rail_tonnes = RailFinal.objects.filter(Q(stage_0__gt=0)| Q(stage_1__gt=0)| Q(stage_2__gt=0)| Q(stage_3__gt=0)| Q(stage_4__gt=0)| Q(stage_5__gt=0)| Q(stage_6__gt=0)| Q(stage_7__gt=0)| Q(stage_8__gt=0))
    for obj in rail_tonnes.iterator():
        obj.stage_0 = round((obj.stage_0)/1000,2)
        obj.stage_1 = round((obj.stage_1)/1000,2)
        obj.stage_2 = round((obj.stage_2)/1000,2)
        obj.stage_3 = round((obj.stage_3)/1000,2)
        obj.stage_4 = round((obj.stage_4)/1000,2)
        obj.stage_5 = round((obj.stage_5)/1000,2)
        obj.stage_6 = round((obj.stage_6)/1000,2)
        obj.stage_7 = round((obj.stage_7)/1000,2)
        obj.stage_8 = round((obj.stage_8)/1000,2)
        obj.save()
           
@shared_task        
def set_rail_capacity():
    rail_dataset = RBC.objects.all() #RailFinal, RBC
    for obj in rail_dataset.iterator():
        obj.addittional_capacity_0 = int(round((obj.stage_0 -7000)/7000))
        obj.addittional_capacity_1 = int(round((obj.stage_1 - 7000)/7000))
        obj.addittional_capacity_2 = int(round((obj.stage_2 -7000)/7000))
        obj.addittional_capacity_3 = int(round((obj.stage_3 -7000)/7000))
        
        obj.addittional_capacity_4 = int(round((obj.stage_4 -37000)/37000))
        obj.addittional_capacity_5 = int(round((obj.stage_5 -37000)/37000))
        obj.addittional_capacity_6 = int(round((obj.stage_6 -37000)/37000))
        obj.addittional_capacity_7 = int(round((obj.stage_7 -37000)/37000))
        obj.addittional_capacity_8 = int(round((obj.stage_8 -37000)/37000))
        obj.save()

@shared_task
def set_dataset_label():
    pass 
    """
    for obj in SectionLoading.objects.filter(data='Rail Traffic'):
        obj.data = 'Road Traffic'
        obj.save()
    """
            
@shared_task        
def target_roads_for_upgrade():
    for obj in section_qs.filter(Q(stage_0__gte=1)| Q(stage_1__gte=1)|Q(stage_2__gte=1)| Q(stage_3__gte=1)|Q(stage_4__gte=1)| Q(stage_5__gte=1)|Q(stage_6__gte=1)| Q(stage_7__gte=1)| Q(stage_8__gte=1)):
        obj.requires_upgrade = True
        obj.save()

@shared_task 
def mark_target_roads_for_upgrade():
    for obj in section_qs.iterator():
        if obj.additional_capacity_0 >=1:
           obj.stage_0_upgrade=True
           obj.save()
           
        elif ob.additional_capacity_1 >=1:
             obj.stage_1_upgrade=True
             obj.save()
             
        elif ob.additional_capacity_2 >=1:
             obj.stage_2_upgrade=True
             obj.save()
             
        elif ob.additional_capacity_3 >=1:
             obj.stage_3_upgrade=True
             obj.save()
             
        elif ob.additional_capacity_4 >=1:
             obj.stage_4_upgrade=True
             obj.save()
             
        elif ob.additional_capacity_5 >=1:
             obj.stage_5_upgrade=True
             obj.save()
             
        elif ob.additional_capacity_6 >=1:
             obj.stage_6_upgrade=True
             obj.save()
             
        elif ob.additional_capacity_7 >=1:
             obj.stage_7_upgrade=True
             obj.save()
             
        elif ob.additional_capacity_8 >=1:
             obj.stage_8_upgrade=True
             obj.save()
             break
        
           
    
  # ------------------------- end of civilization as you know it ----------------------#                    
           
@shared_task    
def mark_unpaved_roads_upgrades():
    unpaved_roads= section_qs.filter(Q(data__icontains='Road Traffic')& Q(surfacecla__iexact='unpaved'))
    for obj in unpaved_roads:#w/out iterator
        pcu = D(obj.optimal_pcus)
        stage_0 = int(round((obj.stage_0 - pcu)/5000))
        stage_1 = int(round((obj.stage_1 - pcu)/5000))
        stage_2 = int(round((obj.stage_2 - pcu)/5000))
        stage_3 = int(round((obj.stage_3 - pcu)/5000))
        stage_4 = int(round((obj.stage_4 - pcu)/5000))
        stage_5 = int(round((obj.stage_5 - pcu)/5000))
        stage_6 = int(round((obj.stage_6 - pcu)/5000))
        stage_7 = int(round((obj.stage_7 - pcu)/5000))
        stage_8 = int(round((obj.stage_8 - pcu)/5000))
        
        if  obj.stage_0 > pcu  and stage_0 >= 1:
            obj.additional_capacity_0 = stage_0
            obj.requires_upgrade = True
            obj.save()
           
        elif obj.stage_1 > pcu and stage_1 >= 1:
             obj.additional_capacity_1 = stage_1
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_2 > pcu and stage_2 >= 1:
             obj.additional_capacity_2 = stage_2
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_3 > pcu and stage_3 >= 1:
             obj.additional_capacity_3 = stage_3
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_4 > pcu and stage_4 >= 1:
             obj.additional_capacity_4 = stage_4
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_5 > pcu and stage_5 >= 1:
             obj.additional_capacity_5 = stage_5
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_6 > pcu and stage_6 >= 1:
             obj.additional_capacity_6 = stage_6
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_7 > pcu and stage_7 >= 1:
             obj.additional_capacity_7 = stage_7
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_8 > pcu and stage_8 >= 1:
             obj.additional_capacity_8 = stage_8
             obj.requires_upgrade = True
             obj.save()
             break
        
             


@shared_task    
def mark_paved_roads_upgrades():
    paved_roads= section_qs.filter(Q(data__icontains='Road Traffic')& Q(surfacecla__iexact='paved'))
    
    for obj in paved_roads.iterator():
        
        if obj.stage_0  > obj.optimal_pcus and round(obj.stage_0 - obj.optimal_pcus) >= 1 :
           obj.additional_capacity_0 = int(round((obj.stage_0 - obj.optimal_pcus)/7500))
           obj.requires_upgrade = True
           obj.save()# not saving any data
           
        elif obj.stage_1 > obj.optimal_pcus and round(obj.stage_1 - obj.optimal_pcus) >= 1:
             obj.additional_capacity_1 = int(round((obj.stage_1 - obj.optimal_pcus)/7500))
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_2 > obj.optimal_pcus and round(obj.stage_2 - obj.optimal_pcus) >= 1:
             obj.additional_capacity_2 = int(round((obj.stage_2 - obj.optimal_pcus)/7500))
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_3 > obj.optimal_pcus and round(obj.stage_3 - obj.optimal_pcus) >= 1:
             obj.additional_capacity_3 = int(round((obj.stage_3 - obj.optimal_pcus)/7500))
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_4 > obj.optimal_pcus and round(obj.stage_4 - obj.optimal_pcus) >= 1:
             obj.additional_capacity_4 = int(round((obj.stage_4 - obj.optimal_pcus)/7500))
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_5 > obj.optimal_pcus and round(obj.stage_5 - obj.optimal_pcus) >= 1:
             obj.additional_capacity_5 = int(round((obj.stage_5 - obj.optimal_pcus)/7500))
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_6 > obj.optimal_pcus and round(obj.stage_6 - obj.optimal_pcus) >= 1:
             obj.additional_capacity_6 = int(round((obj.stage_6 - obj.optimal_pcus)/7500))
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_7 > obj.optimal_pcus and round(obj.stage_7 - obj.optimal_pcus) >= 1:
             obj.additional_capacity_7 = int(round((obj.stage_7 - obj.optimal_pcus)/7500))
             obj.requires_upgrade = True
             obj.save()
             
        elif obj.stage_8 > obj.optimal_pcus and round(obj.stage_8 - obj.optimal_pcus) >= 1:
             obj.additional_capacity_8 = int(round((obj.stage_8 - obj.optimal_pcus)/7500))
             obj.requires_upgrade = True
             obj.save()
             break



               
