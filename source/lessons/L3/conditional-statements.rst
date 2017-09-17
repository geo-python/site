Conditional statements
======================

Sources
-------

This lesson is based on the `Software Carpentry group's <http://software-carpentry.org/>`__ lessons on `Programming with Python <http://swcarpentry.github.io/python-novice-inflammation/>`__.

Basics of conditional statements
--------------------------------

Conditional statements can change the code behaviour based on meeting certain conditions.

1. Let's take a simple example.

   .. code:: python

    In [1]: temperature = 17

    In [2]: if temperature > 25:
       ...:     print('it is hot')
       ...: else:
       ...:     print('it is not hot')
       ...:
    it is not hot

   What did we do here?
   First, we used the ``if`` and ``else`` statements to determine what parts of the code to execute.
   Note that both lines containing ``if`` or ``else`` end with a ``:`` and the text beneath is indented.
   What do these tests do?
   The ``if`` test checks to see whether the variable value for ``temperature`` is greater than 25.
   If so, 'it is hot' would be written to the screen.
   Since 17 is smaller than 25, the code beneath the ``else`` is executed.
   The ``else`` statement code will run whenever the ``if`` test is false.

2. The combination of ``if`` and ``else`` is very common, but both are not strictly required.

   .. code:: python

    In [3]: temperature = 13

    In [4]: if temperature > 25:
       ...:     print('13 is greater than 25')
       ...:

   Note that here we use only the ``if`` statement, and because 13 is not greater than 25, nothing is printed to the screen.

3. We can also have a second test for an ``if`` statment by using the ``elif`` (else-if) statement.

   .. code:: python

    In [5]: temperature = -3

    In [6]: if temperature > 0:
       ...:     print(temperature, 'is above freezing')
       ...: elif temperature == 0:
       ...:     print(temperature, 'is freezing')
       ...: else:
       ...:     print(temperature, 'is below freezing')
       ...:
    -3 is below freezing

   Makes sense, right?
   Note here that we use the ``==`` to test if a value is exactly equal to another.
   The complete list of these comparison operators is given in the table below.

   +------------+----------------------------+
   | Operator   | Meaning                    |
   +============+============================+
   | ``<``      | Less than                  |
   +------------+----------------------------+
   | ``<=``     | Less than or equal to      |
   +------------+----------------------------+
   | ``==``     | Equal to                   |
   +------------+----------------------------+
   | ``>=``     | Greater than or equal to   |
   +------------+----------------------------+
   | ``>``      | Greater than               |
   +------------+----------------------------+
   | ``!=``     | Not equal to               |
   +------------+----------------------------+

4. We can also use ``and`` and ``or`` to have multiple conditions.

   .. code:: python

    In [7]: if (1 > 0) and (-1 > 0):
       ...:     print('Both parts are true')
       ...: else:
       ...:     print('One part is not true')
       ...:
    One part is not true

    In [8]: if (1 < 0) or (-1 < 0):
       ...:     print('At least one test is true')
       ...:
    At least one test is true

   This is just a simple example, but a concept that can be quite handy.