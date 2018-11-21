# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import weather
from django.http import JsonResponse
from django.db import connections
from django.core import serializers
from .filters import WeatherFilter
from django.http import HttpResponse
import json



def tables(request):
    data=weather.objects.order_by('date').all()
    context={'data': data}
    return render(request,'weather/tables.html',context)

#def index(request):
#    return render(request,'weather/weather_graph.html')

def index(request):
    data=weather.objects.order_by('date').all()
    context={'thing': data}
    return render(request,'weather/weather_graph.html',context)
  #  return JsonResponse(data,safe=False)
    
    
def search(request):
    user_list = weather.objects.all()
    user_filter = WeatherFilter(request.GET, queryset=user_list)
    return render(request, 'weather/weather_list.html', {'filter': user_filter})
    
    
def myModel_asJson(request):
    object_list = weather.objects.all() #or any kind of queryset
    json = serializers.serialize('json', object_list)
    return = HttpResponse(json,content_type='application/json')

def show(request):
    return render(request, 'weather/thing_template.html')

 
