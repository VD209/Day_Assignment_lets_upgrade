#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ASSIGNMENT DAY 2 Solution


# PROJECT :
# 
# Let's say, you are in a lottery competition. A group of words has been given to you and you are asked to select any one character(only alphabets) which will get you a prize. You are a smart person and you thought of a way to select a character that will have maximum chances of winning a prize i.e. select the highest occurring character from the words.
# 
# 

# In[8]:


lottery  = "hello coders"
# 'h' or 'e' or 'o' or 'c' or 'd'
print("choose correct character of the word '",lottery,"' to win the lottery")
inputs = input(" ")

if inputs == lottery[0].lower() or inputs == lottery[1].lower() or inputs == lottery[4].lower() or inputs == lottery[6].lower() or inputs == lottery[8].lower():
    print("congratulation,you win thwe lottery")
else:
    print("sorry, You didn't win the lottery")


# In[ ]:


# Submitted by  Vikas Dubey


# In[ ]:




