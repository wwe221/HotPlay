from django.urls import path , include
from . import views
app_name='accounts'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('activate/<str:uid64>/<str:token>',views.activate,name="activate"),
    
]