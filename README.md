# Fake-Jobs Web Scraper 🕷️

A robust Python-based web scraper that extracts job listings from the [Real Python Fake Jobs](https://realpython.github.io) site. This tool parses HTML content, extracts job details, and exports them into a structured CSV file.

## 🚀 Features
- **Network Resilience:** Uses `requests` with status checking and error handling.
- **Clean Parsing:** Leverages `BeautifulSoup4` for precise DOM navigation and data cleaning.
- **Data Export:** Automatically generates a `job_listings.csv` for data analysis.
- **Professional Structure:** Modularized code with specific functions for fetching, parsing, and saving.

## 🛠️ Prerequisites
- Python 3.6+
- [Requests](https://requests.readthedocs.io)
- [BeautifulSoup4](https://www.crummy.com)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd fake-jobs-scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install requests beautifulsoup4
   ```

**Usage**
   Run the script from your terminal:
   ```bash
   python scraper.py
   ```

**Upon completion, you will find a file named ***job_listings.csv*** in your project directory containing the:**
* Job Title
* Company Name
* Location
* Application Link

**🏗️ Project Structure**
- scraper.py: The main script containing the fetching, parsing, and saving logic.
- job_listings.csv: The output file generated after running the script.

**📜 License**
This project is open-source and available under the MIT License.
