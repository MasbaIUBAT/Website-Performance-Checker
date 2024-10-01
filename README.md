Website Performance Checker
This Python script is designed to evaluate various aspects of website performance, including content loading, loading speed, SSL validation, mobile responsiveness, and page size. It utilizes libraries such as requests, BeautifulSoup, and Selenium to perform these checks.

Features
Check Website Content: Verifies if images and content are loading correctly, including SEO checks for meta descriptions and title tags.
Check Loading Speed: Measures the time taken to load a website.
SSL/TLS Validation: Checks if the SSL certificate is valid and if the site is served over HTTPS.
Mobile Responsiveness: Tests the website's responsiveness on various screen sizes using Selenium.
Page Size Check: Evaluates the size of the webpage and alerts if it exceeds a specified limit.
Prerequisites
To run this script, you will need to have the following installed:

Python 3.x
Chrome WebDriver (for Selenium)
Required Python packages
You can install the required packages using pip:

bash
Copy code
pip install requests beautifulsoup4 selenium
Usage
Clone this repository or download the script.
Update the list of websites to check in the websites variable.
Run the script using Python:
bash
Copy code
python website_checker.py
Code Overview
Importing Required Libraries
python
Copy code
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
Function Definitions
check_website_content(url)
Checks if images and content are loading correctly and verifies SEO metadata.

Parameters:
url: The website URL to check.
check_loading_speed(url)
Measures the loading speed of the website.

Parameters:
url: The website URL to check.
check_ssl(url)
Validates the SSL/TLS certificate of the website.

Parameters:
url: The website URL to check.
check_mobile_responsiveness(url)
Tests the website's mobile responsiveness using different screen sizes.

Parameters:
url: The website URL to check.
check_page_size(url, size_limit_kb=500)
Checks the size of the webpage and alerts if it exceeds the specified limit.

Parameters:
url: The website URL to check.
size_limit_kb: The maximum allowed page size in kilobytes (default is 500 KB).
Example Usage
Define the websites you want to check in the websites list:

python
Copy code
websites = [
    "https://cems-solarexpo.com",
    "https://cems-apparelsourcing.com"
]
Then, perform checks:

python
Copy code
for site in websites:
    print(f"\nChecking {site}...")
    check_website_content(site)
    check_loading_speed(site)
    check_ssl(site)
    check_mobile_responsiveness(site)
    check_page_size(site, size_limit_kb=300)  # Change limit as needed
Notes
Ensure that the Chrome WebDriver is compatible with your installed version of Chrome.
This script requires internet access to function as it checks live websites.
Depending on the website, some checks (like loading speed) may vary based on network conditions.
License
This project is licensed under the Masba Uddin Rumi.
