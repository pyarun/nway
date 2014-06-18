from django.conf.urls import url, include
import views as mainapp_views
from main import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r"^$", views.nway_login, {"template_name":"home.html"}, name="nway_login"),
    url(r'^dashboard/$', (mainapp_views.HomeView.as_view()), name="dashboard"),
    url(r"^logout$", views.nway_logout, {}, name="nway_logout"),
    
    url(r"^api/", include("main.apiurls"))
]

