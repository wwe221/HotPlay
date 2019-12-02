from django.contrib import admin
from django.urls import path
from . import views


app_name ='live'
urlpatterns = [
    path('',views.main,name='main'),
    path('all/',views.allHTML,name='all'),
    path('slide/',views.slideTest,name='slide'),
    path('youtube/',views.ret_youtube,name='get_youtube'),
    path('twitch/',views.ret_twitch,name='get_twitch'),
    path('afreeca/',views.ret_afreeca,name='get_afreeca'),
    path('getAll/<int:platform>',views.getAllStream,name='get_all'),
    path('getslide/',views.getslide,name='get_slide'),
]