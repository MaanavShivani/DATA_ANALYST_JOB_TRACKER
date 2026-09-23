📊 Data Analyst Market Tracker (Automated ETL Pipeline)
An automated End-to-End Data Engineering and Analytics pipeline designed to track, aggregate, and analyze Data Analyst job market trends across major hiring platforms.
This project programmatically scrapes live job listings, cleans the data, uses Large Language Models (LLMs) to extract required technical skills from unstructured descriptions, and generates automated visual dashboards to track market demands.
🛠️ Tech Stack & Tools
Language: Python 3
Data Extraction: Apify API (Web Scraping)
Data Transformation: Pandas, NumPy
AI & Enrichment: Groq API (llama-3.1-8b-instant)
Data Visualization: Matplotlib, Seaborn
Automation: schedule library
Version Control & Security: Git, GitHub, python-dotenv
⚙️ Architecture & Workflow
Extraction (scrapper.py): Interfaces with the Apify API to extract live job listings from Internshala, Wellfound, and LinkedIn.
Transformation (cleaner.py): Cleans and standardizes raw CSV data using Pandas, handling missing values, encoding issues, and formatting.
AI Skill Matching (skillExtractor.py): Passes unstructured job descriptions to Groq's LLM to dynamically parse and identify core technical skills (e.g., SQL, Python, Tableau).
KPI Generation (KpiMetrics.py & insights.py): Calculates market trends, aggregates top skills, and generates static HTML reports and visual charts.
Automation (scheduler.py): Orchestrates the entire pipeline to run unattended on a scheduled basis, ensuring data and dashboards remain constantly updated.
