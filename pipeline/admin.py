from django.contrib import admin
from .models import *


class PipelineAdmin(admin.ModelAdmin):
    #list_display = ('data','origin_county','origin_centriod','terminating_county','terminating_centriod','commodity_group','destination_code')
    list_display = ('origin_county','terminating_county', 'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',)
    search_fields = ('origin_county','terminating_county',)
    list_filter = ('commodity_group',)
    
admin.site.register(Pipeline,PipelineAdmin)
