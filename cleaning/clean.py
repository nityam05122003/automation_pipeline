"""
Data cleaning module.
"""

def clean_data():
    """Clean and preprocess raw data."""
    pass


import os
import re

RAW_FILE = "raw_data/data.txt"
CLEAN_FOLDER = "clean_data"

def clean_data():

    if not os.path.exists(CLEAN_FOLDER):
        os.makedirs(CLEAN_FOLDER)

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = []

    for line in lines:
        line = re.sub(r"[^a-zA-Z0-9\s]", "", line)
        line = line.strip()

        if line:
            cleaned_lines.append(line)

    clean_file = os.path.join(CLEAN_FOLDER, "clean_data.txt")

    with open(clean_file, "w", encoding="utf-8") as f:
        for line in cleaned_lines:
            f.write(line + "\n")

    return clean_file

def run_cleaning():
    print("Cleaning data...")