#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


mnr = pd.read_csv('london_crime_by_lsoa.csv')


# In[4]:


mnr.head()


# In[5]:


mnr.tail()


# In[6]:


mnr.rename(columns={'lsoa_code':'Code','major_category':'Major', 'minor_category':'Minor'}, inplace=True)
mnr.columns


# In[7]:


mnr.groupby("Minor")["Minor"].count().sort_values()


# In[9]:


minor = mnr[
    (mnr["year"] >= 2011) &
    (mnr["year"] <= 2016)
].groupby(["Minor","year"])["value"].sum()
mnr


# # Apa perubahan jumlah kasus dari 2011 ke 2016?

# In[10]:


# we are using the inline backend
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt


# In[11]:


minor.plot()


# # Apa tindak kriminal yang paling sering terjadi per daerah di 2016?

# In[12]:


import numpy as np
import pandas as pd


# In[13]:


crime = pd.read_csv('london_crime_by_lsoa.csv')


# In[14]:


crime.head()


# In[15]:


crime.tail()


# In[16]:


crime.rename(columns={'lsoa_code':'Code','major_category':'Major', 'minor_category':'Minor'}, inplace=True)
crime.columns


# In[17]:


crime.head()


# In[18]:


kriminal = crime[
    (crime["year"] == 2016)
].groupby(["borough","Minor","year"])["value"].sum()
kriminal


# In[19]:


kriminal.plot()

