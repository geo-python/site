Anatomy of a plot
=================

Before starting to plot our data we need to start with an obvious question: **What actually is a plot?**
We won't go too deep into the details of different plots (as it is not the purpose of this lesson), but rather we will give a short introduction to different plots that can be created with Python, and the (typical) elements of a plot.

There are a variety of different kinds of plots (also known as graphs, charts, diagrams, etc. - Our dear child has many names) available that have been designed to visually represent the characteristics of a dataset.
Here is a list of several different types of plots that can be used to visualize different kinds of datasets:

- `Bar chart <https://en.wikipedia.org/wiki/Bar_chart>`__
- `Histogram <https://en.wikipedia.org/wiki/Histogram>`__
- `Scatter plot <https://en.wikipedia.org/wiki/Scatter_plot>`__
- `Line chart <https://en.wikipedia.org/wiki/Line_chart>`__
- `Pie chart <https://en.wikipedia.org/wiki/Pie_chart>`__
- `Box plot <https://en.wikipedia.org/wiki/Box_plot>`__
- `Violin plot <https://en.wikipedia.org/wiki/Violin_plot>`__
- `Dendrogram <https://en.wikipedia.org/wiki/Dendrogram>`__
- `Chord diagram <https://en.wikipedia.org/wiki/Chord_diagram>`__
- `Treemap <https://en.wikipedia.org/wiki/Treemap>`__
- `Network chart <https://en.wikipedia.org/wiki/Network_chart>`__

In spite of the large variety of plots, there are certain elements that are common for most of the plots (not all).
Thus, it is useful to know at least the basic terminology since it makes it easier to find help and information from the internet when you start creating or modifying your own plots.

The following figure illustrates different elements of a basic line plot.

.. figure:: img/basic-elements-of-plot.png
   :width: 800px
   :align: center
   :alt: Basic elements of a plot

   Basic elements of a plot.

Common plotting terms
---------------------

These common terms may vary a bit depending on the plotting library that you use, but these are some typical terms used when plotting in Matplotlib, for example.

- **axis** - Axis of the graph that are typically x, y and z (for 3D plots).
- **title** - Title of the whole plot.
- **label** - Name for the whole axis.
- **legend** - Legend for the plot.
- **tick label** - Text or values that are represented on the axis.
- **symbol** - Symbol for data point(s) (on a scatter plot) that can be presented with different symbol shapes/colors.
- **size** - Size of, for example, a point on a scatter plot. Also used for referring to the text sizes on a plot.
- **linestyle** - The style how the line should be drawn. Can be solid or dashed, for example.
- **linewidth** - The width of a line in a plot.
- **alpha** - Transparency level of a filled element in a plot (values between 0.0 (fully transparent) to 1.0 (no trasnparency)).
- **tick(s)** - Refers to the tick marks on a plot.
- **annotation** - Refers to the text added to a plot.
- **padding** - The distance between a (axis/tick) label and the axis.