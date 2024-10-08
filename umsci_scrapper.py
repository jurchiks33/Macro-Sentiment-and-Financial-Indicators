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

