#!/usr/bin/env python
# coding: utf-8

# Assignment: Use filter function to filter out the elements from a list that are divisible by 3 & 5

# In[10]:


def fun(n):
    return n % 3 == 0 and n % 5 == 0


# In[5]:


No = [ 3, 7, 9, 87, 56, 100 , 42, 88, 999, 2100, 4555, 12, 80, 397, 411]


# In[11]:


x = print(list(filter(fun, No)))


# In[22]:


# using 3 OR 5
def fun2(n):
    return n % 3 == 0 or n % 5 == 0


# In[24]:


x = print(list(filter(fun2, No)))


# In[25]:


# Using range
y = print(list(filter(fun, list(range(501)))))
z = print(list(filter(fun2, list(range(501)))))


# In[ ]:


# Submitted by Vikas Dubey

