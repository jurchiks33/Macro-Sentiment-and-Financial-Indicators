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

    