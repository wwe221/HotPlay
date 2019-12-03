from django.urls import path
from . import views as boot_views
from crawling import views as craw_views

urlpatterns = [
    path('', boot_views.index, name="boot"),
    path('twitch/', craw_views.ret_twitch, name="get_twitch"),
    path('youtube/', craw_views.ret_youtube, name="get_youtube"),
    path('afreeca/', craw_views.ret_afreeca, name="get_afreeca"),
    
]