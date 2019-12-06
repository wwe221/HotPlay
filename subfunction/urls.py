from django.urls import path
from . import views as boot_views
from crawling import views as craw_views
from crawling.views import frequnctly
urlpatterns = [
    path('', boot_views.index, name="boot"),
    path('twitch/', craw_views.ret_twitch, name="get_twitch"),
    path('youtube/', craw_views.ret_youtube, name="get_youtube"),
    path('afreeca/', craw_views.ret_afreeca, name="get_afreeca"),
    path('getlives/', boot_views.getlives, name="getlives"),
    path('double_screen/', boot_views.double_screen, name="double_screen"),
]

