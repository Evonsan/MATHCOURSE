#!/usr/bin/env python
# coding: utf-8

# In[5]:


from math import factorial


# In[12]:


p = 0.0004


# In[13]:


n = 5000


# In[14]:


z = n*p


# In[15]:


k = 0


# In[16]:


Y = int(z**0/factorial(0))*(2.71**-z) # ни одна не перегорит


# In[17]:


Y


# In[18]:


T = int(z**2/factorial(2))*(2.71**-z) #перегорят 2


# In[19]:


T


# In[ ]:




