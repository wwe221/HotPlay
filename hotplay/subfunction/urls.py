from django.urls import path
from . import views as boot_views

urlpatterns = [
    path('', boot_views.index, name="boot"),
]