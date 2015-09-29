import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.query import *

from django.utils import six
from section_loading.models import *
from .utils import *


def road_bs_cs_section_loading(request):
    #sheet_name = 'SectionLoadings'
    queryset = RoadBaseCase.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RoadBaseCaseSectionLoading.xls"'
    workbook.save(response)
    return response
    
def road_bs_cs_section_loading_csv(request):
    
    queryset = RoadBaseCase.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RoadBaseCaseSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response
    
    
def road_bs_cs_projections(request):
    queryset = RoadBaseCase.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RoadBaseCaseProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def road_bs_cs_projections_csv(request):
    
    queryset = RoadBaseCase.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RoadBaseCaseProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response
    
    
# ----------  downloads    -------------#
def pipeline_section_loading(request):
    queryset = Pipeline.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="PipelineSectionLoading.xls"'
    workbook.save(response)
    return response
    
def pipeline_section_loading_csv(request):
    
    queryset = Pipeline.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="PipelineSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response





# ----------end downloads ---------------#


# ----------  downloads    -------------#
def rail_bs_cs_section_loading(request):
    queryset = RBC.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RailBaseCaseSectionLoading.xls"'
    workbook.save(response)
    return response
    
def rail_bs_cs_section_loading_csv(request):
    
    queryset = RBC.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RailBaseCaseSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response





# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def rl_final_section_loading(request):
    queryset = RailFinal.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RailFinalSectionLoading.xls"'
    workbook.save(response)
    return response
    
def rl_final_section_loading_csv(request):
    
    queryset = RailFinal.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RailFinalSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response






# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def rltfc_working_section_loading(request):
    queryset = RailTrafficWorking.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RailTrafficWorkingSectionLoading.xls"'
    workbook.save(response)
    return response
    
def rltfc_working_section_loading_csv(request):
    
    queryset = RailTrafficWorking.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RailTrafficWorkingSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def bwf_section_loading(request):
    queryset = BWF.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RoadBaseWorkingFileSectionLoading.xls"'
    workbook.save(response)
    return response
    
def bwf_section_loading_csv(request):
    
    queryset = BWF.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RoadBaseWorkingFileSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



def bwf_projections(request):
    queryset = BWF.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RoadBaseWorkingFileProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def bwf_projections_csv(request):
    
    queryset = BWF.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RoadBaseWorkingFileProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response




# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def rd_final_section_loading(request):
    queryset = RoadFinal.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RoadFinalSectionLoading.xls"'
    workbook.save(response)
    return response
    
def rd_final_section_loading_csv(request):
    
    queryset = RoadFinal.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RoadFinalSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



def rd_final_projections(request):
    queryset = RoadFinal.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RoadFinalProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def rd_final_projections_csv(request):
    
    queryset = RoadFinal.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RoadFinalProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response




# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def bcsp_section_loading(request):
    queryset = BCSP.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="BaseCaseProjectionsSectionLoading.xls"'
    workbook.save(response)
    return response
    
def bcsp_section_loading_csv(request):
    
    queryset = BCSP.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="BaseCaseProjectionsSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



def bcsp_projections(request):
    queryset = BCSP.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="BaseCaseProjectionsProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def bcsp_projections_csv(request):
    
    queryset = BCSP.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="BaseCaseProjectionsProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response




# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def xpol_section_loading(request):
    queryset = xPOL.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="WithoutPOLImportsSectionLoading.xls"'
    workbook.save(response)
    return response
    
def xpol_section_loading_csv(request):
    
    queryset = xPOL.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="WithoutPOLImportsSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



def xpol_projections(request):
    queryset = xPOL.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="WithoutPOLImportsProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def xpol_projections_csv(request):
    
    queryset = xPOL.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="WithoutPOLImportsProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response




# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def lpw_section_loading(request):
    queryset = LPW.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="WithLamuPortWorkingSectionLoading.xls"'
    workbook.save(response)
    return response
    
def lpw_section_loading_csv(request):
    
    queryset = LPW.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="WithLamuPortWorkingSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



def lpw_projections(request):
    queryset = LPW.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="WithLamuPortWorkingProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def lpw_projections_csv(request):
    
    queryset = LPW.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="WithLamuPortWorkingProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response




# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def ltfc_section_loading(request):
    queryset = LTFC.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="LamuTrafficSectionLoading.xls"'
    workbook.save(response)
    return response
    
def ltf_section_loading_csv(request):
    
    queryset = LTFC.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="LamuTrafficSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



def ltfc_projections(request):
    queryset = LTFC.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="LamuTrafficProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def ltfc_projections_csv(request):
    
    queryset = LTFC.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="LamuTrafficProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response




# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def lpcu_section_loading(request):
    queryset = LPCU.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RdTfcLoadingPCUSectionLoading.xls"'
    workbook.save(response)
    return response
    
def lpcu_section_loading_csv(request):
    
    queryset = LPCU.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RdTfcLoadingPCUSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



def lpcu_projections(request):
    queryset = LPCU.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="RdTfcLoadingPCUProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def lpcu_projections_csv(request):
    
    queryset = LPCU.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RdTfcLoadingPCUProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response




# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def pls_section_loading(request):
    queryset = PLS.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ProportionateLamuShareSectionLoading.xls"'
    workbook.save(response)
    return response
    
def pls_section_loading_csv(request):
    
    queryset = PLS.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ProportionateLamuShareSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



def pls_projections(request):
    queryset = PLS.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ProportionateLamuShareProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def pls_projections_csv(request):
    
    queryset = PLS.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ProportionateLamuShareProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response




# ----------end downloads ---------------#
    
    
    

    

# ----------  downloads    -------------#
def ttl_tfc_section_loading(request):
    queryset = TTFCP.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="TotalTrafficSectionLoading.xls"'
    workbook.save(response)
    return response
    
def ttl_tfc_section_loading_csv(request):
    
    queryset = TTFCP.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'stage_0','stage_1','stage_2','stage_3','stage_4','stage_5','stage_6','stage_7','stage_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="TotalTrafficSectionLoading.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response



def ttl_tfc_projections(request):
    queryset = TTFCP.objects.all()
    columns = (
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    workbook = queryset_to_workbook(queryset, columns)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="TotalTrafficProjections.xls"'
    workbook.save(response)
    return response
    

    
    
def ttl_tfc_projections_csv(request):
    
    queryset = TTFCP.objects.values(
    'origin_county','origin_centriod','terminating_county','terminating_centriod','distance',
    'additional_capacity_0','additional_capacity_1','additional_capacity_2','additional_capacity_3','additional_capacity_4','additional_capacity_5','additional_capacity_6','additional_capacity_7','additional_capacity_8'
    )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="TotalTrafficProjections.csv"'
    response['Cache-Control'] = 'no-cache'

    write_csv(queryset, response)

    return response




# ----------end downloads ---------------#
    
    
    

    


    
    
    

    


