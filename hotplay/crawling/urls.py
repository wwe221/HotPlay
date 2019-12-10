from django.contrib import admin
from django.urls import path
from . import views


app_name ='live'
urlpatterns = [  
    path('platform/<int:platform>',views.platform,name='get_platform'),
    path('getAll/<int:platform>',views.ret_stream,name='get_all'),
    path('getslide/',views.getslide,name='get_slide'),
    path('get_main_thumb/<int:platform>',views.get_main_thumbnail , name='get_main_thumbnail'),
]