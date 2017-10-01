Hints for Exercise 5
====================

Below are some tips for working on Exercise 5. Each section contains
some practical tips for the different parts of the exercise, and we have
included some pseudocode for Parts 1 and 2 to help guide you in writing
your code. As a reminder, pseudocode is simply an explanation of what
the code should do in plain English (or your language of choice).

Part 1 - Reading and dividing the data file
-------------------------------------------

Pseudocode
~~~~~~~~~~

1. Open the ``816295.csv`` data file for reading.
2. Read the values into a list where each list entry is one line of the
   file.
3. Loop over all lines in the resulting list (excluding the header). For
   each line:

-  Split the line into a list of values using the commas.
-  Extract the value for the year using the list item containing the
   date in the split line list above.
-  Create a varaible that is contains a character string of the name of
   the output file for that year (e.g., ``"AA-1926.csv"``).
-  Open the file named above for appending.
-  Write the entire line to that data file.

Practical tips
~~~~~~~~~~~~~~

1. **Extracting the year for each line of the data file**. In order to
   isolate the year when processing the data in the data file for this
   exercise, you need to use a substring, or part of a character string,
   from the values in column 6 of the ``816295.csv`` data file. Those
   values have the form ``YYYYMMDD`` where ``YYYY`` is the year of the
   observation, ``MM`` is the month, and ``DD`` is the day. You want to
   use only the year, and let's assume that for each line of the data
   file that is read, you assign the value in column 6 to a variable
   ``date``. The year part of ``date`` would then just be the first 4
   characters in ``date``, and since character strings are simply a list
   of characters, you can use the index values to extract a slice (or
   substring) from the variable ``date``. Since the first number in the
   year in ``date`` would simply be ``date[0]``, and the last would be
   ``date[3]``, all we need is a way to use only index values 0-3 in
   date. You can access a range of index values in a string variable or
   list using the colon (``:``) character. The example below may help
   make things more clear:

   .. code:: python

       >>> text = "Helsinki"
       >>> print(text[0])
       'H'
       >>> print(text[3])
       's'
       >>> print(text[0:3]
       'Hel'

   **Note**: Like the ``range()`` function, the last index value given
   in a range of values is not included in the list of indices.
2. **Skipping header lines when looping over file data**. Just a
   reminder that we showed how to skip over a set number of header lines
   when reading a file in `this week's
   lesson <reading-data-from-file.md#headers-of-a-known-number-of-lines>`__.
3. **Changing file names for different years**. If you are in a loop in
   which your script is determining the year of a given temperature
   observation, you will likely also want to automatically have the file
   name used for reading or writing change for different years. This is
   fairly simple. Let's say you have a variable ``year`` used to store
   the year. If ``year`` is a numerical value, you will need to convert
   it to a character string. We saw how to do this in `Exercise
   3 <https://github.com/Python-for-geo-people/Exercise-3>`__, for
   example. Once ``year`` is a character string, you can simply add the
   parts of the file name that come before and after the year together
   using the math operator ``+`` to change the file name.

Part 2 - Calculating annual summer and winter temperatures
----------------------------------------------------------

Pseudocode
~~~~~~~~~~

1. Create a list of names of all of the files generated in Part 1.
2. Loop over that list. For each file:

-  Open the file for reading.
-  Create two empty lists for storing the daily temperatures for summer
   and winter.
-  Loop over every line in each file. For each line:

   -  Split the line into a list of values using the commas.
   -  Extract the value for the month using the list item containing the
      date in the split line list above.
   -  Check to see if the month is a summer or winter month. If so,
      append the temperature to the corresponding temperature list.

-  After checking all lines, calculate the average summer and winter
   temperatures.
-  Open the summer and winter average temperature files for appending.
-  Append the year and average temperature.

Practical tips
~~~~~~~~~~~~~~

1. **Calculating the average value of list values**. It is fairly easy
   to calculate the average value of a set of numbers in a list,
   provided the values are in fact stored as data type ``float`` or
   ``int``, and not stored as type ``str``. If the values in the list
   are character string values (type ``str``), they will need to be
   converted to ``float`` values first, using the ``float()`` function.
   You can check ``help(float)`` for how it works. Once the list values
   are of type ``float``, they can be summed using the ``sum()``
   function and dividing the sum by the length of the list will give the
   average value.
2. **Limiting the number of decimal places written to numerical values
   in a file**. When you write floating point values to a file it is
   often nice to specify the number of decimal places for the
   representation of the values. This can be done using the
   ``.format()`` method for character strings. It is perhaps easiest to
   see how this works with an example:

   .. code:: python

       >>> number = 1.234556789
       >>> print(number)
       1.234556789
       >>> print( "{0:.3f}".format(number) )
       1.235
       >>> print( "{0:.1f}".format(number) )
       1.2
       >>> print( "The rounded value of number is {0:.4f} when rounded to 4 decimal places".format(number) )
       The rounded value of number is 1.2346 when rounded to 4 decimal places

   OK, so what does this all mean? Well, there's a few things we can
   say.

-  The ``.format()`` method must be used on a character string, and the
   variable (or variables) within the parentheses is the value that will
   be formatted (``number`` in this case).
-  The stuff in the curly brackets ``{`` and ``}`` is used to indicate a
   value that should be modified by the ``.format()`` method. Keep in
   mind that those curly brackets should be in a character string (i.e.,
   enclosed in quotation marks ``'`` or ``"``.
-  The ``0`` is used to indicate which item in the list of variables
   should be formatted, like an index value. If there was a second value
   given in the ``.format()`` method's list of arguments, its index
   would be ``1``.
-  The ``:f`` is used to specify that the value in the ``.format()``
   method's parentheses should be formatted as a floating point value.
-  The ``.3``, ``.1``, and ``.4`` are the number of decimal places. This
   should hopefully help when you write out your average summer and
   winter temperature values.

Part 3 - Saving your seasonal average files to GitHub
-----------------------------------------------------

Practical tips
~~~~~~~~~~~~~~

1. **Check your files before uploading them to GitHub**. Just a
   suggestion here. You should take a look at the values in your data
   files before you upload them to make sure the values look reasonable.
   The temperature values are in Fahrenheit. Feel free to convert them
   to Celsius, but make a note that the temperatures are in Celsius when
   you commit the files.

**Home**: `Lesson 5 main
page <https://github.com/Python-for-geo-people/Lesson-5-Reading-Writing>`__\ 
**Previous**: `Exercise 5: Analysing NOAA climate
data <https://classroom.github.com/assignment-invitations/17f0f2ee87873cb1bcb2c6a9ec228c42>`__
