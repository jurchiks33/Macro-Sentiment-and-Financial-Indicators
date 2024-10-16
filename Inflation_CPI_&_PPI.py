import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt

# function to get CPI and PPI data from FRED
def get_inflation_data(start, end):
    cpi_data = web.DataReader('CPIAUCSL', 'fred', start, end)
    ppi_data = web.DataReader('PPIACO', 'fred', start, end)
    return cpi_data, ppi_data

# function to analyze and plot CPI and PPI data
def analyze_inflation():
    # time range
    start_date = '2000-01-01'
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')

    # getting CPI and PPI data
    cpi_data, ppi_data = get_inflation_data(start_date, end_date)

    