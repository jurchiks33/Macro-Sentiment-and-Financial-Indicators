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

# data set merging into a single dataframe.
data = pd.merge(m2_monthly, sp500_monthly, left_index=True, right_index=True)

# renaming columns for clarity
data.columns = ['M2_Supply', 'S&P500']

# dropping any Nan values, if any (missing values in dataset)
data = data.dropna()

# plotting data trend visualisation
plt.figure(figsize=(10, 6))
plt.plot(data['M2_supply'], label='M2 Money Supply', color='blue')
plt.twinx().plot(data['S&P500'], label='S&P500', color='green')
plt.title('M2 Money Supply vs S&P 500')
plt.legend(loc='upper left')
plt.show()

# performing correlation analysis on a data
correlation = data['M2_supply'].pct_change().corr(data['S&P500'].pct_change())
print(f"Correlation between M2 Money Supply and S&P 500: {correlation:.2f}")

# regression analysis M2 vs SP500
m2_change = data['M2_supply'].pct_change().dropna()
sp500_change = data['S&P500'].pct_change().dropna()

# data for regression analysis
aligned_data = pd.concat([m2_change, sp500_change], axis=1).dropna()
slope, intercept, r_value, p_value, std_err = linregress(aligned_data['M2_Supply'], 
                                                         aligned_data['S&P500'])


