from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User

from registration import signals
from registration.views import RegistrationView as BaseRegistrationView
from django.http.response import HttpResponse
import json
from registration.forms import RegistrationFormUniqueEmail as BaseRegistrationForm
from django import forms
import string
import random
from django.core.urlresolvers import reverse_lazy


class RegistrationForm(BaseRegistrationForm):
    
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100, required=False)
    
    def clean_username(self):
        """
        In this system usernames are system defined. So
        overriding the clean method to generate unique username
        """
        while(True):
            username = "".join(random.sample(string.letters, 6))
            if not User.objects.filter(username=username).exists():
                break
        return username
    

class RegistrationView(BaseRegistrationView):
    """
    A registration backend which implements the simplest possible
    workflow: a user supplies a username, email address and password
    (the bare minimum for a useful account), and is immediately signed
    up and logged in).
    
    """
    disallowed_url = 'registration_disallowed'
    form_class = RegistrationForm
    http_method_names = ['post']
    success_url = reverse_lazy("dashboard")
    template_name = 'registration/registration_form.html'
    
    def form_invalid(self, form, request=None):
        return HttpResponse(json.dumps(form.errors), status=422, mimetype="application/json")
    
    def register(self, request, **cleaned_data):
        username, email, password= cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        User.objects.create_user(username, email, password, 
                                 first_name = cleaned_data['firstname'],
                                 last_name = cleaned_data['lastname'])

        new_user = authenticate(username=email, password=password)
#         login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:

        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.

        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.
        
        """
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def form_valid(self, request, form):
        new_user = self.register(request, **form.cleaned_data)
        success_url = self.get_success_url(request, new_user)
        context = dict(
                redirect_url = success_url
            )
        
        return HttpResponse(json.dumps(context), mimetype="application/json")
    