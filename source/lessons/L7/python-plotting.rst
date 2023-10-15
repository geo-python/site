Plotting in Python
==================

.. figure:: https://rougier.github.io/python-visualization-landscape/landscape-colors.png
   :width: 800px
   :align: center
   :alt: Python plotting options
   :class: dark-light

   Plotting libraries available in Python. Source: `https://pyviz.org/overviews/index.html <https://pyviz.org/overviews/index.html>`__\.

Python has many nice, useful libraries that can be used for plotting.
In the figure above, you can see a number of the available plotting library options, along with how they relate to one another.
Of the options above, we would like to highlight:

- `Matplotlib <https://matplotlib.org/>`__: Matplotlib is one of the most widely used Python plotting libraries, sometimes referred to as "*the grand old man of Python plotting*". Plot examples can be found in the `Matplotlib gallery <https://matplotlib.org/stable/gallery/index.html>`__.

  - `Matplotlib Basemap <https://matplotlib.org/basemap/index.html>`__: The Matplotlib Basemap Toolkit is a plugin for visualizing maps in Python. Example plots available in the `Matplotlib basemap gallery <https://matplotlib.org/basemap/users/examples.html>`__. **Note**: The Matplotlib Basemap project is being depricated in favor of `Cartopy <https://scitools.org.uk/cartopy/docs/latest/>`__ (`Cartopy gallery <https://scitools.org.uk/cartopy/docs/latest/gallery/index.html>`__).
  - `Seaborn <https://seaborn.pydata.org/>`__: Seaborn is a high-level interface for drawing attractive statistical graphics that is built on top of Matplotlib. Example plots can be found in the `Seaborn gallery <https://seaborn.pydata.org/examples/index.html>`__.

- `Bokeh <https://docs.bokeh.org/en/latest/>`__: Bokeh is a modern plotting library for static and interactive web-based plots including graphs, maps, and charts. Examples can be found in the `Bokeh gallery <https://docs.bokeh.org/en/latest/docs/gallery.html>`__.
- `Plotly <https://plotly.com/python/>`__: Similar in some ways to Bokeh, Plotly is a modern plotting library for static and interactive web-based plots. Some features are commercial. Example plots are available in the `Plotly gallery <https://plotly.com/python/basic-charts/>`__.
- `Dash <https://plotly.com/dash/>`__: Dash is a Python framework for building analytical web applications. No JavaScript required.
- `ggplot <https://yhat.github.io/ggpy/>`__: ggplot is a Python plotting environment for those familiar with creating plots in R using ggplot2. You can use ggplot in Python too! Plot examples can be found in the `(ggplot examples) <https://yhat.github.io/ggpy/>`__.
- `HoloViews <https://holoviews.org/>`__ and `GeoViews <https://geoviews.org/>`__: HoloViews and GeoViews aim to let the data visualize itself. Learn more in the `HoloViews introductory video <https://www.youtube.com/watch?v=hNsR2H7Lrg0>`__.

  - Modern and powerful visualization libraries built on top of Matplotlib and Bokeh that makes exploring and visualizing your data quicker than ever before
  - HoloViews is designed for basic plotting (`HoloViews tutorial <https://holoviews.org/Tutorials/index.html>`__ and `HoloViews examples <https://holoviews.org/Examples/index.html>`__)
  - GeoViews is designed for creating nice and interactive maps (`GeoViews gallery <https://geoviews.org/gallery/index.html>`__)

.. attention::

   Explore the galleries and examples of different visualization libraries above to learn what's possible to do in Python.

As you can see from the examples, the plotting possibilities in Python are numerous and rich.
Do you need to know them all?
Of course not.
Not even we do.
It is not even reasonable to use them all.
Instead you should start by learning to use one that suits your needs and then later extend your knowledge and skills to other visualization libraries when necessary.

.. note:: 

   In the Automating GIS processes II course we will be learning a bit of some other plotting libraries not used in the Geo-Python/AutoGIS I course.
