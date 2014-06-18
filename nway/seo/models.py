'''
Created on 18-Jun-2014

@author: arun
'''
from django.db import models
from taggit.managers import TaggableManager

class Seo(models.Model):
    """
    Model to keep SEO details
    """
    seo_title = models.CharField(max_length=256)
    description = models.CharField(max_length=1000, null=True, blank=True)
    keywords = TaggableManager()
    
