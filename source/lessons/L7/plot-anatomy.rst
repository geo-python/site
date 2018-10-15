Anatomy of a plot
=================

Before starting to do plotting it is useful if we take a look and try to understand **what actually is a plot?**
We won't go too deep into the details of different plots (as it is not the purpose of this lesson) but we rather give a short introduction to different plots that can be done with Python, and what kind of (typical) elements a plot has.

There are a variety of different kinds of plot (also known as graphs or charts or diagrams etc. - Our dear child has many names) available that have been designed to represent visually the characteristics of a dataset.
Here is a list of few different types of plots that can be used to visualize different kinds of datasets:

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

There are certain elements that are common in most of the plots (not all).
It is useful to know at least the basic terminology since it makes it easier to find help and information from the internet when you start doing or modifying your own plot.

Following figure illustrates different elements of a basic line chart.

.. figure:: img/basic-elements-of-plot.png
   :width: 600px
   :align: center
   :alt: Basic elements of a plot

   Basic elements of a plot.

Common terms when doing plotting
--------------------------------

These common terms may vary a little bit depending on the plotting library that you use.
These are few typical terms used when doing plotting in Matplotlib.

- **axis** - Axis of the graph that are typically x, y and z (for 3D plots).
- **title** - Title of the whole plot.
- **label** - Name for to the whole axis.
- **legend** - Legend for the plot.
- **tick label** - Refers to the text or values that are represented on the axis.
- **symbol** - Symbol for data point(s) (on a scatter plot) that can be presented with different symbols.
- **size** - Size of e.g. a point on a scatter plot, also used for referring to the text sizes on a plot.
- **linestyle** - The style how the line should be drawn. Can be e.g. solid or dashed.
- **linewidth** - The width of a line in a plot.
- **alpha** - Transparency level of a filled element in a plot (values between 0.0 (fully transparent) to 1.0 (no trasnparency)).
- **tick(s)** - Refers to the tick marks on a plot.
- **annotation** - Refers to the added text on a plot.
- **padding** - The distance between a (axis/tick) label and the axis.