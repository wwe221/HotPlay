from django.shortcuts import render, redirect
from django.http.response import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, 'index.html') 