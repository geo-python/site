Hints for Exercise 5
====================

Below are some tips for working on Exercise 5.

Selecting date ranges
---------------------

In the Problem 4 part 2, the aim is to select rows that belong to certain month. The key here is to understand that
the data values in ``YR--MODAHRMN`` column are integer numbers using a format ``YYYYMMDDHHmm`` where ``YYYY`` is the
year of the observation, ``MM`` is the month, ``DD`` is the day, ``HH`` is the hour, and ``mm`` is the minute.

Using these values it is possible to make simple mathematical queries such as finding the values starting from August:

.. code:: python

    august_values = data.ix[data['YR--MODAHRMN'] >= 201708010000]

Here, the value ``201708010000`` corresponds to the first day of August at 00:00 hour.