Exercise 2
==========

.. note::

    Please complete this exercise by **09:00 Wednesday, 18 September 2019**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 2 by** `accepting the GitHub Classroom assignment <https://classroom.github.com/a/f3fEs1Xn>`__.

You can also take a look at at the template repository for `Exercise 2 on GitHub <https://github.com/Geo-Python-2019/Exercise-2>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

.. warning::

    Please note that **we provide assignment feedback only for students enrolled in the course at the University of Helsinki**.

Cloud computing environments
-----------------------------

.. image:: https://img.shields.io/badge/launch-binder-red.svg
   :target: https://mybinder.org/v2/gh/Geo-Python-2019/Binder/master?urlpath=lab

.. image:: https://img.shields.io/badge/launch-CSC%20notebook-blue.svg
   :target: https://notebooks.csc.fi/#/blueprint/d71cd2d26d924f48820dc22b67a87d8e

Exercise 2 hints
----------------

Here are a few things that may be helpful in completing Exercise 2.

Git
~~~~

You can find step-by-step instructions for using Git `in here <git-basics.html>`__.
Remember to commit your changes after each major edit! Also, it's better to push your changes to GitHub every now and then, rather than only at the very end.

List methods
~~~~~~~~~~~~

In Problem 2 you will likely need two lists and to use the ``.index()`` method.
These were covered in `this week's lesson <python-basic-elements.html#the-concept-of-objects>`__.

Indentation woes
~~~~~~~~~~~~~~~~

We have not really run into this problem in the lessons, but Python codes are sensitive to how much you indent the start of each line.
This is perhaps easiest to see with an example.

.. code:: python

    name = 'Dave'
        dogs = 0
    print('My name is', name, 'and I own', dogs, 'dogs.')

If you copy and paste this code into the **Jupyter Notebook** cell and run it, you will see that is gives an ``IndentationError``.

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

