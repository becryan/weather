# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class weather(models.Model):
    date=models.DateTimeField('DateTime')
    apparent_temp=models.DecimalField(max_digits=6, decimal_places=2)
    air_temp=models.DecimalField(max_digits=6, decimal_places=2)
    
def natural_key(self):
    return self.my_natural_key

