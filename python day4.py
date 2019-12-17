#!/usr/bin/env python
# coding: utf-8

# # Tuples
# 

# - Tuples are enclosed in paranthesis()
# - updations are not possible in tuples
# 

# # Difference between lists an tuples
# - lists -->[],tuples-->()
# - lists-->modify,add,or delete the lists items(mutable),tuple-->cannot do any modifications(immutabe)
# - tuples are used only for accessing the data

# In[1]:


tuple1=(1,2,3,4,12.4,'python')
print(tuple1)
type(tuple1)


# In[3]:


tuple1[0:3] # indexing and slicing is same as lists in tuples


# In[4]:


tuple[0]='gitam'


# ##### indexing and slicing should be given in [ ].

# In[5]:


help('tuple')


# ##### help function is used by any datatype to know the methods.

# # Directories
# - Data will be enclosed in[ ].
# - the data will be in the form of key value pairs.
# - Each key is separated with its value by a colon(:).
# - Each key value pair is separated by a comma(,).
# 

# In[4]:


d1={1:'gitam',2:'hyd',1:'abc'}
print(d1)
type(d1)


# In[16]:


dict1={'name':'gitam','email':'gitam@123','address':'hyderabad'}
dict1['name']


# In[17]:


dict1['mail']='gitam@gmail.com'# add a new pair of dictionary
dict1


# In[18]:


dict1['course']='python'
dict1


# In[6]:


dict1['branch']='cse'
dict1


# In[8]:


del dict1['course']# del one at a time


# In[9]:


dect1


# In[10]:


dict1


# In[11]:


del dict1['branch']


# In[12]:


dict1


# In[13]:


del dict1# del entire dictionary


# In[14]:


dict1


# In[15]:


dict1


# In[19]:


dict1


# In[20]:


dict1_keys()


# In[21]:


dict1.keys()


# In[22]:


dict1.values()


# In[23]:


dict1.items()


# In[ ]:




