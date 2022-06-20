#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# In[3]:


print(a[0])


# In[7]:


a = np.array([1, 2, 3])
print(a)


# In[8]:


np.zeros(6)


# In[9]:


np.ones(6)


# In[10]:


np.empty(6)


# In[11]:


print(np.arange(4))
print(np.arange(0,10,2))


# In[12]:


np.arange(2,29,5)


# In[14]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr)


# In[15]:


np.append(arr, [1,2])


# In[16]:


np.delete(arr, 1)


# In[18]:


arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(arr)


# In[19]:


np.sort(arr)


# In[30]:


array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]]])

print(array_example)


# In[31]:


array_example.ndim


# In[32]:


array_example.size


# In[33]:


array_example.shape


# In[35]:


arr_one = np.array([[1, 2, 3, 4, 5]])
print(arr_one)


# In[36]:


arr_one.ndim


# In[37]:


arr_one.size


# In[38]:


arr_one.shape


# In[39]:


a = np.arange(6)

print(a)


# In[40]:


b = a.reshape(3,2)

print(b)


# In[41]:


a.reshape(6,1)


# In[42]:


a = np.array([1, 2, 3, 4, 5, 6])
a.shape


# In[43]:


a2 = a[np.newaxis]
print(a2.shape)
print(a2)


# In[44]:


row_vector = a[np.newaxis, :]
print(row_vector.shape)
print(row_vector)


# In[46]:


col_vector = a[:, np.newaxis]
print(col_vector.shape)
print(col_vector)


# In[47]:


a = np.array([1, 2, 3, 4, 5, 6])
a.shape


# In[48]:


b = np.expand_dims(a, axis=1)
b.shape


# In[49]:


c = np.expand_dims(a, axis=0)
c.shape


# In[50]:


data = np.array([1,2,3])

print(data)
print(data[0])
print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])


# In[51]:


a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a


# In[52]:


b = a.view()
b


# In[53]:


c = a.copy()
c


# In[54]:


a = np.array([1, 2, 3, 4])

# Add all of the elements in the array
a.sum()


# In[55]:


b = np.array([[1, 1], [2, 2]])
b


# In[56]:


b.sum(axis=0)


# In[57]:


data = np.array([1, 2])
data


# In[58]:


ones = np.ones(2)
ones


# In[59]:


data + ones


# In[60]:


data * data


# In[61]:


data / data


# In[62]:


data * 2


# In[63]:


A = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(A)


# In[64]:


A.sum()


# In[65]:


A.min()


# In[66]:


A.min(axis=0)


# In[67]:


A.max()


# In[68]:


A.max(axis=1)


# In[69]:


A.std()


# In[70]:


np.ones((3,2))
np.zeros((3,2))
np.random.random((3,2))
print(np.ones((3,2)))
print(np.zeros((3,2)))
print(np.random.random((3,2)))


# In[71]:


data = np.array([[1, 2], [3, 4]])
print(data)


# In[72]:


ones = np.ones([2, 2])
print(ones)


# In[73]:


print(data + ones)


# In[74]:


ones_row = np.ones([1, 2])
print(ones_row)


# In[75]:


print(data + ones_row)


# In[76]:


a_1 = np.array([[1, 2, 3], [4, 5, 6]])
print(a_1)
print(a_1.shape)

a_2 = np.array([[7, 8], [9, 10], [11, 12]])
print(a_2)
print(a_2.shape)


# In[77]:


np.dot(a_1, a_2)


# In[78]:


data = np.array([[1, 2], [3, 4], [5, 6]])

print(data)
print(data[0])
print(data[1])
print(data[2])
print(data[0,1])
print(data[1:3])
print(data[0:2,1])


# In[80]:


print(data.max())
print(data.min())
print(data.sum())


# In[81]:


print(data.max(axis=0))
print(data.max(axis=1))


# In[82]:


ndarr = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])

print(ndarr)


# In[83]:


print(np.zeros((4,3,2)))


# In[84]:


arrflat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(arrflat)

