from __future__ import absolute_import

from django.db import models
from django.db.models import *
from django.conf import settings
from traffic_modelling.settings import *
from django.contrib.gis.db import models
from django.contrib.gis.db.models.fields import MultiPointField


from django.db.models.fields import IntegerField


class BigIntegerField(IntegerField):
    empty_strings_allowed=False
    def get_internal_type(self):
        return "BigIntegerField"	
    def db_type(self):
        return 'bigint' # Note this won't work with Oracle.


class MashupExtras(models.Model):
    #for origin county
    o_county_easting = models.FloatField(default=0.0)
    o_county_northing = models.FloatField(default=0.0)
   
    o_centriod_easting = models.FloatField(default=0.0)
    o_centriod_northing = models.FloatField(default=0.0)
   
    #for terminating county
    t_county_easting = models.FloatField(default=0.0)
    t_county_northing = models.FloatField(default=0.0)
   
    t_centriod_easting = models.FloatField(default=0.0)
    t_centriod_northing = models.FloatField(default=0.0)
    
    #other model objects/fields
    annual_traffic = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    road_pcus = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    excl_road_pcus = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_0 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    additional_capacity_0 = models.IntegerField(default=0)
    
    stage_1 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    additional_capacity_1 = models.IntegerField(default=0)
    
    stage_2 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    additional_capacity_2 = models.IntegerField(default=0)
    
    stage_3 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    additional_capacity_3 = models.IntegerField(default=0)
    
    stage_4 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    additional_capacity_4 = models.IntegerField(default=0)
    
    stage_5 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    additional_capacity_5 = models.IntegerField(default=0)
    
    stage_6 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    additional_capacity_6 = models.IntegerField(default=0)
    
    stage_7 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    additional_capacity_7 = models.IntegerField(default=0)
    
    stage_8 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    additional_capacity_8 = models.IntegerField(default=0)
    #emergency field objs
    dataset_0 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_0'
    ) 
    dataset_1 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_1'
    ) 
    dataset_2 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_2'
    ) 
    dataset_3 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_3'
    ) 
    dataset_4 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_4'
    ) 
    dataset_5 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_5'
    ) 
    dataset_9 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_9'
    ) 
    dataset_6 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_6'
    ) 
    dataset_7 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_7'
    ) 
    dataset_8 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2,
    verbose_name='To be edited_8'
    ) 
    class Meta(object):
        abstract=True
 



       
class Mashup(MashupExtras):
    #normalization of all datasets viz. routes
    origin_county = models.CharField(max_length=50)
    origin_centriod = models.CharField(max_length=50)
    commodity_group = models.CharField(max_length=50)
    terminating_county = models.CharField(max_length=50)
    terminating_centriod = models.CharField(max_length=50)
    distance = models.IntegerField(default=0)
    #---- special unit items --------------------#
    optimal_pcus = models.DecimalField(default=0.00,max_digits=50,decimal_places=2) 
    #dataset = models.CharField(max_length=10,choices=settings.DATA,null=True,blank=True)
    scenario = models.CharField(max_length=100,default='Base Case')
    road_class = models.CharField(max_length=10,default='N/A')
    data = models.CharField(max_length=20,default='N/A')
    period =models.CharField(max_length=20,default='N/A')
    mapping_road_class = models.CharField(max_length=5,null=True,blank=True)#contingency_road_class
    surfacecla = models.CharField(max_length=254,null=True,blank=True)
    requires_updgrade = models.BooleanField(default=False)
    length_km = models.FloatField(default=0.0)
    northing = models.FloatField(default=0.00)#origin_county & origin_centriod
    easting = models.FloatField(default=0.0)#origin_county & origin_centriod
   
    
    #we need another pair of northing & easting for: terminating_centriod,terminating_county?
    multi = models.FloatField(default=0.0)#dummy
    #geom = models.MultiPointField(srid=4326)

    objects =  models.Manager()
    geo = models.GeoManager()
    
    class Meta(object):
        db_table = 'Mashup'
        verbose_name_plural = 'Mashup'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(Mashup,self).save(*args,**kwargs)
        
        




