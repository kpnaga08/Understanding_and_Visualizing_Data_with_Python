
# coding: utf-8

# ## Unit Testing
# While we will not cover the [unit testing library](https://docs.python.org/3/library/unittest.html) that python has, we wanted to introduce you to a simple way that you can test your code.
# 
# Unit testing is important because it the only way you can be sure that your code is do what you think it is doing. 
# 
# Remember, just because ther are no errors does not mean your code is correct.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as plt
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe


# In[2]:


# Download NHANES 2015-2016 data
df = pd.read_csv("nhanes_2015_2016.csv")
df.index = range(1,df.shape[0]+1)


# In[3]:


df.head()


# ### Goal
# We want to find the mean of first 100 rows of 'BPXSY1' when 'RIDAGEYR' > 60

# In[4]:


# One possible way of doing this is:
pd.Series.mean(df[df.RIDAGEYR > 60].loc[range(0,100), 'BPXSY1']) 
# Current version of python will include this warning, older versions will not


# In[5]:


# test our code on only ten rows so we can easily check
test = pd.DataFrame({'col1': np.repeat([3,1],5), 'col2': range(3,13)}, index=range(1,11))
test


# In[6]:


# pd.Series.mean(df[df.RIDAGEYR > 60].loc[range(0,5), 'BPXSY1'])
# should return 5

pd.Series.mean(test[test.col1 > 2].loc[range(0,5), 'col2'])


# What went wrong?

# In[7]:


test[test.col1 > 2].loc[range(0,5), 'col2']
# 0 is not in the row index labels because the second row's value is < 2. For now, pandas defaults to filling this
# with NaN


# In[8]:


# Using the .iloc method instead, we are correctly choosing the first 5 rows, regardless of their row labels
test[test.col1 >2].iloc[range(0,5), 1]


# In[9]:


pd.Series.mean(test[test.col1 >2].iloc[range(0,5), 1])


# In[10]:


# We can compare what our real dataframe looks like with the incorrect and correct methods
df[df.RIDAGEYR > 60].loc[range(0,5), :] # Filled with NaN whenever a row label does not meet the condition


# In[11]:


df[df.RIDAGEYR > 60].iloc[range(0,5), :] # Correct picks the first fice rows such that 'RIDAGEYR" > 60


# In[12]:


# Applying the correct method to the original question about BPXSY1
print(pd.Series.mean(df[df.RIDAGEYR > 60].iloc[range(0,100), 16]))

# Another way to reference the BPXSY1 variable
print(pd.Series.mean(df[df.RIDAGEYR > 60].iloc[range(0,100), df.columns.get_loc('BPXSY1')]))

