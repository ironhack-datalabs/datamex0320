#!/usr/bin/env python
# coding: utf-8

# # Introduction to Pandas Lab
# 
# Complete the following set of exercises to solidify your knowledge of Pandas fundamentals.

# ### 1. Import Numpy and Pandas and alias them to `np` and `pd` respectively.

# In[1]:


import numpy as np
import pandas as pd


# ### 2. Create a Pandas Series containing the elements of the list below.

# In[2]:


lst = [5.7, 75.2, 74.4, 84.0, 66.5, 66.3, 55.8, 75.7, 29.1, 43.7]


# In[12]:


serie=pd.Series(lst)
print(serie)


# ### 3. Use indexing to return the third value in the Series above.
# 
# *Hint: Remember that indexing begins at 0.*
print(serie[2])
# ### 4. Create a Pandas DataFrame from the list of lists below. Each sublist should be represented as a row.

# In[13]:


b = [[53.1, 95.0, 67.5, 35.0, 78.4],
     [61.3, 40.8, 30.8, 37.8, 87.6],
     [20.6, 73.2, 44.2, 14.6, 91.8],
     [57.4, 0.1, 96.1, 4.2, 69.5],
     [83.6, 20.5, 85.4, 22.8, 35.9],
     [49.0, 69.0, 0.1, 31.8, 89.1],
     [23.3, 40.7, 95.0, 83.8, 26.9],
     [27.6, 26.4, 53.8, 88.8, 68.5],
     [96.6, 96.4, 53.4, 72.4, 50.1],
     [73.7, 39.0, 43.2, 81.6, 34.7]]


# In[53]:


colnames=['col1','col2','col3','col4','col5']
df=pd.DataFrame(b,columns=colnames)
print(df)


# ### 5. Rename the data frame columns based on the names in the list below.

# In[54]:


colnames = ['Score_1', 'Score_2', 'Score_3', 'Score_4', 'Score_5']


# In[55]:


df=df.rename(columns={'col1':'Score_1','col2':'Score_2','col3':'Score_3','col4':'Score_4','col5':'Score_5'})
print(df)


# ### 6. Create a subset of this data frame that contains only the Score 1, 3, and 5 columns.

# In[56]:


sub_df=df[['Score_1','Score_3','Score_5']]
print(sub_df)


# ### 7. From the original data frame, calculate the average Score_3 value.

# In[73]:


print (df['Score_3'].mean())


# ### 8. From the original data frame, calculate the maximum Score_4 value.

# In[63]:


print (df['Score_4'].max())


# ### 9. From the original data frame, calculate the median Score 2 value.

# In[64]:


print (df['Score_4'].median())


# ### 10. Create a Pandas DataFrame from the dictionary of product orders below.

# In[68]:


orders = {'Description': ['LUNCH BAG APPLE DESIGN',
  'SET OF 60 VINTAGE LEAF CAKE CASES ',
  'RIBBON REEL STRIPES DESIGN ',
  'WORLD WAR 2 GLIDERS ASSTD DESIGNS',
  'PLAYING CARDS JUBILEE UNION JACK',
  'POPCORN HOLDER',
  'BOX OF VINTAGE ALPHABET BLOCKS',
  'PARTY BUNTING',
  'JAZZ HEARTS ADDRESS BOOK',
  'SET OF 4 SANTA PLACE SETTINGS'],
 'Quantity': [1, 24, 1, 2880, 2, 7, 1, 4, 10, 48],
 'UnitPrice': [1.65, 0.55, 1.65, 0.18, 1.25, 0.85, 11.95, 4.95, 0.19, 1.25],
 'Revenue': [1.65, 13.2, 1.65, 518.4, 2.5, 5.95, 11.95, 19.8, 1.9, 60.0]}


# In[79]:


orders=pd.DataFrame(orders)
print(orders)


# ### 11. Calculate the total quantity ordered and revenue generated from these orders.

# In[80]:


print(orders['Quantity'].sum())
print(orders['Revenue'].sum())


# ### 12. Obtain the prices of the most expensive and least expensive items ordered and print the difference.

# In[83]:


diff=(orders['UnitPrice'].max())-(orders['UnitPrice'].min())
print(diff)


# In[85]:


orders.rename(columns={'UnitPrice':'Price'})

