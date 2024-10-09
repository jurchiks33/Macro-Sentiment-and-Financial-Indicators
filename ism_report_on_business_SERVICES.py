import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# helper function to convert text to float if needed
def convert_to_float(text):
    try:
        return float(text)
    except ValueError:
        return np.nan

# function to scrape ISM report on business - services. for september, change month as needed
def scrape_ism_services_report():
    url = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/services/september/"

    # send request to fetch the page content
    response = requests.get(url)

    # check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve ISM Service report. Status code: {response.status_code}")
        return None
    
    # parsing HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

# Hardcode index column names for ISM services
index_names = {
    "Services PMI", "Business Activity/Production",
    "New Orders", "Employment",
    "Supplier Deliveries", "Inventories",
    "Prices", "Backlog of Orders",
    "New Export Orders", "Imports",
    "Inventory Sentiment", "Customers Inventories"
}

# preparing dictionary for extracted data
data = {
    'index': index_names,
    'Series Index Sep': [],
    'Series Index Aug': [],
}

# extracting table with ISM data
table = soup.find('table')

# extracting rows from the table
rows = table.find_all('tr')

# process from second row to shift all data one row up
for i in range(1, len(index_names) + 1):
    try:
        cols = rows[i].find_all('td')

        # extracting September and August data
        if len(cols) >= 2:
                sep_value = convert_to_float(cols[0].get_text(strip=True))  # September data
                aug_value = convert_to_float(cols[1].get_text(strip=True))  # August data
        else:
                sep_value = np.nan
                aug_value = np.nan
    except IndexError:
            sep_value = np.nan
            aug_value = np.nan
