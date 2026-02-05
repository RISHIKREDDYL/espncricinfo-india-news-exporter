# ESPNcricinfo India News Exporter 🏏

An autonomous, Dockerized news scraper that fetches the latest cricket news from ESPNcricinfo's India feed and exports it to a structured CSV file.

## Features
- ✅ **Automated Scraping:** Fetches headlines, links, and descriptions from the ESPNcricinfo India news page.
- ✅ **Dockerized:** Runs in an isolated environment with all dependencies pre-installed.
- ✅ **Headless Mode:** Uses Selenium with a headless browser for reliable scraping in server environments.
- ✅ **Structured Output:** Saves results to `output/india_news.csv`.

---

## Step-by-Step Usage Guide

### 1. Prerequisites
Ensure you have the following installed on your system:
- [Docker](https://docs.docker.com/get-docker/) (v2.0+ recommended)

### 2. Clone the Repository
```bash
git clone https://github.com/RISHIKREDDYL/espncricinfo-india-news-exporter.git
cd espncricinfo-india-news-exporter
```

### 3. Build the Image
Build the Docker container to install the environment and Chromium driver:
```bash
docker compose build
```

### 4. Run the Scraper
Start the container. It will automatically initialize the browser, scrape the news, and save the CSV:
```bash
docker compose up
```

### 5. View Your Data
Once the process finishes, you will find the scraped news in the local `output/` directory:
```bash
ls -l output/india_news.csv
```

---

## Configuration

The scraper can be configured via environment variables in `docker-compose.yml`:

| Variable | Description | Default |
|----------|-------------|---------|
| `OUTPUT_PATH` | Where to save the CSV inside the container | `/app/output/india_news.csv` |
| `HEADLESS` | Whether to run the browser in headless mode | `true` |

---

## Project Structure
- `scraper.py`: Core Selenium logic for data extraction.
- `Dockerfile`: Ubuntu-based environment with Python 3.12, Chromium, and WebDriver.
- `docker-compose.yml`: Orchestration for volume mounting and environment setup.
- `requirements.txt`: Python dependencies (Selenium, Pandas).

---
*Developed by RISHIKREDDYL* 🐉
