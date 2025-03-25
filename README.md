
# 📰 Web Scraper - News Content Extractor

This project is a **web scraper** designed to automatically extract titles, dates, links, and article content from various news websites.

## 📌 Objective

To automate the collection of news articles for purposes like text analysis, media monitoring, or building a dataset for NLP and data science projects.

## 🚀 Features

- 🔎 Scrapes titles, dates, URLs, and full article content
- 🧠 Modular structure for easily adding new news sources
- 📂 Saves the extracted data to a `.csv` file
- 🕵️ Simple text cleaning utility

## 🛠️ Technologies Used

- `Python 3.x`
- `requests`
- `BeautifulSoup` (bs4)
- `pandas`
- `re` (regex)

## 🗂️ Project Structure

Web_Scraper_news_content/ ├── data/ │ └── news_data.csv # Extracted data ├── scrapers/ │ ├── scraper_lemonde.py # Scraper for Le Monde │ ├── scraper_liberation.py # Scraper for Libération │ └── ... # Additional scrapers go here ├── utils/ │ └── text_cleaning.py # Utility functions for text processing ├── main.py # Main script to run all scrapers ├── requirements.txt # Python dependencies └── README.md # This file

📌 Future Improvements
 Add logging system

 Improve speed with multithreading or async requests

 Build a Streamlit dashboard for article exploration

👨‍💻 Author
Saad Yaqine
📧 saadyaqine91@gmail.com



