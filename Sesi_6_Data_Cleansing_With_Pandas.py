#!/usr/bin/env python
# coding: utf-8

# # Sources of Missing Values

# In[8]:


import numpy as np
import pandas as pd


# In[4]:


df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/property_data.csv')


# In[5]:


df.head(10)


# # Standard Missing Values

# In[6]:


df['ST_NUM']


# In[7]:


df['ST_NUM'].isnull()


# # Non-Standard Missing Values

# In[9]:


df['NUM_BEDROOMS']


# In[14]:


missing_values = ["n/a", "na", "--"]


# # Unexpected Missing Values

# In[18]:


df['OWN_OCCUPIED']


# In[19]:


df['OWN_OCCUPIED'].isnull()


# In[21]:


cnt=0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
    except ValueError:
        pass
    cnt+=1
df.head(9)


# # Summarizing Missing Values

# In[22]:


df.isnull().sum()


# In[23]:


df.isnull().values.any()


# In[24]:


df.isnull().sum().sum()


# # Replacing

# In[25]:


df['ST_NUM'].fillna(125, inplace=True)


# In[29]:


df.isnull().sum()


# In[ ]:




