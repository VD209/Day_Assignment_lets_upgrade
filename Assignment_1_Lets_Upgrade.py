#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Taking Multiple Values AS input and print sum of them.


# In[5]:


#For 2 inputs,
x, y = [int(x) for x in input("Entered Two Values:").split()]

print('sum of Two values:', x + y)


# In[7]:


#For 3 Inputs,
x, y, z = [int(x) for x in input('Entered Three Values:').split()]

print('sum of three values:', x + y + z)


# In[11]:


#For Multiple Inputs
x = [int(i) for i in input('Entered Values:').split()]

print('sum of Entered Values:', sum(x))


# In[12]:


x = [int(i) for i in input('Entered Values:').split()]

print('sum of Entered Values:', sum(x))


# In[13]:


x = [int(i) for i in input('Entered Values:').split()]

print('sum of Entered Values:', sum(x))


# In[ ]:


# Submitted by Vikas Dubey

