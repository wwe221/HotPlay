from django.shortcuts import render, redirect
from django.http.response import HttpResponse
import json

# Create your views here.
def index(request):    
    return render(request, 'index.html',) 

def twitch(request):
    return render(request, 'twitch.html')
def getlives(request):
    return render(request , 'slide.html')

def double_screen(request):
    return render(request, 'double_screen.html')

