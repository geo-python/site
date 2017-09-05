Plotting in Python
==================

Topics
~~~~~~

1. `Overview of useful modules for plotting in
   Python <#overview-of-useful-modules-for-plotting-in-Python>`__

-  `Task 1: Learn about the Python plotting options <#task1>`__

2. `Anatomy of a plot <#anatomy-of-a-plot>`__
3. `Plotting in Python with
   Matplotlib <#plotting-in-python-with-matplotlib>`__

-  `Task 2: Plotting like the "pros" <#task-2-plotting-like-the-pros>`__
-  `Task 3: Plotting only part of a
   dataset <#task-3-plotting-only-part-of-a-dataset>`__

Overview of useful modules for plotting in Python
-------------------------------------------------

Python has many nice and useful modules that can be used for plotting,
such as:

-  `**Matplotlib** <http://matplotlib.org/>`__ - *"the grand old man of
   Python plotting"* (`see
   gallery <http://matplotlib.org/gallery.html>`__)

   -  `**Matplotlib
      Basemap** <http://matplotlib.org/basemap/index.html>`__ -
      Matplotlib plugin for visualizing maps in Python `(see
      gallery) <http://matplotlib.org/basemap/users/examples.html>`__
   -  `**Seaborn** <https://seaborn.github.io/>`__ - High-level
      interface for drawing attractive statistical graphics that is
      built on top of Matplotlib (`see
      gallery <https://seaborn.github.io/examples/index.html>`__)

-  `**Bokeh** <http://bokeh.pydata.org/en/latest/>`__ - Modern plotting
   library for static / interactive web-based plots such as graphs,
   maps, charts etc. (`see
   gallery <http://bokeh.pydata.org/en/latest/docs/gallery.html>`__)
-  `**Plotly** <https://plot.ly/python/>`__ - Modern plotting library
   for static / interactive web-based plots such as graphs, maps, charts
   etc. Some features are commercial. (`see
   gallery <https://plot.ly/python/#basic-charts>`__)
-  `**ggplot** <https://github.com/yhat/ggplot>`__ - Familiar with doing
   plots in R using ggplot2? You can use ggplot in Python too! `(see
   examples) <https://github.com/yhat/ggplot/blob/master/docs/Gallery.ipynb>`__
-  `**HoloViews** <http://holoviews.org/>`__ and
   `**GeoViews** <http://geo.holoviews.org/>`__ - New! Let the data
   visualize itself. (see this `introductory
   video <https://www.youtube.com/watch?v=hNsR2H7Lrg0>`__)

   -  Modern and powerful visualization libraries built on top of
      **Matplotlib** and **Bokeh** that makes exploring and visualizing
      your data quicker than ever before.
   -  **HoloViews** is designed for basic plotting (`see
      tutorial <http://holoviews.org/Tutorials/index.html>`__ and
      `examples <http://holoviews.org/Examples/index.html>`__)
   -  **GeoViews** is designed for creating nice and interactive maps
      (`see
      gallery <https://www.continuum.io/blog/developer-blog/introducing-geoviews>`__).

\ **Task 1**: *Explore the galleries and examples of different
visualization libraries to learn what's possible to do in Python.*

As you can see from the examples, the plotting possibilities in Python
are numerous and rich. Do you need to know them all? Of course not. Not
even us do. It is not even rational for trying to use them all, instead
you should start by learning to use one of them that suits your needs
and then later extend your knowledge and skills to other visualizing
libraries when necessary. In our courses, we will be start our plotting
experiments with Matplotlib and Plotly that makes it possible to store
and show our interactive plots in the web.

*Later, in the Automating GIS processes -course, we will be learning a
little bit of Bokeh as well.*

**Pro -tip**: for doing interactive visualizations in Python, it can be
extremely useful to use a specific software called
**`Jupyter <https://jupyter.readthedocs.io/en/latest/index.html#>`__**
that is extensively used nowadays for documenting, presenting and
visualizing interactive plots in Python using specific
`Notebooks <https://tmp58.tmpnb.org/user/JfCwgSeJpZUg/notebooks/Welcome%20to%20Python.ipynb>`__.
Jupyter Notebook is also installed in our computer instance.

