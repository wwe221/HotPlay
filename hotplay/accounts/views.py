from django.shortcuts import render , redirect
from .forms import AuthenticationForm,UserCreationForm 
from django.contrib.auth import login as  auth_login, logout as auth_logout
from .forms import CustomAuthenticationForm, CustomUserCreateionForm
# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreateionForm(request.POST)        
            if form.is_valid() :
                user = form.save()
                auth_login(request , user)
                return redirect('boot')
        else:
            form = CustomUserCreateionForm()
        context={
            'form':form
        }
        return render(request , 'accounts/signup.html', context)
    else:
        return redirect('boot')
def login(request):
    if request.user.is_authenticated:
        return redirect('boot')
    else:
        if request.method == "POST":
            form = CustomAuthenticationForm(request, request.POST)
            #문지기 form 이기 때문에 request와 reqeust.POST 두개의 인자를 받는다.
            if form.is_valid() :
                user = form.get_user()
                auth_login(request, user)
                return redirect(request.GET.get('next')or 'boot')                
        else:
            form = CustomAuthenticationForm()
        context={
            'form':form
        }
        return render(request , 'accounts/login.html', context)
def logout(request):
    auth_logout(request)
    return redirect('boot')

def favorite(request):
    
    return ''