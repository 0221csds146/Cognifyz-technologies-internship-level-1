#!/usr/bin/env python
# coding: utf-8

# # Task 1: Top 3 Cuisines

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\Rajeev kumar\\Downloads\\Dataset .csv")


# In[8]:


print(df.shape)
print(df.columns)


# In[9]:


print(df['Cuisines'])


# In[10]:


cuisine_count= df['Cuisines'].str.split(', ').explode('Cuisines').value_counts()
print(cuisine_count)
top_cuisine=cuisine_count.head(3)
print("The Top 3 Cuisines are : ",top_cuisine)


# In[12]:


colours = ['green', 'orange', 'red']
plt.bar(top_cuisine.index, top_cuisine.values, color=colours)
plt.xlabel('Cuisine')
plt.ylabel('Count')
plt.title('Top Three Cuisines')
plt.show()


# # Task 2: Percentage of restaurants that serve each of the top cuisines.

# In[14]:


total_restaurant = len(df)
print(total_restaurant)
top_cuisine5=cuisine_count.head()
percentages = (top_cuisine5 / total_restaurant) * 100
print("The Market share of Top 5 Cuisines are : ")
print(percentages)


# In[15]:


plt.bar(top_cuisine10.index, percentages.values, color=colours)
plt.xlabel('Cuisine Name')
plt.ylabel('Percentage')
plt.title('Top five Cuisines %')
plt.figure(figsize=(12,6))
plt.show()


# In[ ]:




