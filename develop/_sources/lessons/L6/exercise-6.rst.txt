Exercise 6
==========

.. warning::

    Please note that **we provide assignment feedback only for students enrolled in the course at the University of Helsinki**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 6 by** accepting `the GitHub Classroom assignment <https://classroom.github.com/a/afub-sCk>`__.

    **Exercise 6 is due by 16:00 on Wednesday 17.10**.

You can also take a look at the open course copy of `Exercise 6 in the course GitHub repository <https://github.com/Geo-Python-2018/Exercise-6>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

Exercise 6 hints for Pandas
---------------------------

Data format for problems 1-3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first 5 rows of the data file look like the following:

.. code:: python

    STATION           ELEVATION  LATITUDE   LONGITUDE  DATE     PRCP     TAVG     TMAX     TMIN     
    ----------------- ---------- ---------- ---------- -------- -------- -------- -------- -------- 
    GHCND:FIE00142080         51    60.3269    24.9603 19520101 0.31     37       39       34       
    GHCND:FIE00142080         51    60.3269    24.9603 19520102 -9999    35       37       34       
    GHCND:FIE00142080         51    60.3269    24.9603 19520103 0.14     33       36       -9999    

As you can see, we have rainfall data (``PRCP``) in inches, and temperature data (``TAVG``, ``TMAX``, and ``TMIN``) in degrees Fahrenheit.
Dates of the observations are given in the format YYYYMMDD.
No-data values are indicated with ``-9999``.

Reading in fixed-width text files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rather than having separation by commas, our data file this week has a variable number of spaces between values.
Previously, we read in comma-separated values using the option ``sep=','`` for the Pandas ``read_csv()`` function.
For a variable number of spaces, we can simply change the ``sep`` value to be ``sep='\s+'``.

Skipping the second row of a file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``skiprows=n`` option of the Pandas ``read_csv()`` function is an easy way to skip the first *n* rows of a file when reading it.
If we wanted to skip the first two rows of our data file, we could thus use ``skiprows=2``.
The value for ``n``, however, need not be a single value, but can also be given in the form of a list.
In this way, one can skip reading the second row of a file using a list with an index value for the second row.
In other words, you can use ``skiprows=[1]``.

Joining data from one DataFrame to another
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One quite useful functionality in Pandas is the ability to conduct a **table join**
where data from one DataFrame is merged with another DataFrame based on a common **key**.
Hence, making a table join requires that you have at least one common variable in both
of the DataFrames that can be used to combine the data together.

Consider a following example. Let's first create some test data to our DataFrames.

.. ipython:: python
    :suppress:

        import pandas as pd

.. ipython:: python

    data1 = pd.DataFrame(data=[['20170101', 'Pluto'], ['20170102', 'Panda'], ['20170103', 'Snoopy']], columns=['Time', 'Favourite_dog'])
    data2 = pd.DataFrame(data=[['20170101', 1], ['20170101', 2], ['20170102', 3], ['20170104', 3], ['20170104', 8]], columns=['Time', 'Value'])
    data1
    data2

As we can see here, there different number of rows in the DataFrames. Important thing to notice is that there seems to be a common column called ``Time`` that we can use to
join these DataFrames together. In Pandas we can conduct a table join with ``merge`` -function. Consider following example where we join the data **from** ``data2`` DataFrame **to** ``data1`` DataFrame.

.. ipython:: python

    join1 = data1.merge(data2, on='Time')
    join1

Ahaa! Now we can see that we managed to get the ``Value`` column from ``data2`` in our ``data1`` DataFrame (here we just assigned those values to a new variable ``join1``).
Notice also that the ``Pluto`` is two times in the joined DataFrame although, it was only once in the original one. Hence, Pandas automatically duplicates the values in such
columns where there are more matching values in one DataFrame compared to the other.

However, it is important to notice that there were more values in the ``data2`` DataFrame than in ``data1``. The result ``join1``, does not contain the values ``3 and 8`` that were from day ``20170104`` and they were omitted.
This might be okey, but in some cases it is useful to also bring **all** values from another DataFrame even though there would not be a matching value in the column that used for making the join (i.e. the ``key``).

We can bring all the values from another DataFrame by specifyin parameter ``how='outer'``, i.e. we will make an **outer** join.
Let's consider another example with the outer join.

.. ipython:: python

    join2 = data1.merge(data2, on='Time', how='outer')
    join2

Cool! Nowe we have all the values included from both DataFrames and if Pandas did not find a common value in the ``key`` column, it still kept them and inserted ``NaN`` values into ``Favourite_dog`` column and ``Value`` column.
Overall, knowing how to conduct a table join can be really handy in many different situations.
See more examples and documentation from `official documentation of Pandas <https://pandas.pydata.org/pandas-docs/stable/merging.html>`__.

