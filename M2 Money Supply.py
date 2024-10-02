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

# defining range. Change as needed
start_date = '2000-01-01'
end_date = '2024-09-09'

# getting M2 money supply data
m2 = get_m2_data(start_date, end_date)

# getting S&P 500 stock market data
sp500 = get_stock_data('^GSPC', start_date, end_date)

# resampling M2 and S&P 500 data to a monthly frequency and we merge them.
m2_monthly = m2.resample('M').last()
sp500_monthly = sp500.resample('M').last()