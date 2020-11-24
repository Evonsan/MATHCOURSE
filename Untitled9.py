#!/usr/bin/env python
# coding: utf-8

# In[10]:


from math import factorial


# In[11]:


n = 144
k = 70
x = 0.5


# In[12]:


C = int(factorial(n) / (factorial(k) * factorial(n - k)))


# In[13]:


C


# In[16]:


P = C * (x)**144


# In[17]:


P


# In[ ]:




