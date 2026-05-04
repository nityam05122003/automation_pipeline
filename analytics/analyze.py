"""
Analytics and reporting module.
"""

def analyze_data():
    """Analyze cleaned data and generate insights."""
    pass


import os

CLEAN_FILE = "clean_data/clean_data.txt"
REPORT_FOLDER = "reports"

def generate_report():

    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)

    with open(CLEAN_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    paragraph_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)

    report_file = os.path.join(REPORT_FOLDER, "report.txt")

    with open(report_file, "w") as f:
        f.write(f"Total Paragraphs: {paragraph_count}\n")
        f.write(f"Total Words: {word_count}\n")

    return report_file

def run_analysis():
    print("Running analytics...")