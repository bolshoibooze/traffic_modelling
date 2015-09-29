from django.http import *
from django.contrib.auth import  *
from django.shortcuts import render
from django.views.generic.edit import *
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from accounts.forms import *
from .utils import *

# Create your views here.


class LoginView(FormView):
    template_name = 'login_form.html'
    form_class = MyAuthForm
    success_url = '/section_loading/datasets/' 
    
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)
        
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.success_url:
            redirect_to = self.success_url
        else:
            redirect_to = self.request.REQUEST.get(self.redirect_field_name, '')

        netloc = urlparse.urlparse(redirect_to)[1]
        if not redirect_to:
            redirect_to = settings.LOGIN_REDIRECT_URL
        # Security check -- don't allow redirection to a different host.
        elif netloc and netloc != self.request.get_host():
            redirect_to = settings.LOGIN_REDIRECT_URL
        return redirect_to

    def set_test_cookie(self):
        self.request.session.set_test_cookie()

    def check_and_delete_test_cookie(self):
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            return True
        return False

    def get(self, request, *args, **kwargs):
        """
        Same as django.views.generic.edit.ProcessFormView.get(), but adds test cookie stuff
        """
        self.set_test_cookie()
        return super(LoginView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        adds test cookie stuff
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.check_and_delete_test_cookie()
            return self.form_valid(form)
        else:
            self.set_test_cookie()
            return self.form_invalid(form)
            
            
def logout_view(request):
    logout(request)
    request.session.flush()
    request.user = AnonymousUser

    return HttpResponseRedirect('/accounts/login/')    
            
class SignUpView(FormView):
    template_name ='signup_form.html'
    form_class = UserCreationForm
    success_url = '/accounts/access/'
    
    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)
