Introduction to NumPy
=====================

Contents
--------

1. `Downloading and extracting this week's lesson
   data <#downloading-and-extracting-the-data>`__
2. `Overview of NumPy and how it is imported <#import>`__
3. `Reading data file with NumPy <#load-file>`__
4. `NumPy data types & type conversions <#data-types>`__
5. `Indices and selecting data using index slicing <#index>`__

-  `Task: Iterate columns and change data type <#task1>`__

6. `Useful NumPy functions <#functions>`__

Downloading and extracting the data
-----------------------------------

1. You can start by downloading `this week's volcano data zip
   file <../Data/volcano-data.zip>`__, which we will be using for this
   lesson.

-  The Firefox browser will likely download the file to the
   ``Downloads`` directory in the home directory of your computer
   instance. If so, you should move the file into the home directory
   using the file browser.

2. Once you have moved the ``volcano-data.zip`` file into your home
   directory, you can unzip the file using the ``unzip`` command in the
   Terminal window.

   .. code:: bash

       $ cd $HOME
       $ unzip volcano-data.zip
       $ ls volcano-data
       GVP-Volcano-Lat-Lon-Elev.csv GVP-Volcano-List.csv GVP_Volcano_List.xls

   You should now have a directory titled ``volcano-data`` in your home
   directory. It contains three files from `version 4.5.1 of the
   Smithsonian Institution's Holocene volcano database (updated
   23.9.2016) <http://volcano.si.edu/list_volcano_holocene.cfm>`__.
   **Note**: These files have the same names, but differ slightly from
   those used last week in that no data has been removed from the files.
   The three files are:

-  ``GVP-Volcano-List.csv``: The complete Holocene volcano database file
   in ``.csv`` format and with header lines. **Note**: Values are
   separated by semicolons (``;``) in this version of the file rather
   than the commas (``,``).
-  ``GVP-Volcano-List.xls``: The Excel version of the complete Holocene
   volcano database.
-  ``GVP-Volcano-Lat-Lon-Elev.csv``: The volcano ID, latitude, longitude
   and elevation for all volcanoes in the Holocene volcano database.
   There is no header in this file and values are separated by commas
   (``,``).

Introducing NumPy
-----------------

NumPy is a library for Python designed for efficient scientific
(numerical) computing. It is an essential library in Python that is used
under the hood in many other modules. Here, we willl get a sense of a
few things NumPy can do.

1. To start using the NumPy library we will need to ``import`` it.

``python   >>> import numpy as np   >>>`` Note that we've imported NumPy
a bit differently this time. The ``import library as`` syntax can be
used to give the library a different name in memory. Since we may want
to use NumPy many time, shortening ``numpy`` to ``np`` is helpful.

2. Now we'll import an example data file.

``python   >>> data = np.loadtxt(fname='GVP-Volcano-Lat-Lon-Elev.csv', delimiter=',')   >>> print(data)   [[  2.10010000e+05   5.01700000e+01   6.85000000e+00   6.00000000e+02]    [  2.10020000e+05   4.57750000e+01   2.97000000e+00   1.46400000e+03]    [  2.10030000e+05   4.21700000e+01   2.53000000e+00   8.93000000e+02]    ...,    [  3.90829000e+05  -6.41500000e+01  -5.77500000e+01   1.63000000e+03]    [  3.90847000e+05  -6.20200000e+01  -5.76700000e+01   5.49000000e+02]    [  6.00000000e+05   0.00000000e+00   0.00000000e+00   0.00000000e+00]]``
Again, the data above is probably not very clear at this point, but is
an example of data from the Smithsonian Institution's Global Volcanism
Program. Here, we have the ID number, latitude, longitude, and elevation
of Holocene volcanoes in the database. Let's see what we can do with
this information.

3. First off, you may notice we've used NumPy to read in the data. What
   does that mean for us?

``python   >>> type(data)   numpy.ndarray`` OK, so we have something new
here. NumPy has its own data types that are part of the module. In this
case, our data is stored in an NumPy *n*-dimensional array.

4. How much data do we have in our ``data`` variable?

``python   >>> print(data.shape)   (1520, 4)`` 1520 rows of data, 4
columns. ``shape`` is a *member* or *attribute* of ``data``, and is part
of any NumPy ``ndarray``. Printing ``data.shape`` tells us the size of
the array.

5. We can also check the data type of our data-columns by calling
   ``data.dtype``

``python   >>> print(data.dtype)   float64`` Okey, so it seems that all
the data in our file is float data type, i.e., decimal numbers (stored
with a precision of 64 bytes).

6. It is also possible to change the data type of the data which can be
   useful sometimes. Let's take a copy of our data and convert our
   dataset into integer numbers

