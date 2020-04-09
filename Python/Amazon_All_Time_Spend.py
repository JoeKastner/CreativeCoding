#%%
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import cm
import mplcyberpunk
import re

df = pd.read_csv(r'/Users/joe/Downloads/01-Jan-2011_to_08-Apr-2020.csv')

#%% Convert Data Types to float for costs
df['Order Date'] = df['Order Date'].apply(pd.to_datetime)
float_cols = ['Item Total', 'Item Subtotal', 'Item Subtotal Tax', 'List Price Per Unit']
for col in float_cols:
    df[col] = df[col].str.replace('$', '').astype(float)

#%%
df['Pay Type'] = df['Payment Instrument Type'].str.extract('(\d+)')
df['Pay Type'] = df['Pay Type'].map(
    {'4859': 'Mel', 
     '6792': 'Joe', 
     '2922': 'Joe', 
     '1212': 'Joe', 
     '6697': 'Joe', 
     '5425': 'Mel'}
    )
df['Pay Type'].fillna('Gift Card', inplace=True)

#%% Get cumulative Sums
dfCumSum = df.groupby(by=['Pay Type','Order Date']).sum()\
.groupby(level=[0]).cumsum().reset_index()
#%%
plt.rcParams['figure.figsize'] = [10, 6]
plt.style.use("cyberpunk")
plt.plot('Order Date', 'Item Total', 
         data = dfCumSum[dfCumSum['Pay Type'] == 'Joe'],
         label = 'Joe')

plt.plot('Order Date', 'Item Total', 
         data = dfCumSum[dfCumSum['Pay Type'] == 'Mel'],
         label = 'Mel')

plt.plot('Order Date', 'Item Total', 
         data = dfCumSum[dfCumSum['Pay Type'] == 'Gift Card'],
         label = 'Gift Card')

plt.legend()
plt.title('Cumulative Amazon Spend')
mplcyberpunk.make_lines_glow()
mplcyberpunk.add_underglow()
plt.show()



