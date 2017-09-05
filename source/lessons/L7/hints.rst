Exercise 7 hints
================

Problem 1
---------

Problem 2
---------

Pseudocode
~~~~~~~~~~

There is no pseudocode to post since the exercise included a starter
code. There are, however, some important practical tips below.

Practial tips
~~~~~~~~~~~~~

-  **Using plotly-friendly plot colors**. One of the bad surprises this
   week with plotly was that you cannot save your plots if they contain
   any "pro" colors, like solid red, black or blue. One option that is
   easy to implement is to simply give the commands in matplotlib that
   produce different parts of the plot the ``color`` parameter. For
   instance, when you plot a set of red points using ``plt.plot()``, you
   could change the formatting parameter from ``'ro'`` to simply
   ``'o'``, and add a parameter to the list for ``color="#D62728"``, the
   "free" red on the plotly site. To be perfectly clear, this would look
   like

   .. code:: python

       plt.plot(x, y, 'o', color="#D62728")   # This is OK for plotly

   rather than

   .. code:: python

       plt.plot(x, y, 'ro')   # This uses the non-free "pro" red on plotly

   In fact, you could even go one step further and create a list of
   colors at the top of your script, and use those with the ``color``
   option. For example,

   .. code:: python

       # Define some plotly-friendly colors
       red="#D62728"
       blue="#1F77B4"
       dkgray="#444444"

       # Make some plot
       plt.plot(x, y, 'o', color=red)
       plt.title('My amazing plot', color=dkgray)

   et voilà, your plot should now use plotly-friendly colors, which
   means you can modify things *and save* without problems.
-  **Getting plots with a legend to export to plotly**. Yet another
   unpleasant surprise. As far as I can tell, it is currently not
   possible to use matplotlib to create a line and symbol legend on a
   plot, and have the exported to plotly. If you've tried this, you have
   undoubtedly encountered problems. Fortunately, we have a solution,
   albeit not a solution that is simply fixing a single line. To start,
   we can compare the codes below for making a plot and exporting to
   plotly. The top one will not work, the lower has been fixed to export
   to plotly. The ``...`` lines are places where many other lines of
   code exist, but are not relevant for this issue.

   .. code:: python

       # THIS WILL NOT WORK WITH PLOTLY

       # Import libraries
       import numpy as np
       import matplotlib.pyplot as plt
       import plotly.plotly as py
       from scipy.stats import linregress

       ...

       # Add legend
       plt.legend()

       # Export figure to plotly
       unique_url = py.plot_mpl(mpl_fig, filename="Seasonal average temperatures")

       ...

   .. code:: python

       # THIS WILL WORK WITH PLOTLY

       # Import libraries
       import numpy as np
       import matplotlib.pyplot as plt
       import plotly.plotly as py
       import plotly.tools as tls   # THIS IMPORT HAS BEEN ADDED
       from scipy.stats import linregress

       ...

       # DO NOT USE plt.legend(), DO THIS INSTEAD
       plotly_fig = tls.mpl_to_plotly(mpl_fig)   # This makes a plotly figure from matplotlib

       # Add plotly legend
       plotly_fig['layout']['showlegend'] = True
       plotly_fig['layout']['legend'] = {}

       # Export to plotly
       plot_url = py.plot(plotly_fig, filename='Seasonal average temperatures')

       ...

   As you can see, this is not a one-line fix, but it is also not that
   complicated. In essence, we need to ``import plotly.tools as tls``,
   and replace the use of ``plt.legend()`` and ``py.ploy(...)`` with the
   corresponding commands to have plotly create the legend. In this way,
   your plots should go nicely to plotly, including the legend. If you
   combine this fix with the plotly colors tip above, you should be in
   business!
-  **Example data files** In case you don't yet have Exercises 5 or 6
   working properly, we would still like you to be able to complete
   Exercise 7. For that task we have provided example data files
   produced by Exercises 5 and 6. For these data files, the data starts
   at 1940 and ends at 2015, which simply allows us to see whether
   you've used your own data file you produced, or the example data
   files. Otherwise, they should be identical to the expected results
   from Exercises 5 and 6. Links to the files are below.
-  `Summer temperatures from Exercise
   5 <../Data/summer-avg-temps-ex5.csv>`__
-  `Summer temperatures from Exercise
   6 <../Data/summer-avg-temps-ex6.csv>`__
-  `Winter temperatures from Exercise
   5 <../Data/winter-avg-temps-ex5.csv>`__
-  `Winter temperatures from Exercise
   6 <../Data/winter-avg-temps-ex6.csv>`__
-  **Using ``linregress()``**
-  **Modifying the axis ranges**
-  **Useful links from this week's lesson**

**Home**: `Lesson 7 main
page <https://github.com/Python-for-geo-people/Lesson-7-Plotting>`__\ 
**Previous**: `Exercise 7: Plotting with
Python <https://classroom.github.com/assignment-invitations/54ad87560677b78169f1c18717bb312e>`__
