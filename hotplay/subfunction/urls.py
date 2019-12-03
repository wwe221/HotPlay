from django.urls import path
from . import views as boot_views
from crawling.views import frequnctly
urlpatterns = [
    path('', boot_views.index, name="boot"),
    path('getlives/', boot_views.getlives, name="getlives"),
    path('double_screen/', boot_views.double_screen, name="double_screen"),
]
# frequnctly()