Anatomy of a plot
-----------------

Before starting to do plotting it is useful if we take a look and try to
understand **what actually is a plot?** We won't go too deep into the
details of different plots (as it is not the purpose of this lesson) but
we rather give a short introduction to different plots that can be done
with Python, and what kind of (typical) elements a plot has.

There are a variety of different kinds of plot (also known as graphs or
charts or diagrams etc. - Our dear child has many names) available that
have been designed to represent visually the characteristics of a
dataset. Here is a list of few different types of plots that can be used
to visualize different kinds of datasets:

-  `Bar chart <https://en.wikipedia.org/wiki/Bar_chart>`__
-  `Histogram <https://en.wikipedia.org/wiki/Histogram>`__
-  `Scatter plot <https://en.wikipedia.org/wiki/Scatter_plot>`__
-  `Line chart <https://en.wikipedia.org/wiki/Line_chart>`__
-  `Pie chart <https://en.wikipedia.org/wiki/Pie_chart>`__
-  `Box plot <https://en.wikipedia.org/wiki/Box_plot>`__
-  `Violin plot <https://en.wikipedia.org/wiki/Violin_plot>`__
-  `Dendrogram <https://en.wikipedia.org/wiki/Dendrogram>`__
-  `Chord diagram <https://en.wikipedia.org/wiki/Chord_diagram>`__
-  `Treemap <https://en.wikipedia.org/wiki/Treemap>`__
-  `Network chart <https://en.wikipedia.org/wiki/Network_chart>`__

There are certain elements that are common in most of the plots (not
all). It is useful to know at least the basic terminology since it makes
it easier to find help and information from the internet when you start
doing or modifying your own plot.

Following figure illustrates different elements of a basic line chart:

Common terms when doing plotting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: these terms may vary a little bit depending on the plotting
library that you use. These are few typical terms used when doing
plotting in Matplotlib.

-  **axis** - Axis of the graph that are typically x, y and z (for 3D
   plots)
-  **title** - Title of the whole plot.
-  **label** - Name for to the whole axis.
-  **legend** - Legend for the plot.
-  **tick label** - Refers to the text or values that are represented on
   the axis.
-  **symbol** - Symbol for data point(s) (on a scatter plot) that can be
   presented with different symbols.
-  **size** - Size of e.g. a point on a scatter plot, also used for
   referring to the text sizes on a plot.
-  **linestyle** - The style how the line should be drawn. Can be e.g.
   solid or dashed.
-  **linewidth** - The width of a line in a plot.
-  **alpha** - Transparency level of a filled element in a plot (values
   between 0.0 (fully transparent) to 1.0 (no trasnparency)).
-  **tick(s)** - Refers to the tick marks on a plot.
-  **annotation** - Refers to the added text on a plot.
-  **padding** - The distance between a (axis/tick) label and the axis.

Plotting in Python with matplotlib
----------------------------------

Though there are many options for plotting data in Python, we will be
using `matplotlib <http://matplotlib.org/>`__. In particular, we will be
using the pyplot module in matplotlib, which provides MATLAB-like
plotting. The reason for this is simple: Matplotlib is the most common
module used for plotting in Python and many examples of plotting you may
find online will be using matplotlib.

1. To start, we will need to import both pyplot and NumPy.

   .. code:: python

       import matplotlib.pyplot as plt
       import numpy as np

   Note again that we are renaming the modules when we import them.
   Perhaps now it is more clear why you might want to rename a module on
   import. Having to type ``matplotlib.pyplot`` every time you use one
   of its methods would be a pain.
2. With our modules imported, we now can quickly define a few variables
   to make our first plot.

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

**Next**: `Connecting Matplotlib with plotly <using-plotly.md>`__\ 
**Home**: `Lesson 7 main
page <https://github.com/Python-for-geo-people/Lesson-7-Plotting>`__\ 

.. |Sine curve from zero to two pi| image:: ../img/sine-curve.png
.. |Fancy sine curve| image:: ../img/sine-curve-improved.png
.. |Saving a plot| image:: ../img/saving-plot.png
.. |Plot file types| image:: ../img/plot-file-types.png
.. |The matplotlib gallery| image:: ../img/matplotlib-gallery.png

