from django import forms
from django.forms import *
from django import template
from django.forms.fields import *
from django.forms.widgets import *
from django.forms import ModelForm
from django.template import loader
from django.contrib.auth.models import User


from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.contrib.auth.hashers import *

from django.forms.util import ValidationError
from django.contrib.auth.forms import *
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.db.models import *

from django.contrib.auth.models import *
from traffic_modelling.settings import *
from accounts.models import *
from .models import *





class MyAuthForm(forms.Form):
    username = forms.CharField(
    max_length=254,
    label=_('E-mail')
    )
    password = forms.CharField(
    label=_("Password"), 
    widget=forms.PasswordInput()
    ) 
    
    error_messages = {
        'invalid_login': _("Please enter the correct e-mail / password. "
                           ),
        'no_cookies': _("Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': _("This account is inactive."),
    }
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(MyAuthForm, self).__init__(*args, **kwargs)
        
       
       

        # Set the label for the "username" field.
        UserModel = get_user_model()
        

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'])
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data

    #throws errors:to be deleted
    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages['no_cookies'])

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
        
        
class UserCreationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(max_length=50,label=_("Choose Password"))
    #,widget=forms.PasswordInput()
    
    class Meta(object):
        model = get_user_model()
        fields = ('email','full_name',)
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            return email
        raise forms.ValidationError("A user with that e-mail address already exists.") 
          
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1", "")
        if len(password1) < 3:
            raise forms.ValidationError("Your password should be more than 3 characters.")
        return password1
        
    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        
        if len(full_name) > 50:
            raise ValidationError(_('Your name should not exceed 50 characters'))
        return full_name
        
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

