Reading data from multiple files
================================

Sources
-------

This lesson is partially based on the `Software Carpentry
group's <http://software-carpentry.org/>`__ lessons on `Programming with
Python <http://swcarpentry.github.io/python-novice-inflammation/>`__.

Topics
------

1. `Download and extract data <#download>`__
2. `Listing files <#list-files>`__
3. `Reading data from multiple files <#read-multiple>`__

 1. Download and extract data
-----------------------------

During this demo the data is about inflammation in patients who have
been given a new treatment for arthritis that are stored in multiple
data files that are stored in comma-separated values (CSV).

1. **Download the data** (a zip-file) into the HOME folder of your
   computer instance

   -  Note: \_Mozilla may automatically donwnload the data into
      "Downloads" -folder. If so, move the \*.zip package to HOME
      folder.\_

2. Extract the data using ``unzip`` command in Terminal window:

``bash   $ cd   $ unzip python-novice-inflammation-data.zip`` 3. Now we
should have "data" folder in the HOME directory of our computer instance
with following files:

.. figure:: ../img/data-folder.PNG
   :alt: Data Folder

   Data Folder

 2. Listing files
-----------------

Listing and searching for file pathnames from file system can be done
using a specific module called
**`glob <https://docs.python.org/3/library/glob.html>`__**.

The glob library contains a function, also called glob, that finds files
and directories whose names match a pattern [0]. We provide those
patterns as strings: the character \* matches zero or more characters,
while ? matches any one character.

1. We can use this to get the names of all files in the data directory
   ('/home/geo/data'):

``python   >>> import glob   >>> print(glob.glob('/home/geo/data/*'))   ['/home/geo/data/inflammation-08.csv',    '/home/geo/data/inflammation-10.csv',    '/home/geo/data/inflammation-11.csv',    '/home/geo/data/inflammation-06.csv',    '/home/geo/data/inflammation-12.csv',    '/home/geo/data/small-03.csv',    '/home/geo/data/small-02.csv',    '/home/geo/data/inflammation-07.csv',    '/home/geo/data/inflammation-05.csv',    '/home/geo/data/small-01.csv',    '/home/geo/data/inflammation-03.csv',    '/home/geo/data/inflammation-04.csv',    '/home/geo/data/inflammation-02.csv',    '/home/geo/data/inflammation-01.csv',    '/home/geo/data/inflammation-09.csv']``

2. We can also search for only specific files and file formats. Here, we
   search for files that starts with the word 'small' and ends with file
   format '.csv':

``python   >>> print(glob.glob('/home/geo/data/small*.csv'))   ['/home/geo/data/small-03.csv', '/home/geo/data/small-02.csv', '/home/geo/data/small-01.csv']``

 3. Reading data from multiple files
------------------------------------

As the previous examples show, glob.glob’s result is a **list** of file
and directory paths in arbitrary order. This means we can loop over it
to do something with each filename in turn. What we want to do next is
to read the first line of each file and add it to a list called
``headers``.

1. Let's create a list of csv-files (called *filepaths*) that contain
   data about inflammation:

``python   >>> filepaths = glob.glob("/home/geo/data/inflammation*.csv")   >>> print(fps)   ['/home/geo/data/inflammation-08.csv',    '/home/geo/data/inflammation-10.csv',    '/home/geo/data/inflammation-11.csv',    '/home/geo/data/inflammation-06.csv',    '/home/geo/data/inflammation-12.csv',    '/home/geo/data/inflammation-07.csv',    '/home/geo/data/inflammation-05.csv',    '/home/geo/data/inflammation-03.csv',    '/home/geo/data/inflammation-04.csv',    '/home/geo/data/inflammation-02.csv',    '/home/geo/data/inflammation-01.csv',    '/home/geo/data/inflammation-09.csv']``

2. Let's create a list for headers and append the first line of each
   file into that list:

``python    >>> headers = []    >>> for fp in filepaths:            with open(fp, 'r') as f:                # Read the first line                first_line = f.readline()                # Append the first line into the list                headers.append(first_line)    >>> print(headers)    ['0,0,0,2,0,4,1,7,2,6,4,7,2,4,10,7,3,13,9,3,0,1,0,15,0,5,12,3,8,6,8,6,4,3,3,2,0,0,0,0\n',     '0,1,0,0,3,2,3,6,7,5,10,9,10,9,5,15,12,14,13,9,15,17,4,4,4,8,5,4,7,10,3,4,4,1,1,3,1,3,0,0\n',     '0,0,0,2,0,4,1,7,2,6,4,7,2,4,10,7,3,13,9,3,0,1,0,15,0,5,12,3,8,6,8,6,4,3,3,2,0,0,0,0\n',     '0,0,2,0,3,4,5,7,6,7,8,4,4,6,9,5,10,12,16,8,19,17,16,16,12,12,12,9,8,4,2,8,3,5,6,3,2,2,0,0\n',     '0,0,2,3,3,1,6,6,3,6,10,6,8,5,5,8,16,12,13,5,13,18,11,12,11,9,10,13,9,4,4,7,7,3,1,5,3,1,1,1\n',     '0,1,0,2,2,5,6,2,4,7,2,2,11,5,6,4,4,7,18,17,9,5,7,15,10,4,10,3,3,2,3,4,3,7,3,3,4,1,1,1\n',     '0,1,0,2,4,4,5,1,2,5,5,8,10,12,10,9,15,9,7,9,10,7,5,8,9,6,7,5,11,9,3,8,6,7,5,1,3,0,2,1\n',     '0,0,0,2,0,4,1,7,2,6,4,7,2,4,10,7,3,13,9,3,0,1,0,15,0,5,12,3,8,6,8,6,4,3,3,2,0,0,0,0\n',     '0,1,2,2,4,4,2,5,2,4,8,4,10,7,3,13,10,11,7,7,9,17,7,6,12,13,12,6,5,4,8,6,7,3,5,1,1,0,1,0\n',     '0,0,0,1,3,4,6,5,2,7,7,8,6,11,5,6,10,4,5,9,15,15,14,13,14,12,10,9,8,8,6,6,6,6,5,4,2,1,1,0\n',     '0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0\n',     '0,0,0,2,4,5,5,4,4,6,8,2,3,8,7,13,8,14,17,6,5,15,14,13,8,6,9,9,11,10,3,5,3,1,5,4,4,3,2,1\n']``

Now we have printed the first lines of each file in the data directory.
This is a handy way to find out what kind of data we have in the files.
In this way it is for example possible to see that 1) the separator in
each file is comma, and 2) each file contains numerical data, and 3)
there does not exist column names in any of the files. All of this is
important information to know when starting to do data analysis.

Footnotes
---------

-  [0]: Similar search patterns can be used when finding files in
   Terminal.

**Next**: `Writing data to a file <writing-to-file.md>`__\  **Home**:
`Lesson 5 main
page <https://github.com/Python-for-geo-people/Lesson-5-Reading-Writing>`__\ 
**Previous**: `Reading data from a file <reading-data-from-file.md>`__
