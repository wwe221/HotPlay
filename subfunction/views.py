from django.shortcuts import render, redirect
from django.http.response import HttpResponse
import json
from django.shortcuts import render
from crawling.models import Stream
from django.db.models import Q

# Create your views here.
def index(request):    
    return render(request, 'index.html',) 

def twitch(request):
    return render(request, 'twitch.html')
def getlives(request):
    return render(request , 'slide.html')

def double_screen(request):
    return render(request, 'double_screen.html')

def search(request):
    keyword = request.GET["keyword"]
    result = Stream.objects.filter(Q(channel_name__contains=keyword)| Q(title__contains=keyword))
    context = {
        'results':result
    }
    return render(request,'subfunction/search_result.html',context)

def show_one_stream(request,stream_id):
    stream = Stream.objects.get(id=stream_id)
    a = ''
    if stream.platform == 0:
        l = stream.stream_url.split('/')
        a = f'https://www.twitch.tv/embed/{l[-1]}/chat'        
    context = {
        'stream':stream,
        'chat':a

    }
    return render(request,'subfunction/one_stream.html',context)

