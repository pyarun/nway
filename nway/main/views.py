from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login, logout
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    """
    Renders the home page
    """
    template_name = "dashboard.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return TemplateView.dispatch(self, request, *args, **kwargs)


def nway_login(request, *args, **kwargs):
    '''
    login mechanism based on userID as email and password 
    if user is already logged in user will be directed to dashboard
    '''
    if not request.user.is_authenticated():
        return login(request, *args, **kwargs)
    else: return redirect(reverse("dashboard"))

def nway_logout(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect(reverse("nway_login"))
