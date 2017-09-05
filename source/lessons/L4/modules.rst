Loading and using Python modules
================================

Sections
--------

1. `What is a module? <#what-is-a-module>`__
2. `How can modules be loaded? <#how-can-modules-be-loaded>`__
3. `How can modules be used? <#how-can-modules-be-used>`__
4. `What should I *not* do? <#what-should-i-not-do>`__

What is a module?
-----------------

A *module* in Python is simply a Python ``.py`` file that contains a
list of related functions that can be loaded and used. Modules are
similar to what are more generally called *libraries* in programming
languages, which again contain code related to a specific task such as
mathematical operations. There are a *HUGE* number of Python modules,
and many of them greatly extend what can be done in a normal Python
interpreter window. In fact, the abundance of free Python modules is one
of the best reasons to learn and start using Python.

How can modules be loaded?
--------------------------

Python modules can be loaded in a number of different ways.

1. Let's start simple with the ``math`` module. Here, we'll load the
   ``math`` module using the ``import`` statement.

   .. code:: python

       >>> import math
       >>> math.sqrt(81)
       9.0

   Here we have loaded the ``math`` module by typing ``import math``,
   which tells Python to read in the functions in the ``math`` module
   and make them available for use. In our example, we see that we can
   use a function within the ``math`` library by typing the name of the
   module first, a period, and then the name of function we would like
   to use afterward (e.g., ``math.sqrt()``). Built-in functions such as
   ``print()`` do not require the name of the module first since nothing
   is explicitly imported.
2. We can also rename modules when they are imported. This can be
   helpful when using modules with longer names.

   .. code:: python

       >>> import math as m
       >>> m.sqrt(49)
       7.0
       >>> type(m)
       module

   In this example we now see that when the ``math`` module is imported,
   it is imported to be usable with the name ``m`` instead of ``math``.
   It doesn't matter much in our toy example here since math is not a
   long module name, but we will see other examples later in the course
   where renaming the modules is very helpful (e.g., ``matplotlib``).
3. It is also possible to import only a single function from a module,
   rather than the entire module. This is sometimes useful when using
   large modules that have much more available than the desired use.

   .. code:: python

       >>> from math import sqrt
       >>> sqrt(121)
       >>> 11.0

   Though this can be useful, it has the drawback that the imported
   function could conflict with other built-in or imported function
   names, and you lose the information about which module contains the
   function. You should really only do this when you truly need to.
4. Some modules have sub-modules that can also be imported without
   importing the entire module. We will see examples of this later when
   making data plots using the pyplot sub-module of the `Matplotlib
   module <http://matplotlib.org/>`__. In case you're curious, here is
   an example.

   .. code:: python

       >>> import matplotlib.pyplot as plt
       >>> plt.figure()
       <matplotlib.figure.Figure at 0x10bfac4e0>

   This creates a new figure window for a pyplot figure. Again, we'll
   see how this works and what it means later in the course.

How can modules be used?
------------------------

As we see above, the easiest way to use a module is to import it and
then use its functions by typing *modulename.functionname()* and
providing the necessary arguments. Yes, it is that simple.

However, there are times you may not know the names of all of the
functions in a given module, or which are part of a module. You can view
the list of functions that are part of a module by using the ``dir()``
function.

.. code:: python

    >>> print(dir(math))
    ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

So that's helpful, but what about when you don't know what a given
function does? The easiest solution is to use the ``help()`` function.

.. code:: python

    >>> help(math.sin)
    Help on built-in function sin in module math:

    sin(...)
        sin(x)

        Return the sine of x (measured in radians).
    (END)

Note that you'll need to press **q** to exit the help viewer.

What should I *not* do?
-----------------------

Here are a few things to avoid.

1. **Don't use ``from X import *``**. This may be easier to understand
   by way of an example, but assuming ``X`` above is a Python module,
   ``from X import *`` will import all of the functions in module ``X``.
   Though you might think this is helpful, it is much better to simply
   ``import X`` or ``import X as Y`` to keep the connection between the
   functions and their module. It is also much more likely you will
   encounter conflicting names when using ``from X import *``.
2. **Don't use confusing names when renaming on import**. Be smart when
   you import modules. If you want to make the module name shorter on
   import, pick a reasonable abbreviation. For instance,
   ``import matplotlib as m`` could be confusing, especially if you're
   also using ``import math as m`` in other script files. Similarly,
   ``import matplotlib as math`` is perfectly OK syntax in Python, but
   bound to cause a world of trouble. Remember, people need to be able
   to read and understand the code you write, keep it simple and
   logical.

**Next**: `Exercise 4: A temperature
calculator <https://classroom.github.com/assignment-invitations/b1ad919e5a8248a11839fec83e45093e>`__\ 
**Home**: `Lesson 4 main
page <https://github.com/Python-for-geo-people/Lesson-4-Functions-Modules>`__\ 
**Previous**: `Basic concepts of functions <functions.md>`__
