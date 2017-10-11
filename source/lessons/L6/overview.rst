Lesson overview
===============

In this lesson we will continue to develop our data analysis skills using `Pandas <http://pandas.pydata.org/>`__ and also learn a bit about debugging our scripts and interpreting errors.
In :doc:`Lesson 5 <../L5/overview>` we were introduced to basic data analysis using Pandas, and this week we will learn a few more ways in which we can do things like replace values, using functions in Pandas, and aggregating data.
In the second half of the lesson we will focus on debugging.
Many new programmers struggle with removing problems in their code (debugging) because they start randomly making changes without a clear picture of what is wrong or even what the code should do!
By learning a few basic ideas about debugging and interpreting error messages, we hope to save you time and frustration as your scripts become more complex.

- :doc:`Processing data with Pandas, part II <pandas-analysis>`
- :doc:`Interpreting error messages <interpreting-errors>`
- :doc:`Debugging your scripts <debugging-scripts>`
- :doc:`Exercise 6 <ex-6>`
- :doc:`Hints for Exercise 6 <exercise-6-hints>`

Learning goals
--------------

After this weeks lesson your should be able to:

- Analyze data files in Python using Pandas
- Understand common Python errors
- Follow a simple set of guidelines to debug programs efficiently

*BELOW STILL NEEDS TO BE REMOVED - HERE ONLY TO NOTE WHAT TO COVER*

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