Functions
=========

Sources
-------

This lesson is partly based on the `Software Carpentry
group's <http://software-carpentry.org/>`__ lessons on `Programming with
Python <http://swcarpentry.github.io/python-novice-inflammation/>`__.

**Contents**:

1. `What is a function? <#1>`__
2. `Anatomy of a function <#2>`__
3. `Calling functions <#3>`__
4. `"Pro" tips (optional extra material) <#4>`__

   1. `Saving functions in a Python script <#4.1>`__
   2. `Calling functions from a script <#4.2>`__
   3. `Temperature calculator <#4.3>`__

1. What is a function?
----------------------

A function is a block of organized, reusable code that can make your
code more effective, clearer to read and easier to handle. You can think
functions as little self-contained programs that can perform a specific
task which you can use repeatedly in your code. One of the basic
principles in good programming is "not to repeat yourself", i.e. you
shouldn't have duplicate lines of code in your script. Functions are a
way to avoid such situations and they can save you a lot of time and
effort as you don't need to retell the computer what to do every time it
does a common task, such as converting temperatures from Fahrenheit to
Celsius. During the course we have already used some functions such as
``print()`` command which is actually a built-in function in Python.

 2. Anatomy of a function
-------------------------

Let's consider the task from the first week when we converted
temperatures from Fahrenheit to Celsius. Such an operation is a fairly
common task when dealing with temperature data. Thus we might need to
repeat such calculations quite frequently when analysing or comparing
e.g. weather or climate data between the US and Europe.

1. Let's define our first function called ``celsius_to_fahr``:

   .. code:: python

       >>> def celsius_to_fahr(temp):
       ...    return 9/5 * temp + 32

The function definition opens with the keyword ``def`` followed by the
name of the function and a list of parameter names in parentheses. The
body of the function — the statements that are executed when it runs —
is indented below the definition line.

When we call the function, the values we pass to it are assigned to the
corresponding parameter variables so that we can use them inside the
function (e.g., the variable ``temp`` in this function example). Inside
the function, we use a return statement to define the value that should
be given when the function is used.

 3. Calling functions
---------------------

2. Let’s try running our function. Calling our self-defined function is
   no different from calling any other function such as ``print()``. You
   need to call it with its name and send your value to the required
   parameter(s) inside the parentheses:

   .. code:: python

       >>> freezing_point =  celsius_to_fahr(0)
       >>> print('Freezing point of water in Fahrenheit:', freezing_point)
       Freezing point of water in Fahrenheit: 32.0
       >>> print('Boiling point of water in Fahrenheit:', celsius_to_fahr(100))
       Boiling point of water in Fahrenheit: 212.0

3. Now that we know how to create a function to convert Celsius to
   Fahrenheit, let's create another function called
   ``kelvin_to_celsius``:

   .. code:: python

       >>> def kelvin_to_celsius(temp_k):
       ...    return temp_k - 273.15

4. And let's use it in a similar way as the earlier one:

   .. code:: python

       >>> absolute_zero = kelvin_to_celsius(temp_k=0)
       >>> print('Absolute zero in Celsius:', absolute_zero)
       Absolute zero in Celsius: -273.15

5. What about converting Kelvins to Fahrenheit? We could write out an
   own formula for it, but we don’t need to. Instead, we can compose it
   by using the two functions we have already created and calling those
   from the function we are now creating:

   .. code:: python

       >>> def kelvin_to_fahrenheit(temp_k):
       ...    # Kelvin in celsius
       ...    temp_c = kelvin_to_celsius(temp_k)
       ...    # Celsius in Fahrenheit
       ...    temp_f = celsius_to_fahr(temp_c)
       ...    # Return the result
       ...    return temp_f

6. Let's use the function:

   .. code:: python

       >>> absolute_zero_f = kelvin_to_fahrenheit(temp_k=0)
       >>> print('Absolute zero in Fahrenheit:', absolute_zero_f)
       Absolute zero in Fahrenheit: -459.66999999999996

