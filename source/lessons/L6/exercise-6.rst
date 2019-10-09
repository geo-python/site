Exercise 6
==========

.. note::

    Please complete this exercise by **09:15 Wednesday, 16 October 2019**.


.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 6 by** accepting `the GitHub Classroom assignment <https://classroom.github.com/a/ooOQQI1V>`__.


You can also take a look at the open course copy of `Exercise 6 in the course GitHub repository <https://github.com/Geo-Python-2019/Exercise-6>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

.. warning::

    Please note that **we provide assignment feedback only for students enrolled in the course at the University of Helsinki**.

Cloud computing environments
-----------------------------

.. image:: https://img.shields.io/badge/launch-binder-red.svg
   :target: https://mybinder.org/v2/gh/Geo-Python-2019/Binder/master?urlpath=lab

.. image:: https://img.shields.io/badge/launch-CSC%20notebook-blue.svg
   :target: https://notebooks.csc.fi/#/blueprint/d71cd2d26d924f48820dc22b67a87d8e

Exercise 6 hints
-----------------

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
For a variable number of spaces we can either use the ``sep`` or ``delim_whitespace parameter``; ``sep='\s+`` or ``delim_whitespace=True`` will work, but not both.
In this case, we suggest using ``delim_whitespace``.

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
