Plotting in Python with matplotlib
==================================

Though there are many options for plotting data in Python, we will be using `matplotlib <http://matplotlib.org/>`__.
In particular, we will be using the pyplot module in matplotlib, which provides MATLAB-like plotting.
The reason for this is simple: Matplotlib is the most common module used for plotting in Python and many examples of plotting you may find online will be using matplotlib.

1. To start, we will need to import both pyplot and NumPy.

   .. ipython:: python

    import matplotlib.pyplot as plt
    import numpy as np

   Note again that we are renaming the modules when we import them.
   Perhaps now it is more clear why you might want to rename a module on import.
   Having to type ``matplotlib.pyplot`` every time you use one of its methods would be a pain.

2. With our modules imported, we now can quickly define a few variables to make our first plot.

   .. code:: python

       x = np.linspace(0, 2 * np.pi, 20)
       y = np.sin(x)

   We haven't seen ``np.linspace()`` previously. It simply creates a
   NumPy array starting from the first parameter value given, ending
   with the second, and using the third for the total number of values
   to include in the array. Values between the start and end are equally
   spaced, or linearly interpolated (hence the name ``linspace`` -
   linear space). Those in the Introduction to Quantitative Geology
   course will see ``np.linspace()`` again. As you might guess,
   ``np.sin()`` simply calculates the value of the sine function for
   each value of ``x``.
3. Now we're ready for our first plot.

   .. code:: python

       >>> plt.plot(x, y)
       [<matplotlib.lines.Line2D at 0x109e25898>]
       >>> plt.show()

   This should produce a plot like the one below.

   |Sine curve from zero to two pi|\  OK, so what happened here? First,
   it should be pretty obvious that ``plt.plot()`` is a function in
   pyplot that produces a simple x-y plot. However, just like most
   variables in Python, creating the plot simply stores the information
   about the plot in memory. The plot is not displayed on the screen
   until you type ``plt.show()``.
4. We can make our plot look a bit nicer and provide more information by
   using a few additional pyplot options.

   .. code:: python

       >>> plt.plot(x, y, 'ro--')
       [<matplotlib.lines.Line2D at 0x10bd249e8>]
       >>> plt.title('Sine curve')
       <matplotlib.text.Text at 0x10b0af320>
       >>> plt.xlabel('x-axis'); plt.ylabel('y-axis')
       <matplotlib.text.Text at 0x10b08df98>
       >>> plt.show()

   This should produce the plot below.

   |Fancy sine curve|\  Now we see our sine curve as a red dashed line
   with circles showing the points along the line. This comes from the
   additional ``ro--`` used with ``plt.plot()``. In this case, ``r``
   tells the ``plt.plot()`` function to use red color, ``o`` tells it to
   show circles at the points, and ``--`` says to use a dashed line. You
   can use ``help(plt.plot)`` to find out more about formatting plots.
   Better yet, check out the `documentation for ``plt.plot()``
   online <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot>`__.
   We have also added a title and axis labels, but their use is
   straightforward.
5. Adding text to plots can be done using ``plt.text()``.

   .. code:: python

       >>> plt.text(0.5, 0.5, 'Here is some text')

   This will display the text "Here is some text" at the location *x* =
   0.5, *y* = 0.5 on the plot. You would need to type ``plt.show()``
   again to display the plot.
6. Changing the plot axes can be done using the ``plt.axis()`` function.

   .. code:: python

       >>> plt.axis([0.0, np.pi, -0.5, 1.0])

   The format for ``plt.axis()`` is ``[xmin, xmax, ymin, ymax]``
   enclosed in square brackets (i.e., a Python list). Here, the *x*
   range would be changed to 0-π and the *y* range would be 0-1.
7. Saving plots created using matplotlib done several ways, but the
   easiest is simply to click on the disk icon on the pyplot window when
   a plot is displayed, as shown below.

   |Saving a plot|\  This brings up a familiar file saving window.
   Matplotlib plots can be saved in a number of useful file formats,
   including JPEG, PNG, PDF, and EPS, as you can see below.

   |Plot file types|\  PNG is a nice format for raster images, and EPS
   is probably easiest to use for vector graphics.

Task 2: Plotting like the "pros"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We're only introducing a tiny amount of what can be done with pyplot. In
most cases, when we would like to create some more complicated type of
plot, we would search using `Google <https://www.google.fi>`__ or visit
the `Matplotlib plot gallery <http://matplotlib.org/gallery.html>`__.
The great thing about the `Matplotlib plot
gallery <http://matplotlib.org/gallery.html>`__ is that not only can you
find example plots there, but you can also find the Python commands used
to create the plots. This makes it easy to take a working example from
the gallery and modify it for your use.

|The matplotlib gallery|\  *The matplotlib plot gallery*

Your job in this task is to:

1. Visit the `Matplotlib plot
   gallery <http://matplotlib.org/gallery.html>`__
2. Find an interesting plot and click on it
3. Copy the code you find listed beneath the plot on the page that loads
4. Paste that into an IPython window or the IPython console in
   **Spyder** to reproduce the plot.

After you have reproduced the plot, you are welcome to try to make a
small change to the plot commands and see what happens. For this, it may
be easiest to save a copy of the commands in a ``.py`` script file that
you can edit and run.

Task 3: Plotting only part of a dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this task, you should use the values for arrays ``x`` and ``y``
calculated earlier in this part of the lesson, and use ``plt.axis()`` to
limit the plot to the following *x* and *y* ranges: *x* = 0 to π, *y* =
0.0 to 1.0. - What do you expect to see in this case? - **Note**: In
order to get the plot to display properly, you will need to first type
in the ``plt.plot()`` command, then ``plt.axis()``, and finally
``plt.show()``.

.. |Sine curve from zero to two pi| image:: ../img/sine-curve.png
.. |Fancy sine curve| image:: ../img/sine-curve-improved.png
.. |Saving a plot| image:: ../img/saving-plot.png
.. |Plot file types| image:: ../img/plot-file-types.png
.. |The matplotlib gallery| image:: ../img/matplotlib-gallery.png

