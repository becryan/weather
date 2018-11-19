

from django.conf.urls import url


from . import views
#from .views import graph, weather, weather_time
app_name='weather'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tables/$',views.tables,name='tables'),
    url(r'^search/$',views.search,name='search'),
    url(r'^ajax/$',views.myModel_asJson,name='my_ajax_url'),


 #   url(r'^tables/$', views.tables, name='tables'),
#   url(r'^$',views.graph,name='graph'),
   # url(r'^$',views.weather_time,name='weather_time')
]
#from django.conf.urls import url

#from . import views
#app_name = 'polls'
#urlpatterns = [
#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

