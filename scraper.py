# ESPNcricinfo India RSS Feed Scraper
# This Python script scrapes the latest headlines from the 'India' category RSS feed on ESPNcricinfo
# and exports the data into a file format of your choice: Excel, CSV, or JSON.

print("📢 Welcome to the ESPNcricinfo India News Scraper!")
print("📌 This script fetches the latest news from the India section of ESPNcricinfo's RSS feed.")
print("🔽 Choose how you'd like to export the news:")
print("- Excel")
print("- CSV")
print("- JSON")
print("########################################")

export_format = input("📝 Your choice: ").lower().strip()
print("########################################")

# Validate the user input
while export_format not in ['excel', 'csv', 'json']:
    print("❌ Invalid choice. Please enter one of: Excel, CSV, or JSON.")
    export_format = input("📝 Your choice: ").lower().strip()

print("✅ You selected:", export_format.upper())
file_name = input("📄 Enter the output file name (without extension): ").strip()

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
    file_path = f"{file_name}.xlsx"
    df.to_excel(file_path, index=False)
elif export_format == 'csv':
    file_path = f"{file_name}.csv"
    df.to_csv(file_path, index=False)
elif export_format == 'json':
    file_path = f"{file_name}.json"
    df.to_json(file_path, orient='records')

print(f"✅ Export complete! Your file '{file_path}' has been saved in the current directory.")
