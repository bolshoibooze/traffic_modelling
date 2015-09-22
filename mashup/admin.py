from django.contrib import admin
from mashup.models import *

from mashup.export_as_excel import *
#from .mashup_as_excel import *


class MashupAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod',)
    list_display = ('data','scenario','origin_county','road_class','surfacecla','optimal_pcus','terminating_county','road_pcus','excl_road_pcus','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',)
    #list_display = ('id','data','scenario','road_class','surfacecla','optimal_pcus','origin_county','origin_centriod','terminating_county','terminating_centriod')
    exclude = (
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3',
    'additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',
    'dataset_0','dataset_1','dataset_2','dataset_3','dataset_4','dataset_5','dataset_6',
    'dataset_7','dataset_8','dataset_9','o_county_easting','o_county_northing','o_centriod_easting',
    'o_centriod_northing','t_county_easting','t_county_northing','t_centriod_easting','t_centriod_northing',
    )
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod'
    )
    list_filter = ('data','scenario',)
    actions = [export_mashup_xls,]
    
    
admin.site.register(Mashup,MashupAdmin)


