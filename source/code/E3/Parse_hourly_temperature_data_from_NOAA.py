# -*- coding: utf-8 -*-
"""
Parse hourly temperature data for Exercise 3 from Malmi Airport, Helsinki. 

Data source:
    https://www.ncdc.noaa.gov/orders/isd/1367077431691dat.txt

Created on Thu Sep 14 15:10:42 2017

@author: Henrikki Tenkanen
"""

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

# Filepath
fp = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Geo-Python\data\Hourly_temps_Malmi_airport\1367077431691dat.txt"

# Read file (fixed width)
data = pd.read_fwf(fp)

# Select only necessary columns
cols = ['YR--MODAHRMN', 'TEMP']
d = data[cols]

# Create a Datetime Index
d['datetime'] = pd.to_datetime(d['YR--MODAHRMN'], format="%Y%m%d%H%M")

# Set datetime as index
d = d.set_index(d['datetime'])

# Aggregate to daily averages
daily = d['Celsius'].resample(rule='D').mean()
night_day = d['Celsius'].resample(rule='8H').mean()

# Round to 1 decimal
night_day = night_day.round(1)

# Convert TEMP (fahrenheit) to Celsius
d['Celsius'] = (d['TEMP'] - 32) * 5/9
               
# Plot
d.plot(x='datetime', y='Celsius')
