#!/usr/bin/env python
# coding: utf-8

# # jupyter notebook
# 

# - python
#     - subpoint1
#     - subpoint2
#     - **text**
#     - *text*
#     - ***text***
# 

# ### python introduction
# 

# In[1]:


#input and output function
#output function
print("hello world")
print("python programming")


# In[5]:


print("markdown cell", end='_')
print("code")


# In[6]:


#input function
print('enter name')
a=input(' ')
print('your name is',a)


# # variable are also called as identifiers
# # var name always start with alphabets
# ##  doesn't starts with any spl char except _
# ## doesn't start with digits

# In[8]:


x=10 
type(x)


# In[9]:


y=12
x+y


# # Fundamental datatypes
# ### int
# ### float
# ### complex
# ### boolean
# ### string
# 

# In[16]:


x=10
y=10.5
print(x+y)
type(y)


# In[17]:


c=2+2j
d=3+3j
c+d


# In[18]:


# typecasting
a=12.56
int(a)


# In[19]:


# typecasting
a=12.56
complex(a)


# In[20]:


# typecasting
a=12.56
print(int(a))
complex(a)


# In[22]:


# typecasting
a=12.6
print(int(a))
print(complex(a))


# In[23]:


complex(3,4)


# ### boolean datatype will have either
# #### True or False
# 

# In[26]:


a = True
type(a)


# In[27]:


# string:
a = 'python'
b = 'p'
print(type(a))
print(type(b))


# In[28]:


a='100'
type(a)


# In[29]:


a='100'
print(type(a))
b= int(a)
print(type(b))


# In[32]:


a='100'
print(type(a))
b= int(a)
print(type(b))
c= float(a)
(type(c))


# In[33]:


a='1234'
len(a)


# In[34]:


a=1234
len(str(a))#converts into string and print the number of charecters


# # operators
# ## arthematic operators:
# ### +,-,*,%,//,**
# #### //- floor division(removes the decimal part
# #### **-exponent

# In[35]:


123/ 5


# In[36]:


123// 5


# In[38]:


a= 3
b= 2
print(a+b)
print(a-b)
print(a%b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)


# # logical operators
# ## and,or,not

# In[43]:


x= 12
y= 5
print(x >=20 and y <=3)#both cond should be satisfied
print (x >=20 or y>2)#any one cond is satisfied it gives output
not x


# # relational operators
# ## <,>,<=,>=,==,!=

# In[46]:


x= 3
y= 5
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print(x!=y)


# # membership operators
# ## in,not in

# In[50]:


a= 'Python'
print('P' in a)
print('p' in a)
print('h' in a)
print('P' not in a)
print('H' not in a)


# # conditional statements
# ## if(single condition)
# ## if  else(two conditions)
# ## elif(multiple conditions)

# # syntax:
# 

# ### if condition:
# - statements
#     

# #### tab space after collen is known as intendation
# 

# In[52]:


# to check the given number is even or odd
a= input('enter a number')


# In[53]:


type(a)


# In[62]:


a= int(input('enter a number'))
type(a)
if a%2==0:
    print('even')
else:
    print('odd')


# In[63]:


#to check number is divisible by 3 and 5
a= int(input('enter a number'))
if a%3==0 and a%5==0:
    print('divisible')
else:
    print('not divisible')


# In[67]:


#to check the number is positive or negative or zero
n=  int(input(''))
if n>0:
    print('positive')
elif n<0:
    print('negative')
else:#or we can keep elif n==0
    print('zero')


# In[81]:


#to check year is leap year or not
n= int(input('enter a year'))
if ((n%400==0) or (n%4==0) and (n%100!=0)):
    print('yes')
else:
    print('no')


# 

# # loops
# ## syntax
# - while condition
#     - statements

# In[82]:


#print numbers from 1 to n
n= int(input(''))
i= 1
while i<=n:
    print(i)
    i+=1 #i=i+1 incrementing i value
    
    


# In[1]:


import os


# In[2]:


pwd


# In[ ]:




