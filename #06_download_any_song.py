# -*- coding: utf-8 -*-

import requests,time,sys
from bs4 import BeautifulSoup
from clint.textui import progress

def download(url):
    u = requests.get(url, stream=True)
    time.sleep(2)
    x = u.headers.get('Content-Disposition')
    try:
        y = x.split("filename=",1)[1]
        file_name = y[1:-1]
        blacklist = ["lyrics","lyric","video","full","(",")","official","[","]","hd"]
        for word in blacklist:
            file_name = file_name.lower().replace(word,"")
        file_size = float(u.headers.get('Content-Length'))
        print ("Downloading: %s" % (file_name))
        
        
        with open(file_name, 'wb') as f:
            total_length = file_size
            for chunk in progress.bar(u.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                if chunk:
                    f.write(chunk)
                    f.flush()
                    
        
    except:
        download(url)
    

def search(query):
    query = query.replace(" ","+")
    url = "https://www.youtube.com/results?search_query="+query
    h3 = BeautifulSoup(requests.get(url).text, "html.parser").find('h3',{'class' : 'yt-lockup-title'})
    x = BeautifulSoup('',"html.parser")
    child = h3.findChildren()
    for c in child:
        x.append(c)

    watch_url = ''
    for link in x.findAll('a',{'rel':'spf-prefetch'}):
        watch_url = link.get('href')

    yt_url = "https://www.youtube.com"+watch_url
    return yt_url

def dlink(yt_url):
    yt_in_mp3 = "http://www.youtubeinmp3.com/fetch/?format=text&video="+yt_url
    downloadLink = requests.get(yt_in_mp3).text.split("Link: ",1)[1]
    print("Please wait..")
    return downloadLink


if len(sys.argv) > 1:
    print(len(sys.argv))
    name = str(sys.argv[1])
else:
    name = input("Enter song name(eg. See you again - Wiz Khalifa) : ")

start = time.time()

yt_url = search(name)
downloadLink = dlink(yt_url)
download(downloadLink)

stop = time.time()
duration = stop - start
print("Task took total",int(duration),"sec")    
    
    
    
    
