#!/usr/bin/env python
# coding: utf-8

# In[34]:


#
# Demo 爬取中国大学排名 https://www.shanghairanking.cn/
#

import requests
import bs4
import re
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            rank = tr.find('div', attrs = re.compile("ranking")).string.strip()
            name = tr.find('a', attrs = re.compile("name-cn")).string.strip()
            score = tr.find_all('td', recursive = False)[4].string.strip()
            ulist.append([rank, name, score])
            ##print(rank)

def printUnivList(ulist, num):
    print("{:<4} {:\u3000<12} {:<5}".format("Rank", "Name", "Score"))
    for i in range(num):
        print("{:<4} {:\u3000<12} {:<5}".format(ulist[i][0], ulist[i][1], ulist[i][2]))

def printUnivList_zhCN(ulist, num):
    print("{0:<4} {1:<24} {2:<5}".format("Rank", "Name", "Score"))
    tplt = "{0:<4} {1:{3}<12} {2:<5}"
    for i in range(num):
        print(tplt.format(ulist[i][0], ulist[i][1], ulist[i][2], chr(12288)))
            
def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2023"
    html = getHTMLText(url)
    getUnivList(uinfo, html)
    printUnivList_zhCN(uinfo, 30)

main()

