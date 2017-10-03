Processing data with Pandas
===========================

Now you should know the basics of the data structures in Pandas and how to explore your data using some tools that is provided by Pandas.
Next we continue to explore some of the basic data operations that are regularly needed when doing data analysis.

Let's first read the same data as before into Pandas to have a clean start.

.. ipython:: python
   :suppress:

       import os; import pandas as pd
       fp = os.path.join(os.path.abspath('data'), 'L5', "Kumpula-June-2016-w-metadata.txt")
       dataFrame = pd.read_csv(fp, sep=',', skiprows=8)

.. code:: python

    In [1] dataFrame = pd.read_csv('Kumpula-June-2016-w-metadata.txt', sep=',', skiprows=8)


Calculating with DataFrames
---------------------------

One of the most common things to do in Pandas is to create new columns based on calculations between different variables (columns).

Creating a new column into our DataFrame is easy by specifying the name of the column and giving it some default value (in this case decimal number 0.0).

.. ipython:: python

    dataFrame['DIFF'] = 0.0
    print(dataFrame)

Let's check the datatype of our new column

.. ipython:: python

    dataFrame['DIFF'].dtypes

Okey, so we see that Pandas created a new column and recognized automatically that the data type is float as we passed a 0.0 value to it.


We can also easily do calculations inside our DataFrame. Let's update the column ``DIFF`` by calculating the difference between ``MAX`` and ``MIN`` columns to get an idea how much the temperatures have
been varying during different days. Calculations can be done with following syntax where we first specify the column that we want to update (i.e. ``DIFF``) and then do the actual calculation
using the columns that we have in our dataFrameFrame.

.. ipython:: python

    dataFrame['DIFF'] = dataFrame['MAX'] - dataFrame['MIN']
    print(dataFrame)

Okey so now we can see that the calculations were inserted into the ``DIFF`` column as planned. Notice that you can do calculations directly without first creating the column. Let's test
this by calculating the difference between minimum temperature (``MIN``) and the mean temperature of the day (``TEMP``).

.. ipython:: python

    dataFrame['DIFF_Min'] = dataFrame['TEMP'] - dataFrame['MIN']
    print(dataFrame)

As you can see, now we created directly a new column with the calculation. In a similar manner, you can do calculations using as many columns as you need and using any kind of math
algebra (e.g. subtracttion, addition, multiplication, division, exponentiation, etc.).


We can for example convert the Fahrenheit temperatures in ``TEMP`` column into Celsius using the formula that we have seen already many times:

.. ipython:: python

    dataFrame['TEMP_Celsius'] = (dataFrame['TEMP'] - 32) / (9/5)
    print(dataFrame)


Selecting data using indices
----------------------------

One quite common procedure in programming that you want to select only specific rows from your data and possibly apply some operations into those rows only.
In Pandas there are different ways of doing this.

One common way of selecting only specific rows from your DataFrame is done via **index slicing** to extract part of the DataFrame.

Let's select the first five rows and assign them to a variable called ``rows5``.

.. ipython:: python

    rows5 = dataFrame[0:5]
    print(rows5)

As you can see, slicing is done in a similar manner as with normal Python lists, i.e. you specify index range you want to select inside the square brackets
``selection = dataFrame[start_index:stop_index]``.

You can also select an individual row from specific position using ``.loc[]`` indexing. Here we select all the data values from row 8.

.. ipython:: python

    row8 = dataFrame.loc[8]
    print(row8)

``.loc[]`` indexing returns the values from that position as a ``pd.Series`` where the indices are actually the column names of those variables. Hence, you can access the value of an individual column
by referring to its index using following format (both should work):

.. ipython:: python

    print(row8['TEMP'])
    print(row8.YEARMODA)

It is also possible to select multiple rows simultaniously. Here, we select only temperature values (``TEMP``) between indices of 5-10:

.. ipython:: python

    temps_5to10 = dataFrame.loc[5:10, 'TEMP']
    print(temps_5to10)

