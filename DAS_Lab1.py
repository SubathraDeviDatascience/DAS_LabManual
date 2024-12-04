#!/usr/bin/env python
# coding: utf-8

# # Array Concatenation

# In[2]:


import numpy as np


# In[3]:


arr1=np.array([1,2,3])


# In[4]:


arr2=np.array([4,5,6])


# In[5]:


concatenated = np.concatenate((arr1, arr2))


# In[6]:


print("Concatenated Array:", concatenated)


# # Array Indexing

# In[7]:


import numpy as np


# In[8]:


arr=np.array([10,20,30,40,50])


# In[9]:


print("First Element:",arr[0])


# In[10]:


print("Last Element:", arr[-1])


# In[11]:


print("Slice(1 to 3):", arr[1:4])


# # Basic Array Operations

# In[12]:


import numpy as np


# In[13]:


arr=np.array([1,2,3,4,5])


# In[14]:


print("Array",arr)


# In[15]:


add=arr+5


# In[16]:


print("Add 5", add)


# In[17]:


mul=arr*2


# In[18]:


print("Multiply by 2:", mul)


# # Boolean Indexing to filter array

# In[19]:


import numpy as np


# In[20]:


arr=np.array([1,2,3,4,5])


# In[21]:


filter_arr=arr[arr>2]


# In[22]:


print("Greater than 2", filter_arr)


# # Calculate Mean, Median, Standard Deviation

# In[23]:


import numpy as np


# In[24]:


arr=np.array([1,2,3,4,5,6,7,8,9,10])


# In[25]:


print("Mean:", np.mean(arr))


# In[26]:


print("Median:", np.median(arr))


# In[27]:


print("Standard Deviation:", np.std(arr))


# # Dot product

# In[28]:


import numpy as np


# In[29]:


arr1=np.array([1,2,3])


# In[30]:


arr2=np.array([4,5,6])


# In[31]:


dot_product=np.dot(arr1,arr2)


# # Linear Algebra Operations

# In[32]:


import numpy as np


# In[33]:


matrix=np.array([[1,2],[3,4]])


# In[34]:


determinant=np.linalg.det(matrix)


# In[35]:


inverse=np.linalg.inv(matrix)


# In[36]:


print("Determinate", determinant)


# In[37]:


print("Inverse",inverse)


# # Reshaping arrays

# In[38]:


import numpy as np


# In[39]:


arr=np.arange(1,13)


# In[40]:


reshape_arr=arr.reshape(3,4)


# In[41]:


print("Reshape array:\n", reshape_arr)

