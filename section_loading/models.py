from __future__ import absolute_import

from django.db import models
from django.db.models import *
from django.conf import settings
from traffic_modelling.settings import *
from django.contrib.gis.db import models
from django.contrib.gis.db.models.fields import MultiPointField
from django.dispatch import receiver
from django.db.models.signals import *
from .fields import *



        
class Main(models.Model):
    origin_county = models.CharField(max_length=50)
    origin_centriod = models.CharField(max_length=50)
    terminating_county = models.CharField(max_length=50)
    terminating_centriod = models.CharField(max_length=50)
    distance = models.IntegerField(default=0)
    optimal_pcus = models.DecimalField(default=0.00,max_digits=50,decimal_places=2) 
    scenario = models.CharField(max_length=20,null=True,blank=True)
    road_class = models.CharField(max_length=10,null=True,blank=True)
    data = models.CharField(max_length=50,null=True,blank=True)
    period =models.CharField(max_length=20,null=True,blank=True)
    surfacecla = models.CharField(max_length=254,null=True,blank=True)
    length_km = models.FloatField(default=0.0)
    northing = models.FloatField(default=0.00)
    easting = models.FloatField(default=0.0)
    
    road_pcus = models.DecimalField(default=0.00,max_digits=50,decimal_places=2) 
    excl_road_pcus = models.DecimalField(default=0.00,max_digits=50,decimal_places=2) 
    
    
    stage_0 = models.DecimalField(default=0.00,max_digits=250,decimal_places=2) 
    additional_capacity_0 = models.BigIntegerField(default=0)
    stage_0_upgrade = models.BooleanField(default=False)
    
    stage_1 = models.DecimalField(default=0.00,max_digits=250,decimal_places=2) 
    additional_capacity_1 = models.BigIntegerField(default=0)
    stage_1_upgrade = models.BooleanField(default=False)
    
    stage_2 = models.DecimalField(default=0.00,max_digits=50,decimal_places=2) 
    additional_capacity_2 = models.BigIntegerField(default=0)
    stage_2_upgrade = models.BooleanField(default=False)
    
    stage_3 = models.DecimalField(default=0.00,max_digits=250,decimal_places=2) 
    additional_capacity_3 = models.BigIntegerField(default=0)
    stage_3_upgrade = models.BooleanField(default=False)
    
    stage_4 = models.DecimalField(default=0.00,max_digits=50,decimal_places=2) 
    additional_capacity_4 = models.BigIntegerField(default=0)
    stage_4_upgrade = models.BooleanField(default=False)
    
    stage_5 = models.DecimalField(default=0.00,max_digits=250,decimal_places=2) 
    additional_capacity_5 = models.BigIntegerField(default=0)
    stage_5_upgrade = models.BooleanField(default=False)
    
    stage_6 = models.DecimalField(default=0.00,max_digits=250,decimal_places=2) 
    additional_capacity_6 = BigIntegerField(default=0)
    stage_6_upgrade = models.BooleanField(default=False)
    
    stage_7 = models.DecimalField(default=0.00,max_digits=250,decimal_places=2) 
    additional_capacity_7 = BigIntegerField(default=0)
    stage_7_upgrade = models.BooleanField(default=False)
    
    stage_8 = models.DecimalField(default=0.00,max_digits=250,decimal_places=2) 
    additional_capacity_8 = models.BigIntegerField(default=0)
    stage_8_upgrade = models.BooleanField(default=False)
    class Meta(object):
        abstract = True
        
def create_scenario_wrapper(sender, **kwargs):
    from rail.models import create_scenario
    create_scenario(sender, **kwargs)  
        
class Pipeline(Main):
    pass
    
    class Meta(object):
        db_table = 'Pipeline Dataset'
        verbose_name_plural = 'Pipeline Dataset'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(Pipeline,self).save(*args,**kwargs)
        
        
# ------------ rail datasets -----------------#
        
class RBC(Main):
    pass
    
    class Meta(object):
        db_table = 'Rail Base Case'
        verbose_name_plural = 'Rail Base Case'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(RBC,self).save(*args,**kwargs)
        
        
class RailFinal(Main):
    pass
    
    class Meta(object):
        db_table = 'RailFinal'
        verbose_name_plural = 'RailFinal'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(RailFinal,self).save(*args,**kwargs)
        
        

        
class RailTrafficWorking(Main):
    pass
    
    class Meta(object):
        db_table = 'RailTrafficWorking'
        verbose_name_plural = 'RailTrafficWorking'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(RailTrafficWorking,self).save(*args,**kwargs)
        
# --------------- end of rail datasets -------------------#

class RoadBaseCase(Main):
    pass
    class Meta(object):
        db_table = 'RoadBaseCase'
        verbose_name_plural = 'RoadBaseCase'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(RoadBaseCase,self).save(*args,**kwargs)
        
class BWF(Main):
    pass
    
    class Meta(object):
        db_table = 'BWF:Base Working File'
        verbose_name_plural = 'BWF:Base Working File'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(BWF,self).save(*args,**kwargs)
        
        

        
        
