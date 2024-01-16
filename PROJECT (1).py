#!/usr/bin/env python
# coding: utf-8

# In[54]:


import seaborn as sns
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# In[27]:


data=pd.read_csv('HR Data.csv')


# In[28]:


data


# In[29]:


stis=data["Job Satisfaction"].value_counts()
stis


# In[30]:


role=data["Job Role"].value_counts()
role


# In[31]:


data["Job Satisfaction"].value_counts().plot(kind="barh")


# In[32]:


data.describe()


# In[33]:


filtered_data=data[data["Attrition"].str.contains("Yes")]


# In[34]:


filtered_data


# In[35]:


filtered_data["Education Field"].value_counts()


# In[36]:


#education field wise attrition
filtered_data["Education Field"].value_counts().plot(kind="barh")


# In[38]:


#department wise attration
pie_filter=filtered_data[["Attrition","Department"]].value_counts()
pie_filter


# In[39]:


x=[133,92,12]
y=['R&D','Sales','HR']
print(x)


# In[40]:


sns.set_style("whitegrid")
plt.figure(figsize=(6,10))
plt.pie(x, labels=y, autopct='%1.1f%%')
plt.title('My Pie Chart')
plt.show()


# In[41]:


#attration rate by gender for diffrent age group
filtered_data["CF_age band"].value_counts().plot(kind="bar")
plt.grid()


# In[42]:


filtered_data["Gender"].value_counts().plot(kind="bar")


# In[43]:


filtered_data["CF_age band"].value_counts().plot(kind="bar")


# In[44]:


sns.countplot(x=filtered_data["CF_age band"],hue=filtered_data["Gender"])
plt.grid()


# In[45]:


a=filtered_data["Gender"]


# In[46]:


b=filtered_data["CF_age band"]


# In[47]:


data1=data[["Job Role","Job Satisfaction"]]


# In[48]:


data.corr()


# In[49]:


filtered_data


# In[52]:


#department wise attration
labels=["R&D","Sales","HR"]
sizes=filtered_data["Department"].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True)
ax1.axis('equal')
plt.show()


# In[ ]:




