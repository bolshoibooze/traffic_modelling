from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import *


class Abc(models.Model):
    station = models.CharField(max_length=254)
    name = models.CharField(max_length=100)
    from_field = models.CharField(max_length=254)
    to_field = models.CharField(max_length=254)
    total_aadt = models.IntegerField()
    road_class = models.CharField(max_length=1)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()
    
    class Meta(object):
        db_table = 'Abc'
        verbose_name_plural = 'Abc'
        
    def __unicode__(self):
        return self.station
        
    def save(self,*args,**kwargs):
        super(Abc,self).save(*args,**kwargs)




class Stretch(models.Model):
    rid = models.CharField(max_length=20)
    surfacecla = models.CharField(max_length=10)
    old_rid2 = models.CharField(max_length=40)
    road_class = models.CharField(max_length=1)
    station = models.CharField(max_length=40)
    old_class = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    length_km = models.FloatField()
    total_aadt = models.IntegerField()
    from_field = models.CharField(max_length=254)
    to_field = models.CharField(max_length=254)
    easting = models.FloatField()
    northing = models.FloatField()
    surfacing = models.CharField(max_length=254)
    roadcond = models.CharField(max_length=254)
    mc = models.FloatField()
    c = models.FloatField()
    lc_4wd = models.FloatField()
    p_van = models.FloatField()
    m = models.FloatField()
    sb = models.FloatField()
    lb = models.FloatField()
    lt = models.FloatField()
    mt = models.FloatField()
    ht = models.FloatField()
    art_t = models.FloatField()
    other = models.FloatField()
    orig_fid = models.IntegerField()
    new = models.CharField(max_length=3)
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()
    
    class Meta(object):
        db_table = 'Stretch'
        verbose_name_plural = 'Stretch'
        
    def __unicode__(self):
        return self.rid
        
    def save(self,*args,**kwargs):
        super(Stretch,self).save(*args,**kwargs)
        
        
class BatchTest(models.Model):
    rid = models.CharField(max_length=20)
    surfacecla = models.CharField(max_length=10)
    old_rid2 = models.CharField(max_length=40)
    road_class = models.CharField(max_length=1)
    station = models.CharField(max_length=40)
    old_class = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    length_km = models.FloatField()
    total_aadt = models.IntegerField()
    from_field = models.CharField(max_length=254)
    to_field = models.CharField(max_length=254)
    easting = models.FloatField()
    northing = models.FloatField()
    surfacing = models.CharField(max_length=254)
    roadcond = models.CharField(max_length=254)
    mc = models.FloatField()
    c = models.FloatField()
    lc_4wd = models.FloatField()
    p_van = models.FloatField()
    m = models.FloatField()
    sb = models.FloatField()
    lb = models.FloatField()
    lt = models.FloatField()
    mt = models.FloatField()
    ht = models.FloatField()
    art_t = models.FloatField()
    other = models.FloatField()
    orig_fid = models.IntegerField()
    new = models.CharField(max_length=3)
    class Meta(object):
        db_table = 'BatchTest'
        verbose_name_plural = 'BatchTest'
        
    def __unicode__(self):
        return self.rid
        
    def save(self,*args,**kwargs):
        super(BatchTest,self).save(*args,**kwargs)
        
        

class Town(models.Model):
    town_name = models.CharField(max_length=20)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()
    
    class Meta(object):
        db_table = 'Major Town'
        verbose_name_plural = 'Major Towns'
        
    def __unicode__(self):
        return self.town_name
        
    def save(self,*args,**kwargs):
        super(Town,self).save(*args,**kwargs)


class MajorRoad(models.Model):
    kenroad_id = models.FloatField()
    geom = models.MultiLineStringField(srid=-1)
    objects = models.GeoManager()
    
    class Meta(object):
        db_table = 'Major Road'
        verbose_name_plural = 'Major Road'
        
    def __unicode__(self):
        return unicode(self.kenroad_id)
        
    def save(self,*args,**kwargs):
        super(MajorRoad,self).save(*args,**kwargs)


