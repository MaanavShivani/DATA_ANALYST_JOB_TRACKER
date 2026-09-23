#!/usr/bin/env python
# coding: utf-8

# In[42]:


import re 
import pandas as pd 
import numpy as np
import ast
def parse_salary(val):
    if pd.isna(val) or not isinstance(val, str) or "not listed" in str(val).lower():
        return pd.Series([np.nan, np.nan, "unspecified"])

    val_lower = val.lower().replace(",", "") # Remove commas immediately

    # Determine the time period
    period = "month" if "/month" in val_lower or "mo" in val_lower else "year"

    # Extract all numbers (including decimals like 1.5)
    raw_numbers = re.findall(r'\d+\.?\d*', val_lower)

    if not raw_numbers:
        return pd.Series([np.nan, np.nan, "unspecified"])

    # Convert strings to floats so we can multiply them
    numbers = [float(n) for n in raw_numbers]

    # Apply multipliers if 'l' (Lakhs) or 'k' (Thousands) is in the string
    multiplier = 1
    if "l" in val_lower or "lpa" in val_lower:
        multiplier = 100000
        period = "year" # Lakhs are almost always yearly
    elif "k" in val_lower:
        multiplier = 1000

    # Multiply and convert back to integers
    final_numbers = [int(n * multiplier) for n in numbers]

    if len(final_numbers) >= 2:
        return pd.Series([final_numbers[0], final_numbers[1], period])
    else:
        return pd.Series([final_numbers[0], final_numbers[0], period])
def clean_jd_text(text):
    if pd.isna(text) or not isinstance(text,str) :
        return ""
    cleaned = re.sub(r'[*#>\t]', ' ', text)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned
def clean_skills(skill_entry):
    if pd.isna(skill_entry):
        return []
    if isinstance(skill_entry, list):
        return [s.strip() for s in skill_entry]

    if isinstance(skill_entry, str):

        if skill_entry.startswith("["):
            try:
                return [s.strip() for s in ast.literal_eval(skill_entry)]
            except (ValueError, SyntaxError):
                return []
        return [s.strip() for s in skill_entry.split(",") if s.strip()]

    return []
def run_cleaning_pipeline(raw_df,source_name,column_mapping) : 
    df = raw_df.rename(columns=column_mapping).copy()
    core_columns = ['title','company','location','salary_raw','skills_raw','jd_raw']
    for col in core_columns:
        if col not in df.columns:
            df[col] = np.nan
    df[['min_salary', 'max_salary', 'salary_period']] = df['salary_raw'].apply(parse_salary)
    df['jd_clean'] = df['jd_raw'].apply(clean_jd_text)
    df['skills_list'] = df['skills_raw'].apply(clean_skills)


    final_columns = [
        'title', 'company', 'location', 
        'min_salary', 'max_salary', 'salary_period', 
        'skills_list', 'jd_clean'
    ]
    df_clean = df[final_columns].copy()
    df_clean['source'] = source_name

    df_clean = df_clean.dropna(subset=['title', 'company'])

    return df_clean  




# In[5]:





# In[43]:


import pandas as pd
raw_linkedin = pd.read_csv("Jobs_list")
raw_internshala = pd.read_csv("Internshala_Jobs_listings")
raw_wellfound = pd.read_csv("wellfoundjobs")
print("LinkedIn Columns:", raw_linkedin.columns.tolist())
print("Wellfound Columns:", raw_wellfound.columns.tolist())
print("Internshala Columns:",raw_internshala.columns.tolist())



# In[44]:


if __name__ == "__main__" :
    raw_linkedin = pd.read_csv("Jobs_list")
    raw_internshala = pd.read_csv("Internshala_Jobs_listings")
    raw_wellfound = pd.read_csv("wellfoundjobs")

    internshala_map = {
        'title': 'title',
        'company': 'company',
        'location': 'location',
        'stipend': 'salary_raw',
        'skills': 'skills_raw',
        'job_description': 'jd_raw'
    }

    linkedin_map = {
        'title': 'title',       
        'company': 'company',
        'location': 'location'

    }

    wellfound_map = {
        'title': 'title',             
        'companyName': 'company',
        'locationNames': 'location',
        'compensation': 'salary_raw',
        'description': 'jd_raw'
    }
    df_in = run_cleaning_pipeline(raw_internshala, "Internshala", internshala_map)
    df_li = run_cleaning_pipeline(raw_linkedin, "LinkedIn", linkedin_map)
    df_we = run_cleaning_pipeline(raw_wellfound, "Wellfound", wellfound_map)


    master_df = pd.concat([df_in, df_li, df_we], ignore_index=True)
    master_df.to_csv("cleaned_jobs.csv", index=False)


# In[ ]:





# In[ ]:




