#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/nbaallelo.csv')


# In[4]:


df.head() #melihat data 5 baris pertama


# In[5]:


len(df) #jumlah baris


# In[6]:


df.shape #melihat berapa baris dan kolom


# In[7]:


pd.set_option("display.max.columns", None)


# In[8]:


df.head()


# In[9]:


pd.set_option("display.precision", 2)


# In[10]:


df.head()


# In[12]:


df.tail(10) #10 data terbawah


# In[13]:


df.sample(10) #data acak


# In[14]:


df.info() #informasi semua kolom beserta tipe datanya


# In[15]:


df.describe() #Statistika deskriptip


# In[16]:


df.describe(include = 'object')


# In[17]:


df['team_id'].value_counts()


# In[19]:


df.loc[df.fran_id == "Lakers","team_id"].value_counts()


# In[21]:


df.loc[df.team_id == "MNL", "date_game"].min()


# In[23]:


df.loc[df["team_id"] == "MNL", "date_game"].max()


# In[24]:


df.loc[df["team_id"] == "MNL", "date_game"].agg(("min", "max"))


# In[26]:


df.loc[df["team_id"] == "BOS", "pts"].sum() #mengetahui jumlah/total keseluruhan


# In[27]:


revenues = pd.Series([5555, 7000, 1980])


# In[28]:


revenues


# In[29]:


revenues.values


# In[30]:


revenues.index


# In[31]:


city_revenues = pd.Series(
    [4200, 8000, 6500],
    index=["Amsterdam", "Toronto", "Tokyo"]
)
city_revenues


# In[34]:


city_employee_count = pd.Series({"Amsterdam" : 5, "Tokyo" : 8})
city_employee_count


# In[36]:


city_employee_count.keys() #object alias string


# In[39]:


"Tokyo" in city_employee_count


# In[40]:


"Indonesia" in city_employee_count


# In[42]:


city_data = pd.DataFrame({
    "revenue": city_revenues,
    "employee_count": city_employee_count
})
city_data #Nan = not a number / null


# In[43]:


city_data.index


# In[44]:


city_data.values


# In[45]:


city_data.axes[1]


# In[46]:


city_data.keys()


# In[49]:


"Amsterdam" in city_data #seharusnya masuk di index


# In[50]:


"Tokyo" in city_data.index


# In[52]:


df.index


# In[53]:


df.axes


# In[54]:


'points' in df.keys()


# In[55]:


'pts' in df.keys()


# In[57]:


city_revenues["Toronto"]


# In[58]:


city_revenues[1:]


# In[59]:


city_revenues["Toronto":]


# In[61]:


colors = pd.Series(
    ["red", "purple", "blue", "green", "yellow"],
    index=[1, 2, 3, 5, 8]
)
colors #fungsinya sama seperti print untuk manggil variablenya


# In[62]:


colors[1]


# In[63]:


colors.loc[1]


# In[64]:


colors.iloc[1]


# In[66]:


colors.loc[8] #memanggil index keberapa sesuai deskripsi yang di default di atas


# In[68]:


colors.iloc[1:3]


# In[69]:


colors.loc[1:3]


# # Querying Your Dataset

# In[70]:


df


# In[71]:


current_decade = df[df["year_id"] > 2010]
current_decade


# In[72]:


games_with_notes = df[df["notes"].notnull()]
games_with_notes.shape


# In[76]:


ers = df[df["fran_id"].str.endswith("ers")]
ers


# In[77]:


df[
    (df["_iscopy"] == 0) &
    (df["pts"] > 100) &
    (df["opp_pts"] > 100) &
    (df["team_id"] == "BLB")
]


# In[78]:


df[
    (df["_iscopy"] == 0) &
    (df["team_id"].str.startswith("LA")) &
    (df["year_id"] == 1992) &
    (df["notes"].notnull())
]


# In[79]:


city_revenues.sum()


# In[80]:


city_revenues.max()


# In[81]:


df.pts.sum()


# In[83]:


points = df["pts"]
points


# In[84]:


df.head(3)


# In[85]:


df.groupby("fran_id", sort=False)["pts"].sum()


# # Manipulating Columns

# In[86]:


df


# In[88]:


nba = df.copy()
nba.shape


# In[90]:


nba["difference"] = df.pts - df.opp_pts
nba


# In[91]:


nba["difference"].max()


# In[100]:


renamed_nba = nba.rename(
    columns={"game_result": "result", "game_location": "location"}
)

renamed_nba.head()


# # Specifying Data Types

# In[97]:


nba.info()


# In[99]:


nba["date_game"] = pd.to_datetime(nba["date_game"])
nba


# In[101]:


nba["game_location"].nunique()


# In[102]:


nba["game_location"].value_counts()


# # Missing Values

# In[103]:


nba.info


# In[105]:


rows_without_missing_data = nba.dropna()
rows_without_missing_data


# In[ ]:




