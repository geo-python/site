Exercise 3
==========

.. warning::

    Please note that **we provide assignment feedback only for students enrolled in the course at the University of Helsinki**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 3 by** `accepting the GitHub Classroom assignment <https://classroom.github.com/a/ztpdy_GR>`__.

You can also take a look at the open course copy of `Exercise 3 in the course GitHub repository <https://github.com/Geo-Python-2018/Exercise-3>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

Exercise 3 hints
----------------

Here are a few things that may be helpful in completing Exercise 3.

General tips
~~~~~~~~~~~~

1. Start by cloning your personal Exercise 3 repository on your (cloud) computer. See :doc:`instructions for using git from Lesson 2. <../L2/git-basics.rst>`__
2. Remember to commit your changes often!
3. Follow carefully the instructions about variable names and other details (this week's exercises will bee graded automatically!)
4. Ask for help in Slack and/or come to the practical sessions if you get stuck :)


Combining strings
~~~~~~~~~~~~~~~~~

In case you have forgotten, string variables can be added together. For example,

.. code-block:: python

    a = "Taco "
    b = "time"
    c = a + b
    print(c)


Nested if statements
~~~~~~~~~~~~~~~~~~~~

In some cases it might be useful to have nested if statements, meaning that you have another layer of
conditions after the first condition resolves to True.

Take a look of following example:

.. code-block:: python

    season = "Winter"
    temperature = 10

    if season == "Winter":

        if temperature > 7:
            print("No need for winter jacket!")

        else:
            print("It might be cold! Wear a proper jacket!")

   elif season == "Summer":

        if temperature > 20:
            print("It's warm! Time to wear shorts!")

        else:
            print("Well this is Finland, better wear long trousers!")
   else:
        print("Check the weather forecast!")







