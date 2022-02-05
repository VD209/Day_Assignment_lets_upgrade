#!/usr/bin/env python
# coding: utf-8

# Assignment:
# 
# Consider the following function:
# 
# def div(a, b):
#   return a // b
# Write a decorator, mod_div() that will add a feature to the above function which will make sure that numerator will be always greater than the denominator.
# 
# Example:
# 
# If a = 8 & b = 3, then result will be 2.
# 
# If a = 3 & b = 8, then result should be also 2.

# In[5]:


def mod_div(fun):
    def inner(a, b):
        if a < b:
            a , b = b ,a
        fun(a, b)  
    return inner

@mod_div
def div(a, b):
    print(a // b)
    
a , b = (int(i) for i in input("Enter Two Values " ).split())
div(a, b)


# In[ ]:


# submitted by Vikas Dubey

