#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import os


# In[9]:


os.getcwd()


# In[11]:


os.chdir("/Users/hudsonfinchbatista/python-data-manip")
data = pd.read_csv('nhanes.csv')


# In[12]:


data.head(5)


# In[26]:


# exa 1
print(data.columns)
# method 1
data2 = data[(data.BMI > 25) & (data.SmokingStatus == "Current")]

# method 2
exa1 = data.query("(BMI > 25) & (SmokingStatus == 'Current')")


# In[27]:


print(data2.size)
print(exa1.size)


# In[31]:


# exa 2

exa2 = data[data.BMI > data.BMI.quantile(0.90)]


# In[32]:


print(exa2.size)
exa2.head


# In[36]:


# exa 3

exa3 = data[["id","Weight","Height","BMI"]].sort_values(by = "BMI", ascending = False)


# In[37]:


print(exa3.size)
exa3.head


# In[42]:


# exa 4

exa4 = data.groupby("Education")
exa4["Income"].median()


# In[44]:


# exa 5

exa5 = data[(data.Age >= 18) & (data.Gender == "female")].sort_values(by = "Pulse", ascending = False)
exa5.head(10)


# In[45]:


# exa 6

exa6 = data.groupby("Race")
exa6["BPSys"].describe()


# In[56]:


# exa 7

exa7 = data[["id","Education","PhysActive","PhysActiveDays"]].assign(PCTActive = (exa7.PhysActiveDays/7)*100).sort_values(by = "PCTActive")

exa7.head(10)


# In[57]:


# exa 8

exa8 = data[data.Income < data.Income.quantile(0.50)].groupby("Race")
exa8["Weight"].mean()


# In[72]:


# exa 9

exa9 = data1.groupby("Education")
exa9b = exa9["SleepHrsNight"].mean().sort_values(ascending = False)
exa9b


# In[ ]:




