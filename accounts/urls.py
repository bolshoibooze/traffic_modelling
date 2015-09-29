from django.conf.urls import *
from django.views.generic import TemplateView
from djgeojson.views import *
from accounts.views import *
from . import views
from .models import *



urlpatterns = [
    url(r'^signup/$',SignUpView.as_view(),name='signup'),
    url(r'^access/$',TemplateView.as_view(template_name='access_request.html'),name='access'),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$',views.logout_view,name='logout')
   
]