Next steps
----------

Next, if you are interested you can go through the `extra materials
below <#4>`__ that teach you how to write and import functions from a
dedicated Python file. This can be quite handy when you start to have
many customized functions for different tasks. Otherwise, you can
`continue with the lecture materials. <../README.md>`__

 "Pro" tips (extra material)
============================

4. Importing functions from a script
------------------------------------

Functions such as the ones we just created can also be called from
another script. Quite often it is useful to create a dedicated function
library to such functions that you use frequently e.g. when doing data
analysis. Basically this is done by collecting useful functions to a
single ``.py`` file from where you can then import and use them whenever
needed.

 4.1. Saving functions into a script file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before we can import our functions we need to create a new script file
and save the functions that we just created into a Python file called
*temp\_converter.py* [`0 <#Footnotes>`__].

We could write the functions again into our script file but we can also
take advantage of the **History log** tab where we should find all
commands that we wrote in the IPython console [`1 <#Footnotes>`__]:

1. Copy and paste (only) the functions that we wrote earlier from the
   History log tab and save them into the *temp\_converter.py* script (
   *optionally just write them again into the file* ). It should look
   like following:

 4.2. Calling functions from another script file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now as we have saved our temperature conversion functions into a script
file we can start using them.

.. raw:: html

   <ol start="2">

.. raw:: html

   <li>

Let's create another script file called calculator.py. IMPORTANT: Save
the file into the SAME FOLDER where you saved the temp\_converter.py
-file [2].

.. raw:: html

   </li>

.. raw:: html

   </ol>

.. raw:: html

   <ol start="3">

.. raw:: html

   <li>

Let's now import our celsius\_to\_fahr -function from the other script
by adding a specific import statement at the top of our calculator.py
-script. Let's also use the function so that we can see that it is
working [3]:

.. raw:: html

   </li>

.. raw:: html

   </ol>