It is also possible to select multiple columns using those same indices. Here, we select ``TEMP`` and the ``TEMP_Celsius`` columns by passing them inside a list (``.loc[start_index:stop_index, list_of_columns]``):

.. ipython:: python

    temps_5to10 = dataFrame.loc[5:10, ['TEMP', 'TEMP_Celsius']]
    print(temps_5to10)

Of course, you can also get all values from those columns. This, can be done by simply referring to the dataFrame and inserting a list of columns inside the square brackets that you want to include.

.. ipython:: python

    temps_only = dataFrame[['TEMP', 'TEMP_Celsius']]
    print(temps_only)


Filtering and updating data
---------------------------

One really useful feature in Pandas is the ability to easily filter and select rows based on certain criteria using ``.ix[]`` indexing.
The following example shows how to select rows when the Celsius temperature has been higher than 15 degrees into variable ``w_temps`` (warm temperatures).

.. ipython:: python

    w_temps = dataFrame.ix[dataFrame['TEMP_Celsius'] > 15]
    print(w_temps)

It is also possible to combine multiple criteria at the same time. Here, we select temperatures above 15 degrees that were recorded on the second half of June in 2016 (i.e. ``YEARMODA >= 20160615``).
Combining multiple criteria can be done with ``&`` operator (AND) or ``|`` operator (OR). Notice, that it is often useful to separate the different clauses inside the parentheses ``()``.

.. ipython:: python

    w_temps2 = dataFrame.ix[(dataFrame['TEMP_Celsius'] > 15) & (dataFrame['YEARMODA'] >= 20160615)]
    print(w_temps2)

Now we have a subset of our DataFrame with only rows where the ``TEMP_Celsius`` is above 15 and the dates in ``YEARMODA`` column start from 15th of June.


Notice, that the index values (numbers on the left) are still showing the positions from the original DataFrame. It is possible to **reset** the index using ``reset_index()`` function that
might be useful in some cases to be able to slice the data in a similar manner as above. By default the ``reset_index()`` would make a new column called ``index`` to keep track on the previous
index which might be useful in some cases but here not, so we can omit that by passing parameter ``drop=True``.

.. ipython:: python

    w_temps2 = w_temps2.reset_index(drop=True)
    print(w_temps2)

As can be seen, now the index values goes from 0 to 12.

Dealing with missing data
-------------------------

Next we update the first five values of ``TEMP_Celsius`` in our ``w_temps2`` DataFrame to be ``NaN`` (not-a-number). This can be done by utilizing the ``loc[]`` indexing.

.. ipython:: python

    w_temps2.loc[:4, 'TEMP_Celsius'] = None
    print(w_temps2)

Now we can see that we have some missing data in our DataFrame.

.. note::

    Notice here that you don't necessary need to specify the starting index if you select data starting from the beginning of the file (at index 0), hence you can leave it empty as in the example above.

Having missing data in your datafile is really common situation and typically you want to deal with it somehow. Common procedures to deal with NaN is to either **remove** them from
the DataFrame or **fill** them with some value. In Pandas both of these options are really easy to do.

Let's first see how we can remove the NoData values (i.e. clean the data) using ``dropna()`` function. Inside the function
you can pass with ``subset`` parameter a list of column(s) from which the NaN values should be searched from.

.. ipython:: python

    w_temps_clean = w_temps2.dropna(subset=['TEMP_Celsius'])
    print(w_temps_clean)

As you can see, as a result we now have a DataFrame without the NoData values.

Other option is to fill the NoData with some value using ``fillna()`` -function. Here we fill it with value 0.

.. ipython:: python

    w_temps_na_filled = w_temps2.fillna(0)
    print(w_temps_na_filled)

As a result we now have a DataFrame where NoData values are filled with value 0.00000.

.. warning::

    In many cases filling the data with a specific value might be dangerous because you end up modifying the actual data that might affect the results of your analysis. For example in the example above
    we would have dramatically changed the mean Celsius temperature because the 0 values are dramatically decreasing the average temperature of the month. Hence, use filling carefully.

Sorting data
------------

