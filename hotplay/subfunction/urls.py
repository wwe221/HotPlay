from django.urls import path
from . import views as boot_views

urlpatterns = [
    path('', boot_views.index, name="boot"),
    path('getlives', boot_views.getlives, name="getlives"),
]