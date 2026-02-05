# ESPNcricinfo India News Exporter (Dockerized) 🏏

A terminal-based Python scraper that extracts the latest cricket headlines from ESPNcricinfo's India RSS feed and exports them to Excel, CSV, or JSON.

## Docker Usage

### Build and Run
```bash
docker-compose up --build
```

### Configuration
You can configure the export format and file name via environment variables in `docker-compose.yml`:
- `EXPORT_FORMAT`: `excel`, `csv`, or `json` (default: `csv`)
- `FILE_NAME`: name of the output file (default: `india_news`)

### Output
The exported files will be saved in the `./output` directory on your host machine.
