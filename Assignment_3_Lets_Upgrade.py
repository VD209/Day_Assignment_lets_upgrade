#!/usr/bin/env python
# coding: utf-8

# 
#    
# # question: From a dict, how can we print the Key whose value is maximum ??

# In[18]:


Preferred_Cars = {'Honda':100, 'Ford':12, 'Maruti' : 88, 'Tata' : 120}
pc = Preferred_Cars
 
Keymax = max(pc, key= lambda x: pc[x])
print(Keymax)


# In[ ]:


# Submitted by Vikas Dubey


# In[ ]:




