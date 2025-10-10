Exercise 7
==========

.. note::

    Exercise 7 is due by **23:59 on Monday, October 21st, 2024**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 7 by** accepting the `GitHub Classroom assignment <https://classroom.github.com/a/E_Jdi9Ve>`__

You can also take a look at the template repository for `Exercise 7 on GitHub <https://github.com/Geo-Python-2025/Exercise-7>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.


Cloud computing environments
-----------------------------

.. image:: https://img.shields.io/badge/launch-binder-red.svg
   :target: https://mybinder.org/v2/gh/Geo-Python-2024/Binder/main?urlpath=lab
   
.. image:: https://img.shields.io/badge/launch-CSC%20Noppe-blue.svg
   :target: https://noppe.csc.fi/

Hints for Exercise 7
--------------------

Generating random numbers
~~~~~~~~~~~~~~~~~~~~~~~~~

We can generate random numbers using using a method ``random.rand()`` from the `NumPy package <https://numpy.org/>`__. This example generates 10 random values:

.. code-block:: python

    import numpy as np
    random_numbers = np.random.rand(10)

This produces an array object ``random_numbers`` that could look, for example, like this (each time you run the code you get a different set of random numbers!):

.. code-block:: python

    array([0.30888937, 0.02648327, 0.62740074, 0.75795089, 0.41083545,
           0.91937694, 0.90100588, 0.33312242, 0.39950947, 0.8181788 ]

You can insert this array into a column in a pandas DataFrame as follows, assuming that the array length and DataFrame length match:

.. code-block:: python

    ...

    data["new_column"] = random_numbers

Formatting your plots
~~~~~~~~~~~~~~~~~~~~~

- You can control the marker size using the parameter ``markersize`` when plotting. The example plot in Problem 2 uses ``markersize=3``.
- You can add grid lines to your plot using ``plt.grid()``