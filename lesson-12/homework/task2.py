import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

def save_jobs(job_listings):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    
    for job in job_listings:
        cursor.execute('''insert into jobs (title, company, location, description, application_link) values (?, ?, ?, ?, ?);''', (job["title"], job["company"], job["location"], job["description"], job["application_link"]))
    conn.commit()
    conn.close()

def filter_jobs(location=None, company=None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    
    query = "select * from jobs where true"
    params = []
    
    if location:
        query += " and location=?"
        params.append(location)
    
    if company:
        query += " and company=?"
        params.append(company)
    
    cursor.execute(query, params)
    filtered_jobs = cursor.fetchall()
    
    conn.close()
    return filtered_jobs

def export_to_csv(filtered_jobs, filename="filtered_jobs.csv"):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["title", "company", "location", "description", "application_link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for job in filtered_jobs:
            writer.writerow({
                "title": job[0],
                "company": job[1],
                "location": job[2],
                "description": job[3],
                "application_link": job[4]
            })

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
cursor.execute('''
    create table if not exists jobs (
        title text,
        company text,
        location text,
        description text,
        application_link text,
        primary key (title, company, location));''')
conn.commit()
conn.close()

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

job_listings = []
jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    try:
        description = job.find("div", class_="description").text.strip()
    except:
        description = ""
    application_link = job.find("a", class_="card-footer-item")["href"]
    
    job_listings.append({
        "title": title,
        "company": company,
        "location": location,
        "description": description,
        "application_link": application_link
    })

# print(job_listings)
save_jobs(job_listings)

export_to_csv(filter_jobs(location="Remote"))