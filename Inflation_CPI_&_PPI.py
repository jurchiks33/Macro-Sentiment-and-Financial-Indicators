import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt

# function to get CPI and PPI data from FRED
def get_inflation_data(start, end):
    cpi_data = web.DataReader('CPIAUCSL', 'fred', start, end)
    ppi_data = web.DataReader('PPIACO', 'fred', start, end)
    return cpi_data, ppi_data

