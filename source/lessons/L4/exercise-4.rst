Exercise 4
==========

.. warning::

    Please note that **we provide assignment feedback only for students enrolled in the course at the University of Helsinki**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 4 by** `accepting the GitHub Classroom assignment <https://classroom.github.com/a/jEYcSV6q>`__.

You can also take a look at the open course copy of `Exercise 4 in the course GitHub repository <https://github.com/Geo-Python-2018/Exercise-4>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

Exercise 4 hints
----------------

Here are a few things that may be helpful in completing Exercise 4.

Importing variables from a script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the lesson materials we saw how to `import functions from a script <functions.html#Calling-functions-from-a-script-file>`__.

In a similar manner you can also import any variable that has been defined in another script, hence, it is not limited
to functions that you can import.

Counting values from a list
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases it might be useful to know how many times certain value exists in a list. Consider following example:

.. ipython:: python

    my_list = ['car', 'bus', 'bike', 'car', 'car', 'bike']
    car_count = my_list.count('car')
    print("There are", car_count, "cars in my list!")