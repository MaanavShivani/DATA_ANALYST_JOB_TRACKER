#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import json
def market_jobs_metrics(csv_path):
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("Error... Cleaned data not found. Run Cleaner.py again")
        return
    total_jobs = len(df)
    jobs_by_source = df['source'].value_counts().to_dict()
    top_location = df['location'].dropna().value_counts().head(5).to_dict()
    monthly_roles = df[df['salary_period']=='month']
    if not monthly_roles.empty:
        avg_minimum_salary = monthly_roles['min_salary'].mean()
        avg_maximum_salary = monthly_roles['max_salary'].mean()
    else :
        avg_minimum_salary = 0
        avg_maximum_salary = 0

    kpi_report = {
        "Number_of_jobs" : total_jobs,
        "Jobs_source" : jobs_by_source,
        "Primary_loctions" : top_location,
        "Average_minimum_salary" : round(avg_minimum_salary,2),
        "Average_maximum_salary" : round(avg_maximum_salary,2)
        }
    return kpi_report
if __name__ == "__main__":
    clean_report_path = "cleaned_jobs.csv"
    report = market_jobs_metrics(clean_report_path)
    print("\n--- DATA ANALYST MARKET KPIs ---")
    for metric, value in report.items():
        print(f"{metric}: {value}")

    with open("market_kpis.json", "w") as outfile:
        json.dump(report, outfile, indent=4)
    print("\nKPIs successfully saved to market_kpis.json")


# In[ ]:




