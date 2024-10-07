import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt

# function for getting 10 year and 2 year US Treasurry yields from FRED
def get_yield_data(start, end):
    dgs10 = web.DataReader('DGS10', 'fred', start, end)
    dgs2 = web.DataReader('DGS2', 'fred', start, end)
    return dgs10, dgs2

# time range for data retrieval
start_date = '2000-01-01'
end_date = '2024-09-09'

# getting yield data
dgs10, dgs2 = get_yield_data(start_date, end_date)

# data merging into a single data frame
data = pd.merge(dgs10, 
                dgs2, 
                left_index=True, 
                right_index=True, 
                how='inner')
data.columns = ['10_Year', '2_Year']

# calculating yield curve spread
data['Yield_Spread'] = data['10_Year'] - data['2_Year']

#Plotting the yield curve spread (10year - 2year)
plt.figure(figsize=(10, 6))
plt.plot(data.index, 
         data['Yield_Spread'], 
         label='10-Year Minus 2-Year Yield Curve Spread', 
         color='blue')
plt.axhline(0, 
            color='red', 
            linestyle='--', 
            label='Inversion Treshold(Zero)')
plt.title('US Treasury 10-Year vs 2-Year Yield Curve Spread')
plt.xlabel('Date')
plt.ylabel('Yield Spread (%)')
plt.legend(loc='best')
plt.grid(True)

plt.show()
