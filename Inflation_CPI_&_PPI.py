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

    # plotting data
    plt.figure(figsize=(10, 6))

    plt.plot(cpi_data, label='CPI (Consumer Price Index)', color='blue')
    plt.plot(ppi_data, label='PPI (Producer Price Index)', color='green')

    plt.title('CPI vs PPI')
    plt.xlabel('Date')
    plt.ylabel('Index Value')
    plt.legend(loc='best')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # call function from main application
    def main():
        analyze_inflation()
    
    # for standalone running function
    if __name__ == "__main__":
        main()