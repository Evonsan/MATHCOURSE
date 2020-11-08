#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import factorial


# In[5]:


a = int(factorial(13) / (factorial(4) * factorial(13 - 4)))


# In[6]:


a


# In[7]:


b = int(factorial(52) / (factorial(4) * factorial(52 - 4)))


# In[8]:


b


# In[9]:


c = a/b


# In[10]:


c


# In[11]:


P = 1 - (int(factorial(48) / (factorial(4) * factorial(48 - 4)))/int(factorial(52) / (factorial(4) * factorial(52 - 4))))


# In[12]:


P


# In[ ]:




