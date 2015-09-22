from django.contrib import admin
from .models import *


class RoadTrafficAdmin(admin.ModelAdmin):
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')

    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    #list_filter = ('surfacecla',)


admin.site.register(RoadTraffic,RoadTrafficAdmin)


admin.site.register(FinalTraffic)
admin.site.register(Projection)
admin.site.register(ExcPOL)
admin.site.register(LamuPortWorking)
admin.site.register(LamuTraffic)
admin.site.register(RdTfcLoading)


"""
admin.site.register()
admin.site.register()
admin.site.register()
admin.site.register()
admin.site.register()
admin.site.register()
admin.site.register()
admin.site.register()


"""
