Exercise 4
==========

.. note::

    Please complete this exercise by **the start of the next lesson**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 4 by** `accepting the GitHub Classroom assignment <https://classroom.github.com/a/_hiiK8sa>`__.

You can also take a look at the template repository for `Exercise 4 on GitHub <https://github.com/Geo-Python-2023/Exercise-4>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

.. admonition:: Pair programming

    Students attending the course in Helsinki, **note that we continue working in pairs**.
    We will only grade the repository of the member of your pair that is responsible for this week's exercise.
    See more information in Slack, and in week 2: `Why are we working in pairs? <https://geo-python-site.readthedocs.io/en/latest/lessons/L2/why-pairs.html>`_

Cloud computing environments
----------------------------

.. image:: https://img.shields.io/badge/launch-binder-red.svg
   :target: https://mybinder.org/v2/gh/Geo-Python-2023/Binder/main?urlpath=lab
   
.. image:: https://img.shields.io/badge/launch-CSC%20notebook-blue.svg
   :target: https://notebooks.csc.fi/ 


Exercise 4 hints
----------------

Here are a few things that may be helpful in completing Exercise 4.

Importing variables from a script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the lesson materials we saw how to `import functions from a script <../../notebooks/L4/functions.html#calling-functions-from-a-script-file>`__.

In a similar manner you can also import any variable that has been defined in another script, hence, it is not limited
to functions that you can import.

Counting values from a list
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases it might be useful to know how many times certain value exists in a list. Consider following example:

.. code-block:: python

    my_list = ['car', 'bus', 'bike', 'car', 'car', 'bike']
    car_count = my_list.count('car')
    print("There are", car_count, "cars in my list!")