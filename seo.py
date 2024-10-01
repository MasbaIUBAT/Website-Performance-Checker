import requests
from bs4 import BeautifulSoup

def check_seo(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        seo_report = {
            "Title Tag": None,
            "Meta Description": None,
            "H1 Tag": None,
            "Missing Alt Texts": [],
            "Canonical Link": None,
            "Robots.txt": None,
            "Sitemap.xml": None,
            "Open Graph Tags": [],
            "Twitter Card Tags": [],
            "Viewport Tag": None,
            "HTTP Status Code": response.status_code
        }

        # Check title tag
        title_tag = soup.find('title')
        seo_report["Title Tag"] = title_tag.text if title_tag and title_tag.text else "Missing"

        # Check meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        seo_report["Meta Description"] = meta_desc['content'] if meta_desc and meta_desc.get('content') else "Missing"

        # Check H1 tag
        h1_tag = soup.find('h1')
        seo_report["H1 Tag"] = h1_tag.text if h1_tag and h1_tag.text else "Missing"

        # Check for images and their alt attributes
        images = soup.find_all('img')
        for img in images:
            alt_text = img.get('alt')
            if not alt_text:
                seo_report["Missing Alt Texts"].append(img.get('src'))

        # Check for canonical link
        canonical_link = soup.find('link', attrs={'rel': 'canonical'})
        seo_report["Canonical Link"] = canonical_link['href'] if canonical_link and canonical_link.get('href') else "Missing"

        # Check for Open Graph tags
        og_tags = soup.find_all('meta', attrs={'property': 'og:title'})
        if og_tags:
            for tag in og_tags:
                seo_report["Open Graph Tags"].append(tag['content'])

        # Check for Twitter Card tags
        twitter_tags = soup.find_all('meta', attrs={'name': 'twitter:card'})
        if twitter_tags:
            for tag in twitter_tags:
                seo_report["Twitter Card Tags"].append(tag['content'])

        # Check for viewport tag
        viewport_tag = soup.find('meta', attrs={'name': 'viewport'})
        seo_report["Viewport Tag"] = "Present" if viewport_tag else "Missing"

        # Check robots.txt link
        robots_link = url + "/robots.txt"
        try:
            robots_response = requests.get(robots_link)
            robots_response.raise_for_status()  # Ensure the request was successful
            seo_report["Robots.txt"] = "Accessible"
        except requests.exceptions.RequestException:
            seo_report["Robots.txt"] = "Not Accessible"

        # Check for sitemap.xml link
        sitemap_link = url + "/sitemap.xml"
        try:
            sitemap_response = requests.get(sitemap_link)
            sitemap_response.raise_for_status()  # Ensure the request was successful
            seo_report["Sitemap.xml"] = "Accessible"
        except requests.exceptions.RequestException:
            seo_report["Sitemap.xml"] = "Not Accessible"

        # Print the SEO report
        print(f"\nSEO Report for {url}:\n")
        for key, value in seo_report.items():
            print(f"{key}: {value}")

        # Generate recommendations
        generate_recommendations(seo_report)

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

def generate_recommendations(seo_report):
    recommendations = []

    # Check for missing meta description
    if seo_report["Meta Description"] == "Missing":
        recommendations.append("Include a meta description (150-160 characters) to enhance click-through rates.")

    # Check for missing alt texts
    missing_alt_texts = [src for src in seo_report["Missing Alt Texts"] if src]  # Filter out None
    if missing_alt_texts:
        recommendations.append(f"Add alt text for the following images: {', '.join(missing_alt_texts)}")

    # Check for missing canonical link
    if seo_report["Canonical Link"] == "Missing":
        recommendations.append("Add a canonical link to avoid duplicate content issues.")

    # Check for inaccessible sitemap.xml
    if seo_report["Sitemap.xml"] == "Not Accessible":
        recommendations.append("Ensure the sitemap.xml file is accessible to help search engines index your site.")

    # Print recommendations
    if recommendations:
        print("\nRecommendations:")
        for rec in recommendations:
            print(f"- {rec}")
    else:
        print("\nNo recommendations needed.")

# URLs to check
websites = [
    "https://cems-solarexpo.com",
    "https://cems-apparelsourcing.com"
]

# Perform SEO checks
for site in websites:
    print(f"\nChecking SEO for {site}...")
    check_seo(site)
