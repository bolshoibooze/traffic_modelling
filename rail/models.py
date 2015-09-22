from django.db import models
from django.db.models import *
from django.conf import settings
from traffic_modelling.settings import *
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from section_loading.models import *
from pipeline.fields import *
from pipeline.models import *

class Rail(models.Model):
    base_case_mode = models.CharField(
    max_length=50,null=True,blank=True
    )
    rail_cum_road = models.CharField(
    max_length=50,null=True,blank=True
    )
    sn = models.IntegerField(default=0)
    origin_county = models.CharField(max_length=50)
    origin_centriod = models.CharField(max_length=50)
    origin_code = models.IntegerField(default=0)
    terminating_county = models.CharField(max_length=50)
    terminating_centriod = models.CharField(max_length=50)
    destination_code = models.IntegerField(default=0)
    commodity_group = models.CharField(max_length=50)
    commodity_code = models.IntegerField(default=0)
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
        abstract = True
        
class RailTraffic(Rail):
    """rail traffic dataset"""
    data = models.CharField(max_length=20,default='Rail Traffic')
    class Meta(object):
        db_table = 'RailTraffic'
        verbose_name_plural = 'RailTraffic'
        
    def __unicode__(self):
        return self.data
        
    def save(self,*args,**kwargs):
        super(RailTraffic,self).save(*args,**kwargs)
        
        
class RLFinal(Rail):
    """dataset as named"""
    dataset = models.CharField(max_length=10,default='Rail Traffic Working',verbose_name='Scenario')
    data = models.CharField(max_length=20,choices=settings.DATA,default=3)
    class Meta(object):
        db_table = 'RLFinal'
        verbose_name_plural = 'RLFinal'
        
    def __unicode__(self):
        return self.dataset
        
    def save(self,*args,**kwargs):
        super(RLFinal,self).save(*args,**kwargs)


class RaiTfcWrking(Rail):
    """dataset as named"""
    dataset = models.CharField(max_length=10,default='Rail Traffic Working',verbose_name='Scenario')
    data = models.CharField(max_length=20,choices=settings.DATA,default='Rail Traffic')
    class Meta(object):
        db_table = 'RaiTfcWrking'
        verbose_name_plural = 'RaiTfcWrking'
        
    def __unicode__(self):
        return self.dataset
        
    def save(self,*args,**kwargs):
        super(RaiTfcWrking,self).save(*args,**kwargs)




#let's do some post_save() signals


def create_scenario(sender,instance, **kwargs):
    if kwargs.get('created') is True:
       SectionLoading.objects.get_or_create(scenarios=kwargs.get('instance'))
       