Exercise 6 hints for NumPy
--------------------------

Calculating average temperatures for each month (e.g., February 1954)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In problem 2 you're asked to calculate average temperatures for every month between 1952-2016.
There are a number of ways you can do this, like many things in Python programming.
You might be tempted to create an empty array for the temperature values for each month and year in the range of dates, but this is not an ideal solution in case there are months or years missing data (*Hint: there are*).
Instead, I would recommend a different approach where only years with data are included in the monthly averages, and we do not create the empty array first.
Below is an example of such an approach.

.. code-block:: python

    # Note 2016 is missing
    year = np.array(['2014', '2014', '2015', '2017'])
    month = np.array(['01', '01', '02', '03'])

    # Make empty lists to store temperature values and their month
    num_monthly = []

    # Loop over all unique years
    for year_now in np.unique(year):
        # Loop over all unique months
        for month_now in np.unique(month):
            # NOTE: Here you should use an array slice to get tavg values only for month_now of year_now
            #       I am just filling in the average of 10 random values for now, since I don't have tavg defined
            num_m = np.random.rand(10).mean()
            
            # Add the monthly average temperature to the temp_monthly list
            num_monthly.append(num_m)
    
    # Finally, we can convert num_monthly to a NumPy array
    num_monthly = np.array(num_monthly)

This will work even if years are missing, or listed multiple times in the data you're handling.
We could add a test to check that the array slice for a given month is not empty, to protect against the case where we were missing data for some random month during a year when we have data for other months, but don't worry about that for now.
And in case it isn't clear, ``np.array()`` converts a list to a NumPy array.

**There is one other thing you'll need to do!**
Because we need to know which month and year the average temperatures are from, you should also make two other empty lists like you would for the monthly temperatures.
In those lists you can simply store the month and year every time you store a monthly average temperature, in just the same way.
You'll also have to convert those to NumPy arrays.

Calculating average temperatures for all months (e.g., February 1952-1980)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In problem 3 you have to first find the average temperatures for each of the 12 months for the years 1952-1980.
For this you can simply us a ``for`` loop to loop over each month and find the mean temperatures for that month and all years between 1952-1980.
The lesson materials should give you some idea of how to handle this, and it is less complicated than the example from problem 2 of finding monthly average temperatures for each unique month and year.

Calculating temperatures anomalies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To find the temperature anomalies, you will need the average temperatures for the each month in the years 1952-1980 (i.e., 12 values), and the monthly average temperatures for each year and month over the years 1952-2016 (many values).
The array of anomalies itself will be the same size as the number of monthly average temperatures you found in problem 2, so you can create that in advance.
Filling the array can be done several ways, but the example below is one "simple" appraach.

.. ipython:: python
   :suppress:

    anomaly = np.zeros(6)
    ref_temps = np.array([4.6, 5.7, 6.8])
    temp_monthly = np.array([1.0, 2.3, 4.5, 6.3, 4.2, 2.7])
    month_monthly = np.array(['01', '02', '03', '01', '02', '03'])
    year_monthly = np.array(['2014', '2014', '2014', '2015', '2015', '2015'])

.. ipython:: python

    # Loop over all months
    for i in range(len(temp_monthly)):
        # Here we can use a cute little trick to find the current month to compare to for the anomaly calculation
        # month_monthly will have all of the months that correspond to the temp_monthly values.
        # If we convert '01' to an integer and subtract 1, that will allow us to compare to the first value in ref_temps, the one for January (i.e., index 0).
        ref_index = int(month_monthly[i]) - 1
        ref_temp_now = ref_temps[ref_index]
        #
        # Here you should calculate the temperature anomaly. I'm filling in 1.0 since I think you folks can handle this part :)
        anomaly[i] = 1.0

Checking your work for problem 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you want to double check that you are getting the correct answers for problem 2, you code should produce the following when you run the commands below.

.. code:: python

    print(temp_monthly[:7])
    [ 29.47826087  24.8         13.80769231  39.60714286  44.66666667  56.5  61.21428571]

.. code:: python

    print(temp_monthly_celsius[:7])
    [ -1.40096618  -4.         -10.10683761   4.22619048   7.03703704  13.61111111  16.23015873]

Checking your work for problem 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you want to double check that you are getting the correct answers for problem 3, you code should produce the following when you run the commands below.

.. code:: python

    print(ref_temps[:7])
    [ -5.87734242  -6.9904821   -3.84126984   2.42787524   9.52261307  14.71189774  16.49888143]

.. code:: python

    print(anomaly[:11])
    [ 4.47637624  2.9904821  -6.26556777  1.79831523 -2.48557603 -1.10078663 -0.2687227 -0.86436896 -1.44938108 -2.78452381 -2.7044648 ]
