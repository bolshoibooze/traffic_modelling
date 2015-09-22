from django.db import models
from django.db.models import *
from django.conf import settings
from traffic_modelling.settings import *
from pipeline.fields import *
from pipeline.models import *


class Road(Classic):
    base_case_mode = models.CharField(
    max_length=50,null=True,blank=True
    )
    rail_cum_road = models.CharField(
    max_length=50,null=True,blank=True
    )
    rail_based_commodity = models.CharField(
    max_length=50,null=True,blank=True
    )
    class Meta(object):
        abstract=True
        
        
class RoadBase(BaseCaseMode):
    distance =models.IntegerField(default=0)
    stage_0 = models.IntegerField(default=0)
    stage_1 = models.IntegerField(default=0)
    stage_2 = models.IntegerField(default=0)
    stage_3 = models.IntegerField(default=0)
    stage_4 = models.IntegerField(default=0)
    stage_5 = models.IntegerField(default=0)
    stage_6 = models.IntegerField(default=0)
    stage_7 = models.IntegerField(default=0)
    stage_8 = models.IntegerField(default=0)
    data = models.CharField(max_length=50,default='Road Traffic')
    class Meta(object):
        abstract = True
        
        
class BaseWorkingFile(RoadBase):
    dataset = models.CharField(max_length=50,verbose_name='Scenario',default='Base Working File')
    class Meta(object):
        db_table = 'BaseWorkingFile'
        verbose_name_plural = 'BaseWorkingFile'
        
    def __unicode__(self):
        return self.base_case_mode
        
    def save(self,*args,**kwargs):
        super(BaseWorkingFile,self).save(*args,**kwargs)
        
   
        
class RoadTraffic(RoadBase):
    """road traffic dataset"""
    #road traffic final tonnes
    #projection bs cs
    road_tonnes = models.IntegerField(default=0)
    class Meta(object):
        db_table = 'Road Traffic'
        verbose_name_plural = 'Road Traffic'
        
    def __unicode__(self):
        return unicode(self.road_tonnes)
        
    def save(self,*args,**kwargs):
        super(RoadTraffic,self).save(*args,**kwargs)

        
class FinalTraffic(RoadBase):
    dataset = models.CharField(max_length=50,verbose_name='Scenario',default='Road Traffic Final')
    excl_road_tonnes = models.IntegerField(default=0)
    class Meta(object):
        db_table = 'Rd Tfc Final Tonnes'
        verbose_name_plural = 'Rd Tfc Final Tonnes'
        
    def __unicode__(self):
        return self.dataset
        
    def save(self,*args,**kwargs):
        super(FinalTraffic,self).save(*args,**kwargs)
    
        
class Projection(RoadBase):
    """projections base case"""
    excl_road_tonnes = models.IntegerField(default=0)
    rail_based_commodity = models.CharField(max_length=50,null=True,blank=True)
    potential_rail_share = models.DecimalField(default=0.00,max_digits=50,decimal_places=2) 
    dataset = models.CharField(max_length=80,verbose_name='Scenario',default='Base Case Projections')
    
    class Meta(object):
        db_table = 'Projections BS CS'
        verbose_name_plural = 'Projections BS CS'
        
    def __unicode__(self):
        return self.dataset
        
    def save(self,*args,**kwargs):
        super(Projection,self).save(*args,**kwargs)
        
        
        
class ExcPOL(Standard):
    """ projection without POL import """
    dataset = models.CharField(max_length=80,verbose_name='Scenario',default='Projctn Without POL Imports')
    distance =models.IntegerField(default=0)
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
        db_table = 'Projection Without POL Import'
        verbose_name_plural = 'Projection Without POL Imports'
        
    def __unicode__(self):
        return self.dataset
        
    def save(self,*args,**kwargs):
        super(ExcPOL,self).save(*args,**kwargs)
        

        
class PCUData(Standard):
    """has two weird pcu fields"""
    data = models.CharField(max_length=50,default='Road Traffic')
    is_lamu = CustomBooleanField(default=False)#deals with Y/N values
    rail_cum_road = models.CharField(max_length=50)
    rail_based_commodity = models.CharField(max_length=50)
    potential_rail_share = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    distance =models.IntegerField(default=0)
    annual_traffic = models.IntegerField(default=0)
    road_pcus = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    excl_road_pcus = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_0 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_1 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_2 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_3 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_4 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_5 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_6 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_7 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    stage_8 = models.DecimalField(
    default=0.00,max_digits=50,decimal_places=2
    ) 
    class Meta(object):
        abstract=True
        
class LamuPortWorking(PCUData):
    """scenario case data"""
    dataset = models.CharField(max_length=50,verbose_name='Scenario',default='Lamu Port Working',)
    class Meta(object):
        db_table = 'LamuPortWorking'
        verbose_name_plural = 'LamuPortWorking'
        
    def __unicode__(self):
        return self.dataset
        
    def save(self,*args,**kwargs):
        super(LamuPortWorking,self).save(*args,**kwargs)
        
        
        
class LamuTraffic(PCUData):
    """simply named dataset"""
    dataset = models.CharField(max_length=50,verbose_name='Scenario',default='Lamu Traffic')
    class Meta(object):
        db_table = 'LamuTraffic'
        verbose_name_plural = 'LamuTraffic'
        
    def __unicode__(self):
        return self.dataset
        
    def save(self,*args,**kwargs):
        super(LamuTraffic,self).save(*args,**kwargs)
        
        
class RdTfcLoading(PCUData):
    """road traffic loading pcus"""
    dataset = models.CharField(max_length=100,verbose_name='Scenario',default='Road Traffic Loading PCUs')
    class Meta(object):
        db_table = 'RdTfcLoading'
        verbose_name_plural = 'RdTfcLoading'
        
    def __unicode__(self):
        return self.dataset
        
    def save(self,*args,**kwargs):
        super(RdTfcLoading,self).save(*args,**kwargs)
    
    
class LamuProportinateShare(PCUData):
   dataset = models.CharField(max_length=100,verbose_name='Scenario',default='Prop. Lamu Share')
   class Meta(object):
       db_table = 'Proportionate Share of Lamu'
       verbose_name_plural = 'Proportionate Share of Lamu'
       
   def __unicode__(self):
       return self.dataset
       
   def save(self,*args,**kwargs):
       super(LamuProportinateShare,self).save(*args,**kwargs)
       
       
class TotalTfcProjections(Standard):
    """road+rail+pipeline"""
    data = models.CharField(max_length=50,default='Ttl Combined Tfc')
    dataset = models.CharField(max_length=100,verbose_name='Scenario',default='All:Total Tfc')
    distance =models.IntegerField(default=0)
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
        db_table = 'Total Tfc Projection'
        verbose_name_plural = 'Total Tfc Projections'
        
    def __unicode__(self):
        return self.dataset
        
    def save(self,*args,**kwargs):
        super(TotalTfcProjections,self).save(*args,**kwargs)
        
        
        
       
       
   
   
   
