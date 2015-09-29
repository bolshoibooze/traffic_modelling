import xlwt
import csv
import math
import itertools
import datetime

from django.forms.forms import pretty_name
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import ValuesQuerySet
from django.utils import six





# credits: https://djangosnippets.org/snippets/10332/

HEADER_STYLE = xlwt.easyxf('font: bold on')
DEFAULT_STYLE = xlwt.easyxf()
CELL_STYLE_MAP = (
    (datetime.date, xlwt.easyxf(num_format_str='DD/MM/YYYY')),
    (datetime.time, xlwt.easyxf(num_format_str='HH:MM')),
    (bool,          xlwt.easyxf(num_format_str='BOOLEAN')),
)



def multi_getattr(obj, attr, default=None):
    attributes = attr.split(".")
    for i in attributes:
        try:
            obj = getattr(obj, i)
        except AttributeError:
            if default:
                return default
            else:
                raise
    return obj

def get_column_head(obj, name):
    name = name.rsplit('.', 1)[-1]
    return pretty_name(name)

def get_column_cell(obj, name):
    try:
        attr = multi_getattr(obj, name)
    except ObjectDoesNotExist:
        return None
    if hasattr(attr, '_meta'):
        # A Django Model (related object)                                                                                                                                                                          
        return unicode(attr).strip()
    elif hasattr(attr, 'all'):
        # A Django queryset (ManyRelatedManager)                                                                                                                                                                   
        return ', '.join(unicode(x).strip() for x in attr.all())
    return attr

def queryset_to_workbook(queryset, columns, header_style=None,
                         default_style=None, cell_style_map=None):
    workbook = xlwt.Workbook()
    report_date = datetime.date.today()
    sheet_name = 'Data Export {0}'.format(report_date.strftime('%Y-%m-%d'))
    sheet = workbook.add_sheet(sheet_name)
    col_width = 256 * 20   # 20 characters wide

    try: #see:http://reliablybroken.com/b/2011/10/widths-heights-with-xlwt-python/
       for i in itertools.count():
           sheet.col(i).width = col_width
    except ValueError:
         pass
    

    if not header_style:
        header_style = HEADER_STYLE
    if not default_style:
        default_style = DEFAULT_STYLE
    if not cell_style_map:
        cell_style_map = CELL_STYLE_MAP

    obj = queryset.first()
    for y, column in enumerate(columns):
        value = get_column_head(obj, column)
        sheet.write(0, y, value, header_style)

    for x, obj in enumerate(queryset, start=1):
        for y, column in enumerate(columns):
            value = get_column_cell(obj, column)
            style = default_style
            for value_type, cell_style in cell_style_map:
                if isinstance(value, value_type):
                    style = cell_style
            sheet.write(x, y, value, style)

    return workbook
    
    
    
    
# generate csv
def write_csv(queryset, file_obj, **kwargs):
    """
    The main worker function. Writes CSV data to a file object based on the
    contents of the queryset.
    """

    # process keyword arguments to pull out the ones used by this function
    field_header_map = kwargs.get('field_header_map', {})
    field_serializer_map = kwargs.get('field_serializer_map', {})
    use_verbose_names = kwargs.get('use_verbose_names', True)
    field_order = kwargs.get('field_order', None)

    csv_kwargs = {}

    for key, val in six.iteritems(kwargs):
        if key not in DJQSCSV_KWARGS:
            csv_kwargs[key] = val

    # add BOM to support CSVs in MS Excel (for Windows only)
    file_obj.write(_safe_utf8_stringify(u'\ufeff'))

    # the CSV must always be built from a values queryset
    # in order to introspect the necessary fields.
    if isinstance(queryset, ValuesQuerySet):
        values_qs = queryset
    else:
        values_qs = queryset.values()

    try:
        field_names = values_qs.field_names

    except AttributeError:
        # in django1.5, empty querysets trigger
        # this exception, but not django 1.6
        raise CSVException("Empty queryset provided to exporter.")

    extra_columns = list(values_qs.query.extra_select)
    if extra_columns:
        field_names += extra_columns

    aggregate_columns = list(values_qs.query.aggregate_select)
    if aggregate_columns:
        field_names += aggregate_columns

    if field_order:
        # go through the field_names and put the ones
        # that appear in the ordering list first
        field_names = ([field for field in field_order
                       if field in field_names] +
                       [field for field in field_names
                        if field not in field_order])

    writer = csv.DictWriter(file_obj, field_names, **csv_kwargs)

    # verbose_name defaults to the raw field name, so in either case
    # this will produce a complete mapping of field names to column names
    name_map = dict((field, field) for field in field_names)
    if use_verbose_names:
        name_map.update(
            dict((field.name, field.verbose_name)
                 for field in queryset.model._meta.fields
                 if field.name in field_names))

    # merge the custom field headers into the verbose/raw defaults, if provided
    merged_header_map = name_map.copy()
    merged_header_map.update(field_header_map)
    if extra_columns:
        merged_header_map.update(dict((k, k) for k in extra_columns))

    merged_header_map = dict((k, _safe_utf8_stringify(v))
                             for (k, v) in merged_header_map.items())
    writer.writerow(merged_header_map)

    for record in values_qs:
        record = _sanitize_unicode_record(field_serializer_map, record)
        writer.writerow(record)
        
        
########################################
# utility functions
########################################


def _validate_and_clean_filename(filename):

    if filename.count('.'):
        if not filename.endswith('.csv'):
            raise ValidationError('the only accepted file extension is .csv')
        else:
            filename = filename[:-4]

    filename = slugify(unicode(filename)) + '.csv'
    return filename


def _safe_utf8_stringify(value):
    if isinstance(value, str):
        return value
    elif isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return unicode(value).encode('utf-8')


def _sanitize_unicode_record(field_serializer_map, record):

    def _serialize_value(value):
        # provide default serializer for the case when
        # non text values get sent without a serializer
        if isinstance(value, datetime.datetime):
            return value.isoformat()
        else:
            return unicode(value)

    obj = {}
    for key, val in six.iteritems(record):
        if val is not None:
            serializer = field_serializer_map.get(key, _serialize_value)
            newval = serializer(val)
            obj[_safe_utf8_stringify(key)] = _safe_utf8_stringify(newval)

    return obj


def _append_datestamp(filename):
    """
    takes a filename and returns a new filename with the
    current formatted date appended to it.

    raises an exception if it receives an unclean filename.
    validation/preprocessing must be called separately.
    """
    if filename != _validate_and_clean_filename(filename):
        raise ValidationError('cannot datestamp unvalidated filename')

    formatted_datestring = datetime.date.today().strftime("%Y%m%d")
    return '%s_%s.csv' % (filename[:-4], formatted_datestring)
