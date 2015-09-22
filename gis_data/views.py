from django.shortcuts import render
from django.contrib.gis.shortcuts import render_to_kml
from djgeojson.views import *
#from django.contrib.gis.templates import *
from .models import *

def all_kml(request):
     locations  = Stretch.objects.kml()[0:10]
     return render_to_kml("placemarks.kml", {'places' : locations}) 
     
     

    
    
    
    
 
