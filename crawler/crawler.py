"""
Web crawler module for data collection.
"""

def crawl_data(url):
    """Crawl data from sources."""
    pass


import requests
from bs4 import BeautifulSoup
import os

RAW_FOLDER = "raw_data"

def crawl_data(url):

    if not os.path.exists(RAW_FOLDER):
        os.makedirs(RAW_FOLDER)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    file_path = os.path.join(RAW_FOLDER, "data.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        for p in paragraphs:
            f.write(p.get_text() + "\n")

    return file_path

def run_crawler():
    print("Running crawler...")