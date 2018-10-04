Exercise 5
==========

.. warning::

    Please note that **we provide assignment feedback only for students enrolled in the course at the University of Helsinki**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 5 by** `accepting the GitHub Classroom assignment <https://classroom.github.com/a/xlPEDOv7>`__.

    **Exercise 5 is due by the start of lecture in week 6**.

You can also take a look at the open course copy of `Exercise 5 in the course GitHub repository <https://github.com/Geo-Python-2018/Exercise-5>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.


Exercise 5 hints for Pandas
---------------------------

Below are some tips for working on Exercise 5.

Selecting date ranges


In the Problem 4 part 2, the aim is to select rows that belong to certain month. The key here is to understand that
the data values in ``YR--MODAHRMN`` column are integer numbers using a format ``YYYYMMDDHHmm`` where ``YYYY`` is the
year of the observation, ``MM`` is the month, ``DD`` is the day, ``HH`` is the hour, and ``mm`` is the minute.

Using these values it is possible to make simple mathematical queries such as finding the values starting from August:

.. code:: python

    august_values = data.loc[data['YR--MODAHRMN'] >= 201708010000]

Here, the value ``201708010000`` corresponds to the first day of August at 00:00 hour.

Exercise 5 hints for NumPy
---------------------------

Formatting output to written to files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can specify the format of the saved data using the ``fmt`` parameter with ``np.savetxt()``.
Let's consider an example.
We have two columns in a NumPy array called ``data`` that we would like to output to a file called ``test.csv``.
The first column contains integer values, the second are floating point values that we would like to round to 4 decimal places.
We could create a comma-separated data file as follows:

.. code:: python

    np.savetxt('test.csv', data, delimiter=',', fmt='%i, %.4f')

In this case, the ``fmt`` parameter should contain two values separated by a comma, one for each output format.
The ``%`` sign indicates a variable for the output (one of the columns), ``i`` indicates an integer value, and ``.4f`` indicates a floating point value with 4 numbers after the decimal point.

You can find additional data about formatting output at `https://pyformat.info
<https://pyformat.info/>`_.
NumPy, for example, uses the "old" formatting style mentioned on that site.