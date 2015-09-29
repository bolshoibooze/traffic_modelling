import logging
import datetime
from django.db import models
from django.db.models import *
from django.conf import settings
from django.utils import timezone
from django.db.models.query import *
from django.contrib.auth.models import *
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property
from django.utils.encoding import smart_unicode
from django.db.models import get_model

#signals
from django.dispatch import receiver
from django.db.models.signals import *

from traffic_modelling.settings import *


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The email must be set')
        email = UserManager.normalize_email(email)
        user = self.model(email=email,
                          is_staff=False,is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_admin = True
        u.save(using=self._db)
        return u

   



class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    about = models.TextField(max_length=500,null=True,blank=True)
    full_name = models.CharField(max_length=50,verbose_name='First & Last Name')
    mug_shot = models.ImageField(upload_to='images/avatar',null=True,blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active   = models.BooleanField(default=False)#activate users manually ?
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]
    
    objects = MyUserManager()
    
    class Meta(object):
        db_table = 'MyUser'
        verbose_name_plural = 'MyUser'
     
    def __unicode(self):
        return self.full_name
         
    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.full_name)
           
    def get_full_name(self):
        #the user is identified by their id_number
        return self.full_name
        
    def get_short_name(self):
        return self.full_name
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
         
    def save(self,*args,**kwargs):
        super(MyUser,self).save(*args,**kwargs)
        
        

