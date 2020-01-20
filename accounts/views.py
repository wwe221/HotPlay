from django.shortcuts import render , redirect
from .forms import AuthenticationForm,UserCreationForm 
from django.contrib.auth import login as  auth_login, logout as auth_logout
from .forms import CustomAuthenticationForm, CustomUserCreateionForm
from django.contrib.auth.models import User
from crawling.models import Stream
from django.http.response import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
import json

# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreateionForm(request.POST)  
            email = form['email']     
            form.is_active = False
            form.save()
            if form.is_valid() :
                
                user = form.save()
                user = User.objects.all()
                # auth_login(request , form)
                current_site = get_current_site(request) 
                # localhost:8000
                print(user.id)
                message = render_to_string('accounts/activation_email.html',                         {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.id)).encode().decode(),
                    'token': account_activation_token.make_token(user),
                })
                mail_title = "계정 활성화 확인 이메일"
                mail_to = request.POST["email"]
                email = EmailMessage(mail_title,message, to=[mail_to])
                email.send()
                return HttpResponse(
                        '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                        'justify-content: center; align-items: center;">'
                        '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
                        '</div>')
        else:
            form = CustomUserCreateionForm()
        context={
            'form':form
        }
        return render(request , 'accounts/signup2.html', context)
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
        return render(request , 'accounts/login2.html', context)
def logout(request):
    auth_logout(request)
    return redirect('boot')

def favorite(request):
    if request.user.is_authenticated and request.method =="POST":
        id = request.POST['stream']
        user = request.user
        stream = Stream.objects.get(id=id)
        if request.user in stream.fav_user.all():           
            user.favorite.remove(stream)
        else:
            user.favorite.add(stream)
        context={
        }
        return HttpResponse(json.dumps(context),status=200,content_type='application/json')
    else:
        return redirect('boot')
def favlist(request):
    l = request.user.favorite.all()
    length= len(l)
    context = {
        'favs':l,
        'len':length

    }
    return render(request,'subfunction/favorite_list.html',context)