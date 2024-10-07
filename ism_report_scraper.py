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
    
    