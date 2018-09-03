Plotting with Matplotlib
==================================

Though there are many options for plotting data in Python, we will be using `Matplotlib <http://Matplotlib.org/>`__.
In particular, we will be using the pyplot module in Matplotlib, which provides MATLAB-like plotting.
The reason for this is simple: Matplotlib is the most common module used for plotting in Python and many examples of plotting you may find online will be using Matplotlib.

Downloading the data and preparing
----------------------------------

1. For our first lesson plotting data using Matplotlib we will again be using the `weather data file <../../_static/data/L5/Kumpula-June-2016-w-metadata.txt>`__ from :doc:`Lesson 5 <../L5/overview>`.

   - Save a copy of this file in your home directory or a directory for the materials for this week's lesson.

   - The data file contains observed daily mean, minimum, and maximum temperatures from June 2016 recorded from the Kumpula weather observation station in Helsinki.
     It is derived from a data file of daily temperature measurments downloaded from the `US National Oceanographic and Atmospheric Administration's National Centers for Environmental Information climate database <https://www.ncdc.noaa.gov/cdo-web/>`__.

   - We expect something like 30 lines of data in the data file.

2. If you have not already started **Spyder** you should do so now.
   You can find :doc:`directions on how to open Spyder at the start of Lesson 1<../L1/A-taste-of-Python>`.

3. Navigate in Spyder to the directory where you have stored the downloaded data file.
   You can do this most easily in Spyder by using the filesystem browser above the File/Variable explorer panel.
   Click on the file folder to select the directory where you would like to work, click **Open**, then click on the listed file path that is now displated beside the file folder and press **Enter**.

Spyder plots in separate windows
--------------------------------

By default, **Spyder** plots will be shown in the IPython console, but this can be annoying when saving and interacting with the plots we make.
We can change how plots are displayed in Spyder to have them show up in a separate window by changing the preferences.

1. Start by opening the **Spyder** preferences.

   - Mac users can go to **python** -> **Preferences...** in the menubar
   - Linux/Windows users can go to **Tools** -> **Preferences**

2. In the Preferences window, click on **IPython console** on the left side of the window, then on the **Graphics** tab.
3. Under **Graphics backend**, select **Automatic** for the backend.
4. Restart **Spyder**.

Plotting data with Matplotlib
-----------------------------

1. To start, we will need to import both Pandas and pyplot.

   .. ipython:: python

    import pandas as pd
    import matplotlib.pyplot as plt

   Note again that we are renaming the modules when we import them.
   Perhaps now it is more clear why you might want to rename a module on import.
   Having to type ``matplotlib.pyplot`` every time you use one of its methods would be a pain.

2. With our modules imported, we now can read in the data file in the same way we had for :doc:`Lesson 5 <../L5/pandas-basics>`.

   .. ipython:: python
     :suppress:

       import os
       fp = os.path.join(os.path.abspath('data'), 'L5', "Kumpula-June-2016-w-metadata.txt")
       dataFrame = pd.read_csv(fp, skiprows=8)

   .. ipython:: python
     :verbatim:
    
      dataFrame = pd.read_csv('Kumpula-June-2016-w-metadata.txt', skiprows=8)

   As you may recall, we will now have a Pandas DataFrame with 4 columns.

   .. ipython:: python

    print(dataFrame.columns)

3. OK, so let's get to plotting!
   We can start by using the Matplotlib ``plt.plot()`` function.

   .. ipython:: python

    x = dataFrame['YEARMODA']
    y = dataFrame['TEMP']
    plt.plot(x, y)
    @savefig plt_temp.png width=600px
    plt.show()

   If all goes well, you should see the plot above.

   OK, so what happened here?
   Well, first we assigned the values we would like to plot, the year and temperature, to the variables ``x`` and ``y``.
   This isn't necessary, per se, but does make it easier to see what is plotted.
   Next, it is perhaps pretty obvious that ``plt.plot()`` is a function in pyplot that produces a simple *x*-*y* plot.
   However, just like most variables in Python, creating the plot simply stores the information about the plot in memory.
   The plot is not displayed on the screen until you type ``plt.show()``.

4. We can make our plot look a bit nicer and provide more information by using a few additional pyplot options.

   .. ipython:: python

    plt.plot(x, y, 'ro--')
    plt.title('Kumpula temperatures in June 2016')
    plt.xlabel('Date')
    plt.ylabel('Temperature [°F]')
    @savefig plt_temp_annotated.png width=600px
    plt.show()

   This should produce the plot above.

   Now we see our temperature data as a red dashed line with circles showing the data points.
   This comes from the additional ``ro--`` used with ``plt.plot()``.
   In this case, ``r`` tells the ``plt.plot()`` function to use red color, ``o`` tells it to show circles at the points, and ``--`` says to use a dashed line.
   You can use ``help(plt.plot)`` to find out more about formatting plots.
   Better yet, check out the `documentation for plt.plot() online <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot>`__.
   We have also added a title and axis labels, but their use is straightforward.

