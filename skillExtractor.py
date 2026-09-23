#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import json
import time
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# In[2]:


load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPEN_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def Extract_skills_with_groq(jd_text:str , max_retries=3)->list[str]:
    if pd.isna(jd_text) or not  isinstance (jd_text,str) or len(jd_text.strip()) < 10:
        return []
    prompt = f"""
    Extract all specific technical skills, programming languages, databases, 
    and cloud tools from this job description.

    CRITICAL INSTRUCTION: You must respond ONLY with a valid JSON array of strings. 
    Example output: ["Python", "SQL", "Tableau", "AWS"]
    Do not include markdown formatting, conversational text, or explanations.

    Job Description: {jd_text}
    """
    for attempt in range(max_retries):
         try :
            response = client.chat.completions.create(
                 model="openai/gpt-oss-20b",
                 messages=[{"role": "user", "content": prompt}],
                 temperature=0.1,
                )

            raw_text = response.choices[0].message.content.strip()


            if raw_text.startswith("```json"):
                raw_text = raw_text[7:-3].strip()
            elif raw_text.startswith("```"):
                 raw_text = raw_text[3:-3].strip()


            return json.loads(raw_text)


         except Exception as e:
            error_msg = str(e)
            if "429" in error_msg:
                print(f"\n[Rate Limit] Pausing for 30s (Attempt {attempt + 1}/{max_retries})...")
                time.sleep(30)
            else:
                print(f"\nRow error: {e}")
                return []

    return []
if __name__ == "__main__":
    print("Loading Clean Dataset...")
    df  = pd.read_csv("cleaned_jobs.csv")
    print(f"Sending {len(df)} jobs to the AI Agent. This will take a few minutes...")
    tqdm.pandas(desc="Extracting Skills")
    def rate_limited_groq(text):
        skills = Extract_skills_with_groq(text)
        time.sleep(2.1) 
        return skills
    df['extracted_skills'] = df['jd_clean'].progress_apply(rate_limited_groq)
    df.to_csv("jobs_with_skills.csv", index=False)
    print("\nExtraction complete! Enriched dataset saved to jobs_with_skills.csv")


# In[ ]:






# In[ ]:




