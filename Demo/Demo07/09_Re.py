#!/usr/bin/env python
# coding: utf-8

# In[24]:


#
#   Re 库
#

import re

match = re.search(r'[1-9]\d{5}', "BIT 100081")
if match:
    print(match.group(0))

match.string
match.pos
match.endpos
match.re
match.start()
match.end()
match.span()


# In[8]:


match = re.match(r'[1-9]\d{5}', "BIT 100081")


# In[10]:


ls = re.findall(r'[1-9]\d{5}', "BIT100081 TSU100094")
ls


# In[12]:


ls = re.split(r'[1-9]\d{5}', "BIT100081 TSU100094")
ls
ls = re.split(r'[1-9]\d{5}', "BIT100081 TSU100094", maxsplit=1)
ls


# In[13]:


for m in re.finditer(r'[1-9]\d{5}', "BIT100081 TSU100094"):
    if m:
        print(m.group(0))


# In[14]:


re.sub(r'[1-9]\d{5}', "zipcode", "BIT100081 TSU100094")


# In[25]:


match = re.search(r'PY.*N', "PYANBNCNDN")
match

