# -*- coding: utf-8 -*-
"""
Preparations for Lesson 5. Here I aim to understand the data better to think about lesson / exercise contents. 

Created on Tue Oct  3 10:31:39 2017

@author: hentenka
"""

import pandas as pd

# Filepaths
input_fp = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Geo-Python\admin-Geo-Python-2017\data-to-consider\Lesson-5\Kumpula-June-2016-w-metadata.txt"

# Read data
data = pd.read_csv(input_fp, sep=',', skiprows=8)

# Doing calculations in Pandas
# ----------------------------

# We can create an empty column into our DataFrame and set some default value for it (in this case value 0)
data['DIFF'] = 0.0

# Let's check the datatype
print(data['DIFF'].dtypes)

# Okey so we see that Pandas created a new column and recognized automatically that the data type is float

# We can also easily do calculations inside our DataFrame. Let's update the column ``DIFF`` by calculating the difference between MAX and MIN columns to get an idea how much the temperatures have
# been varying during different days. Calculations can be done with following syntax where we first specify the column that we want to update (i.e. ``DIFF``) and then do the actual calculation 
# using the columns that we have in our DataFrame.
data['DIFF'] = data['MAX'] - data['MIN']

# Let's see what we have.
print(data)

# Okey so now we can see that the calculations were inserted into the ``DIFF`` column as planned. Notice that you can do calculations directly without first creating the column. Let's test
# this by calculating the difference between minimum temperature (``MIN``) and the mean temperature of the daty (``TEMP``). 
data['DIFF_Min'] = data['TEMP'] - data['MIN']

print(data)

# In a similar manner, you can do calculations using as many columns as you need and using the basic math algebra (subtracttion, addition, multiplication, division, exponentiation, etc.). 
# We can for example convert the Fahrenheit temperatures into Celsius using the formula that we have used already multiple times
data['TEMP_Celsius'] = (data['TEMP'] - 32) / (9/5) 

print(data)

# Indexing and selecting data 
# ---------------------------

# It is quite common procedure in programming that you want to select only specific rows from your data. 
# In Pandas there are different ways of doing this. 

# One common way of selecting only specific rows from your DataFrame is done via index slicing to extract part of the DataFrame. 
# Let's select the first five rows and assign them to a variable called ``rows5``. 
rows5 = data[0:5]

# Slicing is done in a similar manner as with normal Python lists, i.e. you specify index range you want to select inside the square brackets ``selection = dataFrame[start_index:stop_index]`` 
print(rows5)

# You can also select an individual row from specific position using ``.loc[]`` indexing. Here we select all the values from row 8.
row8 = data.loc[8]
print(row8)

# ``.loc[]`` indexing returns the values from that position as a pd.Series where the indices are the column names. Hence, you can access the value of an individual column 
# by referring to its index using either one of following commands:
print(row8['TEMP'])    
print(row8.YEARMODA)

# With ``.loc[]`` indexing it is also possible to select specific rows from a certain column only (a process called multi-indexing). 
temp_row8 = data.loc[8, 'TEMP']
print(temp_row8)

# It is also possible to select multiple rows simultaniously. Here, we select only temperature values (``TEMP``) between indices of 5-10:

temps_5to10 = data.loc[5:10, 'TEMP']
print(temps_5to10)

# It is also possible to select multiple columns using those same indices. Here, we select ``TEMP`` and the ``TEMP_Celsius`` columns by passing them inside a list: `` .loc[start_index:stop_index, list_of_columns]`` :
temps_5to10 = data.loc[5:10, ['TEMP', 'TEMP_Celsius']]
print(temps_5to10)

# Filtering data and updating data 
# --------------------------------

# One really useful feature in Pandas is the ability to easily filter and select rows based on certain criteria using ``.ix[]`` indexing. 
# The following example shows how to select rows when the Celsius temperature has been higher than 15 degrees into variable ``w_temps`` (warm temperatures).
w_temps = data.ix[data['TEMP_Celsius'] > 15]
print(w_temps)

# It is also possible to combine multiple criteria at the same time. Here, we select temperatures above 15 degrees that were recorded on the second half of June in 2016 (i.e. ``YEARMODA >= 20160615 ``). 
# Combining multiple criteria can be done with `&` operator (AND) or `|`operator (OR).
w_temps2 = data.ix[(data['TEMP_Celsius'] > 15) & (data['YEARMODA'] >= 20160615)]
print(w_temps2)

