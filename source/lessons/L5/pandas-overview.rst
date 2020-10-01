What is Pandas?
===============

.. figure:: img/pandas_logo.png
   :width: 300px

   Source: `Medium.com <https://medium.com/towards-data-science/a-quick-introduction-to-the-pandas-python-library-f1b678f34673>`__

`Pandas <http://pandas.pydata.org/>`__ is a modern, powerful and feature rich library that is designed for doing
data analysis in Python. It is a mature data analytics framework (originally written by Wes McKinney) that is widely used among different fields of science,
thus there exists a lot of good examples and documentation that can help you get going with your data analysis tasks.

Easy-to-use data structures
---------------------------

In Pandas the data is typically stored into a DataFrame that looks like a typical table with rows and columns
(+ indices and column names), where columns can contain data of different data types.
Thus, it reminds of how the data is stored e.g. in Excel or in R that also uses a concept of a dataframe. In fact,
Wes McKinney first `developed Pandas as an alternative for R <https://blog.quantopian.com/meet-quantopians-newest-advisor-wes-mckinney/>`_ to deal with different complex data structures.

Combines functionalities from many Python modules
-------------------------------------------------

Pandas takes advantage of `numpy <http://www.numpy.org/>`__ -module which runs under the hood and is mostly written in C,
which makes it fast and powerful library that can handle efficiently even large datasets.
Pandas offers easier and more intuitive syntax to do data analysis and manipulation using either `numpy`
functionalities in the background or dedicated functionalities written explicitly for Pandas.
However, Pandas is much more than easier-to-use `numpy` as it also combines many functionalities from other Python
libraries such as `matplotlib (plotting) <https://matplotlib.org/>`__ and
`scipy (mathematics, science, engineering) <https://www.scipy.org/>`__. Thus, you can use many of the features
included in those packages even without importing them at all.

Supports data read/write from multiple formats
----------------------------------------------

One of the most useful features of Pandas is its ability to read data from numerous different data formats directly.
Pandas supports reading and writing data e.g. from/to:

- CSV
- JSON
- HTML
- MS Excel
- HDF5
- Stata
- SAS
- Python Pickle format
- SQL (Postgresql, MySQL, Oracle, MariaDB, etc.)

See full list from `Pandas docs <http://pandas.pydata.org/pandas-docs/version/0.20/io.html>`__.