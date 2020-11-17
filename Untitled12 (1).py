#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd


# In[32]:


a = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])


# In[33]:


a


# In[35]:


np.mean([a])


# In[28]:


a.var(ddof=0) ##смещенная


# In[29]:


a.var(ddof=1) ##неcмещенная


# In[40]:


a.std(ddof=0) ## cр. квадратичное отклонение


# In[ ]:




