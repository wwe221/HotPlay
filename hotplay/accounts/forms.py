from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .models import User
from django.conf import settings
class CustomUserCreateionForm(UserCreationForm):
    address = forms.CharField(min_length=3)    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('address',)
        # 기존에 있던 field 에 하나더 추가 한다는 말.

class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User

