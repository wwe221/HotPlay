from django.shortcuts import render , redirect
from .forms import AuthenticationForm,UserCreationForm 
from django.contrib.auth import login as  auth_login, logout as auth_logout
from .forms import CustomAuthenticationForm, CustomUserCreateionForm
from django.contrib.auth.models import User

from .models import User as User2

from crawling.models import Stream
from django.http.response import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
import json
import threading
import datetime
# Create your views here.
def check_validated_email():
    t1 = threading.Thread(target=delete_none_validated_email)
    t1.start()
    threading.Timer(86400,check_validated_email).start()
    return
def delete_none_validated_email():
    print("delete_none_validated_email start............")
    today = datetime.date.today()
    user = User2.objects.filter(is_active=False)
    cnt = 0
    for tmp in user:
        target_day = tmp.date_joined.date()
        if today - target_day>= datetime.timedelta(1):
            tmp.delete()
            cnt = cnt + 1
    print("delete done............")
    return
def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreateionForm(request.POST)  
            email = form['email']     

            if form.is_valid() :
                user = form.save()
                user.is_active = False
                user.save()

                
                # auth_login(request , form)
                current_site = get_current_site(request) 
                # localhost:8000
               
                message = render_to_string('accounts/activation_email.html',                         {

                    'user': user,
                    'domain': current_site.domain,
                    'uid': force_text(urlsafe_base64_encode(force_bytes(user.id))),
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
            if form.is_valid():
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

def activate(request, uid64, token):

    uid = force_text(urlsafe_base64_decode(uid64))
    user = User2.objects.get(id=uid)
    
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #auth.login(request, user)
        return HttpResponse(
                        '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                        'justify-content: center; align-items: center;">'
                        '인증완료</span>'
                        '</div>')
    else:
        return HttpResponse('비정상적인 접근입니다.')