# Here, we see that now we have made a selection of our DataFrame with only rows where the ``TEMP_Celsius`` is above 15 and the dates in ``YEARMODA`` column start from 15th of June. 

# Notice, that the index values (numbers on the left) are still showing the positions from the original DataFrame. It is possible to **reset** the index using ``reset_index()`` function that
# might be useful in terms of being able to slice the data in a similar manner as above. By default the ``reset_index()`` would make a new column called ``index`` to keep track on the previous
# index which might be useful in some cases but here not, so we can omit that by passing parameter ``drop=True``. 

w_temps2 = w_temps2.reset_index(drop=True)

# Dealing with missing values
# ---------------------------

# Next we update the first five values of ``TEMP_Celsius`` in our ``w_temps_2h`` DataFrame to be NaN (the value could be anything). This can be done by utilizing the ``loc[]`` indexing. 
# Notice here that you don't necessary need to specify the starting_index (0) but you can leave it empty.
w_temps2.loc[:4, 'TEMP_Celsius'] = None
print(w_temps)

# Now we can see that we have some missing data in our DataFrame. 

# Having missing data in your datafile is really common situation and typically you want to deal with it somehow. Common procedures to deal with NaN is to either **remove** them from
# the DataFrame or **fill** them with some value. In Pandas both of these options really easy to do. 

# Let's first see how we can remove the NoData values (i.e. clean the data) using ``dropna()`` function
w_temps_clean = w_temps2.dropna()
print(w_temps_clean)

# As you can see, as a result we now have a DataFrame without the NoData values 

# Other option is to fill the NoData with some value using ``fillna()`` -function. Here we fill it with value 0.
w_temps_na_filled = w_temps2.fillna(0)
print(w_temps_na_filled)

# As a result we now have a DataFrame where NoData values are filled with value 0.00000

# Sorting data
# ------------

# Quite often it is useful to be able to sort your data (descending/ascending) based on values in some column
# This can be easily done with Pandas using  ``sort_values(by='YourColumnName')`` function.

# Let's first sort the values on ascending order based on the ``TEMP`` column
print(data.sort_values(by='TEMP'))

# Of course, it is also possible to sort them in descending order with ``ascending=False`` parameter
print(data.sort_values(by='TEMP', ascending=False))


# Rounding and finding unique values
# ----------------------------------

# It is possible to round values easily by using ``round()`` function. Here we round the Celsius temperatures with 0-decimals
data['Celsius_rounded'] = data['TEMP_Celsius'].round(0)
print(data)

# Now we have rounded our Celsius temperatures. Sometimes it is useful to extract the unique values that you have in your column. 
# We can do that by using ``unique_values()`` function
unique = data['Celsius_rounded'].unique()
print(unique)

# As a result we get an array of unique values in that column. We can also see all those values by printing them as a list
print(list(unique))

# How many days with different mean temperature did we have in June 2016? We can check that!
uniq_temp_days = len(unique)
print("There were", uniq_temp_days, "days with different mean temperatures in June 2016.")

# Writing data
# ------------

# Lastly, it is of course important to be able to write the data that you have analyzed into your computer. This is really handy in Pandas as it supports many different data formats
# by default (see more info here). The most typical output format by far is CSV file. Function ``to_csv()`` can be used to easily save your data in CSV format. 

# Let's first save the data from our ``data`` DataFrame into a file called ``Kumpula_temp_results_June_2016.csv`` . 
output_fp = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Geo-Python\admin-Geo-Python-2017\data-to-consider\Lesson-5\Kumpula_temps_June_2016.csv"
data.to_csv(output_fp, sep=',')

# Nice, now we have the data from our DataFrame saved to a file:

# As you can see, the first value in the datafile contains now the index value of the rows. There are also quite many decimals present in the new columns 
# that we created. Let's deal with these and save the temperature values from ``w_temps`` DataFrame without the index and with only 1 decimal in the floating point numbers.
output_fp2 = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Geo-Python\admin-Geo-Python-2017\data-to-consider\Lesson-5\Kumpula_temps_above15_June_2016.csv"
data.to_csv(output_fp2, sep=',', index=False, float_format="%.1f")

# Omitting the index can be with ``index=False`` parameter. Specifying how many decimals should be written can be done with ``float_fomat`` -parameter where text ``%.1f`` defines Pandas to use 1 decimals 
# in all columns when writing the data to a file (changing the value 1 to 2 would write 2 decimals etc.)

# As a results you have a "cleaner" output file without the index column, and with only 1 decimal for floating point numbers. 


