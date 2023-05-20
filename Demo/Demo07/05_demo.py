#!/usr/bin/env python
# coding: utf-8

# # Requests Demo

# In[1]:


import requests

url = "https://item.jd.com/10039449437175.html"

r = requests.get(url)
r.status_code
r.encoding
r.apparent_encoding
r.request.headers
r.text[:1000]


# In[6]:


url = "https://item.jd.com/10039449437175.html"
kv = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url, headers = kv)
r.status_code


# In[17]:


url = "https://www.baidu.com/s"
kv = { 'wd': 'ArkNights' }
kv_hd = { 'user-agent': "Mozilla/5.0" }
r = requests.get(url, params = kv, headers = kv_hd)
r.status_code
r.encoding = r.apparent_encoding
r.text


# In[20]:


## Image

url = "http://httpbin.org/image/jpeg"
filePath = "./image.jpg"
r = requests.get(url)
r.status_code
with open(filePath, 'wb') as f:
    f.write(r.content)
    f.close()


# In[21]:


## Image Demo

import requests
import os

url = "https://webstatic.mihoyo.com/upload/contentweb/2022/07/04/cb95a5b5d57165a4970d801c5dcf0435_8788044469681939890.png"
fileDir = ".//xPics//"
filePath = fileDir + url.split('/')[-1]

try:
    if not os.path.exists(fileDir):
        os.mkdir(fileDir)
    if not os.path.exists(filePath):
        r = requests.get(url)
        with open(filePath, 'wb') as f:
            f.write(r.content)
            f.close()
            print("File saved.")
    else:
        print("File existed.")
except:
    print("Faild.")


# In[33]:


## IP Address search

import requests

url = "https://m.ip138.com/iplookup.php"
kv = { 'ip': '125.32.251.49' }
hd = { 'user-agent': 'Mozilla/5.0' }

try:
    r = requests.get(url, params = kv, headers = hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[2200:2400])
except:
    print("HTTP Error")

