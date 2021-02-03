# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 12:33:46 2021

@author: Ingrid Nilsson
"""


import pandas as pd
import matplotlib.pyplot as plt

#%%
# Read in Excel File and make "Long"
data = pd.read_excel('total_c02.xls', skiprows = 10, na_values = ":") # Read in excel, skip header rows, : = na 
data = pd.melt(data, id_vars = ["GEO/TIME"], var_name = 'year') # Melt data to make narrow/long
print(data)
#%%
data = data.set_index(["GEO/TIME", "year"])

#%%
print(type(data))

print(data.loc['Sweden'])

#%%
print(data.loc['Denmark'].describe())

#%%
plt.plot(data.loc['Sweden'])