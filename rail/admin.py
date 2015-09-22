from django.contrib import admin
from .models import *


class RLFinalAdmin(admin.ModelAdmin):
    list_display = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','commodity_group',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',
    )
    #list_filter = ('stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',)
    search_fields = ('origin_county','origin_centriod','terminating_county','commodity_group',)

admin.site.register(RLFinal,RLFinalAdmin)



class RailTrafficAdmin(admin.ModelAdmin):
    list_display = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','commodity_group',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',
    )
    #list_filter = ('stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',)
    search_fields = ('origin_county','origin_centriod','terminating_county','commodity_group',)

admin.site.register(RailTraffic,RailTrafficAdmin)


class RaiTfcWrkingAdmin(admin.ModelAdmin):
    list_display = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','commodity_group',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',
    )
    #list_filter = ('stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',)
    search_fields = ('origin_county','origin_centriod','terminating_county','commodity_group',)

admin.site.register(RaiTfcWrking,RaiTfcWrkingAdmin)
