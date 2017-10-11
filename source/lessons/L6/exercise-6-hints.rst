Hints for Exercise 6
====================

Below are some tips for working on Exercise 6.

Data format for problems 1-3
----------------------------

The first 5 rows of the data file look like the following:

.. code::

    STATION           ELEVATION  LATITUDE   LONGITUDE  DATE     PRCP     TAVG     TMAX     TMIN     
    ----------------- ---------- ---------- ---------- -------- -------- -------- -------- -------- 
    GHCND:FIE00142080         51    60.3269    24.9603 19520101 0.31     37       39       34       
    GHCND:FIE00142080         51    60.3269    24.9603 19520102 -9999    35       37       34       
    GHCND:FIE00142080         51    60.3269    24.9603 19520103 0.14     33       36       -9999    

As you can see, we have rainfall data (``PRCP``) in inches, and temperature data (``TAVG``, ``TMAX``, and ``TMIN``) in degrees Fahrenheit.
Dates of the observations are given in the format YYYYMMDD.
No-data values are indicated with ``-9999``.

Reading in fixed-width text files
---------------------------------

Rather than having separation by commas, our data file this week has a variable number of spaces between values.
Previously, we read in comma-separated values using the option ``sep=','`` for the Pandas ``read_csv()`` function.
For a variable number of spaces, we can simply change the ``sep`` value to be ``sep='\s+'``.

Skipping the second row of a file
---------------------------------

The ``skiprows=n`` option of the Pandas ``read_csv()`` function is an easy way to skip the first *n* rows of a file when reading it.
If we wanted to skip the first two rows of our data file, we could thus use ``skiprows=2``.
The value for ``n``, however, need not be a single value, but can also be given in the form of a list.
In this way, one can skip reading the second row of a file using a list with an index value for the second row.
In other words, you can use ``skiprows=[1]``.

