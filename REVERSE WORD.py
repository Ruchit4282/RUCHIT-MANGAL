#!/usr/bin/env python
# coding: utf-8

# In[2]:


word = input("input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
   print(word[char], end="")
print("\n")


# In[ ]:




