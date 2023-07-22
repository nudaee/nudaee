#%%
# Let's import the pandas, numpy libraries as pd, and np respectively. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the pyplot collection of functions from matplotlib, as plt 
import matplotlib.pyplot as plt 
# First, make a variable called url_LondonHousePrices, and assign it the following link, enclosed in quotation-marks as a string:
# https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls

url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"

# The dataset we're interested in contains the Average prices of the houses, and is actually on a particular sheet of the Excel file. 
# As a result, we need to specify the sheet name in the read_excel() method.
# Put this data into a variable called properties.  
# Creates a dataframe propertie from an excel file
propertie = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col= None)
properties= propertie
# 
propertie.head()
# Flips the dataframe Columns become row rows become columns
propertie = propertie.transpose()


# Creates a numderical index for the data frame 
propertie = propertie.reset_index(drop= False)

# %%
propertie.head()

rowStart= 34
rowEnd = 48

# Removes Rows RowStart aka row 34 to rowEnd aka row 48
propertie=propertie.drop(properties.index[rowStart:rowEnd+1])

propertie.columns = propertie.iloc[0]

# Removes the first row of the dataframe
propertie= propertie.iloc[1:]


# Renames the the first Column_name to Boroughs
propertie.columns.values[0] ='Boroughs'


# Removes the 00:00:00 from the first row/column_name

propertie.columns = propertie.columns.astype(str).str.split(' ').str[0]


#  Creates a list of dates from the first row in the dataframe  
dates = list(propertie.columns[1:])

# Adds a column named ID# to the front of the dataframe 
row_numbers= len(propertie)

id_column=[]
for i in range(row_numbers):
    id_column.append(i+1)

propertie.insert(0,'ID#',id_column)

# drops the NaT column
propertie = propertie.drop(propertie.columns[2], axis=1)


# Just testing the sum() code
sum(propertie.iloc[2,[2,5]])

propertie 
# Up to this point data cleaning is done. Now I'll start to transfom it.
#%%



#%% 
common_prefix = {}
for col in propertie.columns:
    prefix = col[:4]
    if prefix not in common_prefix:
        common_prefix[prefix] = [col]
    else:
        common_prefix[prefix].append(col)
#%%

common_prefix        

#%%
for prefix, columns in common_prefix.items():
    if len(columns) > 1:
        sum_values = propertie[columns].sum(axis=1)
        propertie[f'{prefix}_sum'] = sum_values

#%%
propertie

#%% creates an empty list then adds -30 to -1 in the list and flips the list order
column_range = []

for i in range(30):
    column_range.append(i*-1)
column_range = column_range[::-1]

#%%
propertiesPrices = propertie.iloc[0:33,column_range] 
propertiesPrices.drop(propertiesPrices.columns[-1], axis=1, inplace= True)
IDBoroughs = propertie.iloc[0:33,[0,1]]
#%%
propertiesPrices
#%%
IDBoroughs
#%%
properties= pd.concat([IDBoroughs,propertiesPrices], axis=1)


#%%
yearNames= properties.columns[2, column_range]
yearNames
#%%
#diff_df= [
properties.iloc[column_range]





# %%
properties['Average Price']= properties[properties.columns[2:31]].mean(axis=1)
properties['Price Change From 95 to 23'] =properties[properties.columns[30]] - properties[properties.columns[2]]
#properties['Average Price Change Per Yer']= ChangePerYer


#%%
#properties.plot(x='Average Price', y='Price Change From 95 to 23', )

properties[3:5].plot()


# %%

properties
#pd.melt(propertie, id_vars=[propertie.columns[0], 'Boroughs'], value_vars = dates , var_name ='Year', value_name='Average Price')
#%%
mostexp= properties['Average Price'].max()
mostexp
#%%
mostexpbororow = properties[properties['Boroughs'] == mostexp]
mostexpbororow
# %%
mostexpboro = mostexpbororow['Boroughs'].values[0]


# %%
