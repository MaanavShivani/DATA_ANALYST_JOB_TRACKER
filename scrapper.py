#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import pandas as pd
cookies = {
    'JSESSIONID': 'ajax:3574243995651069435',
    'lang': 'v=2&lang=en-us',
    'bcookie': '"v=2&bc06a5af-9803-4e57-8f11-3d81d2b38bb9"',
    'bscookie': '"v=1&20260907205206c9f94768-309b-44aa-88f4-fe734561b5a3AQF5Yex4_u0FEMnfhDaKp5sQhUTIRgkI"',
    'lidc': '"b=OGST04:s=O:r=O:a=O:p=O:g=3807:u=1:x=1:i=1788814326:t=1788900726:v=2:sig=AQHyToyMs4mVa3lOuTH-TFh2AE5T7vUk"',
    '__cf_bm': 'XzJ0ZRtlolWu_Bd6g.AWZdAvB.B6UkKyKdH6QmPV1zs-1788814326.0362325-1.0.1.1-cilVZl8OEwaeMPY3h0_WyvuXJZ9drPfr2g3TLnlrBUq2kyp9LHUxybdx.6shF_tInT3RZnKmV82LW5JNYBMOW8paRjuAdkaFspNMxdK5K9e4w3fHm2NAsSHF7H9FOGyv',
    'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
    'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C20704%7CMCMID%7C59470144022049390343870032161878345426%7CMCAAMLH-1789419125%7C12%7CMCAAMB-1789419125%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1788821525s%7CNONE%7CvVersion%7C5.1.1',
    'aam_uuid': '59287483039138613293853447971721606425',
    '_gcl_au': '1.1.210455125.1788814326',
    '_uetsid': 'fc1ad4c0aafd11f1b972234ffa1f07ef',
    '_uetvid': 'fc1b1520aafd11f185b7e39b19f049d5',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8',
    'csrf-token': 'ajax:3574243995651069435',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://in.linkedin.com/jobs/search?keywords=DATA%20ANALYST&location=New%20Delhi%2C%20Delhi%2C%20India&geoId=115918471&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
    'sec-ch-ua': '"Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36',
    # 'cookie': 'JSESSIONID=ajax:3574243995651069435; lang=v=2&lang=en-us; bcookie="v=2&bc06a5af-9803-4e57-8f11-3d81d2b38bb9"; bscookie="v=1&20260907205206c9f94768-309b-44aa-88f4-fe734561b5a3AQF5Yex4_u0FEMnfhDaKp5sQhUTIRgkI"; lidc="b=OGST04:s=O:r=O:a=O:p=O:g=3807:u=1:x=1:i=1788814326:t=1788900726:v=2:sig=AQHyToyMs4mVa3lOuTH-TFh2AE5T7vUk"; __cf_bm=XzJ0ZRtlolWu_Bd6g.AWZdAvB.B6UkKyKdH6QmPV1zs-1788814326.0362325-1.0.1.1-cilVZl8OEwaeMPY3h0_WyvuXJZ9drPfr2g3TLnlrBUq2kyp9LHUxybdx.6shF_tInT3RZnKmV82LW5JNYBMOW8paRjuAdkaFspNMxdK5K9e4w3fHm2NAsSHF7H9FOGyv; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C20704%7CMCMID%7C59470144022049390343870032161878345426%7CMCAAMLH-1789419125%7C12%7CMCAAMB-1789419125%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1788821525s%7CNONE%7CvVersion%7C5.1.1; aam_uuid=59287483039138613293853447971721606425; _gcl_au=1.1.210455125.1788814326; _uetsid=fc1ad4c0aafd11f1b972234ffa1f07ef; _uetvid=fc1b1520aafd11f185b7e39b19f049d5',
}

params = {
    'keywords': 'DATA+ANALYST',
    'location': 'New+Delhi,+Delhi,+India',
    'geoId': '115918471',
    'trk': 'public_jobs_jobs-search-bar_search-submit',
    'start': '175',
}


jobPostingList = []
for start_num in [0,25,50]:
     params = {
         "keywords" : "Data Analyst",
         "location" : "India",
         "start"    : str(start_num)

     }
     response  = requests.get(
         "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search",
         params=params,
         headers=headers
     )
     soup = BeautifulSoup(response.text,"html.parser")
     jobcards = soup.find_all("li")

     for job in jobcards:
         try : 
             title = job.find("h3",class_="base-search-card__title").text.strip()
             company = job.find("h4",class_ = "base-search-card__subtitle").text.strip()

             location_tag  = job.find("span",class_="job-search-card__location")
             location = location_tag.text.strip() if location_tag else "Not_listed"


             jobPostingList.append({
                 "title":title,
                 "company" : company,
                 "location" : location

             })
         except AttributeError :
             continue

   


# In[18]:


df_Linkedin= pd.DataFrame(jobPostingList)


# In[19]:


df_Linkedin.to_csv('Jobs_list',index= False)


# In[3]:


from apify_client import ApifyClient
load_dotenv(override=True)
apify_token = os.getenv("ApifyTOken")
print(f"DEBUG: Token being sent is {len(str(apify_token))} characters long.")
# In[7]:


client = ApifyClient(apify_token)
run_input = {
    "jobCategory": "Data Science", # Must match Internshala's exact category names
    "location": "Delhi",           # Must be a string, NO brackets!
    "workFromHome": False,
    "maxResults": 50
}
print("Scraping Internshala ... This might take a minute.")
run = client.actor("blackfalcondata/internshala-scraper").call(run_input=run_input)
Internshala_jobs = []
for item in client.dataset(run.default_dataset_id).iterate_items(): 
    Internshala_jobs.append(item)
df_Internshala = pd.DataFrame(Internshala_jobs)
print(f"Successfully scraped {len(df_Internshala)} jobs!")



# In[11]:


client = ApifyClient(apify_token)
run_input = {
    "roles":["Data-Analyst"],
    "locations"   : ["India"],
    "maxItems":50
}
print("Scraping Wellfound (AngelList)... This might take a minute.")
run = client.actor("scrapersdelight/wellfound-jobs-scraper").call(run_input=run_input)
wellfound_jobs = []
for item in client.dataset(run.default_dataset_id).iterate_items(): 
    wellfound_jobs.append(item)
df_wellfound = pd.DataFrame(wellfound_jobs)
print(f"Successfully scraped {len(df_wellfound)} jobs!")



# In[21]:


df_Internshala.to_csv("Internshala_Jobs_listings",index=False)


# In[22]:


df_wellfound.to_csv("wellfoundjobs",index = False)


# In[23]:





# In[ ]:




