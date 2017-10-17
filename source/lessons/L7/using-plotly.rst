Connecting Matplotlib with plotly
=================================

In the final part of this week's lesson, we will learn how to automatically export plots from `matplotlib <http://matplotlib.org/>`__ to `plotly <https://plot.ly/>`__, where they can be manipulated and shared online.

Plotly overview
---------------

.. figure:: img/plotly-site.png
   :width: 800px
   :align: center
   :alt: The plot.ly website

   The plot.ly website

`Plotly <https://plot.ly/>`__ is a web-based collaborative data visualization site where you can easily produce interactive plots and perform basic statistical analyses of data.
On the site you can find hundreds of example plots that you can view, interact with, and edit.
Essentially, it is a social plotting and data analysis site, and fortunately the basic community accounts are free.
We'll explore a few basic things we can do with plotly, mainly exporting matplotlib plots to plotly using `Plotly for Matplotlib <https://plot.ly/matplotlib/>`__.
If you're interested in learning more, you may want to start by looking at the `plotly tutorials <http://help.plot.ly/tutorials/>`__.

We're of the opinion that web-based interactive data is the future, and fortunately it is extremely easy to take your basic plots from matplotlib and directly export them to plotly.

Configuring matplotlib to work with plotly
------------------------------------------

The Plotly for Matplotlib modules are already installed on the computer instances for the course, but in order to be able to have plots in matplotlib automatically be tranferred to plotly, you need to have a special "API key" that connects your computer to your plotly account.

1. You can find your personal API key by going to the `plotly API settings page <https://plot.ly/settings/api>`__.
   You will be asked to log in to access this page.
2. After you have logged in, you should see the API settings page, which includes a value for your API key as shown in the image below.

   .. figure:: img/plotly-api-key.png
      :width: 800px
      :align: center
      :alt: The plot.ly API key
   
   You should select your plotly API key and copy it to the clipboard.
3. After you have copied your plotly API key, you should go to the Terminal window on your computer instance.
   If you have closed it, open another by double clicking on the **Terminal** icon on the Desktop.
4. In the terminal window, enter the following command, substituting your plotly user name for ``<username>`` and your API key for ``<api key>``.
   **Note**: This should be done in a **Terminal** window, not an IPython console!

   .. code:: bash

    $ ipython -c "import plotly; plotly.tools.set_credentials_file(username='<username>', api_key='<api key>')"

   This command will set up the connection between your computer instance and plotly.
   **Note**: On the cloud computers, you will need to do this every time you start a new computer instance.
   If you are working on your personal computer, you should only need to do this once (though you may need to `install plotly <https://plot.ly/matplotlib/getting-started/#installation>`__).

At this point you should be all set to start exporting plots to plotly.

Saving your first matplotlib plot to plotly
-------------------------------------------

1. To save plots to plotly, we basically just need to add a "wrapper" around the normal matplotlib commands you would use to make a plot.

   .. code:: python

    import matplotlib.pyplot as plt
    import plotly.plotly as py

    mpl_fig = plt.figure()
    # --> your matplotlib commands <--

    unique_url = py.plot_mpl(mpl_fig, filename="my first plotly plot")

   So that's it?
   Yes, all we need to do is ``import`` plotly and add a line where we use the plotly command to convert a matplotlib plot to plotly format and save to the plotly site (i.e., ``py.plot_mpl()``).
   Nice!
2. OK, so now let's look at a working example that can be saved to plotly.

   .. code:: python

    # Import modules
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.plotly as py

    # Create some data arrays
    x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 51)
    y = np.sin(x)

    # Make a plot
    mpl_fig = plt.figure()
    plt.plot(x, y, 'ko--')
    plt.title('sin(x) from -2*pi to 2*pi')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.show()

    # Export plot to plotly
    unique_url = py.plot_mpl(mpl_fig, filename="sin(x) test plot")

   We've basically see all of this stuff for making the plot with matplotlib, but now we're able to plot and save it directly to plotly by adding only 2 lines.
   If all has gone well, your plot should open on plotly's site after you run this example.

Interacting with and modifying your plot on plotly
--------------------------------------------------

So the point of getting your plots on plotly is that you can interact with your data and share your plots on the web.
For example, in our test plot you can easily zoom in/out or hover over the plotted points to see their values.
However, you can also edit your plots in plotly to change everything from the colors of the lines or points to the type of the plot.
To edit your plot, simply click on **Edit** above your plot on the right side, as shown below.

.. figure:: img/plotly-interact.png
   :width: 800px
   :align: center
   :alt: Interacting with plot.ly

There is a huge amount of editing that can be done for plotly plots.
For the purposes of class today, we'll simply refer you to the `plotly tutorials <http://help.plot.ly/tutorials/>`__ to learn how to edit plots.

.. attention::

   **Task 4: Editing a plotly plot**

   For this task, simply take the test plot generated above, make 3 changes to its format, and save the updated plot to plotly.