from django.conf.urls import url
from main import api

urlpatterns = [
    
    url(r"products/$", api.ProductListView.as_view(), name="product_list")
]

