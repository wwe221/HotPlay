from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import json
import time
from .models import Stream
# Create your views here.
def main(request):
    test = getbysele()
    #lives= getYoutube()
    # context= {
    #     'lives':lives,
    # }    
    # return render(request, 'main.html',context)
    data = getAfreeca()
    context = {
        'lives': data,
        'test':test
    }
    return render(request, 'main.html',context)
def slideTest(request):

    return render(request, 'slideTest.html')
def allHTML(request):    
    html = getTwitch()
    context ={
        'lives':html
    }
    return render(request, 'twitch.html',context)
def getbysele():
    url = 'https://www.youtube.com/channel/UC4R8DWoMoI7CAwX8_LjQHig'
    path ='Y:/chromedriver'
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(path,chrome_options=options)
    browser.get(url)
    html = browser.page_source
    browser.quit()
    soup = BeautifulSoup(html,'html.parser')
    primary = soup.select_one('.contents')
    # item_sctions = primary.select('.ytd-item-section-renderers')
    # for tmp in item_sctions:
    #     print(tmp)
    return soup
    
def getYoutube():
    url = 'https://www.youtube.com/channel/UC4R8DWoMoI7CAwX8_LjQHig'    
    data = requests.get(url).text
    html = BeautifulSoup(data,'html.parser')
    # lives = html.select('#items .style-scope .yt-horizontal-list-renderer')
    test=html.select('.channels-content-item')
    contents = html.select('.feed-item-main-content')
    lives =[]
    length = len(test)
    for tmp in test:
        img = tmp.select_one('img')['data-thumb']
        t = (tmp.select_one('.yt-lockup-title a')['title'])
        embed =  "https://www.youtube.com/embed/"
        link  = tmp.select_one('.yt-lockup-title a')['href']
        key = link.split('=')
        embed = f'{embed}{key[1]}'
        l = (f"https://www.youtube.com{tmp.select_one('.yt-lockup-title a')['href']}")        
        c = (tmp.select_one('.yt-user-name').text)
        vs = (tmp.select_one('ul .yt-lockup-meta-info li').text)        
        text_over_flag= 0        
        if len(t) > 20:
            text_over_flag= 1        
        if vs[0:2] =='시작':
            continue
        if vs[0:2] =='조회':            
            continue
        cma = vs.split('명')
        a = 0
        for tp in cma[0].split(','):
            a *=1000
            a += int(tp)
        print(a)
        v = a
        stream = Stream()        
        stream.channel_name = c
        stream.title = t
        stream.stream_url = l
        stream.stream_embed_url = embed
        stream.stream_views = v
        stream.stream_thumbnail = img
        stream.platform = 1
        stream.save()
        bang = {
            'title':t,
            'embed':embed,
            'link':l,
            'channel':c,
            'viewer':v,
            'img':img,
            'tof':text_over_flag,
        }  
        lives.append(bang)
    context = {
        'lives':lives,
        'length':length
    }
    return context
def getTwitch():    
    url = "https://api.twitch.tv/kraken/streams/"
    params ={
        'language':'ko',
        'stream_type':'all',
        'limit':100,
    }  
    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',        
        'Client-ID': 'u9b5xmjbfx2meuntk2a2r5gj9ax7vc'
    }
    data = requests.get(url, params = params , headers= headers)
    jsons = data.json()['streams']
    lives= []
    length = len(jsons)
    for tmp in jsons:
        c = tmp['channel']['display_name']
        g = tmp['game']
        name = tmp['channel']['name']
        logo = tmp['channel']['logo']
        title = tmp['channel']['status']
        thumbnail = tmp['preview']['medium']
        profile_banner = tmp['channel']['profile_banner']
        u = tmp['channel']['url']
        total_views = tmp['channel']['views']
        now_views = tmp['viewers']
        followers = tmp['channel']['followers']
        text_over_flag= 0
        if len(title) > 20:
            text_over_flag= 1
            
        bang = {            
            'title':title,
            'embed':u,
            'link':u,   
            'channel':c,
            'viewer':now_views,
            'img':thumbnail,
            'tof':text_over_flag,
        }
        lives.append(bang)    
    context = {
        'lives':lives,
        'length':length
    }
    return context
def getAfreeca():
    url = "http://www.afreecatv.com/"
    path ='Y:/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    browser = webdriver.Chrome(path,chrome_options=options)
    browser.get(url)
    g = browser.find_elements_by_css_selector('.onAir')
    html = browser.page_source
    browser.quit()
    soup = BeautifulSoup(html,'html.parser')
    onAir = soup.select_one('.onAir')
    lists = onAir.select('li')
    lives=[]
    length=len(lists)
    for tmp in lists:        
        title = tmp.select_one('.subject').text
        v = tmp.select_one('.viewer').text.split(' ')
        vs = v[0]
        thumbnail = tmp.select_one('.thumb img')['src']
        channel = tmp.select_one('.nick').text
        link = tmp.select_one('.box_link')['href']
        text_over_flag= 0    
        if len(title) > 20:
            text_over_flag= 1
        if vs[0:2] =='시작':
            continue
        if vs[0:2] =='조회':            
            continue
        cma = vs.split('명')
        a = 0
        for tp in cma[0].split(','):
            a *=1000
            a += int(tp)
        print(a)
        v = a
        stream = Stream()        
        stream.channel_name = channel
        stream.title = title
        stream.stream_url = link
        stream.stream_embed_url = link
        stream.stream_views = v
        stream.stream_thumbnail = thumbnail
        stream.platform = 2
        stream.save()
        bang = {
            'title':title,
            'embed':link,
            'link':link,   
            'channel':channel,
            'viewer':vs,
            'img':thumbnail,
            'tof':text_over_flag,            
        }
        lives.append(bang)
    context = {
        'lives':lives,
        'length':length
    }
    return context
def ret_youtube(request):
    get = getYoutube()
    lives = get['lives']
    length = get['length']
    context={
        'lives':lives,
        'length':length
    }
    return render(request,'all.html',context)

def ret_twitch(request):
    get= getTwitch()
    lives = get['lives']
    length = get['length']
    context={
        'lives':lives,
        'length':length
    }
    return render(request,'all.html',context)
def ret_afreeca(request):
    get= getAfreeca()
    lives = get['lives']
    length = get['length']
    context={
        'lives':lives,
        'length':length
    }
    return render(request,'all.html',context)