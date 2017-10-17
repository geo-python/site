# -*- coding: utf-8 -*-
"""
Lesson 7 preparation codes. 

Aims:
    - Read hourly temperatures with Pandas. Use datetime index. 
    - Plot hourly temperatures with Pandas
    - Aggregate data into daily values using resample() -function.
    - Select data by seasons using datetime index. 
    - Create a subplot and plot all 4 seasons into the same Figure.

Created on Tue Oct 17 15:57:20 2017

@author: Henrikki Tenkanen
"""

# At this point you should know the basics of making plots with Matplotlib module. It is also possible to do Matplotlib plots directly
# from Pandas because many of the basic functionalities of Matplotlib are integrated into Pandas. 
# In this part, we will show how to create plots using Pandas, such as this:

# One of the most useful and powerful features in Pandas is its ability to work with time data.
# In Pandas, we can even read the data from a file and tell to Pandas that values from certain column should be
# interpreted as time, and we can actually use that as our index, which is cool! You will see later why.

# Let's start by reading the data in and determing that the values from ``YR--MODAHRMN`` column should be interpreted and converted into a time index.

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# File path
fp = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Geo-Python\2017\data\L7\1924927457196dat.txt"

# When reading the data we can use ``parse_dates`` parameter to parse the time information
data = pd.read_csv(fp, sep='\s+', parse_dates=['YR--MODAHRMN'], na_values=['*', '**', '***', '****', '*****', '******'])

# Let's check the datatypes of our columns
data.dtypes

# As we can see the data type of ``YR--MODAHRMN`` column (third from above) is of type ``datetime64[ns]``. 
# This means that the values on that column are interpreted as time objects. 
# Let's see how our data look like.
data.head()

# As we can see the values on ``YR--MODAHRMN`` indeed look like time information where the first part represents the date and the second part represents the ``hours:minutes:seconds``. 

# Before continue with plotting in Pandas, let's process our data a bit by selecting only few columns, renaming them and converting the Fahrenheit temperatures into Celsius. 
# If you don't remember how the following steps work, you might want to take another look on ``Lesson 6 materials <../L6/pandas-analysis.html#exploring-data-and-renaming-columns.html>``.

# Select data
selected_cols = ['YR--MODAHRMN', 'TEMP', 'SPD']
data = data[selected_cols]

# Rename columns
name_conversion = {'YR--MODAHRMN': 'TIME', 'SPD': 'SPEED'}
data = data.rename(columns=name_conversion)

# Convert Fahrenheit temperature into Celsius
data['Celsius'] = (data['TEMP'] - 32) / 1.8

data.head()

# Okey, great now our data looks better, and we can continue. 
# Let's see how our data looks like by plotting the Celsius temperatures. 

# In Pandas, it is extremely easy to plot data from your DataFrame. You can do this by using ``plot()`` function.
# Let's plot all the Celsius temperatures (y-axis) against the time (x-axis). You can specify the columns that you want to plot
# with ``x`` and ``y`` parameters:
data.plot(x='TIME', y='Celsius')

# Cool, it was this easy to produce a line plot that can be used to understand our data better. 
# We can clearly see that there is quite a lot of variation in the temperatures, and different seasons pop up quite clearly from the data. 

# What is obvious from the figure above, is that the hourly level data is actually slightly too accurate for plotting data covering two full years. 
# Let's see a trick, how we can really easily aggregate the data using Pandas. 

# First we need to set the ``TIME`` as the index of our DataFrame. We can do this by using ``set_index()`` parameter.
data = data.set_index('TIME')
data.head()

# As we can see now the index of our data is not a sequential number from 0 up to 16569, but a ``datetime index`` that represents time.
# What is cool about this thing is that you can really easily e.g. select data from a single day using basic Pandas indexing. 

# Let's select data from first day of January in 2013 to demonstrate. We can slice the data by inserting the start date and end date that we want to include in our dataset.
first_jan = data['2013-01-01': '2013-01-01']
print(first_jan)

# Cool! This is quite much easier to do than when parsing the date information using string manipulation (as we did on Lesson 6).
# In a similar manner you can also specify more accurately the time that you want to select. Let's now select only first 12 hours of the same day
first_jan_12h = data['2013-01-01 00:00': '2013-01-01 12:00']
print(first_jan_12h)

# Great. As we can see it is really easy to select data based on times as well.

