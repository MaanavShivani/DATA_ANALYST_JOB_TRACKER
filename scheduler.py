#!/usr/bin/env python
# coding: utf-8

# In[20]:


import time
import schedule
import subprocess


# In[ ]:


def run_pipeline():
    print("starting automated job market pipline")
    subprocess.run(["python","scrapper.py"],check = True)
    subprocess.run(["python","cleaner.py"],check=True)
    subprocess.run(["python","KpiMetrics.py"],check = True)
    subprocess.run(["python","skillExtractor.py"],check = True)
    subprocess.run(["python","insights.py"] , check = True)
    print("pipeline Complete output files updated")
schedule.every().monday.at("06:00").do(run_pipeline)

if __name__ == "__main__":
    print("Scheduler running. Waiting for next execution window...")
    while True:
        schedule.run_pending()
        time.sleep(60)


# In[23]:





# In[ ]:




