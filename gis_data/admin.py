from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *

class AbcAdmin(admin.ModelAdmin):
    list_display = ('station','name','road_class','from_field','to_field','total_aadt')
    list_filter = ('road_class',)
    searh_fields = ('name',)
    
admin.site.register(Abc,AbcAdmin)


class StretchAdmin(LeafletGeoAdmin):
    #list_display = ('station','name','road_class','from_field','to_field','length_km','total_aadt')
    list_display = ('name','road_class','surfacecla','from_field','to_field','easting','northing')
    list_filter = ('road_class','station')
    search_fields = ('name','from_field','to_field')
    
    
    scrollable = False
    map_width = 700
    map_height = 325
    
admin.site.register(Stretch,StretchAdmin)


class TownAdmin(LeafletGeoAdmin):
    list_display = ('town_name','geom')
    list_filter = ('town_name',)
    search_fields = ('town_name',)
    
admin.site.register(Town,TownAdmin)


"""
class Admin(LeafletGeoAdmin):
    list_display = ()
    list_filter = ()
    
admin.site.register(,Admin)
"""
