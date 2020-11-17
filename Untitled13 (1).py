#!/usr/bin/env python
# coding: utf-8

# In[2]:


P = 1/3


# In[3]:


p_one = 0.3
p_two = 0.8
p_three = 0.5


# In[4]:


P_whole = (P*p_one) + (P*p_two) + (P*p_three)
P_whole


# In[5]:


P_first = (P*p_one)/P_whole
P_first


# In[6]:


P_second = (P*p_two)/P_whole
P_second


# In[7]:


P_third = (P*p_three)/P_whole
P_third


# In[8]:


m = P_third + P_second + P_first


# In[9]:


m


# In[ ]:




