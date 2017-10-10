# -*- coding: utf-8 -*-
"""L6_preparations.py

Description:
    Preparations for Lesson 6. Here I aim to understand the data better to think about lesson / exercise contents. 
    
    Rovaniemi station has values every 20 minutes, BUT, Kumpula has only hourly data.
    To be able to compare these two datasets, we need to aggregate the Rovaniemi
    data into hourly values as well.

Then we want to compare the differences in the Celsius temperatures (using difference and standard deviation).
We can spot the big storm in Helsinki Vantaa in early August.

Aims of the lesson:
    Continue working with real data. Introduce more Pandas functionalities such as 
    replace(), rename(), str.split(), append(), iterrows(), apply(), groupby(), and glob() for reading files (not part of Pandas)

Created on Tue Oct 10 14:08:21 2017

@author: Henrikki Tenkanen
"""

import pandas as pd

# Filepath (we can read a file with varying spaces img/read-csv-varying-spaces.PNG)
fp = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\Geo-Python\admin\data-to-consider\Lesson-6\Helsinki-Vantaa-Jan-Sept-2017-hourly\6591337447542dat_sample.txt"

# Read file with varying spaces and determine varying number of '*' characters to be NaNs
data = pd.read_csv(fp, sep='\s+', na_values=['*', '**', '***', '****', '*****', '******'])

# Let's see how the data looks by printing the first five rows with ``head()`` function
print(data.head())

# Let's check what columns do we have
print(data.columns)

# Okey there are many columns and we are not interested to use all of them. 
# Let's select only columns that can be used to detect unexceptional weather conditions, i.e. 'YR--MODAHRMN', 'DIR', 'SPD', 'GUS','TEMP'
select_cols = ['YR--MODAHRMN', 'DIR', 'SPD', 'GUS','TEMP']
data = data[select_cols]

# Let's see what our data looks like now by printing **last** 5 rows and the datatypes
print(data.tail())
print(data.dtypes)

# Let's also check some basic statistics to understand our data better
print(data.describe())

# The column names that we have are somewhat ackward. Let's change them into more intuitive. This can be done easily with ``rename()`` -function.
# We can define the new column names by using a specific data type in Python called dictionary where we can determine the original column name (the one which will be replaced), and the new column name.
# Let's change ``YR--MODAHRMN`` column into ``TIME``, ``SPD`` into ``SPEED``, and ``GUS`` into ``GUST``
name_conversion_dict = {'YR--MODAHRMN': 'TIME', 'SPD': 'SPEED', 'GUS': 'GUST'}

# Now we can change the column names by passing that dictionary into parameter ``to_replace`` in ``rename()`` -function.
data = data.rename(columns=name_conversion_dict)
print(data.columns)

# Okey now we can see that the column names indeed changed. 

# Let's do the same thing as many times before and convert our Fahrenheit temperatures into Celsius. 
# In this time, however, we will use our self-made function to do the conversion.

# Here I provide you the function that you can copy and paste into your own script.
def fahrToCelsius(temp_fahrenheit):
    """
    Function to convert Fahrenheit temperature into Celsius.
    
    Parameters
    ----------
    
    temp_fahrenheit: int | float
        Input temperature in Fahrenheit (should be a number)
    """
    # Convert the Fahrenheit into Celsius
    converted_temp = (temp_fahrenheit - 32) / 1.8
    return converted_temp 

# Let's first do the conversion by iterating our data line by line and updating the ``CELSIUS`` -column.
# We can iterate over the rows of Pandas DataFrame by using ``iterrows()`` -function. 
# When iterating over the rows in our ``DataFrame`` it is noteworthy to understand that the Pandas actually keeps track on the ``index`` value as well. 
# Hence, the contents of a single row actually contains not only the values, but also the ``index`` of that row.
# Let's see how it works. Here, I will use a specific Python command called ``break`` can be used to stop the iteration right after the first loop. 
# This can be useful as we don't want to fill our consol by printing all the values and indices in our DataFrame, but to just see if the function works as we want. 

for idx, row in data.iterrows():
    print('Index:', idx)
    print(row)
    break
    
# Okey, so here we can see that the ``idx`` variable indeed contains the index value and the ``row`` variable contains all the data from that given row stored as a pd.Series
# Let's now create an empty column for the Celsius temperatures and update the values into that column by using our function.

# Create an empty column for the data
col_name = 'Celsius'
data[col_name] = None

# Iterate ove rows
for idx, row in data.iterrows():
    # Convert the Fahrenheit temperature of the row into Celsius
    celsius = fahrToCelsius(row['TEMP'])
    # Add that value into 'Celsius' column using the index of the row
    data.loc[idx, col_name] = celsius
print(data.head())            

# Great! Now we have converted our temperatures into Celsius by using the function that we created ourselves.

# Hint: Using iterrows() -function is not the most efficient way of using your self-made functions. In Pandas, there is a function called ``apply()`` 
# that takes advantage of the power of numpy when looping, and is hence much faster which can give a lot of speed benefit when you have millions of rows to iterate over. 
# Below I show how to do the similar thing by using our own function with ``apply()``.
# I will make a copy of our original DataFrame so this does not affect our original data. 
# Before using this approach, we need to modify our function a bit to get things working. 
# First, we need to have a parameter called ``row`` that is used to pass the data from row into our function 
# (this is something specific to ``apply()``  -function in Pandas) and then add paramaters for passing the information about the column name that contains the temperatures in Fahrenheit,
# and the column name where the coverted temperatures will be updated (i.e. the Celsius temperatures). 
# Hence, in the end, you can see that this is a bit more generic function to use (i.e. the columns to use in the calculation are not "hard-coded").

def fahrToCelsius(row, src_col, target_col):
    """
    A generic function to convert Fahrenheit temperature into Celsius.
    
    Parameters
    ----------
    
    row: pd.Series
        Input row containing the data for specific index in the DataFrame
    
    src_col : str
        Name of the source column for the calculation. I.e. the name of the column where Fahrenheits are stored.
    
    target_col : str
        Name of the target column where Celsius will be stored.
    """
    # Convert the Fahrenheit into Celsius and update the target column value
    row[target_col] = (row[src_col]- 32) / 1.8
    return row
                                                                                                                                                                    
# Take a copy
data2 = data.copy()

# Apply our new function and update the values into a new column called ``Celsius2``
data2 = data2.apply(fahrToCelsius, src_col='TEMP', target_col='Celsius2', axis=1)

# As you can see here, we use the ``apply()`` function and as the first parameter 
# we pass the name of the function that we want to use with the ``apply()``, and then we pass the names of the source column and the target column.
# Lastly, it is important to add as a last parameter ``axis=1`` that tells for the function to apply the calculations vertically (row by row) instead of horizontally (would move from column to another).

# See the results
data2.head()

# Indeed it seems that our function worked because the values in ``Celsius`` and ``Celsius2`` columns are the same. 
# With this approach it is extremely easy to reuse our function and pass the results into another new colum e.g.
data2 = data2.apply(fahrToCelsius, src_col='TEMP', target_col='Celsius3', axis=1)
print(data2.head())

# Now we just added another column called ``Celsius3`` just by changing the value of the ``target_col`` -parameter.
# This is a good and efficient approach to use in many cases, and hence highly recommended (although it is a bit harder to understand).  


print(data.head(20))
# Let's see the change by printing the first 20 rows. Okey what we can see here, is that some of our variables are measured more often than others. 
# ``GUS`` (gust) seems to be measured only once an hour, whereas ``SPD`` (wind speed), and ``TEMP`` (temperature in Fahrenheits) seems to be measured approximately every 20 minutes (at minutes XX:00, XX:20 and XX:50). 


# Well that is a problem as we cannot compare the wind average wind speeds and the speeds during the gust. 
# How we can solve this problem is to aggregate the wind speeds into hourly level data as well so the attributes become comparable. 
# First we need to be able to group the values by hour. This can be done e.g. by slicing the date+hour time from the ``TIME`` column (i.e. removing the minutes from the end of the value)
# Doing this requires two steps:
#   1. Convert the ``TIME`` column from ``int`` into ``str`` datatype.
#   2. Include only numbers up to hourly accuracy (exclude minutes) by slicing texts

# Note: there are also more advanced functions in Pandas to do time series analysis by utilizing ``datetime`` datatype and ``resample()`` -function, but we won't cover those here. Read more information about creating `datetime index <http://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.to_datetime.html>`__ and aggregating data by time with resampling from `here <https://pandas.pydata.org/pandas-docs/stable/timeseries.html#resampling>`__ if you are interested. 

# Let's convert the time into string 
data['TIME_str'] = data['TIME'].astype(str)
print(data.head())
print(data['TIME_str'].dtypes)
print(type(data.loc[0, 'TIME_str']))

