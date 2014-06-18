from django.contrib import admin

# Register your models here.

from main.models import ProductCategory, Product, PtCar

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(PtCar)