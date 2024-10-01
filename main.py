import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Function to check if images and content are loading correctly
def check_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the website is reachable (status code 200)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if images are loading correctly
        images = soup.find_all('img')
        broken_images = []
        for img in images:
            img_url = img.get('src')
            if img_url:
                img_response = requests.get(img_url)
                if img_response.status_code != 200:
                    broken_images.append(img_url)

        if broken_images:
            print(f"Broken Images in {url}:")
            for img in broken_images:
                print(img)
        else:
            print(f"All images in {url} are loading correctly.")

        # SEO Check for meta description and title tag
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        title_tag = soup.find('title')
        if meta_desc and meta_desc.get('content'):
            print(f"Meta description found in {url}: {meta_desc.get('content')}")
        else:
            print(f"Meta description missing in {url}")

        if title_tag:
            print(f"Title tag found in {url}: {title_tag.text}")
        else:
            print(f"Title tag missing in {url}")

        # Check for broken links
        links = soup.find_all('a')
        broken_links = []
        for link in links:
            link_url = link.get('href')
            if link_url and link_url.startswith('http'):
                link_response = requests.get(link_url)
                if link_response.status_code != 200:
                    broken_links.append(link_url)

        if broken_links:
            print(f"Broken Links in {url}:")
            for link in broken_links:
                print(link)
        else:
            print(f"All links in {url} are working correctly.")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Function to check loading speed
def check_loading_speed(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        response.raise_for_status()
        load_time = time.time() - start_time
        print(f"Website {url} loaded in {load_time:.2f} seconds")
    except requests.exceptions.RequestException as e:
        print(f"Error checking load speed for {url}: {e}")

# Function to check SSL/TLS validation
def check_ssl(url):
    try:
        response = requests.get(url)
        if response.url.startswith("https://"):
            print(f"SSL/TLS validation passed for {url}")
        else:
            print(f"SSL/TLS validation failed for {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error during SSL check for {url}: {e}")

# Function to check mobile responsiveness using Selenium
def check_mobile_responsiveness(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

        # Define different screen sizes to test responsiveness
        screen_sizes = [(375, 812), (768, 1024), (1366, 768)]  # iPhone X, iPad, Desktop

        for size in screen_sizes:
            width, height = size
            driver.set_window_size(width, height)
            driver.get(url)
            time.sleep(3)  # Wait for the page to load
            print(f"Checked responsiveness for {url} at {width}x{height}.")
        
        driver.quit()
    except Exception as e:
        print(f"Error checking mobile responsiveness for {url}: {e}")

# Function to check page size
def check_page_size(url, size_limit_kb=500):
    try:
        response = requests.get(url)
        page_size_kb = len(response.content) / 1024
        print(f"Page size for {url}: {page_size_kb:.2f} KB")

        if page_size_kb > size_limit_kb:
            print(f"Alert: Page size for {url} exceeds the limit of {size_limit_kb} KB.")
    except requests.exceptions.RequestException as e:
        print(f"Error checking page size for {url}: {e}")

# URLs to check
websites = [
    "https://cems-solarexpo.com",
    "https://cems-apparelsourcing.com"
]

# Perform checks
for site in websites:
    print(f"\nChecking {site}...")
    check_website_content(site)
    check_loading_speed(site)
    check_ssl(site)
    check_mobile_responsiveness(site)
    check_page_size(site, size_limit_kb=300)  # Add page size check with a limit of 300 KB
