#!/usr/bin/env python
# coding: utf-8

# QUESTION : 
# Define a function which will take a number as argument and return its factorial.
# 
# Call the function to print factorial of any number(integer).

# In[7]:


def factorial(n):
     
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 

num = int(input("Enter a Number "));
print("Factorial of",num,"is",
factorial(num))


# In[ ]:


# Submitted by Vikas Dubey