``python   # Take a copy   >>> copy = data.copy()   # Lets convert the data into integer numbers   >>> copy = copy.astype(int)    >>> print(copy)   [[210010     50      6    600]    [210020     45      2   1464]    [210030     42      2    893]    ...,    [390829    -64    -57   1630]    [390847    -62    -57    549]    [600000      0      0      0]]``

7. Within the array, we can find any value by using it's *indices*.

``python   >>> data[0,0]   210010.0`` This gives us the value stored in
the first row and first column of ``data``. Note that to refer to a
location in an array you use the square brackets ``[ ]`` just like for
lists. Remember, index values **start at zero, not one**, and the first
row and column refers to the top left value in the array. What will
happen if we try to find ``data[1520,0]``? Try it!

7. 1520 volcanoes is quite a few to deal with at the same time. We can
   explore our data more easily by using *index slicing* to extract part
   of the array. Let's start with just the latitude and longitude for
   the first five rows.

``python   >>> data[0:5, 1:3]   array([[ 50.17 ,   6.85 ],          [ 45.775,   2.97 ],          [ 42.17 ,   2.53 ],          [ 38.87 ,  -4.02 ],          [ 43.25 ,  10.87 ]])``
Nice! Note that in this case, the range of index values for the first 5
rows is 0-5. The data extracted will start at ``0`` and go up to, but
not include ``5``. Be careful with this. We can also extract data for
all columns without listing any index range at all.

``python   >>> data[0:2, :]   array([[  2.10010000e+05,   5.01700000e+01,   6.85000000e+00,             6.00000000e+02],         [  2.10020000e+05,   4.57750000e+01,   2.97000000e+00,             1.46400000e+03]])``
Obviously, this can be useful.

8. We can also use *index slicing* to separate our data into different
   variables to make it easier to work with.

``python   >>> Latitude = data[:,1]   >>> print(Latitude)   [ 50.17   45.775  42.17  ..., -64.15  -62.02    0.   ]``
For many data files, this is a nice way to interact with only the data
of your own interest.

Task 1: 
--------

Create a list called ``dataStr`` where you append all of our ``data``
array columns one by one in string (``str``) format. Use a ``for`` loop
for iterating over the columns.

Useful functions 
-----------------

1. It is common to need to create your own arrays not from a data file,
   but to make a variable that has a range from one value to another. If
   we wanted to calculate the ``sin()`` of a variable ``x`` at 10 points
   from zero to 2 \* pi, we could do the following.

``python   >>> x = np.linspace(0., 2 * np.pi, 10)   >>> print(x)   [ 0.          0.6981317   1.3962634   2.0943951   2.7925268   3.4906585     4.1887902   4.88692191  5.58505361  6.28318531]   >>> y = np.sin(x)   >>> print(y)   [  0.00000000e+00   6.42787610e-01   9.84807753e-01   8.66025404e-01      3.42020143e-01  -3.42020143e-01  -8.66025404e-01  -9.84807753e-01     -6.42787610e-01  -2.44929360e-16]``
In this case, ``x`` starts at zero and goes to 2 \* pi in 10 increments.
Alternatively, if we wanted to specify the size of the increments for a
new variable ``x2``, we could use the ``np.arange()`` function.

``python   >>> x2 = np.arange(0.0, 2 * np.pi, 0.5)   >>> print(x2)   [ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6. ]``
In this case, ``x2`` starts at zero and goes to the largest value that
is smaller than 2 \* pi by increments of 0.5. Both of these types of
array options are useful in different situations.

10. Like normal variables, array variables can also be used for various
    mathematical operations.

``python   >>> doublex = x * 2.0   >>> print(doublex)   [  0.           1.3962634    2.7925268    4.1887902    5.58505361      6.98131701   8.37758041   9.77384381  11.17010721  12.56637061]``

11. In addition to the *attributes* we saw prevously for NumPy
    ``ndarray`` variables, there are also many *methods* that are part
    of the ``ndarray`` data type.

``python   >>> print(x.mean())   3.14159265359   >>> print(doublex.mean())   6.28318530718``
No surprises here. If we think of *variables* as nouns, *methods* are
verbs, actions for the variable values. **NOTE**: When using methods,
you always include the parentheses ``()`` to be clear we are referring
to a *method* and not an *attribute*. There are many other useful
``ndarray`` methods, such as ``x.min()``, ``x.max()``, and ``x.std()``
(standard deviation).

12. *Methods* can also act on part of an array.

``python   >>> print(x[0:5].mean())   1.3962634016``

**Next**: `Exercise 6: Analysing data using
NumPy <https://classroom.github.com/assignment-invitations/91b6f2cfe199617bd94a971f467457be>`__\ 
**Home**: `Lesson 6 main
page <https://github.com/Python-for-geo-people/Lesson-6-Intro-to-NumPy>`__\ 
