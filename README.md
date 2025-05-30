# 📰 ESPNcricinfo India News Exporter

**A terminal-based Python scraper that extracts the latest cricket headlines from ESPNcricinfo's India RSS feed and exports them to Excel, CSV, or JSON.**

> Built by [@RISHIKREDDYL](https://github.com/RISHIKREDDYL)

---

## 📌 What It Does

- Scrapes the official [India category RSS feed](https://www.espncricinfo.com/rss/content/story/feeds/6.xml) from ESPNcricinfo.
- Extracts key information: title, description, publication date, and URL.
- Automatically removes duplicate entries.
- Exports the scraped data into your chosen file format:
  - `Excel (.xlsx)`
  - `CSV (.csv)`
  - `JSON (.json)`

---

## 📦 Installation

```bash
git clone https://github.com/RISHIKREDDYL/espncricinfo-india-news-exporter.git
cd espncricinfo-india-news-exporter
```

---

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the script:
```bash
python scraper.py
```
Follow the prompts in your terminal:
- Choose your export format (`excel`, `csv`, or `json`)
- Provide a file name (no extension needed)

Once done, the file will be saved in the current directory.

---

## 📂 Output Example

You might see outputs like:
- `india_news.xlsx`
- `india_news.csv`
- `india_news.json`

Each file will contain structured data with:
- `title`
- `description`
- `pub_date`
- `url`
