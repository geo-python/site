What is pandas?
===============

.. figure:: img/pandas_logo.png
   :class: dark-light
   :width: 300px

   Source: `Medium.com <https://medium.com/towards-data-science/a-quick-introduction-to-the-pandas-python-library-f1b678f34673>`__

`pandas <http://pandas.pydata.org/>`__ is a modern, powerful and feature-rich library that is designed for doing data analysis in Python.
It is a mature data analytics framework (originally written by Wes McKinney) that is widely used among different fields of science.
Thus, documentation and many good examples exist that can help you get rolling with your data analysis tasks.

Easy-to-use data structures
---------------------------

In pandas, the data is typically stored in a data structure called a DataFrame that looks like a typical table with rows and columns
(+ indices and column names), where columns can contain data of different data types.
Thus, it is similar in some sense to how data is stored in Excel or in R, which also uses a concept of a dataframe.
In fact, Wes McKinney first developed pandas as an alternative for R to deal with different complex data structures.

Combines functionalities from many Python modules
-------------------------------------------------

pandas takes advantage of the `NumPy <http://www.numpy.org/>`__ module under the hood, which is mostly written in C.
This makes it a fast and powerful library that can efficiently handle even very large datasets.
pandas offers an easier and more intuitive syntax to do data analysis and manipulation using either `numpy` functionalities in the background or dedicated functionalities written explicitly for pandas.
However, pandas is much more than an easier-to-use `numpy` as it also combines many functionalities from other Python libraries such as `matplotlib (plotting) <https://matplotlib.org/>`__ and `scipy (mathematics, science, engineering) <https://www.scipy.org/>`__.
Thus, you can use many of the features included in those packages without importing them at all.

Supports data read/write from multiple formats
----------------------------------------------

One of the most useful features of pandas is its ability to read data from numerous different data formats directly.
For example, pandas supports reading and writing data from/to:

- CSV
- JSON
- HTML
- MS Excel
- HDF5
- Stata
- SAS
- Python Pickle format
- SQL (Postgresql, MySQL, Oracle, MariaDB, etc.)

You can view the full list of supported data formats from the `pandas docs <https://pandas.pydata.org/docs/user_guide/io.html>`__.
