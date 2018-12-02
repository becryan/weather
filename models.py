# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class nice(models.Model):
    niceness=models.CharField(max_length=10,default='Nice')
    id=models.AutoField(primary_key=True)
# Create your models here.
class weather(models.Model):
    date=models.DateTimeField('DateTime')
    apparent_temp=models.DecimalField(max_digits=6, decimal_places=2)
    air_temp=models.DecimalField(max_digits=6, decimal_places=2)
    niceness_desc=models.ForeignKey(nice,null=True)
    
    
    def natural_key(self):
        return self.my_natural_key
    


