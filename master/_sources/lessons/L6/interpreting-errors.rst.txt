Dealing with errors
===================

Interpreting error messages
---------------------------

So far in the course we have encountered a number of different types of error messages in Python, but have not really discussed how to understand what the computer is trying to tell you when you get an error message.
We'll do that below.
For most Python errors you will see and exception raised when the error is encountered, providing some insight into what went wrong and where to look to fix it.

Common errors and exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, let's have a look at a few different types of common Python exceptions that are displayed for different program errors.

+----------------------+---------------------------------------------------------------------------------------------+
| Exception            | Description                                                                                 |
+======================+=============================================================================================+
| ``IndexError``       | Occurs when you attempt to reference a value with an index outside the range of values.     |
|                      |                                                                                             |
|                      | If the list ``dogs`` has 5 values, ``dogs[10]`` will raise an ``IndexError``.               |
+----------------------+---------------------------------------------------------------------------------------------+
| ``NameError``        | Occurs when you reference a variable that has not been defined.                             |
|                      |                                                                                             |
|                      | If ``myVar`` has not been assigned a value, ``yourVar = myVar`` will raise a ``NameError``. |
+----------------------+---------------------------------------------------------------------------------------------+
| ``SyntaxError``      | Occurs when there is an error in your Python syntax.                                        |
|                      |                                                                                             |
|                      | ``dogs ?= 3`` will raise a ``SyntaxError``.                                                 |
+----------------------+---------------------------------------------------------------------------------------------+
| ``IndentationError`` | Occurs when text is not properly indented when indentation is expected.                     |
|                      |                                                                                             |
|                      | No indentation beneath a ``for`` statement will raise an ``IndentationError``.              |
+----------------------+---------------------------------------------------------------------------------------------+
| ``TypeError``        | Occurs when data of incompatible types are used in your script.                             |
|                      |                                                                                             |
|                      | ``'iceCream' / 10`` will raise a ``TypeError``.                                             |
+----------------------+---------------------------------------------------------------------------------------------+

There are certainly `other kinds of errors and exceptions in Python <https://docs.python.org/3/tutorial/errors.html>`__, but this list comprises those you're most likely to encounter.
As you can see, knowing the name of each error can be helpful in trying to figure out what has gone wrong, and knowing what these common error types mean will save you time trying to fix your programs.

Reading error messages
~~~~~~~~~~~~~~~~~~~~~~

Let's imagine you've written the script below called ``wind_speed.py`` to convert wind speeds from km/hr to m/s and you're dying to figure out how windy it is in `Halifax, Nova Scotia, Canada <https://www.theweathernetwork.com/ca/weather/nova-scotia/halifax>`__ where they report wind speeds in km/hr.

.. code:: python

    """Converts wind speeds from km/hr to m/s.

    Usage:
        ./wind_speed.py

    Author:
        David Whipp - 10.10.2017
    """

    windSpeedKm = 50
    windSpeedMs = windSpeedKm * 1000 / 3600

    print('A wind speed of', windSpeedKm, 'km/hr is', windSpeedMs, 'm/s.')

Unfortunately, when you run your script you observe the following:

.. code:: python

      File "/Users/whipp/wind_speed.py", line 13
        print('A wind speed of, windSpeedKm', 'km/hr is', windSpeedMs, 'm/s.)
                                                                            ^
    SyntaxError: EOL while scanning string literal

Let's break this example down and see what the error message says.

.. figure:: img/SyntaxError.png
    :width: 800 px
    :align: center
    :alt: A SyntaxError, annotated

    A SyntaxError, annotated

As you can see, there is quite a bit of useful information here.
We have the name of the script, its location, and which line was a problem.
It's always good to double check that you actually are editing the correct script when looking for errors!
We also have the type of error, a ``SyntaxError`` in this case, as well as where it occurred on the line, and a bit more information about its meaning.
The location on the line won't always be correct, but Python makes its best guess for where you should look to solve the problem.
Clearly, this is handy information.

Let's consider another example, where you have fixed the ``SyntaxError`` above and now have made a function for calculating a wind speeds in m/s.

.. code:: python

    """Converts wind speeds from km/hr to m/s.

    Usage:
        ./wind_speed.py

    Author:
        David Whipp - 10.10.2017
    """

    def convertWindSpeed(speed):
        return speed * 1000 / 3600

    windSpeedKm = '30'
    windSpeedMs = convertWindSpeed(windSpeedKm)

    print('A wind speed of', windSpeedKm, 'km/hr is', windSpeedMs, 'm/s.')

When you run this script you encounter a new and bigger error message:

.. code:: python

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    /Users/whipp/wind_speed.py in <module>()
        12 
        13 windSpeedKm = '30'
    ---> 14 windSpeedMs = convertWindSpeed(windSpeedKm)
        15 
        16 print('A wind speed of', windSpeedKm, 'km/hr is', windSpeedMs, 'm/s.')

    /Users/whipp/wind_speed.py in convertWindSpeed(speed)
        9 
        10 def convertWindSpeed(speed):
    ---> 11     return speed * 1000 / 3600
        12 
        13 windSpeedKm = '30'

    TypeError: unsupported operand type(s) for /: 'str' and 'int'

In this case we see a ``TypeError`` that is part of a *traceback*, where the problem in the code arises from something other than on the line where the code was run.
In this case, we have a ``TypeError`` on line 11 where we try to divide a character string by a number, something Python cannot do.
Hence, the ``TypeError`` indicating the data types are not compatible.
That error, however, does not occur when the code is run until line 14 where the function is used.
Thus, we see the traceback showing that not only does the error occur when the function is used on line 14, but also that the problem is in the function definition on line 11.

The traceback above may look a bit scarier, but if you take your time and read through what is written there, you will again find that the information is helpful in finding the problem in your code.
After all, the purpose of the error message is to help the user find a problem :).

Assertions
----------

*Assertions* are a way to assert, or ensure, that the values being used in your scripts are going to be suitable for what the code does.
For instance, if you have the script above for converting wind speeds, you might want to ensure that the values for the wind speed in km/hr are not negative numbers.
That could be done using the following modification to the script.

.. code:: python

    """Converts wind speeds from km/hr to m/s.

    Usage:
        ./wind_speed.py

    Author:
        David Whipp - 10.10.2017
    """

    def convertWindSpeed(speed):
        return speed * 1000 / 3600

    windSpeedKm = -30
    assert windSpeedKm >= 0.0, 'Wind speed values must be positive or zero'
    windSpeedMs = convertWindSpeed(windSpeedKm)

    print('A wind speed of', windSpeedKm, 'km/hr is', windSpeedMs, 'm/s.')

If you run the script above with ``windSpeedKm`` set to be a negative number, then you get the following output:

.. code:: python

    ---------------------------------------------------------------------------
    AssertionError                            Traceback (most recent call last)
    /Users/whipp/wind_speed.py in <module>()
        12
        13 windSpeedKm = -30
    ---> 14 assert windSpeedKm >= 0.0, 'Wind speed values must be positive or zero'
        15 windSpeedMs = convertWindSpeed(windSpeedKm)
        16

    AssertionError: Wind speed values must be positive or zero

This ``AssertionError`` is produced because of the ``assert`` statement we entered in the code above.
If the condition listed after ``assert`` is fales, the error message that follows will be printed to the screen.
More generally, assertions take on the following form:

.. code:: python

    assert <some test>, 'Error message to display'

So we start with the ``assert`` statement, then give a logical test for some condition.
If the test is true, nothing happens and the code continues.
If not, the code stops, and an ``AssertionError`` is displayed with the text written after the comma in the ``assert`` line.

You might also think that it would be useful to check the type of ``windSpeedKm`` to make sure that you don't get a ``TypeError`` as occurred in the previous section.
It turns out that this is not really a good idea, and the philosophical idea is that the ``TypeError`` will show that you have incompatible data types, so why raise an ``AssertionError`` to do the same thing?

More information
~~~~~~~~~~~~~~~~

You can find a bit more information about reading error messages on the `Software Carpentry <http://swcarpentry.github.io/python-novice-inflammation/07-errors/>`__ and `Python <https://docs.python.org/3/tutorial/errors.html>`__ webpages.
More information about assertions can also be found on the `Software Carpentry website <http://swcarpentry.github.io/python-novice-inflammation/08-defensive/>`__.