Quite often it is useful to be able to sort your data (descending/ascending) based on values in some column
This can be easily done with Pandas using ``sort_values(by='YourColumnName')`` -function.

Let's first sort the values on ascending order based on the ``TEMP`` column:

.. ipython:: python

    sorted_temp_a = dataFrame.sort_values(by='TEMP')
    print(sorted_temp_a)

Of course, it is also possible to sort them in descending order with ``ascending=False`` parameter:

.. ipython:: python

    sorted_temp_d = dataFrame.sort_values(by='TEMP', ascending=False)
    print(sorted_temp_d)

Rounding and finding unique values
----------------------------------

It is possible to round values easily by using ``round()`` function. Here we round the Celsius temperatures with 0-decimals

.. ipython:: python

    dataFrame['Celsius_rounded'] = dataFrame['TEMP_Celsius'].round(0)
    print(dataFrame)

Now we have rounded our Celsius temperatures. Sometimes it is useful to extract the unique values that you have in your column.
We can do that by using ``unique_values()`` -function:

.. ipython:: python

    unique = dataFrame['Celsius_rounded'].unique()
    unique

As a result we get an array of unique values in that column.

.. note::

    Sometimes if you have a long list of unique values, you don't necessary see all the unique values directly as IPython hides them. It is, however, possible to see all those values by printing them as a list:

    .. ipython:: python

        print(list(unique))

How many days with unique mean temperature did we have in June 2016? We can check that!

.. ipython:: python

    uniq_temp_days = len(unique)
    print("There were", uniq_temp_days, "days with unique mean temperatures in June 2016.")

Writing data
------------

Lastly, it is of course important to be able to write the data that you have analyzed into your computer. This is really handy in Pandas as it supports many different data formats
by default (`see more info here <pandas-overview.html#supports-data-read-write-from-multiple-formats>`__).
The most typical output format by far is CSV file. Function ``to_csv()`` can be used to easily save your data in CSV format.

Let's first save the data from our ``data`` DataFrame into a file called ``Kumpula_temp_results_June_2016.csv`` .

.. ipython:: python

    output_fp = "Kumpula_temps_June_2016.csv"
    dataFrame.to_csv(output_fp, sep=',')

Nice, now we have the data from our DataFrame saved to a file:

.. figure:: img/pandas_save_file_result_1.PNG
    :width: 500px

As you can see, the first value in the datafile contains now the index value of the rows. There are also quite many decimals present in the new columns
that we created. Let's deal with these and save the temperature values from ``w_temps`` DataFrame without the index and with only 1 decimal in the floating point numbers.

.. ipython:: python

    output_fp2 = "Kumpula_temps_above15_June_2016.csv"
    dataFrame.to_csv(output_fp2, sep=',', index=False, float_format="%.1f")

Omitting the index can be with ``index=False`` parameter. Specifying how many decimals should be written can be done with ``float_fomat`` -parameter where text ``%.1f`` defines Pandas to use 1 decimals
in all columns when writing the data to a file (changing the value 1 to 2 would write 2 decimals etc.)

.. figure:: img/pandas_save_file_result_2.PNG
    :width: 500px

As a results you have a "cleaner" output file without the index column, and with only 1 decimal for floating point numbers.

.. hint::

    It is quite common that people (especially non-programmers) want you to deliver data in MS Excel format. Saving DataFrame into Excel is also straightforward in Pandas.
    First, you need to initialize a specific ``ExcelWriter`` object, and then you specify the filename and the spreadsheet name where you want to save the DataFrame.
    Optionally, you can also omit the index and specify the float formatting as in our earlier examples:

    .. ipython:: python

       excel_output_fp = "Kumpula_temps_June_2016.xlsx"
       writer = pd.ExcelWriter(excel_output_fp)
       dataFrame.to_excel(writer, sheet_name="Kumpula_temperatures", index=False, float_format="%.1f")

    As a result you have the DataFrame in Excel format:

    .. figure:: img/pandas_save_excel_result_1.PNG
       :width: 500px
