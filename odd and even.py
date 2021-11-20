#!/usr/bin/env python
# coding: utf-8

# In[2]:


numbers = (1,2,3,4,5,6,7,8,9)
count_odd = 0
count_even = 0
for X in numbers:
        if not X % 2:
             count_even+=1
        else:
             count_odd+=1
print("Number of even Numbers :",count_even)
print("Number of odd Numbers:",count_odd)
             


# In[ ]:




