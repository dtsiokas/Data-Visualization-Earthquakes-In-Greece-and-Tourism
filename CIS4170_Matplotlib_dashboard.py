#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Demitrios Tsiokas
# CIS 4170 Data Visualization
# Matplotlib Dashboard
# Earthquakes and Tourism in Greece


# In[2]:


import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

greece_data = pd.read_csv('data_vis_greece.csv')
greece_data_2 = pd.read_csv('greece_cleaned.csv')


year = greece_data['Year']
months = greece_data['Month']
richter = greece_data['MAGNITUDE (Richter)']
day = greece_data['Date']


# In[7]:


# Scatter plot

plt.scatter(year, richter)
plt.title("Scatter Plot of Months vs. Richter Scale")
plt.xlabel("Years")
plt.ylabel("Magnitute In Richter Scale")


plt.show()


# In[18]:


# Line Chart

plt.plot(year, richter)
plt.xlabel("Year")
plt.ylabel("Magnitude in Richter")
plt.title("Line Chart: Richter Magnitude of Earthquakes 1900-2020")

plt.show()


# In[14]:


# Bar chart

plt.bar(greece_data_2['Year'], greece_data_2['International Arrivals'])
plt.xlabel("Years")
plt.ylabel("International Arrivals of Tourists")
plt.title("Bar Chart: Arrival of Tourists in Greece 1995-2020")

plt.show()


# In[17]:


# Histogram

plt.hist(months, histtype='bar')
plt.xlabel("Months")
plt.ylabel("Count of Months Where Earthquake has Occured")
plt.title("Histogram: Frequency of Earthquake Occurence per Month")

plt.show()


# In[16]:


# Pie Chart

plt.pie(greece_data_2['International Arrivals'], labels = greece_data_2['Year'])
plt.title("Pie Chart: Years with Most International Arrivals in Greece")


plt.show()


# In[5]:


plt.figure(figsize = (23,15))
plt.subplot(3,2,1)
# Line Chart First
plt.plot(year, richter)
plt.xlabel("Year")
plt.ylabel("Magnitude in Richter")
plt.title("Line Chart: Richter Magnitude of Earthquakes 1900-2020")

# Bar Chart Second

plt.subplot(3,2,2)
plt.bar(greece_data_2['Year'], greece_data_2['International Arrivals'])
plt.xlabel("Years")
plt.ylabel("International Arrivals of Tourists")
plt.title("Bar Chart: Arrival of Tourists in Greece 1995-2020")

# Historgram Third

plt.subplot(3,2,3)
plt.hist(months, histtype='bar')
plt.xlabel("Months")
plt.ylabel("Count of Months Where Earthquake has Occured")
plt.title("Histogram: Frequency of Earthquake Occurence per Month")

# Scatter Plot Fourth

plt.subplot(3,2,4)
plt.scatter(year, richter)
plt.title("Scatter Plot of Months vs. Richter Scale")
plt.xlabel("Years")
plt.ylabel("Magnitute In Richter Scale")

# Pie Chart Fifth

plt.subplot(3,2,5)
plt.pie(greece_data_2['International Arrivals'], labels = greece_data_2['Year'])
plt.title("Pie Chart: Years with Most International Arrivals in Greece")

plt.show()


# In[ ]:




