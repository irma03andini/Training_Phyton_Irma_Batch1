#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[8]:


mjr = pd.read_csv('london_crime_by_lsoa.csv')


# In[9]:


mjr.head()


# In[10]:


mjr.tail()


# In[13]:


mjr.rename(columns={'lsoa_code':'Code','major_category':'Major', 'minor_category':'Minor'}, inplace=True)
mjr.columns


# In[15]:


mjr.groupby("Major")["Major"].count().sort_values()


# In[31]:


major = mjr[
    (mjr["year"] >= 2011) &
    (mjr["year"] <= 2016)
].groupby(["Major","year"])["value"].sum()
major


# # Apa perubahan jumlah kasus dari 2011 ke 2016?

# In[21]:


# we are using the inline backend
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt


# In[32]:


major.plot()


# # Apa tindak kriminal yang paling sering terjadi per daerah di 2016?

# In[33]:


import numpy as np
import pandas as pd


# In[34]:


crime = pd.read_csv('london_crime_by_lsoa.csv')


# In[35]:


crime.head()


# In[36]:


crime.tail()


# In[37]:


crime.rename(columns={'lsoa_code':'Code','major_category':'Major', 'minor_category':'Minor'}, inplace=True)
crime.columns


# In[38]:


crime.head()


# In[41]:


kriminal = crime[
    (crime["year"] == 2016)
].groupby(["borough","Major","year"])["value"].sum()
kriminal


# In[48]:


kriminal.plot()


# In[ ]:




