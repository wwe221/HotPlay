from apscheduler.schedulers.blocking import BlockingScheduler
from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
from .models import Stream
import requests
import json
import time
import random
import threading
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    frequnctly()
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')
sched.start()

def frequnctly():
    print("....Crawling Stared....")
    getTwitch()
    getYoutube()
    getAfreeca()
    print("....Crawling End....")
    return

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
        channel = (tmp.select_one('.yt-user-name').text)
        vs = tmp.select_one('ul .yt-lockup-meta-info li')
        if not vs is None:
            vs = vs.text
        else:
            vs = '0'
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
        v = a
        if Stream.objects.filter(channel_name=channel).exists():
            stream = Stream.objects.get(channel_name=channel)
        else:
            stream = Stream()   
        stream.channel_name = channel
        stream.title = t
        stream.stream_url = l
        stream.stream_embed_url = embed
        stream.stream_views = v
        stream.stream_thumbnail = img
        stream.platform = 1
        stream.tof=text_over_flag
        stream.save()
        lives.append(channel)      
    before = Stream.objects.filter(platform=1)
    for tmp in before:
        t = tmp.channel_name
        if not t in lives:
            tmp.delete()
    print("getYoutube done")
    return
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
        channel = tmp['channel']['display_name']
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
        if Stream.objects.filter(channel_name=channel).exists():
            stream = Stream.objects.get(channel_name=channel)
        else:
            stream = Stream()         
        stream.channel_name = channel
        stream.title = title
        stream.stream_url = u
        stream.stream_embed_url = f'https://player.twitch.tv/?channel={name}'
        stream.stream_views = now_views
        stream.stream_thumbnail = thumbnail
        stream.platform = 0
        stream.tof=text_over_flag
        stream.save() 
        lives.append(channel)
    before = Stream.objects.filter(platform=0)
    for tmp in before:
        t = tmp.channel_name
        if not t in lives:
            tmp.delete()
    print("getTwitch done")
    return
def getAfreeca():
    url = "http://www.afreecatv.com/"
    path ='C:/chromedriver'
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
        v = a
        if Stream.objects.filter(channel_name=channel).exists():
            stream = Stream.objects.get(channel_name=channel)
        else:
            stream = Stream()                        
        stream.channel_name = channel
        stream.title = title
        stream.stream_url = link
        stream.stream_embed_url = link
        stream.stream_views = v
        stream.stream_thumbnail = thumbnail
        stream.platform = 2
        stream.tof=text_over_flag
        stream.save()
        lives.append(channel)
    before = Stream.objects.filter(platform=2)
    for tmp in before:
        t = tmp.channel_name
        if not t in lives:
            tmp.delete()
    print("getAfreeca done")
    return