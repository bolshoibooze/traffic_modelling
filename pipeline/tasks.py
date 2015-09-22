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

from django.core import urlresolvers
from django.db.models.query import QuerySet
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from .models import *
from mashup.models import Mashup


#python manage.py celery worker --loglevel=info

import gc

def queryset_iterator(queryset, chunksize=1000):
    '''''
    Iterate over a Django Queryset ordered by the primary key

    This method loads a maximum of chunksize (default: 1000) rows in it's
    memory at the same time while django normally would load all rows in it's
    memory. Using the iterator() method only causes it to not preload all the
    classes.

    Note that the implementation of the iterator does not support ordered query sets.
    '''
    pk = 0
    last_pk = queryset.order_by('-pk')[0].pk
    queryset = queryset.order_by('pk')
    while pk < last_pk:
        for row in queryset.filter(pk__gt=pk)[:chunksize]:
            pk = row.pk
            yield row
        gc.collect()

def batch_qs(qs, batch_size=1000):
    total = qs.count()
    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        yield (start, end, total, qs[start:end])




#objs = Pipeline.objects.all()[0:5]

objs = queryset_iterator(Pipeline.objects.all())
pipeline_qs = Pipeline.objects.order_by('id')

"""
insert_list = [origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,commodity_group=obj.commodity_group,distance=obj.distance,data=obj.data,annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,stage_1 = obj.stage_1,stage_2 = obj.stage_2,stage_3 = obj.stage_3,stage_4 = obj.stage_4,stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,stage_8 = obj.stage_8 ]


@shared_task
def pipeline_mashup():
    #for loop test
    import csv
    with open('example.csv','wb') as f:
         for obj in pipeline_qs:
             wr = csv.writer(f)
             a_list = [obj.origin_county,obj.origin_centriod,obj.terminating_county,obj.terminating_centriod,obj.commodity_code]
             wr.writerow(a_list)
             
"""
@shared_task
def set_data_category():
    for obj in pipeline_qs:
        return Pipeline.objects.update(data='Pipeline Traffic')
        

@shared_task            
def pipeline_mashup():
   
    for obj in pipeline_qs:
        m = Mashup(origin_county=obj.origin_county,origin_centriod=obj.origin_centriod,
        terminating_county=obj.terminating_county,terminating_centriod=obj.terminating_centriod,
        commodity_group=obj.commodity_group,distance=obj.distance,data='Pipeline Traffic',annual_traffic=obj.annual_traffic,stage_0 = obj.stage_0,stage_1 = obj.stage_1,stage_2 = obj.stage_2,
        stage_3 = obj.stage_3,stage_4 = obj.stage_4,stage_5 = obj.stage_5,stage_6 = obj.stage_6,stage_7 = obj.stage_7,stage_8 = obj.stage_8 )
        m.save()
          

"""
@shared_task
def pipeline_mashup():
    insert_list = []
    for obj in pipeline_qs.iterator():
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





@shared_task()
def pipeline_mashup():
    insert_list = []
    for start, end, total, qs in batch_qs(pipeline_qs):
        print "Now processing %s - %s of %s" % (start + 1, end, total)
        for obj in pipeline_qs.iterator():
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
        	
    

@shared_task
def pipeline_mashup():
    insert_list = []
    for obj in objs.iterator():
        o_county = obj.origin_county
        o_centriod = obj.origin_centriod
        t_county = obj.terminating_county
        t_centriod = obj.terminating_centriod
        c_group =  obj.commodity_group
        #case_scenario = x
        #data_set = y
        d = obj.distance
        traffic = obj.annual_traffic
        stage0 = obj.stage_0
        stage1 = obj.stage_1
        stage2 = obj.stage_2
        stage3 = obj.stage_3
        stage4 = obj.stage_4
        stage5 = obj.stage_5
        stage6 = obj.stage_6
        stage7 = obj.stage_7
        stage8 = obj.stage_8
        insert_list.append(
        Mashup(origin_county=o_county,origin_centriod=o_centriod,terminating_county=t_county,terminating_centriod=t_centriod,
        commodity_group=c_group,distance=d,annual_traffic=traffic,stage_0=stage0,stage_1=stage1,stage_2=stage2,stage_3=stage3,
        stage_4=stage4,stage_5=stage5,stage_6=stage6,stage_7=stage7,stage_8=stage8)
        )
        data_mashup = Mashup.objects.bulk_create(insert_list)
        return data_mashup
        
#----------------------------------------
@shared_task
def pipeline_mashup():
    insert_list = []
    #try:
    for obj in Pipeline.objects.all().iterator():
                
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
 
 
        
