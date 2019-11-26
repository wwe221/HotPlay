from django.contrib import admin
from django.urls import path
from . import views


app_name ='live'
urlpatterns = [
    path('',views.main,name='main'),
    path('all/',views.allHTML,name='all'),
]