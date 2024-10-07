import yfinance as yf
import matplotlib.pyplot as plt

# Function to fetch VIX (Volatility Index) data
def get_vix_data(start, end):
    vix_data = yf.download('^VIX', start=start, end=end)
    return vix_data['Adj Close'] 

# Define the time range for VIX data retrieval
start_date = '2000-01-01'
end_date = '2024-09-09'

# Retrieve the VIX data
vix_data = get_vix_data(start_date, end_date)

# Plotting the VIX data
plt.figure(figsize=(10, 6))
plt.plot(vix_data, 
         label='VIX (S&P 500 Volatility Index)', 
         color='blue')
plt.title('S&P 500 Volatility Index (VIX)')
plt.xlabel('Date')
plt.ylabel('VIX Value')
plt.axhline(20, 
            color='red', 
            linestyle='--', 
            label='Normal Volatility Threshold')
plt.legend(loc='best')
plt.grid(True)

# Show the plot
plt.show()
