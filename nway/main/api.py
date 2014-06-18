'''
Created on 18-Jun-2014

@author: arun
'''
from rest_framework.generics import ListAPIView
from main.models import ProductCategory


class ProductListView(ListAPIView):
    model = ProductCategory