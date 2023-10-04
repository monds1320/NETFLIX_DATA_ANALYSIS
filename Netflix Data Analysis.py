#!/usr/bin/env python
# coding: utf-8

# #                                           NETFLIX DATA SET

# In[1]:


# Importing the dataset
import pandas as pd
data = pd.read_csv("Netflix Dataset.csv")


# In[2]:


data


# # Getting some basic information about the dataset

# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.shape


# In[6]:


data.size


# In[7]:


data.columns


# In[8]:


data.dtypes                              #to show the data typoe of each columns


# In[9]:


data.info()


# # TASK 1. Is there any Duplicate Record in this dataset ? if yes, then remove the duplicate records. 

# In[10]:


data.head()


# In[11]:


data[data.duplicated()]


# In[12]:


data.drop_duplicates(inplace=True)                     #inplace=True is for permanent drop


# In[13]:


data[data.duplicated()]


# In[14]:


data.shape


# # TASK 2. Is there any null value present in any column? show with Heat-Map 

# In[15]:


data.isnull()


# In[16]:


data.isnull().sum()


# In[17]:


import seaborn as sns


# In[18]:


sns.heatmap(data.isnull())


# In[ ]:





# In[ ]:





# # Q.1. For "house of cards",what is show id and who is the director of this show?

# In[19]:


data.head()


# In[20]:


data[data['Title'].isin(['House of Cards'])]                           #  To show all records of particular items in any column


# # Q.2. In which year highest number of the TV Shows & Movies were released? Show with Bar Graph

# In[21]:


data.dtypes


# In[22]:


data['Data_N'] = pd.to_datetime(data['Release_Date'])


# In[23]:


data.head()


# In[24]:


data['Data_N'].dt.year.value_counts()


# In[25]:


data['Data_N'].dt.year.value_counts().plot(kind='bar')


# # Q.3. How many Movies & TV Shows are in the dataset? Show with bar graph.

# In[26]:


data.head(2)


# In[27]:


data.groupby('Category').Category.count()


# In[28]:


sns.countplot(data['Category'])                    #to show the count of all unique values of any coulumn in form of bar graph


# # Q.4 Show all the TV Show that were released in year 2020

# In[29]:


data.head(2)


# In[30]:


data['Year'] = data['Data_N'].dt.year            # creating new coulumn " year"


# In[31]:


data.head()


# # FILTERING

# In[32]:


data [(data['Category'] == 'TV Show') & (data['Year']==2020)]


# # Q.5. Show only the Directors of all the TV shows that were released in INDIA only

# In[33]:


data.head()


# In[34]:


data [(data['Category'] == 'TV Show') & (data['Country']=='India')] ['Director'] 


# # Q.6. Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix

# In[35]:


data['Director'].value_counts().head(10)


# In[36]:


data['Director'].value_counts().head(10)


# # Q.7. Show all the Record,where "Category" is Movie and Type is Comedies or "Country is United Kingdom" .

# # Filtering (And,Or Operators)

# In[37]:


data.head(2)


# In[38]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies')]


# In[39]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# # Q.8. In how many movies/shows,Tom Cruise was cast ?

# In[40]:


data.head()


# In[41]:


data[data['Cast']=='Tom Cruise']


# In[42]:


data_new = data.dropna()                   # remove the null values


# In[43]:


data_new.head(2)


# In[44]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# # Q.9.What are the different Rating defined by Netflix?

# In[45]:


data.head(2)


# In[46]:


data.Rating.nunique()


# In[47]:


data['Rating'].nunique


# # Q.9.1. How many Movies got the 'TV-14'rating,In Canada? 

# In[48]:


data.head(2)


# In[49]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14')].shape


# In[50]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')]


# In[51]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')].shape


# # Q.9.2.How many TV Shows got the 'R' rating after year 2018?

# In[52]:


data[(data['Category']=='TV Show') & (data['Rating'] == 'R')]


# In[53]:


data[(data['Category']=='TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018 )]


# # Q.10.What is the Maximum duration of Movie Show in netflix?

# In[54]:


data.Duration.unique()


# In[55]:


data.Duration.dtype


# In[56]:


data[['Minutes','Unit']] = data['Duration'].str.split(' ',expand=True)


# In[57]:


data.head(2)


# In[58]:


data.Minutes.max()


# In[59]:


data.Minutes.min()


# # Q.11. Which individual country has the Highest No. OF TV shows?

# In[60]:


data.head(2)


# In[62]:


data_tvshow = data[data['Category']=='TV Show']


# In[63]:


data_tvshow.head(2)


# In[66]:


data_tvshow.Country.value_counts()


# In[67]:


data_tvshow.Country.value_counts().head(1)


# # Q.12. How can we sort the dataset by Year?

# In[68]:


data.head(2)


# In[73]:


data.sort_values(by = 'Year')


# In[74]:


data.sort_values(by = 'Year').head(2)


# In[77]:


data.sort_values(by = 'Year',ascending=False)


# In[78]:


data.sort_values(by = 'Year',ascending=False).head(2)


# # Q.13. Find all the instances where n:
#     
#    # Category is 'Movie' and Type is 'Dramas'
#    # or
#   # Category is 'TV Show' and Type is "TV Comedies"
#     

# In[92]:


data[(data['Category']=='Movie') & (data['Type'] == 'Dramas')].head(2)


# In[98]:


data[ (data['Category']=='TV Show') & (data['Type'] == "TV Comedies" )]


# In[99]:


data[(data['Category']=='Movie') & (data['Type'] == 'Dramas') | (data['Category']=='TV Show') & (data['Type'] == "TV Comedies" )]


# 
# 
# 
# 
# 
# # Written by TANMAY MONDAL
