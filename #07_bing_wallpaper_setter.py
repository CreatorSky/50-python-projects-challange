# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 14:01:06 2017

@author: creatorsky

facebook.com/icreatorsky

Try the exe version in Bing-Wallpaper-Setter repository.
(it'll automate the stuff on daily bases)
"""

import requests
import re
import ctypes
import os
from time import sleep

while True:
    try:
        res = requests.get("http://bing.com").text
    except:
        sleep(300)
        continue
    break
match = re.search('([^"]+.jpg)', res)
url = "http://bing.com"+match.group(0)
r = requests.get(url, stream=True)
chunk_size=1024
path = os.environ['USERPROFILE']+'\\AppData\\Local\\Temp\\todaybg.jpg'
with open(path, 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