5. Adding text to plots can be done using ``plt.text()``.

   .. ipython:: python

    plt.text(20160604.0, 68.0, 'High temperature in early June')

   This will display the text "High temperature in early June" at the location *x* = 20160604.0 (i.e., June 4, 2016), *y* = 68.0 on the plot.
   You would need to type the other plotting commands and ``plt.show()`` again to display the plot.

6. Changing the plot axes can be done using the ``plt.axis()`` function.

   .. ipython:: python

    plt.axis([20160615, 20160630, 55.0, 70.0])

   The format for ``plt.axis()`` is ``[xmin, xmax, ymin, ymax]`` enclosed in square brackets (i.e., a Python list).
   Here, the *x* range would be changed to the equivalents of June 15, 2016 to June 30, 2016 and the *y* range would be 55.0-70.0.
   The complete set of commands to plot would thus be:

   .. ipython:: python

    plt.plot(x, y, 'ro--')
    plt.title('Kumpula temperatures in June 2016')
    plt.xlabel('Date')
    plt.ylabel('Temperature [°F]')
    plt.text(20160604.0, 68.0, 'High temperature in early June')
    plt.axis([20160615, 20160630, 55.0, 70.0])
    @savefig plt_temp_annotated_w_text.png width=600px
    plt.show()

   Note that the text does not appear here because of the axis range.

7. In addition to line plots, there are many other options for plotting in Matplotlib.
   Bar charts are one option, which can be used quite similarly to line plots.

   .. ipython:: python

    plt.bar(x, y)
    plt.title('Kumpula temperatures in June 2016')
    plt.xlabel('Date')
    plt.ylabel('Temperature [°F]')
    plt.text(20160604.0, 68.0, 'High temperature in early June')
    plt.axis([20160615, 20160630, 55.0, 70.0])
    @savefig plt_temp_annotated_w_bars.png width=600px
    plt.show()

   You can find more about how to format bar charts on the `Matplotlib documentation website <https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html?highlight=matplotlib%20pyplot%20bar#matplotlib.pyplot.bar>`__.

8. Saving plots created using Matplotlib done several ways, but the easiest is simply to click on the disk icon on the pyplot window when a plot is displayed, as shown below.

   .. figure:: img/saving-plot.png
    :width: 600px
    :align: center
    :alt: Saving a plot in Python

   This brings up a familiar file saving window.
   Matplotlib plots can be saved in a number of useful file formats, including JPEG, PNG, PDF, and EPS, as you can see below.

   .. figure:: img/plot-file-types.png
    :width: 600px
    :align: center
    :alt: Matplotlib plot types
   
   PNG is a nice format for raster images, and EPS is probably easiest to use for vector graphics.

.. attention::

   **Plotting like the "pros"**

   We're only introducing a tiny amount of what can be done with pyplot.
   In most cases, when we would like to create some more complicated type of plot, we would search using `Google <https://www.google.fi>`__ or visit the `Matplotlib plot gallery <http://matplotlib.org/gallery.html>`__.
   The great thing about the `Matplotlib plot gallery <http://matplotlib.org/gallery.html>`__ is that not only can you find example plots there, but you can also find the Python commands used to create the plots.
   This makes it easy to take a working example from the gallery and modify it for your use.

   .. figure:: img/Matplotlib-gallery.png
    :width: 600px
    :align: center
    :alt: The Matplotlib plot gallery

    The Matplotlib plot gallery

   Your job in this task is to:

   1. Visit the `Matplotlib plot gallery <http://matplotlib.org/gallery.html>`__
   2. Find an interesting plot and click on it
   3. Copy the code you find listed beneath the plot on the page that loads
   4. Paste that into an IPython window or the IPython console in **Spyder** to reproduce the plot.

   After you have reproduced the plot, you are welcome to try to make a small change to the plot commands and see what happens.
   For this, it may be easiest to save a copy of the commands in a ``.py`` script file that you can edit and run.

.. attention::

   **Task 3: Plotting only part of a dataset**

   For this task, you should use the values for arrays ``x`` and ``y`` calculated earlier in this part of the lesson, and use ``plt.axis()`` to limit the plot to the following *x* and *y* ranges: *x* = June 7-14, *y* = 45.0 to 65.0.
   
   - What do you expect to see in this case?
   - **Note**: In order to get the plot to display properly, you will need to first type in the ``plt.plot()`` command, then ``plt.axis()``, and finally ``plt.show()``.
