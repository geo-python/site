Exercise 4 hints
================

Here are a few things that may be helpful in completing Exercise 4.

Importing variables from a script
---------------------------------

In the lesson materials we saw how to `import functions from a script <functions.html#calling-functions-from-another-script-file>`__.

In a similar manner you can also import any variable that has been defined in another script, hence, it is not limited
to functions that you can import.

Counting values from a list
---------------------------

In some cases it might be useful to know how many times certain value exists in a list. Consider following example:

.. ipython:: python

    my_list = ['car', 'bus', 'bike', 'car', 'car', 'bike']
    car_count = my_list.count('car')
    print("There are", car_count, "cars in my list!")

