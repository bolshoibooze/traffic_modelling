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
from mashup.models import Mashup

#for dropping down to raw sql
from django.db import connection,transaction

#app = Celery('cardpesr',default_retry_delay=30, max_retries=5)

# celery -A traffic_modelling  worker --loglevel=INFO


rail_tfc_qs = RailTraffic.objects.all().order_by('id')
rl_final_qs = RLFinal.objects.all().order_by('id')
rl_tfc_wrking_qs = RaiTfcWrking.objects.all().order_by('id')

@shared_task()
def railtfc_mashup():
    insert_list = []
    for obj in rail_tfc_qs.iterator():
        rail_tfc = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Rail Traffic',
        	annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,scenario='Rail Base Case',
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8)
        rail_tfc.save()
        
        
        	
@shared_task()
def rail_final_mashup():
    for obj in rl_final_qs.iterator():
        rail_final = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Rail Traffic',
        	annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8,scenario='RL Final')
        rail_final.save()
        
        
@shared_task()
def rl_tfc_wrking_mashup():
    for obj in rl_tfc_wrking_qs.iterator():
        rail = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data='Rail Traffic',
        	annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8,scenario='Rail Traffic Working')
        rail.save()

"""
@shared_task(default_retry_delay=30,max_retries=5) 
def railway_mashup():
    insert_list = []
    try:
    	for obj in objs.iterator():
        	#do_bulk_update
        	insert_list.append(
        	Mashup(
        	origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        	terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        	commodity_group=obj.commodity_group,distance=obj.distance,data=obj.data,
        	annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,
        	stage_1 = obj.stage_1,
        	stage_2 = obj.stage_2,
        	stage_3 = obj.stage_3,
        	stage_4 = obj.stage_4,
        	stage_5 = obj.stage_5,
        	stage_6 = obj.stage_6,
        	stage_7 = obj.stage_7,
        	stage_8 = obj.stage_8
        	))
        	mashup = Mashup.objects.bulk_create(insert_list)
        	return mashup
        	
    except Exception as e:
        print('Retrying task...')
        self.retry(e)            
      
      

# For reference: just in case
------------------------------
def pipeline_mashup():
    insert_list = []
    for obj in objs.iterator()
        o_county = obj.origin_county
        o_centriod = obj.origin_centriod
        t_county = obj.terminating_county
        t_centriod = obj.terminating_centriod
        c_group =  commodity_group
        #case_scenario = x
        data_set = y
        d = int(obj.distance)
        stage_0 = int(obj.stage_0)
        stage_1 = int(obj.stage_1)
        stage_2 = int(obj.stage_2)
        stage_3 = int(obj.stage_3)
        stage_4 = int(obj.stage_4)
        stage_5 = int(obj.stage_5)
        stage_6 = int(obj.stage_6)
        stage_7 = int(obj.stage_7)
        stage_8 = int(obj.stage_8)
        #do_bulk_update
        insert_list.append(
        Mashup(origin_county=o_county,origin_centriod=o_centriod,terminating_county=t_county,
        terminating_centriod=t_centriod,commodity_group=c_group,
        stage_0 = obj.stage_0,
        stage_1 = obj.stage_1,
        stage_2 = obj.stage_2,
        stage_3 = obj.stage_3,
        stage_4 = obj.stage_4,
        stage_5 = obj.stage_5,
        stage_6 = obj.stage_6,
        stage_7 = obj.stage_7,
        stage_8 = obj.stage_8
        )
        


"""  
 
 
        
