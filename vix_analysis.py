import yfinance as yf
import matplotlib.pyplot as plt

# function to get VIX volatility index data
def get_vix_data(start, end):
    vix_data = yf.download('^VIX, start=start, end=end')
    return vix_data['Adj Close']

# defining time frame for VIX index
start_date = '2000-01-01'
end_date = '2024-09-09'

# getting VIX data
vix_data = get_vix_data(start_date, end_date)

