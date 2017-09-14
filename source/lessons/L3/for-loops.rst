``for`` loops
=============

Sources
-------

This lesson is based on the `Software Carpentry
group's <http://software-carpentry.org/>`__ lessons on `Programming with
Python <http://swcarpentry.github.io/python-novice-inflammation/>`__.

Basics of ``for`` loops
-----------------------

Loops allow parts of code to be repeated over some number of times.

1. Let's consider an example. Suppose we want to take a word and print
   out each letter of the word separately. We could do the following:

   .. code:: python

       >>> word = 'rock'
       >>> print(word[0])
       r
       >>> print(word[1])
       o
       >>> print(word[2])
       c
       >>> print(word[3])
       k

   But this is a bad idea. Why? Well there are two reasons. First, it
   does not scale nicely for long strings, and will take forever to type
   in. Second, it won't work if the word is not 4 characters long.

   .. code:: python

       >>> word = 'ore'
       >>> print(word[0])
       o
       >>> print(word[1])
       r
       >>> print(word[2])
       e
       >>> print(word[3])
       ---------------------------------------------------------------------------
       IndexError                                Traceback (most recent call last)
       <ipython-input-14-e3303df6f566> in <module>()
       ----> 1 print(word[3])

       IndexError: string index out of range

2. We could do a much better job by using a ``for`` loop.

   .. code:: python

       >>> word = 'rock'
       >>> for char in word:
       ...    print(char)
       ...
       r
       o
       c
       k

   Note here that the ``...`` is displayed in the IPython window when
   entering code in a loop and you do not need to type in the ``...``.
   Not only is this shorter, but it is also more flexible. Try out a
   different word such as ``granite``. Still works, right?
3. ``for`` loops in Python have the general form below.

   .. code:: python

       for variable in collection:
           do things with variable

   The ``variable`` can be any name you like, and the statement of the
   ``for`` loop must end with a ``:``. The code that should be executed
   as part of the loop must be indented beneath the ``for`` loop, and
   the typical indentation is 4 spaces. There is not additional special
   word needed to end the loop, just change the indentation back to
   normal.
4. Let's consider another example.

   .. code:: python

       >>> length = 0
       >>> for letter in 'earthquake':
       ...    length = length + 1
       ...
       >>> print('There are', length, 'letters')
       There are 10 letters

   Can you follow what happens in this loop?
5. Note that the variable used in the loop, ``letter`` in the case above
   is just a normal variable and still exists after the loop has
   completed with the final value given to letter.

   .. code:: python

       >>> letter = 'x'
       >>> for letter in 'fault':
       ...     print(letter)
       ...
       f
       a
       u
       l
       t
       >>> print('After the loop, letter is', letter)
       t

6. A loop can be used to iterate over any list of values in Python. So
   far we have considered only character strings, but we could also
   write a loop that performs a calculation a specified number of times.

   .. code:: python

       >>> for number in range(5):
       ...     print(number)
       ...
       0
       1
       2
       3
       4

   What happens here? Well, in this case, we use a special function
   called ``range()`` to give us a list of 5 numbers ``[0, 1, 2, 3, 4]``
   and then print each number in the list to the screen. When given a
   integer (whole number) as an argument, ``range()`` will produce a
   list of numbers with a length equal to the specified number. The list
   starts at zero and ends with number-1. You can learn a bit more about
   range by typing

   .. code:: python

       >>> help(range)

7. Often when you use ``for`` loops, you are looping over the values in
   a list and either calculating a new value or modifying the existing
   values. Let's consider an example.

   .. code:: python

       >>> mylist = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
       >>> print(mylist)
       [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
       >>> for i in range(6):
       ...     mylist[i] = mylist[i] + i
       ...
       >>> print(mylist)
       [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]

   So, what happened? We first create a list of 6 numbers. Then, we loop
   over 6 values using the ``range()`` function and add each value to
   the existing location in ``mylist``. What would happen if we ran this
   for loop a second time?

8. One of the drawbacks in the example above is that we need to know the
   length of the list before running that ``for`` loop example. However,
   we already know how to find the length of a list using the ``len()``
   function, and we can take advantage of this knowledge to make our
   ``for`` loop more flexible.

   .. code:: python

       >>> for i in range(len(mylist)):
       ...     mylist[i] = mylist[i] + i
       ...
       >>> print(mylist)
       [0.0, 3.0, 6.0, 9.0, 12.0, 15.0]

   We've done exactly what we had done in the previous example, but
   replaced the known length of the list ``6`` with use of the ``len()``
   function to provide the list length. Now if we add or remove values
   in ``mylist``, our code will still work as expected.

   .. code:: python

       >>> mylist.append(18.0)
       >>> mylist.append(21.0)
       >>> print(mylist)
       [0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0]
       >>> for i in range(len(mylist)):
       ...     mylist[i] = mylist[i] + i
       ...
       >>> print(mylist)
       [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0]

   Using the ``len()`` function with ``range()`` to perform calcluations
   using list or array values is an *extremely* common operation in
   Python.

**Next**: `Conditional statements <conditional-statements.md>`__\ 
**Home**: `Lesson 3 main
page <https://github.com/Python-for-geo-people/Lesson-3-Loops-Conditional-Statements>`__\ 
