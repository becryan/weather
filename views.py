# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import weather, nice
from django.http import JsonResponse
from django.db import connections
from django.core import serializers
from .filters import WeatherFilter
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
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
    if 'q' in request.GET:
        message='You searched for :%r' % request.GET['q']
        q = request.GET['q']
        
    #if 'nness' in request.GET:
    #    nness=request.GET['nness']
        
        if q:
           # if nness:
                #weat =weather.objects.filter(apparent_temp__icontains=q)
           #     nicet = nice.objects.filter(niceness__icontains=nness).values('id')
            weather_nice = weather.objects.filter(apparent_temp__icontains=q).select_related('niceness_desc')
            #else:
            #    weather_nice = weather.objects.filter(apparent_temp__icontaines=q)
            return render(request, 'weather/results.html',{'filter':weather_nice})
    else:
        return HttpResponse('please submit a search form')
    #user_list = weather.objects.all()
    #user_filter = WeatherFilter(request.GET, queryset=user_list)
    #json=serializers.serialize('json',user_filter)
    #return HttpResponse(json,content_type='application/json')
    #return render(request, 'weather/weather_list.html', {'filter': user_filter})


#def show_search(request):
#    return render(request,'weather/weather_list.html')
    
def myModel_asJson(request):
    object_list = weather.objects.all()
    json = serializers.serialize('json', object_list)
    return HttpResponse(json, content_type='application/json')
    #return HttpResponse(json, content_type='application/json', {'template':'weather/thing_template.html'}) 
    #return render(request, 'weather/thing_template.html',{'json':data})
    ##data=HttpResponse(json,content_type='application/json')
    #data = HttpResponse(json,content_type='application/json')
   # data = {'data': test_all}
    #print(test_all)
    #return render(request, 'weather/thing_template.html', {'data': data})
    
def show(request):
    return render(request, 'weather/thing_template.html')

def show_image(request):
    
    filename='DSCN1846.jpg'
    
    return render(request, 'weather/an_image.html',context={'filename': filename})

def search_form(request):
    return render(request,'weather/search_form2.html')
    

        
 