# Okey now we have the times as strings and we can slice them into hourly level by including only 10 first characters from the text.
data['TIME_h'] = data['TIME_str'].str.slice(start=0, stop=10)
print(data.head())

# Nice! Now we have information about time on an hourly basis. 

# Next we want to calculate the average temperatures, wind speeds, etc. on an hourly basis. 
# This can be done by 
# 1. **grouping the data** based on hourly values 
# 2. Iterating over those groups and calculating the avegare values of our attributes
# 3. Inserting those values into a new DataFrame where we store the aggregated data

# Let's first create a new **empty** DataFrame where we will store our aggregated data 
aggr_data = pd.DataFrame()

# Let's then group our data based on ``TIME_h`` attribute that contains the information about the date + hour 
grouped = data.groupby('TIME_h')

# Let's see what we have now
print(type(grouped))
print(len(grouped))

# Okey, interesting. Now we have a new object with type ``DataFrameGroupBy``. And it seems that we have 6549 individual groups in our data.
# Let's see what we can do with it.

# As you might have noticed earler, the first hour in hour data is ``2017010122``. 
# Let's now see what we have on hour ``grouped`` e.g. on that first hour ``2017010122``.
# We can get the values of that hour from ``DataFrameGroupBy`` -object with ``get_group()`` -function.
time1 = '2017080100'
group1 = grouped.get_group(time1)
print(group1)

# Ahaa! Okey so as we can see, a single group contains a **DataFrame** with values only for that specific hour. 
# That is really useful because now we can calculate the average values for all weather measurements that we have. 

# We can do that by using the ``mean()`` -function that we already used during the Lesson 5.
# Let's calculate the mean for attributes ``DIR``, ``SPEED``, ``GUST``, and ``TEMP``
mean_cols = ['DIR', 'SPEED', 'GUST', 'TEMP']
mean_values = group1[mean_cols].mean()
print(mean_values)

# Nice, now we have averaged our data. What is missing here is the information about the time that we at the moment have stored in ``time1`` variable.
# We can insert that into our ``mean_values`` Series so that we have temporal information also associated with our data.
mean_values['TIME_h'] = time1
print(mean_values)
           
# Perfect! Now we have also time information there. The last thing to do is to add these mean values into our DataFrame that we created.
# That can be done with ``append()`` -function in a quite similar manner as with Python lists.
# In Pandas the data insertion is not done **inplace** (as when appending to Python lists) so we need to specify that we are updating the aggr_data (using the ``=`` sign)
# We also need to specify that we ignore the index values of our original DataFrame (i.e. the indices of ``mean_values``)
aggr_data = aggr_data.append(mean_values, ignore_index=True)
print(aggr_data)

# Now we have a single row in our new DataFrame where we have aggregated the data based on hourly mean values. 
# Next we could continue doing and insert the average values from other hours in a similar manner but, of course, that is not
# something that we want to do manually (would require repeating these steps hundreds of times). 
# Luckily, we can actually iterate over all the groups that we have in our data and do these steps using a for loop. 

# When iterating over the groups in our ``DataFrameGroupBy`` object 
# it is noteworthy to understand that a single group in our ``DataFrameGroupBy`` actually contains not only the actual values, but also information about the ``key`` that was used to do the grouping.
# Hence, when iterating over the data we need to assign the ``key`` and the values into separate variables.
# Let's see how we can iterate over the groups and print the key and the data from a single group. 
for key, group in grouped:
    print(key)
    print(group)
    break

# Okey so from here we can see that the ``key`` contains the value ``2017010122`` that is the same
# as the values in ``TIME_h`` column. Meaning that we, indeed, grouped the values based on that column.

# Let's see how we can create a DataFrame where we calculate the mean values for all those weather attributes that we were interested in. 
# I will repeate slightly the earlier steps so that you can see the full picture better.

# Create an empty DataFrame for the aggregated values
aggr_data = pd.DataFrame()

# The columns that we want to aggregate
mean_cols = ['DIR', 'SPEED', 'GUST', 'TEMP']

# Iterate over the groups
for key, group in grouped:
    # Aggregate the data 
    mean_values = group[mean_cols].mean()
    
    # Add the ´key´ (i.e. the time information) into the aggregated values
    mean_values['TIME_h'] = key
    
    # Append the aggregated values into the DataFrame
    aggr_data = aggr_data.append(mean_values, ignore_index=True)
    
# Print the data
print(aggr_data)   