class StretchData(models.Model):
    rid = models.CharField(max_length=20)
    surfacecla = models.CharField(max_length=10)
    old_rid2 = models.CharField(max_length=40)
    road_class = models.CharField(max_length=1)
    station = models.CharField(max_length=40)
    old_class = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    length_km = models.FloatField()
    total_aadt = models.IntegerField()
    from_field = models.CharField(max_length=254)
    to_field = models.CharField(max_length=254)
    easting = models.FloatField()
    northing = models.FloatField()
    surfacing = models.CharField(max_length=254)
    roadcond = models.CharField(max_length=254)
    mc = models.FloatField()
    c = models.FloatField()
    lc_4wd = models.FloatField()
    p_van = models.FloatField()
    m = models.FloatField()
    sb = models.FloatField()
    lb = models.FloatField()
    lt = models.FloatField()
    mt = models.FloatField()
    ht = models.FloatField()
    art_t = models.FloatField()
    other = models.FloatField()
    orig_fid = models.IntegerField()
    new = models.CharField(max_length=3)
    geom = models.MultiLineStringField(srid=3857)
    objects = models.GeoManager()
    
    class Meta(object):
        db_table = 'StretchData'
        verbose_name_plural = 'StretchData'
        
    def __unicode__(self):
        return self.rid
        
    def save(self,*args,**kwargs):
        super(StretchData,self).save(*args,**kwargs)
        
        
        
        
        
class Section(models.Model):
    rid = models.CharField(max_length=20)
    surfacecla = models.CharField(max_length=10)
    old_rid2 = models.CharField(max_length=40)
    road_class = models.CharField(max_length=1)
    station = models.CharField(max_length=40)
    old_class = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    length_km = models.FloatField()
    total_aadt = models.IntegerField()
    from_field = models.CharField(max_length=254)
    to_field = models.CharField(max_length=254)
    easting = models.FloatField()
    northing = models.FloatField()
    surfacing = models.CharField(max_length=254)
    roadcond = models.CharField(max_length=254)
    mc = models.FloatField()
    c = models.FloatField()
    lc_4wd = models.FloatField()
    p_van = models.FloatField()
    m = models.FloatField()
    sb = models.FloatField()
    lb = models.FloatField()
    lt = models.FloatField()
    mt = models.FloatField()
    ht = models.FloatField()
    art_t = models.FloatField()
    other = models.FloatField()
    orig_fid = models.IntegerField()
    new = models.CharField(max_length=3)
    geom = models.MultiLineStringField(srid=3857)
    objects = models.GeoManager()
    class Meta(object):
        db_table = 'Road Stretch'
        verbose_name_plural = 'Road Stretch'
        
    def __unicode__(self):
        return self.rid
        
    def save(self,*args,**kwargs):
        super(Section,self).save(*args,**kwargs)
        
        
        
    
class GoogleRoads(models.Model):
    rid = models.CharField(max_length=50)
    name1 = models.CharField(max_length=100)
    lang1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    lang2 = models.CharField(max_length=100)
    name3 = models.CharField(max_length=100)
    lang3 = models.CharField(max_length=100)
    rtenum = models.CharField(max_length=20)
    cntrycode = models.CharField(max_length=50)
    provname = models.CharField(max_length=50)
    usage = models.CharField(max_length=50)
    surface = models.CharField(max_length=60)
    elevation = models.CharField(max_length=60)
    priority = models.CharField(max_length=20)
    condition = models.CharField(max_length=50)
    divider = models.CharField(max_length=20)
    constructn = models.CharField(max_length=20)
    avgspeed = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    
    objects = models.GeoManager()
    
    class Meta(object):
        db_table = 'GoogleRoads'
        verbose_name_plural = 'GoogleRoads'
        
    def __unicode__(self):
        return self.condition
        
    def save(self,*args,**kwargs):
        super(GoogleRoads,self).save()


