import os
import gis_data
from django.contrib.gis.utils import LayerMapping


from gis_data.models import *

abc_mapping = {
    'station' : 'Station',
    'name' : 'Name',
    'from_field' : 'From_',
    'to_field' : 'To_',
    'total_aadt' : 'Total_AADT',
    'road_class' : 'Class',
    'geom' : 'MULTIPOINT',
}


stretch_mapping = {
    'rid' : 'RID',
    'surfacecla' : 'SurfaceCla',
    'old_rid2' : 'OLD_RID2',
    'road_class' : 'CLASS',
    'station' : 'Station',
    'old_class' : 'OLD_CLASS',
    'name' : 'Name',
    'length_km' : 'Length_KM',
    'total_aadt' : 'Total_AADT',
    'from_field' : 'From_',
    'to_field' : 'To_',
    'easting' : 'Easting',
    'northing' : 'Northing',
    'surfacing' : 'Surfacing',
    'roadcond' : 'RoadCond',
    'mc' : 'MC',
    'c' : 'C',
    'lc_4wd' : 'LC_4WD',
    'p_van' : 'P_VAN',
    'm' : 'M',
    'sb' : 'SB',
    'lb' : 'LB',
    'lt' : 'LT',
    'mt' : 'MT',
    'ht' : 'HT',
    'art_t' : 'Art_T',
    'other' : 'Other',
    'orig_fid' : 'Orig_FID',
    'new' : 'New',
    'geom' : 'MULTILINESTRING',
}

# Auto-generated `LayerMapping` dictionary for Towns model
towns_mapping = {
    'town_name' : 'TOWN_NAME',
    'geom' : 'MULTIPOINT',
}

majorroad_mapping = {
    'kenroad_id' : 'KENROAD_ID',
    'geom' : 'MULTILINESTRING',
}


stretchdata_mapping = {
    'rid' : 'RID',
    'surfacecla' : 'SurfaceCla',
    'old_rid2' : 'OLD_RID2',
    'road_class' : 'CLASS',
    'station' : 'Station',
    'old_class' : 'OLD_CLASS',
    'name' : 'Name',
    'length_km' : 'Length_KM',
    'total_aadt' : 'Total_AADT',
    'from_field' : 'From_',
    'to_field' : 'To_',
    'easting' : 'Easting',
    'northing' : 'Northing',
    'surfacing' : 'Surfacing',
    'roadcond' : 'RoadCond',
    'mc' : 'MC',
    'c' : 'C',
    'lc_4wd' : 'LC_4WD',
    'p_van' : 'P_VAN',
    'm' : 'M',
    'sb' : 'SB',
    'lb' : 'LB',
    'lt' : 'LT',
    'mt' : 'MT',
    'ht' : 'HT',
    'art_t' : 'Art_T',
    'other' : 'Other',
    'orig_fid' : 'Orig_FID',
    'new' : 'New',
    'geom' : 'MULTILINESTRING',
}


googleroads_mapping = {
    'rid' : 'ID',
    'name1' : 'NAME1',
    'lang1' : 'LANG1',
    'name2' : 'NAME2',
    'lang2' : 'LANG2',
    'name3' : 'NAME3',
    'lang3' : 'LANG3',
    'rtenum' : 'RTENUM',
    'cntrycode' : 'CNTRYCODE',
    'provname' : 'PROVNAME',
    'usage' : 'USAGE',
    'surface' : 'SURFACE',
    'elevation' : 'ELEVATION',
    'priority' : 'PRIORITY',
    'condition' : 'CONDITION',
    'divider' : 'DIVIDER',
    'constructn' : 'CONSTRUCTN',
    'avgspeed' : 'AVGSPEED',
    'geom' : 'MULTILINESTRING',
}





#abc_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'ABC_Census_Points_13_04_2015.shp'))

#stretchdata_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Stretch_Based_Traffic_Data_13_04_2015.shp'))

googleroads_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'roads_kenya.shp'))

stretchdata_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'Stretch_3857.shp'))

#towns_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ke_major-towns.shp'))

#majorroad_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'ke_major-roads.shp'))

def run(verbose=True):
    #abc = LayerMapping(Abc, abc_shp, abc_mapping,transform=False, encoding='iso-8859-1')
    #stretch = LayerMapping(Stretch, stretch_shp, stretch_mapping,transform=False, encoding='iso-8859-1')
    #town = LayerMapping(Town, towns_shp, towns_mapping,transform=False, encoding='iso-8859-1')
    #town.save(strict=True, verbose=verbose)
    #abc.save(strict=True, verbose=verbose)
    #stretch.save(strict=True, verbose=verbose) 
    #road = LayerMapping(MajorRoad, majorroad_shp, majorroad_mapping,transform=False, encoding='iso-8859-1')
    #road.save(strict=True, verbose=verbose)
    
    #sd = LayerMapping(Section, stretchdata_shp, stretchdata_mapping,transform=False, encoding='iso-8859-1')
    #sd.save(strict=True, verbose=verbose)
    
    g = LayerMapping(GoogleRoads, googleroads_shp, googleroads_mapping,transform=False, encoding='iso-8859-1')
    g.save(strict=True, verbose=verbose)
    
    
    
    
    
    
