

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime
import djcelery
djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '=@b$!u0c!25f5=f8mmd2%1(6@pz-a8%f@njp%%9)e_u)@ldw_f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




INSTALLED_APPS = (
    'wpadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    
    'accounts',
    'djcelery',
    'djgeojson',
    'kombu.transport.django',
    'section_loading',
    'batchimport',
    'leaflet',
    'gis_data',
    'pipeline',
    'mashup',
    'road',
    'rail'
)

AUTH_USER_MODEL = 'accounts.MyUser'


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


SERIALIZATION_MODULES = {
    'geojson': 'djgeojson.serializers'
}
LEAFLET_CONFIG = {
    # conf here
    #'SPATIAL_EXTENT': (5.0, 44.0, 7.5, 46),
    #'DEFAULT_CENTER': (6.0, 45.0),
    #'DEFAULT_ZOOM': 16,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 50,
    'TILES': 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    #'http://{s}.tile.osm.org/{z}/{x}/{y}.png'
    #'TILES':os.path.join(os.path.dirname(__file__), 'basic_tile.png'),
    #'TILES':os.path.abspath(os.path.join(os.path.dirname(__file__),'basic_tile.png')),
    'SCALE': 'both',
    
}

#CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
#CELERY_RESULT_BACKEND = "amqp"

#CELERY_BROKER_URL = 'amqp://guest@localhost//'
#CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler' 

CELERY_IMPORTS = ('pipeline.tasks',)

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


