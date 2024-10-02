import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt

# function for getting 10 year and 2 year US Treasurry yields from FRED
def get_yield_data(start, end):
    dgs10 = web.DataReader('DGS10', 'fred', start, end)
    dgs2 = web.DataReader('DGS2', 'fred', start, end)
    return dgs10, dgs2

