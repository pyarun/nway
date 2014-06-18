from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey
from categories.models import CategoryBase
from photologue.models import Gallery
from seo.models import Seo

User = get_user_model()


class ProductCategory(CategoryBase):
    """
    To maintain Product category. this can be herirarical data
    """
    class Meta:
        verbose_name_plural = 'Product categories'

class Product(models.Model):
    """
    Maintain Product information
    """
    user = models.ForeignKey(User, help_text="Owner of the product")
    category = models.ForeignKey(ProductCategory)
    
    #all the product table should startwith pt. this will put a check on selecting the content type
    #here only Product type contenttype should be allowed.
    content_type = models.ForeignKey(ContentType, limit_choices_to={"app_label":"main", "name__startswith":"pt"})
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
class ProductTypeBase(models.Model):
    """
    Base class for Product Types
    """
    title = models.CharField(max_length=150)
    description = models.CharField(max_length = 500)
    gallery = models.ForeignKey(Gallery, blank=True, null = True, help_text="Image gallery for Product")
    seo = models.ForeignKey(Seo, blank=True, null=True)
    
    class Meta:
        abstract = True
    
class PtCar(ProductTypeBase):
    """
    Product Type Car.
    Specifically designed to save car data
    """
    FUEL_TYPE_CHOICES = (
            ("petrol", "Petrol"),
            ("deisel", "Deisel"),
        )
    
    brand = models.CharField(max_length=100, help_text="Make Company")
    model = models.CharField(max_length=100, help_text="Model Name")
    fuel_type = models.CharField(choices=FUEL_TYPE_CHOICES, max_length=10)
    color = models.CharField(max_length=10, help_text="Color of the car")
    price = models.FloatField()
    stock = models.PositiveIntegerField(default=0, help_text="how many items are available")
    
    
    
