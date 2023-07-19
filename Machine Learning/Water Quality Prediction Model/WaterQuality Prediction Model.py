#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[2]:


from sklearn.ensemble import RandomForestClassifier


# DATA COLLECTION

# In[3]:


wquality_data=pd.read_csv(r'D:\Users\User\Downloads\archive (7)\Water Quality Testing.csv')


# In[4]:


wquality_data.head()


# In[5]:


wquality_data.tail()


# In[6]:


wquality_data.shape


# In[7]:


wquality_data.describe()


# In[8]:


wquality_data.info()


# In[9]:


wquality_data.isnull()


# In[ ]:





# Data Visualization

# In[10]:


sns.set_style('whitegrid')

sns.pairplot(wquality_data,kind='scatter',height=3.5)


# In[11]:


plt.scatter(x=wquality_data['Dissolved Oxygen (mg/L)'], y=wquality_data['Conductivity (µS/cm)'], marker='x')
plt.show()


# In[12]:


sns.set_style('whitegrid')
sns.pairplot(wquality_data[['pH', 'Temperature (°C)', 'Turbidity (NTU)', 'Dissolved Oxygen (mg/L)', 'Conductivity (µS/cm)']], hue='Conductivity (µS/cm)')


# In[13]:


sns.set_style("darkgrid")
sns.histplot(wquality_data, x='pH')


# In[14]:


sns.heatmap(wquality_data)


# In[15]:


sns.lmplot(data=wquality_data, x='pH', y='Turbidity (NTU)', scatter_kws={'color':'red'}, line_kws={'color':'black'})


# In[16]:


sns.catplot(data=wquality_data,x='Dissolved Oxygen (mg/L)', y='pH')


# In[17]:


plot = plt.figure(figsize=(5,5))
sns.barplot(x='pH',y='Dissolved Oxygen (mg/L)',data=wquality_data)


# In[18]:


plot = plt.figure(figsize=(5,5))
sns.barplot(x='pH',y='Conductivity (µS/cm)',data=wquality_data)


# In[ ]:





# correlation

# 

# positive correlation 
# negative correlation

# In[19]:


correlation=wquality_data.corr()


# In[20]:


plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True , fmt='.2f',annot=True, annot_kws={'size':8}, cmap='Blues')


# In[ ]:





# Data Preprocessing 

# In[21]:


X=wquality_data.drop('Dissolved Oxygen (mg/L)',axis=1)


# In[22]:


print(X)


# In[23]:


#Label Binarization


# In[24]:


Y = wquality_data['Dissolved Oxygen (mg/L)'].apply(lambda y_value: 1 if y_value >= 8.0 else 0  )


# In[25]:


print(Y)


# In[ ]:





# Train & Test Split

# In[26]:


X_train, X_test ,Y_train, Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)


# In[27]:


print(Y.shape,Y_train.shape,Y_test.shape)


# In[28]:


print(X)


# Model Training

# In[ ]:





# Random Forest Classifier

# In[29]:


model = RandomForestClassifier()


# In[30]:


model.fit(X_train,Y_train)


# In[31]:


#Model Evaluation


# In[32]:


X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)


# In[33]:


print('Accuracy:',test_data_accuracy)


# In[ ]:





# Building a Predictive System

# In[34]:


input_data = (21,6.83,22.5,3.3,348)
#change the dtype to np.array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the data as we are predicting the label for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction=model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==1):
    print('Water Quality is Good for Use')
else:
    print('Water Quality is Poor')


# In[ ]:





# In[ ]:





# In[ ]:




