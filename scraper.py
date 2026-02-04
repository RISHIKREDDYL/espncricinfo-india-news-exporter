# ESPNcricinfo India RSS Feed Scraper
# This Python script scrapes the latest headlines from the 'India' category RSS feed on ESPNcricinfo
# and exports the data into a file format of your choice: Excel, CSV, or JSON.

import os
import sys

def get_input(prompt, env_var, default=None):
    val = os.getenv(env_var)
    if val:
        return val
    try:
        if sys.stdin.isatty():
            return input(prompt)
        else:
            if default: return default
            raise ValueError(f"No tty and no env var {env_var}")
    except EOFError:
        if default: return default
        raise

print("📢 Welcome to the ESPNcricinfo India News Scraper!")
export_format = get_input("📝 Your choice (Excel/CSV/JSON): ", "EXPORT_FORMAT", "csv").lower().strip()
file_name = get_input("📄 Enter the output file name: ", "FILE_NAME", "india_news")

# Ensure output directory exists if in Docker
output_dir = "output"
if not os.path.exists(output_dir) and os.path.exists("/app"):
    os.makedirs(output_dir, exist_ok=True)

file_path = os.path.join(output_dir if os.path.exists(output_dir) else ".", f"{file_name}")

# Import required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# NOTE: lxml is required as the parser for BeautifulSoup when using 'xml'
# It's not directly used here, but make sure it is installed in your environment
# import lxml  # Optional: not used directly, but needed for XML parsing

# URL for India category RSS feed on ESPNcricinfo
url = 'https://www.espncricinfo.com/rss/content/story/feeds/6.xml'
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml')  # Parses using lxml if available

# Extract all <item> elements (news articles)
items_list = soup.find_all('item')
print(f"🔍 Found {len(items_list)} news items in the RSS feed.")

data = []
seen_urls = []

# Process and filter out duplicate entries
for item in items_list:
    if item.url.text.strip() not in seen_urls:
        data.append({
            'title': item.title.text.strip(),
            'description': item.description.text.strip(),
            'pub_date': item.pubDate.text.strip(),
            'url': item.url.text.strip(),
        })
        seen_urls.append(item.guid.text.strip())
    else:
        print("⚠️ Duplicate item found. Skipping...")

print(f"✅ Collected {len(data)} unique news items.")

# Convert list of news items to a DataFrame
df = pd.DataFrame(data)
print("📋 Here's a preview of the data:")
print(df.head())

# Export to the desired file format
if export_format == 'excel':
    full_path = f"{file_path}.xlsx"
    df.to_excel(full_path, index=False)
elif export_format == 'csv':
    full_path = f"{file_path}.csv"
    df.to_csv(full_path, index=False)
elif export_format == 'json':
    full_path = f"{file_path}.json"
    df.to_json(full_path, orient='records')

print(f"✅ Export complete! Your file '{full_path}' has been saved.")
