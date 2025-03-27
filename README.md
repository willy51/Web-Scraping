# 📊 Web Scraping Projects Collection

A Python-based school project for data scraping and automation

This repository contains three practical Python scripts developed as part of a school project focused on real-world data extraction using web scraping techniques.

We explore scraping from dynamic websites using Selenium and Scrapy, targeting sources like the NBA official stats page, YouTube, and Genshin Impact France.

## 🏀 NBA Player Stats Scraper

**Purpose:**  
Scrapes player statistics and headshots from the official [NBA Stats](https://www.nba.com/stats/players) page.

**Key Features:**
- Extracts player data and saves it to a CSV file.
- Automatically downloads high-resolution player images.
- Saves all assets locally in organized folders.

**Technologies:**  
- `Selenium`  
- `CSV`  
- `Requests`

**Output:**
- `NBA.csv`: Player stats and profile image links.
- `/NBA_Player_Images`: Headshots of players.

## 📺 YouTube Data Scraper

**Purpose:**  
Scrapes YouTube's homepage and search results to extract:
- Number of images on the homepage.
- Sidebar links (e.g., Music, Sports).
- Search results (e.g., video titles).
- Related videos and metadata from a specific video.

**Key Features:**
- Interacts with dynamic content.
- Uses Selenium for automation and data extraction.

**Technologies:**
- `Selenium`  
- `CSV` (if extended)  
- `YouTube’s dynamic interface`

**Example Searches:**
- Searches for `Stairway to Heaven` and logs the first 3 results.
- Analyzes the video: `https://www.youtube.com/watch?v=qHFxncb1gRY`

## ⚔️ Genshin Impact Characters Scraper

**Purpose:**  
Uses **Scrapy** to collect detailed data on Genshin Impact characters from [genshin-impact.fr](https://www.genshin-impact.fr/personnages/).

**Key Features:**
- Extracts character name, rarity, weapon, element, base ATK/DEF/HP.
- Downloads character build images.
- Saves data into a structured CSV file.

**Technologies:**
- `Scrapy`  
- `Requests`  
- `CSV`  
- `CSS Selectors`

**Output:**
- `genshin_characters.csv`
- `/BuildGenshinCharacters`: Character build images

**Run Command:**
```bash
scrapy crawl genshinCharacters
```

## 🛠️ Requirements

Make sure to install the dependencies before running the scripts:
```bash
pip install selenium scrapy requests
```

Also, you need **ChromeDriver** installed and added to your system path.

## 🚀 How to Use

Each script is standalone. Just run them individually:
```bash
python NBA.py
python Youtube.py
# For Scrapy:
cd your_scrapy_project
scrapy crawl genshinCharacters
```

## 💡 Tips & Notes

- Always respect the terms of service of the websites you scrape 🙏.
- Consider adding `try/except` blocks for better error handling.
- Use virtual environments for cleaner setups.

## 📂 Folder Structure

```
.
├── NBA.py
├── Youtube.py
├── genshin_scraping.py
├── NBA.csv
├── NBA_Player_Images/
├── genshin_characters.csv
├── BuildGenshinCharacters/
```

