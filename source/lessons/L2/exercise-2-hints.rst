Exercise 2 hints
================

Here are a few things that may be helpful in completing Exercise 2.

Where to make changes
---------------------

To help make sure you don't end up modifying parts of the code we did not anticipate, you should know that lines 32-34 and line 40 should not be modified.

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