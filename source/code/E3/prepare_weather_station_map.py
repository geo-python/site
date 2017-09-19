# -*- coding: utf-8 -*-
"""
Prepare figure for Exercise 3 Problem 3. 

Weather station data was extracted (copy/paste) from:
    http://en.ilmatieteenlaitos.fi/observation-stations
    
To reduce the amount of stations, we only take a look at stations that are older than 50 years. 

Created on Tue Sep 19 09:36:59 2017

@author: Henrikki Tenkanen
"""

import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point, MultiLineString
import pandas as pd
from fiona.crs import from_epsg
import os

# Script location
basepath = os.path.dirname(os.path.realpath(__file__))

# Projections: http://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html
# Weather stations: 

# Filepath
country_fp = os.path.join(basepath, 'data', 'Finland_boundaries.shp')
station_fp = os.path.join(basepath, 'data', "Weather_stations_all_Finland.txt")
outfp = os.path.join(basepath, 'img', "FMI_stations_70_years_older.png")

# Read data
data = gpd.read_file(country_fp)
stations = pd.read_csv(station_fp, sep='\t', encoding='latin1', header=None, names=['Name', 'FMISID', 'LPNN', 'WMO', 'Lat', 'Lon', 'Elevation', 'Groups', 'Started'])

# Prepare stations into GeoDataFrame
# ----------------------------------

# Create Point geometries from coordinates
stations['geometry'] = None
stations['geometry'] = stations.apply(lambda row: Point(row['Lon'], row['Lat']), axis=1)    
    
# Create GeoDataFrame
stations_geo = gpd.GeoDataFrame(stations, geometry='geometry', crs=from_epsg(4326))

# Select only 'Weather stations'
stations_geo = stations_geo.ix[stations_geo['Groups']=='Weather stations']

# Select stations that are older than 50 years
stations_geo = stations_geo.ix[stations_geo['Started'] <= 1947]

# Plot the map and axis 
# ---------------------

# Coordinates for Finland's (mainland) centroid
centroid_x = 26.3
centroid_y = 64.5

# Cross coordinates
left_x = 20
right_x = 31.8
top_y = 70.2
bottom_y = 59

# Vertical line
v_line = LineString([(26.3, 59), (26.3, 70.2)])

# Horizontal line
h_line = LineString([(20.0, 64.5), (31.8, 64.5)])

# MultiLine
multi_line = MultiLineString([((26.3, 59), (26.3, 69.2)), ((20.0, 64.5), (31.8, 64.5))])

# Create a GeoDataFrame
geo_lines = gpd.GeoDataFrame()
geo_lines['geometry'] = None
geo_lines.loc[0, 'geometry'] = v_line
geo_lines.loc[1, 'geometry'] = h_line
            
            
# Specify CRS
crs = gcrs.UTM(zone=35)
# Initialize the Figure
fig, ax = plt.subplots(subplot_kw={'projection': crs})

# Plot data in UTM35 projection
ax = gplt.polyplot(data, ax=ax, facecolor='none', projection=crs)
ax = gplt.polyplot(geo_lines, ax=ax, projection=crs)
ax = gplt.pointplot(stations_geo, color='blue', ax=ax, projection=crs)

# Get xlim
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Set ylim
ax.set_ylim(6549957.0035361676, 7912500.2913647108)

# Save figure
plt.tight_layout()
#plt.savefig(outfp, dpi=300)

# Get the coordinates of Weather stations
x_coords = stations_geo['Lon'].values
y_coords = stations_geo['Lat'].values
names = stations_geo['Name'].values
print(list(x_coords.astype(str)))
print(list(y_coords.astype(str)))
print(list(names))                       
