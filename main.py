import requests
from bs4 import BeautifulSoup
import csv

def fetch_html(url):
    """Handles network requests and status checking."""
    try:
        response = requests.get(url, timeout=10)
        # Raises an HTTPError if the response was an error (4xx, 5xx)
        response.raise_for_status() 
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def parse_job_data(html_content):
    """Extracts structured data from raw HTML."""
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    job_cards = soup.find_all("div", class_="card-content")
    results = []

    for card in job_cards:
        # Using .get_text(strip=True) is a cleaner BeautifulSoup way to clean text
        job_data = {
            "title": card.find("h2", class_="title").get_text(strip=True),
            "company": card.find("h3", class_="company").get_text(strip=True),
            "location": card.find("p", class_="location").get_text(strip=True),
            "link": card.find("a", string="Apply")["href"]
        }
        results.append(job_data)
    
    return results

def main():
    """Main entry point of the script."""
    url = "https://realpython.github.io/fake-jobs/"
    
    print("Fetching jobs...")
    html = fetch_html(url)
    
    if html:
        jobs = parse_job_data(html)
        print(f"Found {len(jobs)} jobs:\n")
        
        for job in jobs:
            print(f"{job['title']} @ {job['company']}")
            print(f"Location: {job['location']} | Link: {job['link']}")
            print("-" * 30)
        save_to_csv(jobs, "job_listings.csv")

import csv

def save_to_csv(data, filename):
    """Saves a list of dictionaries to a CSV file."""
    if not data:
        print("No data to save.")
        return

    # Extract headers from the first dictionary keys
    headers = data[0].keys()

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            # Create a DictWriter object
            writer = csv.DictWriter(file, fieldnames=headers)
            
            # Write the header row (title, company, etc.)
            writer.writeheader()
            
            # Write all the job rows at once
            writer.writerows(data)
            
        print(f"Successfully saved {len(data)} jobs to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