#CELERY_ACCEPT_CONTENT = ['json']
#CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    #railway_data_tasks
    'load_rail_data': {
        'task': 'rail.tasks.railway_data_mashup',
        'schedule': datetime.timedelta(seconds=1)
    },
    'basic-rail-traffic':{
     'task':'rail.railtfc_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'rail-final-traffic':{
     'task':'rail.rail_final_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'rail-traffic-working':{
     'task':'rail.rl_tfc_wrking_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    #pipeline_data_tasks
    'load_pipeline_data': {
        'task': 'pipeline.tasks.pipeline_mashup',
        'schedule': datetime.timedelta(seconds=1)
    },
    'set-pdata-category':{
         'task':'pipeline.tasks.set_data_category',
         'schedule': datetime.timedelta(seconds=1)
    },
    
    #road_data_tasks
    'basic-road-traffic':{
     'task':'road.road_tfc_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'base-working-file':{
     'task':'road.base_working_file_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'final-road-traffic':{
     'task':'road.final_tcf_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'projections-bs-cs':{
     'task':'road.projection_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'excluding-pol-imports':{
     'task':'road.expol_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'with-lamu-port-working':{
     'task':'road.lamu_working_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'lamu-traffic':{
     'task':'road.lamu_tcf_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'rd-tfc-loading-pcus':{
     'task':'road.road_tfc_loading_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'total_projections':{
     'task':'road.total_projections_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    'lamu_proportionate':{
     'task':'road.lamu_proportionate_mashup',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    #road-section-pcu-summations
    'base-scenario-summation':{
      'task':'road.base_scenario_summation',
      'schedule': datetime.timedelta(seconds=1) 
    },
    'base_working_file-scenario-summation':{
      'task':'road.base_working_file_scenario_summation',
      'schedule': datetime.timedelta(seconds=1) 
    },
    'road_tfc_final-scenario-summation':{
      'task':'road.road_tfc_final_scenario_summation',
      'schedule': datetime.timedelta(seconds=1) 
    },
    'projections-scenario-summation':{
      'task':'road.projections_scenario_summation',
      'schedule': datetime.timedelta(seconds=1) 
    },
    'expol-scenario-summation':{
      'task':'road.expol_scenario_summation',
      'schedule': datetime.timedelta(seconds=1) 
    },
    'lamu_port_working-scenario-summation':{
      'task':'road.lamu_port_working_scenario_summation',
      'schedule': datetime.timedelta(seconds=1) 
    },
    'rtfc_loading-scenario-summation':{
      'task':'road.rtfc_loading_scenario_summation',
      'schedule': datetime.timedelta(seconds=1) 
    },
    'prop_lamu_share-scenario-summation':{
      'task':'road.prop_lamu_share_scenario_summation',
      'schedule': datetime.timedelta(seconds=1) 
    },
    'total_combined_tfc-scenario-summation':{
      'task':'road.total_combined_tfc_scenario_summation',
      'schedule': datetime.timedelta(seconds=1) 
    },
    # --------- end of section summation -----#
    
    #mashup tasks: match road sections to gis sections
    'daily-tonnage':{
     'task':'mashup.road_daily_tfc_tonnes',
     'schedule': datetime.timedelta(seconds=1)
    },
    'daily-pcus':{
     'task':'mashup.road_daily_tfc_pcus',
     'schedule': datetime.timedelta(seconds=1)
    },
    'ttl-combined-traffic-tonnage':{
     'task':'mashup.combined_total_tfc_tonnes',
     'schedule': datetime.timedelta(seconds=1)
    },
    'ttl-combined-traffic-pcus':{
     'task':'mashup.combined_total_tfc_pcus',
     'schedule': datetime.timedelta(seconds=1)
    },
    'plain-road_data-tonnage':{
     'task':'mashup.road_tfc_data_tonnes',
     'schedule': datetime.timedelta(seconds=1)
    },
    'plain-road_data-pcus':{
     'task':'mashup.road_tfc_data_pcus',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    'rail-plain-tonnage':{
     'task':'mashup.rail_data_tonnes',
     'schedule': datetime.timedelta(seconds=1)
    },
    'rail-final-tonnage':{
     'task':'mashup.rail_final_tonnes',
     'schedule': datetime.timedelta(seconds=1)
    },
    'rail-tfc-tonnage':{
     'task':'mashup.rail_tfc_working_tonnes',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    #namanga
    'namanga-centriod-updates':{
     'task':'mashup.namanga_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'namanga-origin-updates':{
     'task':'mashup.namanga_origin_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'namanga-terminal-updates':{
     'task':'mashup.namanga_terminal_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'namanga-terminal-centriod-updates':{
     'task':'mashup.namanga_terminal_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    #busia
    'busia-centriod-updates':{
     'task':'mashup.busia_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'busia-origin-updates':{
     'task':'mashup.busia_origin_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'busia-terminal-updates':{
     'task':'mashup.busia_terminal_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'busia-terminal-centriod-updates':{
     'task':'mashup.busia_terminal_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    #lokichar
    'sudan_centriod_updates':{
     'task':'mashup.sudan_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'sudan_origin_updates':{
     'task':'mashup.sudan_origin_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'sudan_terminal_updates':{
     'task':'mashup.sudan_terminal_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'sudan_terminal_centriod_updates':{
     'task':'mashup.sudan_terminal_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    #ethiopia
    'ethiopia_centriod_updates':{
     'task':'mashup.ethiopia_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'ethiopia_origin_updates':{
     'task':'mashup.ethiopia_origin_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'ethiopia_terminal_updates':{
     'task':'mashup.ethiopia_terminal_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'ethiopia_terminal_centriod_updates':{
     'task':'mashup.ethiopia_terminal_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    # somalia
    'somalia_centriod_updates':{
     'task':'mashup.somalia_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'somalia_origin_updates':{
     'task':'mashup.somalia_origin_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'somalia_terminal_updates':{
     'task':'mashup.somalia_terminal_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    'somalia_terminal_centriod_updates':{
     'task':'mashup.somalia_terminal_centriod_updates',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    
    
    #make dumb data intelligent: gis layer
    'set_origin_road_markers':{
     'task':'mashup.set_origin_road_markers',
     'schedule': datetime.timedelta(seconds=1)
    },
    'set_terminating_road_markers':{
     'task':'mashup.set_terminating_road_markers',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    # a simpler approach
    'set_class_a_markers':{
      'task':'mashup.set_class_a_markers',
      'schedule': datetime.timedelta(seconds=1)
    },
    'set_class_b_markers':{
      'task':'mashup.set_class_b_markers',
      'schedule': datetime.timedelta(seconds=1)
    },
    'set_class_c_markers':{
      'task':'mashup.set_class_c_markers',
      'schedule': datetime.timedelta(seconds=1)
    },
    
    #others
    'set_dataset_period':{
      'task':'mashup.set_dataset_period',
      'schedule': datetime.timedelta(seconds=1)
    },
    
    'clean_road_tfc_base_case':{
      'task':'mashup.clean_road_tfc_base_case',
      'schedule': datetime.timedelta(seconds=1)
    },
    
    'clean_road_tfc_dataset':{
      'task':'section_loading.clean_road_tfc_dataset',
      'schedule': datetime.timedelta(seconds=1)
    },
    
    'set_paved_optimal_pcus':{
      'task':'mashup.paved_optimal_pcus',
      'schedule': datetime.timedelta(seconds=1)
    },
    
    'set_upaved_optimal_pcus':{
      'task':'mashup.upaved_optimal_pcus',
      'schedule': datetime.timedelta(seconds=1)
    },
    
    #merge duplicate road-sections
    'get-duplicates':{
     'task':'road.get_mashup_duplicates',
     'schedule': datetime.timedelta(seconds=1)
    },
    #merge duplicate road-sections
    'delete-duplicates':{
     'task':'mashup.remove_mashup_dupes',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    
    # mark-roads-for-upgrades
    'mark_paved_roads_upgrades':{
     'task':'section_loading.mark_paved_roads_upgrades',
     'schedule': datetime.timedelta(seconds=1)
    },
    'mark_unpaved_roads_upgrades':{
     'task':'section_loading.mark_unpaved_roads_upgrades',
     'schedule': datetime.timedelta(seconds=1)
    },
    
    #section-loading-algos
    'get_corridor_duplicates':{
      'task':'section_loading.get_corridor_duplicates',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    #section-loading-algos
    'tag_road_sections':{
      'task':'section_loading.tag_road_sections',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
    #extract  duplicates
    'extract_road_corridors':{
      'task':'section_loading.extract_road_corridors',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    'extract_rail_sections':{
      'task':'section_loading.extract_rail_sections',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    'extract_combined_sections':{
      'task':'section_loading.extract_combined_sections',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    # ------ end of extraction ------------#
    
    #----populate scenario analytics models ---- #
    'populate_section_loadings':{
      'task':'section_loading.populate_section_loadings',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    'populate_combined_tfc':{
      'task':'section_loading.populate_combined_tfc',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    'populate_rail_section_loadings':{
      'task':'section_loading.populate_rail_section_loadings',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    'lamu_edge_case_dataset':{
      'task':'section_loading.lamu_edge_case_dataset',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    # ----------- end of section -----------------------#
    
    'base_case_section_loading':{
      'task':'section_loading.base_case_section_loading',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
    'stage_one':{
      'task':'section_loading.stage_one',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
    # Deal with capacities
    'reset_projections':{
      'task':'section_loading.reset_projections',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
    'pivot_mashup_data':{
      'task':'section_loading.pivot_mashup_data',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
    'reset_all_capacities':{
      'task':'section_loading.reset_all_capacities',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    'normalize_rail_tonnes':{
      'task':'section_loading.normalize_rail_tonnes',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
    'set_unpaved_capacity':{
      'task':'section_loading.set_unpaved_capacity',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
    'set_paved_capacity':{
      'task':'section_loading.set_paved_capacity',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    'set_rail_capacity':{
      'task':'section_loading.set_rail_capacity',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
    #lamu edge case dataset
    'set_unpaved_lamu_capacity':{
      'task':'section_loading.set_unpaved_lamu_capacity',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    'set_paved_lamu_capacity':{
      'task':'section_loading.set_paved_lamu_capacity',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
    #set labels to aggregate routes data
    'set_dataset_label':{
       'task':'section_loading.set_dataset_label',
       'schedule': datetime.timedelta(seconds=1)
       
    },
    'set_data_scenario':{
       'task':'section_loading.set_data_scenario',
       'schedule': datetime.timedelta(seconds=1)
       
    },
    
    'test_choice_field':{
       'task':'section_loading.test_choice_field',
       'schedule': datetime.timedelta(seconds=1)
       
    },
    
    #----extract routes marked for upgrade-----#
    'extract_all_section_upgrades':{
       'task':'section_loading.extract_all_section_upgrades',
       'schedule': datetime.timedelta(seconds=1)
       
    },
    'extract_unpaved_section_upgrades':{
       'task':'section_loading.extract_unpaved_section_upgrades',
       'schedule': datetime.timedelta(seconds=1)
       
    },
    
    'extract_lamu_edge_case_projections':{
       'task':'section_loading.extract_lamu_edge_case_projections',
       'schedule': datetime.timedelta(seconds=1)
       
    },
    
    #------ end route upgrade extraction ------#
    
    
    # A-n-d the last awesome tasks is.....**drum rolls**
    'mark_target_roads_for_upgrade':{
      'task':'section_loading.mark_target_roads_for_upgrade',
      'schedule': datetime.timedelta(seconds=1)
      
    },
    
}

#BROKER_URL = 'amqp://guest:guest@localhost:5672//'
#CELERY_IGNORE_RESULT = True 
#CELERY_DISABLE_RATE_LIMITS = True

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'traffic_modelling.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#comment this out in production
#WSGI_APPLICATION = 'traffic_modelling.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
"""
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', 
            'NAME': 'trafficdata',
            'USER': 'superadmin',
            'PASSWORD': 'bolshoi53$',
            'HOST': 'localhost',
              
        }
"""

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        #'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'trafficdata',
        'USER': 'dataman',
        'PASSWORD': 'admin',
        'HOST': 'localhost',                      
        'PORT': '',  
    }
}




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




#MEDIA_ROOT =  os.path.join(os.path.dirname(__file__), 'static/media/')


#MEDIA_URL = '/static/media/'

#STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static/')

STATIC_ROOT = '/var/www/masterplanke.com/static/'
STATIC_URL = '/static/'

"""
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static')

)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
"""




BATCH_IMPORT_IMPORTABLE_MODELS = [
    #'section_loading.PData',
    
    
    
    'road.RoadTraffic',
    'road.FinalTraffic',
    'road.Projection',
    'road.ExcPOL',
    'road.LamuPortWorking',
    'road.LamuTraffic',
    'road.RdTfcLoading',
    'road.BaseWorkingFile',
    'road.TotalTfcProjections',
    'road.LamuProportinateShare',
    'section_loading.SectionLoading',
    
    #section-loading-objects
    'section_loading.RBC',
    'section_loading.RailFinal',
    'section_loading.RailTrafficWorking',
    
    'section_loading.BWF',
    'section_loading.RoadBaseCase',
    'section_loading.RoadFinal',
    'section_loading.BCSP',
    'section_loading.xPOL',
    'section_loading.LPW',
    'section_loading.LTFC',
    'section_loading.LPCU',
    'section_loading.PLS',
    
    # combined total traffic
    'section_loading.TTFCP',
    
    
    #'rail.RailTraffic',
    #'rail.RLFinal',
    #'rail.RaiTfcWrking',
    
    #'pipeline.Pipeline',
]

PERIOD = (
    ('2013 - 2014','2013 - 2014'),
    ('2014 - 2015','2014 - 2015'),
    ('2019 - 2020','2019 - 2020'),
    ('2024 - 2025','2024 - 2025'),
    ('2029 - 2030','2029 - 2030'),
    ('2034 - 2035','2034 - 2035'),
    ('2044 - 2045','2044 - 2045'),
    ('2054 - 2055','2054 - 2055'),
    ('2064 - 2065','2064 - 2065')
)

DATA = (
    ('Rtfc','Road Traffic'),
    ('Ptfc','Pipeline Traffic'),
    ('Rtfc','Rail Traffic'),
)

#every model should be a scenario
SCENARIO = (
    
   
   (1,'Rail Base Case'),
   (2,'Rail Traffic Working'),
   (3,'RL Final'),
   
   (4,'Road Base Case'),
   (5,'Base Working File'),
   (6,'Road Traffic Final'),
   (7,'Without POL Imports'),
   (8,'Lamu Port Working'),
   (9,'RdTfcLoading PCUs'),
   (10,'Projections BS CS'),
   (11,'Prop. Lamu Share'),
   (12,'None')
   
    
    
)

# not as exact in real sense
ROAD_CLASS = (
    ('A','A'),
    ('B','B'),
    ('C','C'),
)





