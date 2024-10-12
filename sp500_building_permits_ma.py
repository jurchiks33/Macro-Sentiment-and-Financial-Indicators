import yfinance as yf
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt

# Function to get S&P 500 stock market data (from Yahoo Finance)
def get_sp500_data(start, end):
    sp500_data = yf.download('^GSPC', start=start, end=end)
    return sp500_data['Adj Close']

# Function to get U.S. Building Permits data (from FRED)
def get_building_permits_data(start, end):
    permits_data = web.DataReader('PERMIT', 'fred', start, end)
    return permits_data

