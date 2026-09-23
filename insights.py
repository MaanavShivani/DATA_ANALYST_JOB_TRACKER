#!/usr/bin/env python
# coding: utf-8

# In[1]:




# In[19]:


import pandas as pd
import ast
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
df_skills = pd.read_csv("jobs_with_skills.csv")

all_skills = []
for skills_string in df_skills["extracted_skills"]:
    if pd.isna(skills_string):
        continue
    real_list  = ast.literal_eval(skills_string)
    all_skills = real_list + all_skills
skills_counts = Counter(all_skills).most_common(10)


# In[20]:


insights_df = pd.DataFrame(skills_counts)
insights_df.to_csv("Insights",index=False)

# In[ ]:




