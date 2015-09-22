from django.contrib import admin
from .relatedfield_admin import *
from .export_excel import *
from mashup.models import *
from .models import *



class RBCAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    #list_filter = ()
    
    
admin.site.register(RBC,RBCAdmin)


class RailFinalAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    #list_filter = ()
    
    
admin.site.register(RailFinal,RailFinalAdmin)


class RailTrafficWorkingAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
   
    #list_filter = ()
    
    
admin.site.register(RailTrafficWorking,RailTrafficWorkingAdmin)


class BWFAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(BWF,BWFAdmin)

"""
class RoadBaseCaseAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(RoadBaseCase,RoadBaseCaseAdmin)
"""

class RoadFinalAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(RoadFinal,RoadFinalAdmin)


class BCSPAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(BCSP,BCSPAdmin)


class xPOLAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(xPOL,xPOLAdmin)


class LPWAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','road_pcus','excl_road_pcus','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','road_pcus','excl_road_pcus','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(LPW,LPWAdmin)


class LTFCAdmin(admin.ModelAdmin):
    list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    #list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(LTFC,LTFCAdmin)


class LPCUAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(LPCU,LPCUAdmin)


class PLSAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(PLS,PLSAdmin)


class TTFCPAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(TTFCP,TTFCPAdmin)


class RoadBaseCaseAdmin(admin.ModelAdmin):
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8')
    list_display = ('origin_county','origin_centriod','terminating_county','terminating_centriod','additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',)
    search_fields = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    list_filter = ('surfacecla',)
    
    
admin.site.register(RoadBaseCase,RoadBaseCaseAdmin)
    


"""
class DuplicateAdmin(admin.ModelAdmin):
    list_display = ('id','origin_county','origin_centriod','terminating_county','terminating_centriod')
    list_filter = ('origin_county','terminating_county',)
    actions = [export_xls,]
admin.site.register(Duplicate,DuplicateAdmin)

"""
"""
admin.site.register(Scenario)

class SectionLoadingAdmin(RelatedFieldAdmin):
   
    list_display = ('data','scenarios__name','origin_county','origin_centriod','terminating_county','terminating_centriod','stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8',)
    #list_display = ('data','scenario','origin_county','origin_centriod','terminating_county','terminating_centriod')
    
    list_display = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3',
    'additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7',
    )
   
    search_fields = ('origin_county','origin_centriod','terminating_county','terminating_centriod')
    list_filter = ('data','scenarios','surfacecla',)
    #actions = [export_xls,]
    
    #def set_scenarios(self,obj):
        #return "\n".join([s.name for s in obj.scenarios.all() ])
     
admin.site.register(SectionLoading,SectionLoadingAdmin)


class TestTableAdmin(admin.ModelAdmin):
    list_display = ('item','value')
    list_filter = ('item','choice')
    
admin.site.register(TestTable,TestTableAdmin)

"""

