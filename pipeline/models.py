from django.db import models
from django.db.models import *
from django.conf import settings
from traffic_modelling.settings import *
from pipeline.fields import *

# Create your models here.

class BaseCaseMode(models.Model):
    base_case_mode = models.CharField(max_length=50,null=True,blank=True)
    rail_cum_road = models.CharField(max_length=50,null=True,blank=True)
    sn = models.IntegerField(default=0)
    origin_county = models.CharField(max_length=50)
    origin_centriod = models.CharField(max_length=50)
    origin_code = models.IntegerField(default=0)
    terminating_county = models.CharField(max_length=50)
    terminating_centriod = models.CharField(max_length=50)
    destination_code = models.IntegerField(default=0)
    commodity_group = models.CharField(max_length=50)
    commodity_code = models.IntegerField(default=0)
    class Meta(object):
        abstract=True

class Standard(models.Model):
    sn = models.IntegerField(default=0)
    origin_county = models.CharField(max_length=50)
    origin_centriod = models.CharField(max_length=50)
    origin_code = models.IntegerField(default=0)
    terminating_county = models.CharField(max_length=50)
    terminating_centriod = models.CharField(max_length=50)
    destination_code = models.IntegerField(default=0)
    commodity_group = models.CharField(max_length=50)
    commodity_code = models.IntegerField(default=0)
    class Meta(object):
        abstract=True
        
class Classic(Standard):
    distance = models.IntegerField(default=0)
    annual_traffic_0 = models.IntegerField(default=0)
    tkm_0 = models.IntegerField(default=0)
    annual_traffic_1 = models.IntegerField(default=0)
    tkm_1 = models.IntegerField(default=0)
    annual_traffic_2 = models.IntegerField(default=0)
    tkm_2 = models.IntegerField(default=0)
    annual_traffic_3 = models.IntegerField(default=0)
    tkm_3 = models.IntegerField(default=0)
    annual_traffic_4 = models.IntegerField(default=0)
    tkm_4 = models.IntegerField(default=0)
    annual_traffic_5 = models.IntegerField(default=0)
    tkm_5 = models.IntegerField(default=0)
    annual_traffic_6 = models.IntegerField(default=0)
    tkm_6 = models.IntegerField(default=0)
    annual_traffic_7 = models.IntegerField(default=0)
    tkm_7 = models.IntegerField(default=0)
    annual_traffic_8 = models.IntegerField(default=0)
    tkm_8 = models.IntegerField(default=0)
    class Meta(object):
        abstract = True
        


        

        

    
        
class Other(BaseCaseMode):
    """ mostly covers road traffic projections"""
    rail_based_commodity = models.CharField(max_length=50)
    potential_rail_share = models.DecimalField() 
    distance =models.IntegerField(default=0)
    annual_traffic = models.IntegerField(default=0)
    road_tonnes = models.IntegerField(default=0)
    stage_1 = models.IntegerField(default=0)
    stage_2 = models.IntegerField(default=0)
    stage_3 = models.IntegerField(default=0)
    stage_4 = models.IntegerField(default=0)
    stage_5 = models.IntegerField(default=0)
    stage_6 = models.IntegerField(default=0)
    stage_7 = models.IntegerField(default=0)
    stage_8 = models.IntegerField(default=0)
   
    class Meta(object):
        abstract = True
        
class BaseTfcProjection(BaseCaseMode):
    """projections with base traffic working"""
    rail_based_commodity = models.CharField(max_length=50)
    potential_rail_share = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    distance =models.IntegerField(default=0)
    annual_traffic = models.IntegerField(default=0)
    stage_0 = models.IntegerField(default=0)
    stage_1 = models.IntegerField(default=0)
    stage_2 = models.IntegerField(default=0)
    stage_3 = models.IntegerField(default=0)
    stage_4 = models.IntegerField(default=0)
    stage_5 = models.IntegerField(default=0)
    stage_6 = models.IntegerField(default=0)
    stage_7 = models.IntegerField(default=0)
    stage_8 = models.IntegerField(default=0)
    class Meta(object):
        pass 
        
        
class MashupExtras(models.Model):
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
     

        


    

class Pipeline(Standard):
    """doesn't regard model obj ordering"""
    rail_based_commodity = models.CharField(max_length=50)
    potential_rail_share = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    )  
    distance =models.IntegerField(default=0)
    annual_traffic = models.IntegerField(default=0)
    stage_0 = models.IntegerField(default=0)
    stage_1 = models.IntegerField(default=0)
    stage_2 = models.IntegerField(default=0)
    stage_3 = models.IntegerField(default=0)
    stage_4 = models.IntegerField(default=0)
    stage_5 = models.IntegerField(default=0)
    stage_6 = models.IntegerField(default=0)
    stage_7 = models.IntegerField(default=0)
    stage_8 = models.IntegerField(default=0)
    data = models.CharField(
    max_length=20,default='Pipeline Traffic'
    )
    
    class Meta(object):
        db_table = 'Pipeline'
        verbose_name_plural = 'Pipeline'
        
    def __unicode__(self):
        return self.rail_based_commodity
        
    def save(self,*args,**kwargs):
        super(Pipeline,self).save(*args,**kwargs)
        
"""        
def tag_scenario():
    for obj in objs:
        if obj.rail_based_scenario not None:
           return #obj.scenario_name = update appropriate boolean field
        elif continue
"""



"""
    base_case_mode = models.CharField(
    max_length=50,null=True,blank=True
    )
    rail_cum_road = models.CharField(
    max_length=50,null=True,blank=True
    )

"""
