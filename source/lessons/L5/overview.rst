Lesson overview
===============

In this lesson we will learn basics in reading and writing data from/to a file, and do some basic data manipulation
and analysis using a Python module called **Pandas**.
`Pandas <http://pandas.pydata.org/>`__ is a modern and feature rich data analysis framework for Python that is designed
to make data analysis and manipulation straightforward and powerful using easy-to-use data structures and operations.

- :doc:`Summary of early course feedback <midterm-feedback>`
- :doc:`What is Pandas? <pandas-overview>`
- Reading data from a file using Pandas
  - Skipping file headers and other unwanted data
  - Determining NoData value
- Pandas DataFrame and its properties
  - columns
  - rows
  - datatypes
  - shape
- Pandas Series and built-in functions
  - Pandas Series vs Numpy-array
  - Series functions (mean, avg, std, min, max)
  - Describe your data with .describe() -function
  - Type conversions with .astype() -function
- Data selections
  - Slicing data
  - Selecting data based on specific criteria using indexing (.ix )
- Iterating over rows
- Writing data

1. `Summary of early course feedback <Lesson/midterm-feedback.md>`__
2. `Reading data from a file <Lesson/reading-data-from-file.md>`__

-  `Reading an entire file at
   once <Lesson/reading-data-from-file.md#reading-an-entire-file-at-once>`__
-  `Interacting with our file
   data <Lesson/reading-data-from-file.md#interacting-with-our-file-data>`__
-  `Skipping file headers and other unwanted
   data <Lesson/reading-data-from-file.md#skipping-file-headers-and-other-unwanted-data>`__
-  `Pro tips <Lesson/reading-data-from-file.md#pro-tips>`__

3. `Reading multiple data files <Lesson/reading-multiple-files.md>`__

-  `Listing files <Lesson/reading-multiple-files.md#list-files>`__
-  `Reading data from multiple
   files <Lesson/reading-multiple-files.md#read-multiple>`__

4. `Writing data to a file <Lesson/writing-to-file.md>`__

-  `Writing to a new
   file <Lesson/writing-to-file.md#Writing-to-a-new-file>`__
-  `Appending to a file <Lesson/writing-to-file.md#append>`__
-  `Useful functions related to
   filepaths <Lesson/writing-to-file.md#useful-functions>`__
-  `Copying contents from a file into
   another <Lesson/writing-to-file.md#copying-files>`__

5. `Exercise 5: Analysing NOAA climate
   data <https://classroom.github.com/assignment-invitations/17f0f2ee87873cb1bcb2c6a9ec228c42>`__
6. `Hints for Exercise 5 <Lesson/hints-ex5.md>`__

Resources
---------

-  Past lesson materials
-  `Functions and
   modules <https://github.com/Python-for-geo-people/Functions-and-modules>`__
-  `Control
   flow <https://github.com/Python-for-geo-people/Control-flow>`__
-  `Intro to version control and
   GitHub <https://github.com/Python-for-geo-people/Diving-into-Python/tree/master/Lesson/intro-to-GitHub.md>`__
-  `Writing script
   files <https://github.com/Python-for-geo-people/Diving-into-Python/tree/master/Lesson/writing-scripts.md>`__
-  `Working on the
   exercises <https://github.com/Python-for-geo-people/Diving-into-Python/tree/master/Lesson/working-on-assignment.md>`__
-  Web pages
-  `Codecademy's Learn to program in
   Python <https://www.codecademy.com/learn/python>`__
-  `Software Carpentry's programming in
   Python <https://swcarpentry.github.io/python-novice-inflammation/>`__
-  Books
-  `Learn Python the Hard
   Way <http://learnpythonthehardway.org/book/>`__
-  `Dive into Python 3 <http://www.diveinto.org/python3/>`__
