from django.urls import path
from . import views as boot_views
from crawling import views as craw_views
from accounts import views as account_views
from crawling.views import frequnctly
urlpatterns = [
    path('', boot_views.index, name="boot"),
    path('double_screen/', boot_views.double_screen, name="double_screen"),
    path('show_stream/<int:stream_id>',boot_views.show_one_stream, name="show_one"),

    path('login/', account_views.login, name="login"),
    path('logout/', account_views.logout, name="logout"),
    path('signup/', account_views.signup, name="signup"),
    path('favorite/',account_views.favorite, name="favorite"),
    path('favlist/',account_views.favlist, name="favlist"),
]   
frequnctly()
