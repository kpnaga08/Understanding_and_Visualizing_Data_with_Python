
# coding: utf-8

# In this assignment we'll ask you to plot multiple variables.   
# 
# You will use what you find in this assignment to answer the questions in the quiz that follows. It may be useful to keep this notebook side-by-side with this week's quiz on your screen.

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 100)

path = "Cartwheeldata.csv"


# In[2]:


# First, you must import the cartwheel data from the path given above
df = pd.read_csv("Cartwheeldata.csv")# using pandas, read in the csv data found at the url defined by 'path'


# In[3]:


# Next, look at the 'head' of our DataFrame 'df'. 
df.head()


# If you can't remember a function, open a previous notebook or video as a reference, or use your favorite search engine to look for a solution.

# ## Scatter plots

# First, let's looks at two variables that we expect to have a strong relationship, 'Height' and 'Wingspan'.

# In[6]:


# Make a Seaborn scatter plot with x = height and y = wingspan using sns.scatterplot(x, y)
sns.regplot(x="Height", y="Wingspan", data=df, fit_reg=False, scatter_kws={"alpha": 0.5})


# How would you describe the relationship between 'Height' and 'Wingspan'?   
# Questions you can ask:
# * Is it linear?
# * Are there outliers?
# * Are their ranges similar or different?  
# 
# How else could you describe the relationship?

# Now let's look at two variables that we don't yet assume have a strong relationship, 'Wingspan' and 'CWDistance'

# In[9]:


# Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance
sns.regplot(x="Wingspan", y="CWDistance", data=df, fit_reg=False, scatter_kws={"alpha": 0.8})


# How would you describe the relationship between 'Wingspan' and 'CWDistance'?   
# * Is it linear?
# * Are there outliers?
# * Are their ranges similar or different?  
# 
# How else could you describe the relationship?

# Let makes the same plot as above, but now include 'Gender' as the color scheme by including the argument
# ```
# hue=df['Gender']
# ```
# in the Seaborn function

# In[22]:


# Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance, and hue = gender
df["hue"] = df.Gender.replace({"M": "Male", "F": "Female"}) 
sns.FacetGrid(df, col="hue").map(plt.scatter, "Wingspan", "CWDistance", alpha=0.8).add_legend()


# Does does this new information on the plot change your interpretation of the relationship between 'Wingspan' and 'CWDistance'?

# ## Barcharts
# Now lets plot barplots of 'Glasses'

# In[24]:


# Make a Seaborn barplot with x = glasses and y = cartwheel distance
sns.barplot(data=df, x="Glasses", y="CWDistance")


# What can you say about the relationship of 'Glasses' and 'CWDistance'?

# In[25]:


# Make the same Seaborn boxplot as above, but include gender for the hue argument
sns.barplot(data=df, x="Glasses", y="CWDistance", hue="Gender")


# How does this new plot change your interpretation about the relationship of 'Glasses' and 'CWDistance'?
