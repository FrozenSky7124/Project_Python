#!/usr/bin/env python
# coding: utf-8

# In[38]:


import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')
#print(soup.prettify())

soup.title

#
# 基本元素
#

soup.a                 # 获取第一个 a 标签
soup.a.name         
soup.a.parent          # 获取第一个 a 标签的父标签
soup.a.parent.name

soup.a.attrs           # 获取标签属性
soup.a.attrs["class"]  # 获取标签属性中的 class 属性
soup.a.attrs["href"]

soup.a.string
soup.p.string

soup2 = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment.</p>", 'html.parser')
soup2.b.string
soup2.p.string
type(soup2.b.string)   # bs4.element.Comment
type(soup2.p.string)   # bs4.element.NavigableString

#
# 标签树的下行遍历
#

soup.head.contents

soup.body.contents
len(soup.body.contents)

for child in soup.body.children:
    print(child)

#
# 标签树的上行遍历
#

soup.title.parent
soup.html.parent

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
        
#
# 标签树的平行遍历
#

soup.a.next_sibling
soup.a.previous_sibling

for sibling in soup.a.next_siblings:
    print(sibling)


#
# BeautifulSoup Demo
#

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

