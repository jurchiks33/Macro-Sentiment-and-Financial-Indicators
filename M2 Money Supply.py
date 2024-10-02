import yfinance as yf
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# function to get M2 supply data
def get_m2_data(start, end):
    m2_data = web.DataReader('M2SL', 'fred', start, end)
    return m2_data

# function to get stock market data (S&P 500)
def get_stock_data(ticker, start, end):
    stock_data = yf.download(ticker, start=start, end=end)
    return stock_data['Adj Close']