\`\`\`python from temp\_converter import celsius\_to\_fahr

# Testing that the function from another file works print("Water
freezing point in Fahrenheit:", celsius\_to\_fahr(0)) \`\`\`

.. raw:: html

   <ol start="4">

.. raw:: html

   <li>

Run the code by pressing F5 button or by pressing the -button in Spyder.
We should now get following output:

.. raw:: html

   </li>

.. raw:: html

   </ol>

-  *It is also possible to import more functions at the same time by
   listing and separating them with colon:*

``python   from my_script import func1, func2, func3``

.. raw:: html

   <ol start="5">

.. raw:: html

   <li>

Sometimes it is useful to import the whole script and its' functions at
once.
Let's modify the import statement in our script and test that all
functions work [4]:

.. raw:: html

   </li>

.. raw:: html

   </ol>

\`\`\`python import temp\_converter as tc

# Testing that all functions from another file works print("Water
freezing point in Fahrenheit:", tc.celsius\_to\_fahr(0)) print('Absolute
zero in Celsius:', tc.kelvin\_to\_celsius(temp\_k=0)) print('Absolute
zero in Fahrenheit:', tc.kelvin\_to\_fahrenheit(temp\_k=0)) \`\`\`

 4.3. Temperature calculator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So far our functions has had only one parameter but it is also possible
to define a function with multiple parameters. Let's now make a simple
``temp_calculator`` -function that converts and returns Kelvin
temperature to either Celsius or Fahrenheit. Function will have two
parameters:

-  **temp** = parameter for passing temperature in Kelvin
-  **convert\_to** = parameter that determines whether to output should
   be in Celsius or in Fahrenheit (using letters "C" or "F" accordingly)

1. Let's start defining our function by giving it a name and setting the
   parameters:

   .. code:: python

       def temp_calculator(temp, convert_to):

2. Next, we need to add conditional statements that check whether the
   result temperature is wanted in Celsius or in Fahrenheit and then
   call corresponding function that was imported from temp\_converter.py
   file.

   .. code:: python

       def temp_calculator(temp, convert_to):
           # Check if user wants the temperature as Celsius
           if convert_to == "C":
               # Convert the value to Celsius using dedicated function for the task that we imported from another script
               converted_temp = kelvin_to_celsius(temp_k=temp)
           elif convert_to == "F":
               # Convert the value to Fahrenheit using dedicated function for the task that we imported from another script
               converted_temp = kelvin_to_fahrenheit(temp_k=temp)

3. Next, we need to add a **return statement** so that our function
   sends back the value that we are interested in:

   .. code:: python

       def temp_calculator(temp, convert_to):
           # Check if user wants the temperature as Celsius
           if convert_to == "C":
               # Convert the value to Celsius using dedicated function for the task that we imported from another script
               converted_temp = kelvin_to_celsius(temp_k=temp)
           elif convert_to == "F":
               # Convert the value to Fahrenheit using dedicated function for the task that we imported from another script
               converted_temp = kelvin_to_fahrenheit(temp_k=temp)
           # Return the result
           return converted_temp

4. Lastly, as we want to be good programmers, we add a short message at
   the beginning of our function that tells what the function does and
   how the parameters work:

   .. code:: python

       def temp_calculator(temp, convert_to):
           """
           Function for converting Kelvin temperature to Celsius or Fahrenheit.

           Parameters:
           -----------
           temp: Temperature in Kelvin <numerical>
           convert_to: Target temperature that can be either Celsius ('C') or Fahrenheit ('F'). Possible values: 'C' | 'F'
           """

           # Check if user wants the temperature as Celsius
           if convert_to == "C":
               # Convert the value to Celsius using dedicated function for the task that we imported from another script
               converted_temp = kelvin_to_celsius(temp_k=temp)
           elif convert_to == "F":
               # Convert the value to Fahrenheit using dedicated function for the task that we imported from another script
               converted_temp = kelvin_to_fahrenheit(temp_k=temp)
           # Return the result
           return converted_temp

5. That's it! Now we have a simple temperature calculator that has a
   simple control for the user where s/he can change the output by using
   the ``convert_to`` -parameter. Now as we added the short description
   in the beginning of the function we can use the ``help()`` function
   in Python to find out how our function should be used. Run the script
   and try following:

``python   >>> help(temp_calculator)``

Let's use it:

``python   >>> temp_in_kelvin = 30   >>> temperature_c = temp_calculator(temp=temp_in_kelvin, convert_to="C")   >>> print("Temperature", temp_in_kelvin, "in Kelvin is", temperature_c, "in Celsius")   Temperature 30 in Kelvin is -243.14999999999998 in Celsius.``

Footnotes
---------

-  [0] See `earlier materials concerning Spyder <spyder.md>`__ if you
   don't remember how to save a new script file from Spyder.
-  [1] History log -tab can be found from the same panel where we have
   executed our codes (bottom right next to IPython console).
-  [2] When communicating between script files, it is necessary to keep
   them in the same folder so that Python can find them (there are also
   other ways but this is the easiest).
-  [3] Following the principles of good programming all ``import``
   -statements that you use should always be written at the top of the
   script file.
-  [4] It is also possible to import functions by using specific \*
   -character:``from module_X import *``. Downside of using \* symbol to
   import all functions is that you won't see what functions are
   imported, unless checking them from the script itself or use
   ``dir()`` -function to list them (see
   `modules.md <modules.md#using-modules>`__). Warning: there is a risk
   of conflict when doing this, use with care (see more from modules.md)

**Next**: `Loading and using modules <modules.md>`__\  **Home**: `Lesson
4 main
page <https://github.com/Python-for-geo-people/Lesson-4-Functions-Modules>`__\ 
**Previous**: `Using the Spyder IDE <spyder.md>`__
