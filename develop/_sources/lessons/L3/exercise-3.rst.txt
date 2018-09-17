Exercise 3
==========

.. warning::

    Please note that **we provide assignment feedback only for students enrolled in the course at the University of Helsinki**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 2 by** `accepting the GitHub Classroom assignment <https://classroom.github.com/a/L4gRzQ92>`__.

You can also take a look at the open course copy of `Exercise 3 in the course GitHub repository <https://github.com/Geo-Python-2018/Exercise-3>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

Exercise 3 hints
----------------

Here are a few things that may be helpful in completing Exercise 3.

General tips
~~~~~~~~~~~~

1. Create a general template for your new script files and commit it to GitHub right when you start working on your script(s).
2. Your scripts should also follow the format described earlier in the course with a block comment at the start of the file, inline comments describing how it works and good use of blank lines to make the code easy to read.
3. Look carefully at the requirements for each exercise and be sure to follow them.

Combining strings
~~~~~~~~~~~~~~~~~

In case you have forgotten, string variables can be added together. For example,

.. ipython:: python

    a = "Taco "
    b = "time"
    c = a + b
    print(c)

Nested if statements
~~~~~~~~~~~~~~~~~~~~

In some cases it might be useful to have nested if statements, meaning that you have another layer of
conditions after the first condition resolves to True.

Take a look of following example:

.. ipython:: python

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

