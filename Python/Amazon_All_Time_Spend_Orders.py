#%%
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import cm
import mplcyberpunk
import re

df = pd.read_csv(r'/Users/joe/Downloads/01-Jan-2014_to_08-Apr-2020 (2).csv')

#%% Convert Data Types to float for costs
df['Order Date'] = df['Order Date'].apply(pd.to_datetime)
float_cols = ['Total Charged', 'Tax Charged', 'Total Promotions', 'Subtotal', 'Shipping Charge', 'Tax Before Promotions']
for col in float_cols:
    df[col] = df[col].str.replace('$', '').astype(float)
    
#%% Get payment types for spend > 2000
dfpt = df.groupby('Payment Instrument Type')['Total Charged'].sum()
pay_types = list(dfpt[dfpt>2000].index)

#%% Get cumulative Sums
df = df.groupby(by=['Payment Instrument Type', 'Order Date'])\
    ['Total Charged'].sum().groupby(level=[0]).cumsum().reset_index()

#%%
plt.rcParams['figure.figsize'] = [10, 6]
plt.style.use("cyberpunk")
for paytype in pay_types:
    plt.plot('Order Date', 
             'Total Charged', 
             data = df[df['Payment Instrument Type'] == paytype],
             label = paytype)

plt.legend()
plt.title('Cumulative Amazon Spend')
mplcyberpunk.make_lines_glow()
mplcyberpunk.add_underglow()
plt.show()

#%% Total Cumulative
plt.rcParams['figure.figsize'] = [10, 6]
plt.style.use("cyberpunk")
plt.plot('Order Date', 'Item Total', 
         data = dfTotCumSum,
         label = 'Friet')

plt.legend()
plt.title('Cumulative Amazon Spend')
mplcyberpunk.make_lines_glow()
mplcyberpunk.add_underglow()
plt.show()


# %%