# Let's now continue with our original problem which was to aggregate the data into daily observations.
# We can do this easily by using a ``resample()`` function that does the aggregation for us by utilizing our ``datetime`` index.                                                                                                            
# We can specify the ``rule`` how we aggregate the data. In below, we use ``'D'`` to specify that we want to aggregate our data based on **Daily** averages. 
# The last function in following command basically determines that we want to calculate the mean from our data values. 
daily = data.resample(rule='D').mean()
daily.head()

# Awesome, now we have values on a daily level that we were able to aggregate with one simple command. Of course it is also possible to aggregate
# based on multiple different time intervals such as hours (``H``), weeks (``W``) months (``M``), etc. See all possible aggregation types (=*offset aliases*) from ``Pandas documentation <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>``__

# Let's now plot our daily temperatures in a similar manner as earlier. Note, that now our time is the index of our DataFrame, so we can pass that into our plotting function. Let's also change the width and the color of our line to red)
daily.plot(x=daily.index, y='Celsius', lw=0.75, c='r')                                                          

# Now we can see that our plot does not look so "crowded" as we have only daily observations instead of hourly. 
# What we can also see is that Pandas actually formats now the x-axis tick-labels really nicely (showing month names and years below them) because we are using the datetime-index to plot the data.

# We can also save this figure to disk by using ``plt.savefig()`` function. With ``dpi`` parameter it is possible to specify the resolution of the Figure.
plt.savefig(r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Geo-Python\2017\data\L7\temp_plot1.png", dpi=300)                                                             
                                                                                                
# .. note:: In previous lesson, we did this by using string manipulation and grouping the data that are really useful skills, but the technique showed here, 
# is much more convenient way of producing the same result.

# -----------------------------------------
# Making subplots
# -----------------------------------------

# Let's continue working with the weather data and learn how to do subplots, i.e. 
# such Figures where you have multiple plots in different panels as was shown in the beginning.                                                                                                            

# Let's start by changing our plotting style into a nicely looking ``seaborn-whitegrid``.
# You can take a look of different readily-available styles from ``here <https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html>``__.
plt.style.use('seaborn-whitegrid')

# Let's first divide our data into different seasons: Winter (December-February), Spring (March-May), 
# Summer (June-August), and Fall (Septempber-November).

# We can do this really easily by selecting data based on the datetime index that we learned earlier.
winter = daily['2012-12-01': '2013-02-28']
spring = daily['2013-03-01': '2013-05-31']
summer = daily['2013-06-01': '2013-08-31']
fall = daily['2013-09-01': '2013-11-30']

# We can plot them separately first, just to see how they look
winter.plot(winter.index, 'Celsius')
spring.plot(spring.index, 'Celsius')
summer.plot(summer.index, 'Celsius')
fall.plot(fall.index, 'Celsius')

# Okey, so from these plots we can already see that the temperatures in different seasons are quite different, which is quite obvious of course.
# It is important to notice that the scale of the y-axis changes in these different plots. If we would like to compare different seasons to each other
# we need to make sure that the temperature scale is similar with all different seasons.

# We want to have our y-axis limits so that the upper limit is the maximum temperature + 5 degrees
# in our data (full year), and the lowest is the minimum temperature - 5 degrees, accordingly.
min_temp = daily['Celsius'].min() - 5
max_temp = daily['Celsius'].max() + 5
print(min_temp)
print(max_temp)

# Okey so we can see that the minimum temperature in our data is approximately -21 degrees and the maximum is +24 degrees.
# We can now use those values to standardize the y-axis scale of our plot.

# Let's now continue and see how we can plot all these graphs different into the same Figure.
# We can create a 2x2 panel for our visualization using matplotlib's ``subplots()`` function where we specify how many rows and columns we want to have in our Figure.
# We can also specify the size  of our figure with ``figsize()`` parameter that takes the ``width`` and ``height`` values (in inches) as input. 
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,8))
print(axes)

# We can see that as a result we have now a list containing two nested lists where the first one contains the axis for column 1 and 2 on **row 1** 
# and the second list contains the axis for columns 1 and 2 for **row 2**.
# We can parse these axes into own variables so it is easier to work with them.
ax11 = axes[0][0]
ax12 = axes[0][1]
ax21 = axes[1][0]
ax22 = axes[1][1]

