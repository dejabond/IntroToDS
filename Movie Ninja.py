
# coding: utf-8

# In[1]:


import pandas as pd


# In[147]:


metadata=pd.read_csv("movie_metadata_with_score_metacritic.csv", index_col="Unnamed: 0")
metadata=metadata.loc[~metadata["metacritic_metascore"].isna()]
metadata=metadata.drop("homepage",1)
metadata=metadata.drop("keywords",1)
metadata=metadata.drop("overview",1)
metadata=metadata.drop("status",1)
metadata=metadata.drop("tagline",1)
metadata=metadata.drop("imdb_metascore",1)
metadata=metadata.drop_duplicates()
#metadata=metadata.loc[metadata.id==2661].replace("Batman","Batman: The Movie")
#metadata=metadata.loc[metadata.id==2661].replace(69.0,71.0)
metadata=metadata.loc[metadata.id!=3647]
metadata

#Normalizing Data for metadata
metadata["budget"]=(metadata["budget"]-metadata["budget"].mean())/metadata["budget"].std()
metadata["popularity"]=(metadata["popularity"]-metadata["popularity"].mean())/metadata["popularity"].std()
metadata["revenue"]=(metadata["revenue"]-metadata["revenue"].mean())/metadata["revenue"].std()
metadata["vote_count"]=(metadata["vote_count"]-metadata["vote_count"].mean())/metadata["vote_count"].std()

# In[131]:


rev_data=pd.read_csv("Revenue.csv")
rev_data["Budget"]=rev_data["Budget($M)"]*1000000
rev_data["Worldwide Gross"]=rev_data["Worldwide Gross($M)"]*1000000
rev_data["Domestic Gross"]=rev_data["Domestic Gross($M)"]*1000000
rev_data=rev_data.drop("Budget($M)",1)
rev_data=rev_data.drop("Domestic Gross($M)",1)
rev_data=rev_data.drop("Worldwide Gross($M)",1)
rev_data=rev_data.rename(columns={"Movie":"title"})
rev_data=rev_data.drop_duplicates()
rev_data.head()

#Normalizing Data for revenue data
rev_data["Budget"]=(rev_data["Budget"]-rev_data["Budget"].mean())/rev_data["Budget"].std()
rev_data["Worldwide Gross"]=(rev_data["Budget"]-rev_data["Worldwide Gross"].min())/(rev_data["Worldwide Gross"].max()-rev_data["Worldwide Gross"].min())
rev_data["Domestic Gross"]=(rev_data["Domestic Gross"]-rev_data["Domestic Gross"].mean())/rev_data["Domestic Gross"].std()


# In[102]:


critic_revenue=metadata.merge(rev_data,on="title")
critic_revenue=critic_revenue.drop_duplicates()
critic_revenue=critic_revenue.loc[(critic_revenue["Worldwide Gross"]!=0) | (critic_revenue["revenue"]!=0)]
critic_revenue


# In[111]:


dup=critic_revenue.loc[critic_revenue.duplicated("title")]
dup


# In[123]:


rev_data.loc[rev_data.duplicated("title")]


# In[141]:


mdc=metadata.copy()
mdc=mdc.loc[metadata.id==2661].replace("Batman","Batman: The Movie")
mdc=mdc.loc[metadata.id==2661].replace(69.0,71.0)
mdc.loc[metadata.id==2661]

