#!/usr/bin/env python
# coding: utf-8

# In[16]:


#
# Selenium
#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("")
title = driver.title
title


# In[25]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(driver.page_source, 'html.parser')


# In[48]:


opImg = soup.find(id = 'charimg')
for child in opImg.children:
    print(child.attrs['src'].replace(r"?image_process=format,webp/quality,Q_90", ""))


# In[53]:


type(driver)
btn2 = driver.find_element(By.CSS_SELECTOR, "#charinfo-wrapper > div.top-btns > div.stage-btn-wrapper > div:nth-child(2)")
btn2.click()

driver.quit()