# Now we have four different axis variables for different panels in our Figure.
# Next we can use them to plot the seasonal data into them.
# Let's first plot the seasons and give different colors for the lines, and specify the y-scale limits to be the same with all subplots.
line_width = 2.5
winter.plot(x=winter.index, y='Celsius', ax=ax11, c='blue', legend=False, lw=line_width, ylim=(min_temp, max_temp))
spring.plot(x=spring.index, y='Celsius', ax=ax12, c='orange', legend=False, lw=line_width, ylim=(min_temp, max_temp))
summer.plot(x=summer.index, y='Celsius', ax=ax21, c='green', legend=False, lw=line_width, ylim=(min_temp, max_temp))
fall.plot(x=fall.index, y='Celsius', ax=ax22, c='brown', legend=False, lw=line_width, ylim=(min_temp, max_temp))

# Great, now we have all the plots in same Figure! However, we can see that there are some problems with our x-axis as the number of ticks is different in different subplots.
# We can change that. It is basically possible to adjust all elements of your visualization. Quite many of them can be adjusted 
# by referring to the ``axis`` object and modifying different parameters from there. 

# The following parts where we adjust the asthetics of the subplots might be a bit difficult to understand, but don't worry if you don't understand everything.
# With other data types of data (other than time data) modifying e.g. the tick intervals is much easier. 

# Let's first clean all the x-axis ticks. We can do that by going through all the axis and setting an empty list as ticks.
# At the same time we can specify that the y-ticks should be visible every 5 degree intervals. For this purpose, we can take advantage of ``arange()`` function from numpy module. We can also set the size of our ticklabels larger at this point.
import numpy as np
yticks = np.arange(start=-25, stop=31, step=5)

for ax in [ax11, ax12, ax21, ax22]:
    # Clear x axis ticks
    ax.get_xaxis().set_ticks([])
    # Specifu y-axis ticks
    ax.yaxis.set_ticks(yticks)
    # Specify major tick-label sizes larger
    ax.tick_params(axis='both', which='major', labelsize=12)
    
# Let's specify that we want to have daily ticks for all our plots. This can be done by utilizing a specific functionality from matplotlib called ``dates`` that we can use to specify the ticks.
# This part is quite advanced plotting, so again, do not worry if you don't understand everything.
from matplotlib import dates
for ax in [ax11, ax12, ax21, ax22]:
    # Set minor ticks with day numbers
    ax.xaxis.set_minor_locator(dates.DayLocator(interval=7))
    ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
    # Set major ticks with month names
    ax.xaxis.set_major_locator(dates.MonthLocator())
    ax.xaxis.set_major_formatter(dates.DateFormatter('\n%b'))

# Perfect now we have similar scales for all of our subplots.

# As a last step let's add text on top of the plots to specify the seasons. Adding text on top of your plot 
# can be done easily with ``text()`` function. When using the ``text()`` function you need to specify (at least)
# the x-position, y-position and the text which will be added to the plot. 

# Let's specify the location for the Winter, Spring, Summer and Fall annotations. 
# In here, we can use the same y-position for all of our plots. However, with x-position we need to specify the position as
# ``datetime()`` objects because the x-axis includes datetime values. 
all_y = -23
wint_x = datetime(2013, 2, 10)
spr_x = datetime(2013, 5, 10)
sum_x = datetime(2013, 8, 7)
fal_x = datetime(2013, 11, 18)

# Let's add those texts on top of our subplots
ax11.text(wint_x, all_y, 'Winter', size=16)
ax12.text(spr_x, all_y, 'Spring', size=16)
ax21.text(sum_x, all_y, 'Summer', size=16)
ax22.text(fal_x, all_y, 'Fall', size=16)

# Let's add a common Y-label for the figure and a title, this can be done by adding another subplot that covers the area of the whole 
# Figure and adding labels on top of that.
fig.add_subplot(111, frameon=False)
# Let's make sure that there are no ticks or labels added 
plt.grid('off')
plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
plt.ylabel("Temperature in Celsius", size=22, family='Arial')
plt.title("Seasonal variations in temperature", size=22, family='Arial')

# By calling plt.tightlayout() it is possible to remove most of the extra whitespace around your figure.
plt.tight_layout()

# Now we can save our Subplot to disk
plt.savefig(r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Geo-Python\2017\data\L7\temp_plot2.png", dpi=300)                                                             
