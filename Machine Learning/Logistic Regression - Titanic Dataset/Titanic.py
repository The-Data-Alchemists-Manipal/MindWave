#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv('titanic_train.csv')


# # Exploratory Data Analysis

# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull()


# In[7]:


df.isnull().sum()


# In[8]:


sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')


# Every yellow dash stands for a true point where true it was NULL.

# In[9]:


sns.set_style('whitegrid')


# In[10]:


sns.countplot(x='Survived', data = df)


# In[11]:


sns.countplot(x='Survived', hue='Sex', data = df)


# - People who did not survive -> much more likely to be MALE
# - People who did survive -> twice as likely to be FEMALE

# In[12]:


sns.countplot(x='Survived', hue='Pclass', data = df)


# - People who did not survive -> most probably the class 3.
# - People who did survive -> leaning a little more towards the higher classes

# In[13]:


sns.histplot(df['Age'].dropna(), kde=False, bins=30)


# In[14]:


df['Age'].plot.hist(bins = 30)


# In[15]:


sns.countplot(x='SibSp', data = df)


# In[16]:


df['Fare'].hist()


# In[17]:


df['Fare'].hist(bins=40, figsize=(10,4))


# Things are distributed towards the cheaper fare tickets as we have already seen most passengers are actually in the cheaper third class.

# In[18]:


import cufflinks as cf
cf.go_offline()

df['Fare'].iplot(kind='hist', bins=40)


# # Data Preprocessing

# In[19]:


plt.figure(figsize=(10, 7))
sns.boxplot(x='Pclass', y='Age', data = df)


# When we separate by class, the wealthier passengers in the first class and second class tend to actually be a bit older than passengers in the third class.

# In[20]:


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age


# In[21]:


df['Age'] = df[['Age', 'Pclass']].apply(impute_age, axis=1)


# We impute data in **Age** to have **zero NaN values.**

# In[22]:


sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')


# We are no longer having any missing info for the age column.<br>
# We successfully put in values that were reasonable guesses for people's age based off of their class

# In[23]:


df.drop('Cabin', axis=1, inplace = True)


# In[24]:


df.head()


# In[25]:


df.dropna(inplace = True)


# ### Categorical feature -> Dummy variables

# To deal of categorical features, we'll need to convert categorical features into **dummy variables using pandas.**
# 
# Otherwise our machine learning algorithm won't be able to directly take in those features as inputs.

# In[26]:


pd.get_dummies(df['Sex'])


# Now there's one slight issue that one column here is a perfect predictor of the other column, meaning if our machine learning algorithm gets fed both columns the machine learning algorithm will immediately know that if it's zero female it can predict perfectly that it's going to be one male.
# 
# And this is going to be an issue known as **multi-collinearity** and it basically will mess up the algorithm because a bunch of calls will be perfect predictors of another column.
# 
# To avoid this, we add another argument **drop_first**

# In[27]:


sex = pd.get_dummies(df['Sex'], drop_first=True)


# In[28]:


sex.head()


# In[29]:


embark = pd.get_dummies(df['Embarked'], drop_first=True)


# In[30]:


embark.head()


# In[31]:


df = pd.concat([df, sex, embark], axis = 1)


# In[32]:


df.head()


# In[33]:


df.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)


# In[34]:


df.head()


# In[35]:


df.tail()


# In[36]:


df.drop('PassengerId', axis=1, inplace=True)


# In[37]:


df.head()


# # Training the Model

# In[38]:


X = df.drop('Survived', axis=1)
Y = df['Survived']


# In[39]:


from sklearn.linear_model import LogisticRegression


# In[40]:


logmodel = LogisticRegression()


# In[41]:


logmodel.fit(X, Y)


# ![image.png](attachment:image.png)
# ![image-2.png](attachment:image-2.png)

# In[42]:


logmodel = LogisticRegression(solver = 'lbfgs', max_iter = 200)


# In[43]:


logmodel.fit(X, Y)


# # Testing the Model

# In[44]:


test = pd.read_csv('titanic_test.csv')


# In[45]:


test.head()


# In[46]:


test.isnull().sum()


# **We will have to pre-process the Test Data first!**

# In[47]:


test['Age'] = test[['Age', 'Pclass']].apply(impute_age, axis=1)


# In[48]:


test.drop('Cabin', axis=1, inplace = True)


# In[49]:


sex = pd.get_dummies(test['Sex'], drop_first=True)


# In[50]:


embark = pd.get_dummies(test['Embarked'], drop_first=True)


# In[51]:


test = pd.concat([test, sex, embark], axis = 1)


# In[52]:


test.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)


# In[53]:


test.drop('PassengerId', axis=1, inplace=True)


# In[54]:


test.isnull().sum()


# In[55]:


test.head()


# In[56]:


test.dropna(axis=0, how='any', inplace=True)


# - **axis:** axis takes int or string value for rows/columns. Input can be 0 or 1 for Integer and ‘index’ or ‘columns’ for String.
# - **how:** how takes string value of two kinds only (‘any’ or ‘all’). **‘any’ drops the row/column if ANY value is Null and ‘all’ drops only if ALL values are null.**
# - **thresh:** thresh takes integer value which tells **minimum amount of na values to drop.**
# - **subset:** It’s an array which **limits the dropping process to passed rows/columns through list.**
# - **inplace:** It is a boolean which **makes the changes in data frame itself if True.**

# In[57]:


logmodel.predict(test)


# In[ ]:




