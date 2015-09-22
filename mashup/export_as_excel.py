
from mashup.models import *
from django.http import *

def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Duplicate Sections")
    
    row_num = 0
    
    columns = [
        (u"ID", 2000),
        (u"origin_county", 15000),
        (u"origin_centriod", 15000),
        (u"terminating_county", 15000),
        (u"terminating_centriod", 15000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    
    for obj in queryset:
        row_num += 1
        row = [
            obj.pk,
            obj.origin_county,
            obj.origin_centriod,
            obj.terminating_county,
            obj.terminating_centriod
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)
    return response
    
export_xls.short_description = u"Export As XLS"



# For Mashup datasets
def export_mashup_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Duplicate Sections")
    
    row_num = 0
    
    columns = [
        #(u"ID", 2000),
        #(u"data", 15000),
        #(u"scenario", 2000),
        #(u"road_class", 15000),
        #(u"optimal_pcus", 15000),
        #(u"surfacecla", 15000),
        (u"origin_county", 15000),
        (u"origin_centriod", 15000),
        (u"terminating_county", 15000),
        (u"terminating_centriod", 15000),
        (u"stage_0", 15000),
        (u"stage_1", 15000),
        (u"stage_2", 15000),
        (u"stage_3", 15000),
        (u"stage_4", 15000),
        (u"stage_5", 15000),
        (u"stage_6", 15000),
        (u"stage_7", 15000),
        (u"stage_8", 15000),
        #(u"period", 15000),
        #(u"easting", 15000),
        #(u"northing", 15000),
        #(u"distance", 15000),
        #(u"length_km", 15000),
        
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    
    for obj in queryset:
        row_num += 1
        row = [
            #obj.pk,
            #obj.data,
            #obj.scenario,
            obj.origin_county,
            obj.origin_centriod,
            obj.terminating_county,
            obj.terminating_centriod,
            obj.stage_0,
            obj.stage_1,
            obj.stage_2,
            obj.stage_3,
            obj.stage_4,
            obj.stage_5,
            obj.stage_6,
            obj.stage_7,
            obj.stage_8,
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)
    return response
    
export_mashup_xls.short_description = u"Export Mashup As XLS"
