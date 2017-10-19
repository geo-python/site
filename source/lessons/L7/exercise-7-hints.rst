Hints for Exercise 7
====================

Converting a column of date-strings into datetime format
--------------------------------------------------------

In some cases Pandas cannot understand and parse automatically the date information from a column when you read the
data with ``read_csv()`` function. In these cases, you need to parse the date information afterwards.

Let's see an example with following data

.. code::

    DATE, Value
    "201401", 1
    "201402", 2
    "201403", 3
    "201404", 5

.. ipython:: python
    :suppress:

        import os
        import pandas
        fp = os.path.join(os.path.abspath('data'), 'L7', "hintData.txt")

Let's try to read the data and parse the date.

.. ipython:: python

    data = pd.read_csv(fp, sep=',', parse_dates=['DATE'])
    data.head()
    data.dtypes

As we can see from above, Pandas was not able to convert the datatype of ``DATE`` into ``datetime`` format.
This is because the DATE values does not include information about the day of the year but only the year and month.

There is a way to tell to Pandas to read the ``DATE`` information with a custom format such as the one we have here
with ``pd.to_timestamp()`` function where we can specify with ``format`` parameter the custom format how the dates
are represented in the data. Consider following example:

.. ipython:: python

    data['datetime'] =  pd.to_datetime(data['DATE'], format='%Y%m')
    data.head()
    data.dtypes

Great, now we have the data in ``datetime`` format!

Creating an empty DataFrame with a datetime index
-------------------------------------------------

For Problem 2 in this exercise you are asked to calculate average seasonal ages for each year in our data file.
The easiest way to do this is to create an empty DataFrame to store the seaonal temperatures, with one temperature for each year and season.
Thus, the DataFrame should have columns for each season and the date as an index.
In order to do this, we'll need first to create a variable to store the dates for the index, then create the DataFrame using that index.
Let's consider an example for my world, where there are two seasons: ``coldSeason`` and ``warmSeason``.
For each season, I want list the number of times I wore a jacket, with data from the past 4 years.
I can start by making a variable with 1 date for each of the past 4 years using the Pandas ``pd.date_range()`` function.

.. ipython:: python

    timeIndex = pd.date_range('2014', '2017', freq='AS')
    print(timeIndex)

As you can see, we now have a variable ``timeIndex`` in the Pandas datetime format with dates for January 1 of the past 4 years.
The starting and ending years are clear, and the ``freq='AS'`` indicates the frequecy of dates between the listed starting and ending times.
In this case, ``AS`` refers to annual values (1 time per year) at the start of the year.

With the ``timeIndex`` variable, we can now create our empty DataFrame to store the seasonal jacket numbers using the Pandas ``pd.DataFrame()`` function.

.. ipython:: python

    seasonData = pd.DataFrame(index=timeIndex, columns=['coldSeason', 'warmSeason'])
    print(seasonData)

Now we have our empty DataFrame where I can fill in the number of times I needed a jacket in each season using the date index!

Slicing up the seasons
----------------------

The other main task in Problem 2 is to sort values from the different months into seasonal average values.
There are several ways in which this can be done, but one nice way to do it is using a ``for`` loop to loop over each year of data you consider and then fill in the seasonal values for that year.
For each year, you want to identify the slice of dates that correspond to that season, calculate their mean, then store that result in the corresponding location in the new DataFrame created in the previous hint.
For the ``for`` loop itself, it may be easiest to start with the second full year of data (1953), since we do not have temperatures for December of 1951.
If you loop over the years from 1953-2016, you can then easily calculate the seasonal average temperatures for each season.
For the winter, you can use ``year - 1`` to find the temperature for December, assuming ``year`` is your variable for the current year in your ``for`` loop.

In `this week's lesson <https://geo-python.github.io/2017/lessons/L7/pandas-plotting.html#selecting-data-based-on-time-in-pandas>`__ we saw how to select a range of dates, but we did not cover how to take the mean value of the slice and store it.
Because a slice of a DataFrame is still a DataFrame object, we can simply use the ``.mean()`` method to calculate the mean of that slice.

.. code:: python

    meanValue = dataFrame['2016-12':'2017-02']['TEMP'].mean()

This would assign the mean value for the ``TEMP`` field between December 2016 and February 2017 to the variable ``meanValue``.
In terms of storing the output value, we can use the ``DataFrame.loc()`` function.
For example:

.. code:: python

    dataFrame.loc[year, 'coldSeason'] = 5

This would store the value ``5`` in the column ``coldSeason`` at index ``year`` of ``dataFrame``.
That's a tricky sentence, but hopefully the idea is clear :).

Labels and legends
------------------

In the plot for Problem 2 you're asked to include a line legend for each subplot.
To do this, you need to do two things:

1. You need to add a ``label`` value when you create the plot using the ``plt.plot()`` function.
   This is as easy as adding a parameter that say ``label='some text'`` when you call ``plt.plot()``.
2. You'll need to display the line legend, which can be done by calling ``plt.legend()`` for each subplot.
