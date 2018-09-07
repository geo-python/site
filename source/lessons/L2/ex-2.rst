Exercise 2
==========

.. warning::

    Please feel free to use the link below to create your personal copy of this assignment using GitHub Classroom.
    However, note that **we provide assignment feedback only for students enrolled in the course at the University of Helsinki**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 2 by** `accepting the GitHub Classroom assignment <https://classroom.github.com/a/AgzvDCtR>`__.

You can also take a look at the open course copy of `Exercise 2 in the course GitHub repository <https://github.com/Geo-Python-2017/Exercise-2>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

Exercise 2 hints
================

Here are a few things that may be helpful in completing Exercise 2.

Where to make changes
---------------------

In Problem 1 lines 32-34 and line 40 should not be modified.

List methods
------------

In Problem 2 you will likely need two lists and to use the ``.index()`` method.
These were covered in `this week's lesson <python-basic-elements.html#the-concept-of-objects>`__.

Indentation woes
----------------

We have not really run into this problem in the lessons, but Python codes are sensitive to how much you indent the start of each line.
This is perhaps easiest to see with an example.

.. code:: python

    name = 'Dave'
        dogs = 0
    print('My name is', name, 'and I own', dogs, 'dogs.')

If you copy and paste this code into the **Spyder** editor and run it, you will see that is gives an ``IndentationError``.
**Spyder** already makes it clear there is an error in the program by showing a yellow exclamation mark icon on the problem line.

.. code:: python

        dogs = 0
        ^
    IndentationError: unexpected indent

We will see examples later of why indentation matters, but for now just be sure you don't indent lines to different levels.
Thus, the fix is simply to remove the spaces on the second line.

.. code:: python

    name = 'Dave'
    dogs = 0
    print('My name is', name, 'and I own', dogs, 'dogs.')

Now, running the code results in the expected output.

.. code:: python

    My name is Dave and I own 0 dogs.
