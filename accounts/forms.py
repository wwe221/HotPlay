from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .models import User
from django.conf import settings
class CustomUserCreateionForm(UserCreationForm):
    nickname = forms.CharField(min_length=3)
    username = forms.CharField(min_length=4)
    email = forms.EmailField()
    class Meta(UserCreationForm.Meta):
        
        model = User
        fields = ['username', 'email']
        # 기존에 있던 field 에 하나더 추가 한다는 말.

class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User
        



