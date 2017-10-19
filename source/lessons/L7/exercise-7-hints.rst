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
