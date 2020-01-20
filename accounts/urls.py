from django.urls import path , include
from . import views
from .views import check_validated_email
app_name='accounts'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    
]
check_validated_email()