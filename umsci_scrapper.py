import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd

# Function to fetch UMCSI data from FRED
def fetch_umcsi_data():
    # FRED series ID for the University of Michigan Consumer Sentiment Index (UMCSI)
    series_id = "UMCSENT"
    
    # Define the start and end date for fetching the data
    start_date = '1980-01-01'
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')  # Use today's date
    
    # Fetch data from FRED
    df = web.DataReader(series_id, 'fred', start_date, end_date)
    
    # Rename the column for easier reference
    df.columns = ['Sentiment']
    
    return df

# Function to plot UMCSI data with only the UMCSI line and horizontal lines
def plot_umcsi(df):
    # Plot the Consumer Sentiment Index as a line chart
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Sentiment'], label='UMCSI', color='green', linewidth=2)
    
    # Plot horizontal lines at 75 and 95
    plt.axhline(y=75, 
                color='black', 
                linestyle='--', 
                label='75 Mark')  # Horizontal line at 75
    plt.axhline(y=95, 
                color='black', 
                linestyle='--', 
                label='95 Mark')  # Horizontal line at 95
    
    