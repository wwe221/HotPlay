from django.contrib import admin
from django.urls import path
from . import views


app_name ='live'
urlpatterns = [
    path('',views.main,name='main'),
    path('all/',views.allHTML,name='all'),
    path('slide/',views.slideTest,name='slide'),    
    path('platform/<int:platform>',views.platform,name='get_platform'),
    path('getAll/<int:platform>',views.ret_stream,name='get_all'),

    path('getslide/',views.getslide,name='get_slide'),

    path('get_main_thumb/<int:platform>',views.get_main_thumbnail , name='get_main_thumbnail'),

    path('youtube/',views.ret_youtube,name='get_youtube'),
    path('twitch/',views.ret_twitch,name='get_twitch'),
    path('afreeca/',views.ret_afreeca,name='get_afreeca'),
]