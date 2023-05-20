#!/usr/bin/env python
# coding: utf-8

# In[26]:


import requests
import re
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
    
for link in soup.find_all(True):
    print(link.name)

for link in soup.find_all(re.compile('b')):
    print(link.name)

soup.find_all('p', attrs = 'course')
soup.find_all(id = 'link1')

soup.find_all(string = re.compile("python"))

