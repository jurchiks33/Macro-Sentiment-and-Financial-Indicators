import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# helper function to convert text to float if needed
def convert_to_float(text):
    try:
        return float(text)
    except ValueError:
        return None

# function to scrape ISM, adjust MONTH as needed
def scrape_ism_report():
    url = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/pmi/september/"

    # send response to get a page content
    response = requests.get(url)

    # check if request succeed
    if response.status_code != 200:
        print(f"failed to get ISM repor. Status Code: {response.status_code}")
        return None
    
    # parsing HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # harcoding column names
    index_names = [
        "Manufacturing PMI", "New Orders",
        "Production", "Supplier Deliveries",
        "Inventories", "Customer's Inventories",
        "Prices", "Baclog of Orders",
        "New Export Orders", "Imports"
    ]

    # preparing dictionary to store extracted data
    data = {
        'index': index_names,
        'Series Index Sep': [], # latest data
        'Series Index Aug': []  # data before last one
    }

    # table with ism data
    table = soup.find('table')

    # rows for the table
    rows = table.find_all('tr')

    for i, row in enumerate(rows[1:]):
        cols = row.find_all('td')

        # extracting first two data columns
        sep_value = convert_to_float(cols[0].get_text(strip=True))
        aug_value = convert_to_float(cols[1].get_text(strip=True))

        # Append numeric values and skip non numerical ones
        if sep_value is not None and aug_value is not None:
            data['Series Index Sep'].append(sep_value)
            data['Series Index Aug'].append(aug_value)
    
    return pd.DataFrame(data)

# function to display table
