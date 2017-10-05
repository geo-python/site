Plan for Lesson 5
=================

Contents that were introduced last year during Lessons 5 and 6, and modified to this year:

Dave from here:
- Reading a single data file
- Skipping file headers and other unwanted data
- DataFrame dimensions:
  - columns (data.columns)
  - rows
  - datatypes
  - shape
- pd.Series() --> np.array()
- pd.Series() functions (mean, avg, std, min, max, corr)
- type conversion

# Henkka:
- Writing data

- Slicing data
- Selecting data (.ix)
- Exercise 5

6 lesson:
---------

Rovaniemi station has values every 20 minutes, BUT, Kumpula has only hourly data.
To be able to compare these two datasets, we need to aggregate the Rovaniemi
data into hourly values as well.

Then we want to compare the differences in the Celsius temperatures (using difference and standard deviation).
We can spot the big storm in Helsinki Vantaa in early August.

- Replacing values
- Renaming columns
- Str split() method
- Append method with DataFrame
- Iterating over lines in a file (iterrows() -method)
- Using functions in Pandas
- Reading multiple data files (glob)
- Grouping data (aggregation)

Debugging and errors
- Understanding the error messages
- Using version control to see the changes (to find what is going wrong)
- try & except, assert()


To AutoGIS
----------

- Table joins
