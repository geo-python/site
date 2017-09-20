Conditional statements
======================

Sources
-------

This lesson is based on the `Software Carpentry group's <http://software-carpentry.org/>`__ lessons on `Programming with Python <http://swcarpentry.github.io/python-novice-inflammation/>`__.

Basics of conditional statements
--------------------------------

Conditional statements can change the code behaviour based on meeting certain conditions.

1. Let's take a simple example.

   .. ipython:: python

        temperature = 17

        if temperature > 25:
            print('it is hot')
       else:
            print('it is not hot')


   What did we do here?
   First, we used the ``if`` and ``else`` statements to determine what parts of the code to execute.
   Note that both lines containing ``if`` or ``else`` end with a ``:`` and the text beneath is indented.
   What do these tests do?
   The ``if`` test checks to see whether the variable value for ``temperature`` is greater than 25.
   If so, 'it is hot' would be written to the screen.
   Since 17 is smaller than 25, the code beneath the ``else`` is executed.
   The ``else`` statement code will run whenever the ``if`` test is false.

   .. note::

    As it turns out, we all use logic similar to ``if`` and ``else`` conditional statements daily.
    Imagine you're getting ready to leave your home for the day and want to decide what to wear.
    You might look outside to check the weather conditions.
    If it is raining, you will wear a rain jacket.
    Otherwise, you will not.
    In Python we could say:

    .. ipython:: python

        weather = 'Rain'
        if weather == 'Rain':
            print('Wear a raincoat')
       else:
            print('No raincoat needed')

    Note here that we use the ``==`` to test if a value is exactly equal to another.

2. The combination of ``if`` and ``else`` is very common, but both are not strictly required.

   .. ipython:: python

    temperature = 13

    if temperature > 25:
        print('13 is greater than 25')

   Note that here we use only the ``if`` statement, and because 13 is not greater than 25, nothing is printed to the screen.

3. We can also have a second test for an ``if`` statment by using the ``elif`` (else-if) statement.

   .. ipython:: python

        temperature = -3

        if temperature > 0:
            print(temperature, 'is above freezing')
       elif temperature == 0:
            print(temperature, 'is freezing')
       else:
            print(temperature, 'is below freezing')

   Makes sense, right?
   Note here that we again use the ``==`` to test if a value is exactly equal to another.
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

   .. attention::

    Time to check your understanding.
    Let's assume that yesterday it was 14°C, it is 10°C outside today, and tomorrow it will be 13°C.
    The following code compares these temperatures and prints something to the screen based on the comparison.

    .. code:: python

        yesterday = 14
        today = 10
        tomorrow = 13

        if yesterday <= today:
            print('A')
        elif today != tomorrow:
            print('B')
        elif yesterday > tomorrow:
            print('C')
        elif today == today:
            print('D')

    Which of the letters ``A``, ``B``, ``C``, and ``D`` would be printed to the screen?
    Select your answer from the poll options at https://geo-python.github.io/poll/.

.. NOTE: The question above is tricky because of the elif statements, only "B" should be written to the screen.
   This year it worked out nicely because we had the discussion about why the options were all wrong, and it was helpful to see how the logic works.

4. We can also use ``and`` and ``or`` to have multiple conditions.

   .. ipython:: python

        if (1 > 0) and (-1 > 0):
            print('Both parts are true')
       else:
            print('One part is not true')

   .. ipython:: python

        if (1 < 0) or (-1 < 0):
            print('At least one test is true')

   These are just simple examples, but concepts that can be quite handy.

   .. note::

    Again, making decisions based on multiple conditions is something we regularly do.
    Imagine that we consider not only the rain, but also whether or not it is windy.
    If it is windy and raining, we'll just stay home.
    Otherwise, we need appropriate clothing to go out.
    We can again handle this kind of decision with Python.

    .. ipython:: python

        weather = 'Rain'
        wind = 'Windy'
        if (weather == 'Rain') and (wind == 'Windy'):
            print('Just stay home')
       elif weather == 'Rain':
            print('Wear a raincoat')
       else:
            print('No raincoat needed')

    As you can see, we better just stay home if it is windy and raining.