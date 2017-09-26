# -*- coding: utf-8 -*-
"""
Parse hourly temperature data for Exercise 3 from Malmi Airport, Helsinki. 

Data source:
    https://www.ncdc.noaa.gov/orders/isd/1367077431691dat.txt

Created on Thu Sep 14 15:10:42 2017

@author: Henrikki Tenkanen
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
plt.style.use('seaborn-whitegrid')

# Script location
basepath = os.path.dirname(os.path.realpath(__file__))

# Filepath
fp = os.path.join(basepath, 'data', "1367077431691dat.txt")

# Read file (fixed width)
data = pd.read_fwf(fp)

# Select only necessary columns
cols = ['YR--MODAHRMN', 'TEMP']
d = data[cols]

# Create a Datetime Index
d['datetime'] = pd.to_datetime(d['YR--MODAHRMN'], format="%Y%m%d%H%M")

# Set datetime as index
d = d.set_index(d['datetime'])

# Convert TEMP (fahrenheit) to Celsius
d['Celsius'] = (d['TEMP'] - 32) * 5/9
               
# Plot
d.plot(x='datetime', y='Celsius')

# Aggregate to daily averages
daily = d['Celsius'].resample(rule='D').mean()
night_day = d['Celsius'].resample(rule='8H').mean()

# Round to 1 decimal
night_day = night_day.round(1)

# Print the values as strings so it is possible to easily copy/paste to exercise
# ==> Find/Replace ' characters to convert the values to floats
print(list(night_day.astype(str).values))

# Save hourly Fahrenheit temps to csv
outfp = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Geo-Python\2017\source\code\E3\data\Malmi_temps_Fahr.csv"
d['n'] = None
temp = d[['TEMP', 'n']].copy()
temp = temp.reset_index(drop=True)

# Take First week of data (first 2*24*7)
temp = temp[0:336]

temp.to_csv(outfp, sep=',', index=False)

