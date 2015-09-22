
from section_loading.models import *
from django.http import *

def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Duplicate Sections")
    
    row_num = 0
    
    columns = [
        #(u"ID", 2000),
        #(u"data", 15000),
        #(u"scenario", 15000),
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
            #obj.pk,
            #obj.data,
            #obj.scenario,
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
