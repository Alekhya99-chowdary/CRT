#!/usr/bin/env python
# coding: utf-8

# In[2]:


li=[10,20,30,4,5]
print(li[0])
print(li[-1])
print(li[0:3])
print(li[::2])
print(li[::3])


# In[3]:


li=[10.20,30,4,5]
li[0:4:2]


# In[6]:


list1=['python',3,6,'hyd']
print(list1)
list1[1]='gitam' #updating values in a list
list1


# In[12]:


#del list item
del list1[1]
list1


# In[19]:


#basic list operations
l=[2,5,7,8,4]
len(l) # to check length of list
l*2 #list repetation
print(4 in l) #to check certain element is present in the list
print(10 not in l)#to check certain element is not present in the list
#acess all the elements present in the list
print(l)
for i in l:
    print(i)


# In[20]:


#range functions to print the list of elements
print(l)
for i in range(len(l)):
    print(l[i])


# In[25]:


print(l)
print(max(l)) #prints maxvalue from the list
print(min(l)) #prints min value from the list
print(sum(l)) #prints sum of elements in the list
print(sum(l)/len(l)) #prints avg of elements in list


# In[29]:


print(l)
l.append('python') #adds the item to the end of the list
l.insert(0,'gitam') #adds the element at a specified index


# In[31]:


print(l.count(4)) #gives how many times a element is there in list
print(l.index(2))
print(l.index(4))


# In[32]:


list1=[6,89,3,2,1,78]
list1.sort() #sort the list according in accending order
list1


# In[37]:


print(list1)
print(list1.pop())#pops the last element in list
list1


# In[38]:


list2=[1,4,7,8]
list2.pop(2) #pops the particular element from mentioned index


# In[39]:


list2


# In[41]:


li1=[1,2,3]
list2.extend(li1)#adding new items to the existing list
list2


# In[42]:


list2.reverse()#reverse the entire list
list2


# In[52]:


#a function to return the largest element from list
def largenumber(li):
    li.sort()
    return li[:-1]
li=[3,45,32,67,890,12]
largenumber(li)


# In[ ]:




