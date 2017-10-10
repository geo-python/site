Hints for Exercise 6
====================

Below are some tips for working on Exercise 6.

Data format for problems 1 and 2
--------------------------------

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