class RoadFinal(Main):
    pass
    
    class Meta(object):
        db_table = 'RoadFinal'
        verbose_name_plural = 'RoadFinal'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(RoadFinal,self).save(*args,**kwargs)
        
class BCSP(Main):
    pass
    
    class Meta(object):
        db_table = 'Projections: Base Case'
        verbose_name_plural = 'Projections: Base Case'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(BCSP,self).save(*args,**kwargs)
        
class xPOL(Main):
    pass
    
    class Meta(object):
        db_table = 'Projections:Without POL Import'
        verbose_name_plural = 'Projections:Without POL Imports'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(xPOL,self).save(*args,**kwargs)
        
        
class LPW(Main):
    pass
    
    class Meta(object):
        db_table = 'LPW: With Lamu Port Working'
        verbose_name_plural = 'LPW: With Lamu Port Working'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(LPW,self).save(*args,**kwargs)
        
        
class LTFC(Main):
    pass
    
    class Meta(object):
        db_table = 'LTFC: Lamu Traffic'
        verbose_name_plural = 'LTFC: Lamu Traffic'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(LTFC,self).save(*args,**kwargs)
        
        
class LPCU(Main):
    pass
     
    class Meta(object):
        db_table = 'Road Tfc Loading PCU'
        verbose_name_plural = 'Road Tfc Loading PCU'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(LPCU,self).save(*args,**kwargs)
        
class PLS(Main):
    pass
     
    class Meta(object):
        db_table = 'Prop. Lamu Share'
        verbose_name_plural = 'Prop. Lamu Share'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(PLS,self).save(*args,**kwargs)
        
        
class TTFCP(Main):
    pass
     
    class Meta(object):
        db_table = 'Projections: Total Traffic'
        verbose_name_plural = 'Projections: Total Traffic'
        
    def __unicode__(self):
        return self.origin_county
        
    def save(self,*args,**kwargs):
        super(TTFCP,self).save(*args,**kwargs)
        
        
        
        

        
#models.signals.post_save.connect(create_scenario_wrapper,sender=Scenario)
        
# --------- end of road dataset -------------#

# ---- Main Mashup Model -----#

"""
class SectionMashup(models.Model):
    dataset = models.ForeignKey(TTFCP,null=True,blank=True,verbose_name='Total Tfc Projection')
    rbc = models.ForeignKey(RBC,null=True,blank=True,verbose_name='Rail Tfc Base Case')
    rlfinal = models.ForeignKey(RailFinal,null=True,blank=True,verbose_name='RL Final')
    rlw = models.ForeignKey(RailTrafficWorking,null=True,blank=True,verbose_name='Rail Tfc Working')
    
    bwf = models.ForeignKey(BWF,null=True,blank=True,verbose_name='Base Working File')
    rdbc  = models.ForeignKey(RdBC,null=True,blank=True,verbose_name='Road Tfc Base Case')
    rdfinal = models.ForeignKey(RoadFinal,null=True,blank=True,verbose_name='Road Final Tfc Tonnes')
    bcsp = models.ForeignKey(BCSP,null=True,blank=True,verbose_name='Porjections BS CS')
    xpol = models.ForeignKey(xPOL,null=True,blank=True,verbose_name='Without POL Imports')
    lpw  = models.ForeignKey(LPW,null=True,blank=True,verbose_name='Lamu Port Working')
    ltfc = models.ForeignKey(LTFC,null=True,blank=True,verbose_name='Lamu Traffic')
    lpcu = models.ForeignKey(LPCU,null=True,blank=True,verbose_name='Rd Tfc Loading PCU')
    pls = models.ForeignKey(PLS,null=True,blank=True,verbose_name='Prop. Share Lamu')
    
    class Meta(object)
        db_table = 'SectionLoadingMashup'
        verbose_name_plural = 'SectionLoadingMashup'
        
    def _unicode__(self):
        return unicode(self.dataset)
        
    def save(self,*args,**kwargs):
        super(SectionMashup,self).save(*args,**kwargs)
        
"""
# ----- end of mashup model ---- #      
        

        
"""
 RailBase = 'RlBC'
    RailWorking = 'RTfcW'
    RailFinal = 'RLFinal'
    
    RoadBase = 'RdBC'
    BaseWF = 'BWF'
    RoadFinal = 'RdFinal'
    POL = 'exPOL'
    LPort = 'LPW'
    RdPCUs = 'RdTfcPCUs'
    PjBSCS = 'PjctnBSCS'
    PROP = 'PropLShare'
    EMPTY = 'EMPTY'
    
    SCENARIOS = (
        (EMPTY,'Empty'),
   	(RailBase,'Rail Base Case'),
   	(RailWorking,'Rail Traffic Working'),
   	(RailFinal,'RL Final'),
   
   	(RoadBase,'Road Base Case'),
   	(BaseWF,'Base Working File'),
   	(RoadFinal,'Road Traffic Final'),
   	(POL,'Without POL Imports'),
   	(LPort,'Lamu Port Working'),
   	(RdPCUs,'RdTfcLoading PCUs'),
   	(PjBSCS,'Projections BS CS'),
   	(PROP,'Prop. Lamu Share'),
    
    )
    

    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    'section_loading.',
    


"""
