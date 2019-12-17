#!/usr/bin/env python
# coding: utf-8

# # functions:
# - code reusability
# - simpler
# - program can be further divided into sub programs
# 

# # syntax
# - def functions()
#     - statements
#     - return
#     

# In[1]:


#find a number
#output:sum of even digits from the given number
#input:1234
#output:6(2+4)


# In[4]:


def evendigitsum(n):
    s=0
    while n!=0:
        r=n%10
        if r%2==0:# 1234 %10=4
            s=s+r
        n=n//10 #1234//10=123
    return s
evendigitsum(1234)


# In[13]:


#input: 19353
#output: 9(print the largest digit from given number)
def largedigit(n):
    larger=0
    while n!=0:
        r=n%10
        if larger<r:#0<3 # 19353%10=3
            larger=r #large<3
        n=n//10
    return(larger) #19353//10=19353 #19353//10=195
l=largedigit(19353)# return will allocate some memory
l


# # for loop
# ### syntax:
# - for variable_name in iterable_obj:
#     - statements
# - for variable_name in range(start,stop,step):
#     - statements

# In[9]:


for i in range(0,10):
    print(i)


# In[10]:


for i in range(0,10+1,4):
    print(i)


# In[12]:


l


# # collection types:
# - list
# - tuple
# - set
# - dictionary
# ### list
#     - list is the one of the data structure in python
#     - lists are enclosed in[]
#     - list{1,2,3,4}
# 

# In[14]:


li=[1,'gitam','python',32.5]
type(li)


# In[23]:


print(li[0])
print(li[-1])
print(li[1:2])
print(li[1:3])
print(li[2:3])
print(li[0:4])


# In[ ]:




