Exercise 7
==========

.. note::

    Exercise 7 is due by **17:00 on Friday, October 23rd**.

.. admonition:: Start your assignment

    **You can start working on your copy of Exercise 7 by** accepting the `GitHub Classroom assignment <https://classroom.github.com/a/OsC2NOCU>`__

You can also take a look at the template repository for `Exercise 7 on GitHub <https://github.com/Geo-Python-2020/Exercise-7>`__ (does not require logging in).
Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

.. admonition:: Pair programming (optional!)

    Students attending the course in Helsinki, **if you wish, you can continue working in pairs**.
    See more information in Slack, and in week 2: `Why are we working in pairs? <https://geo-python-site.readthedocs.io/en/latest/lessons/L2/why-pairs.html>`_.
    Those students who want to submit their own solutions, please contact the course assistant that is grading your assignments (see list in Slack).

Cloud computing environments
-----------------------------

.. image:: https://img.shields.io/badge/launch-binder-red.svg
   :target: https://mybinder.org/v2/gh/Geo-Python-2020/Binder/master?urlpath=lab

.. image:: https://img.shields.io/badge/launch-CSC%20notebook-blue.svg
   :target: https://notebooks.csc.fi/#/blueprint/7e62ac3bddf74483b7ac7333721630e2

Hints for Exercise 7
--------------------

Labels and legends
~~~~~~~~~~~~~~~~~~

In the plot for Problem 3 you're asked to include a line legend for each subplot.
To do this, you need to do two things:

1. You need to add a ``label`` value when you create the plot using the ``plt.plot()`` function.
   This is as easy as adding a parameter that say ``label='some text'`` when you call ``plt.plot()``.
2. You'll need to display the line legend, which can be done by calling ``plt.legend()`` for each subplot.

Using ``enumerate()``
~~~~~~~~~~~~~~~~~~~~~

In case the ``enumerate()`` function is causing you some confusion, here is a simple example.
The general idea is that ``enumerate()`` will return both the value in a list and its index when you use it.
Let's see if this helps...

.. ipython:: python

    animals=['dog', 'cat', 'frog']
    for index, animal in enumerate(animals):
        print(animal, 'is in location', index)

Saving multiple plots into a directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Problems 3 and 4 the aim is to create 65 individual plots, and save those into your computer.
In these kind of situations, the smartest thing to do is to use a ``for`` loop and at the end of each
loop, save the image into a folder that you have specified. There are some useful tricks related to saving
files and generating good file names automatically.

A good approach when saving multiple files into a folder, is to define a separate variable where you store
only the directory path. Then during every loop you combine this directory path, and the file name together.
This can be done by using a function ``os.path.join()`` which is part of ``os`` built-in Python module.

Consider following example:

.. ipython:: python

    import os
    myfolder = r"C:\MyUserName\Temp_visualizations"
    for i in range(5):
        filename = "My_File_" + str(i) + ".png"
        filepath = os.path.join(myfolder, filename)
        print(filepath)

Here, we created a folder path and a unique filename, and in the end parsed a full filepath that could be
used to save a plot into that location on your computer.

Settings for multiple subplots:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are different ways of manipulating matplotlib subplots.
Here is one trick for modifying multiple subplot properties (of `axes`) at once:

.. code-block:: python

    # Set axis labels for all subplots
    for ax in axes.flat:
        ax.set(xlabel='xxx', ylabel='xxx')

    # Set ylim for all subplots
    for ax in axes.flat:
        ax.set_ylim(0, 10)

Preventing plot display
~~~~~~~~~~~~~~~~~~~~~~~

When creating the series of images needed for the animation in Problem 5, you may be stuck with many plots being displayed in JupyterLab.
You can suppress the display of plots by calling ``plt.close()`` after the ``plt.savefig(...)`` command.
In other words, you can do

.. code-block:: python

    ...
    plt.savefig(...)
    plt.close()
    ...

which will close the plot before it would normally be displayed.

Creating an animation from multiple images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Problems 3 and 4 the aim was to plot multiple images on a predefined folder. An optional task
was to create an animation out of those figures. Animating the figures in Problems 3 and 4 is fairly
straightforward task to do in Python. All you need to do is to install a module called ``imageio`` and
run couple lines of code that I show below.

But, first you need to install ``imageio`` module.

Installing the module can be done by running following command **from the command prompt / terminal** with **admin rights**:

.. code-block:: bash

    $ conda install -c conda-forge imageio


.. note::

    If everything works fine you should not see any errors coming into the screen. If you receive an error, the most typical
    one is that you did not have **admin rights** when trying to install the module. In such case, you should open command prompt
    with admin rights (Command prompt --> right click --> Run as administrator..)

When you have imageio installed you should be able to import it, in Spyder:

.. code-block:: python

    import imageio

Creating the animation
~~~~~~~~~~~~~~~~~~~~~~

Following commands should produce a nice gif-animation out of your plots. The idea is that you list all the
files from the folder where you saved the plots using ``glob`` function, and then pass that file list into imageio
function called ``imageio.mimsave()``. A following example shows how to do that.

First we list all the files from folder that has ``.png`` file format using ``glob``. The ``*`` wildcard character tells to computer that
the name of the file can be anything (the purpose of the star). ``.png`` after the star tells that the filename should end with ``.png`` characters.
If there are some other files with other file format than .png, they will be excluded.
Finally, we create the animation into the computer.

.. code-block:: python

    import glob
    import imageio

    # Find all files from given folder that has .png file-format
    search_criteria = r"C:\MyUserName\Temp_visualizations\*.png"

    # Execute the glob function that returns a list of filepaths
    figure_paths = glob.glob(search_criteria)

    # Save the animation to disk with 48 ms durations
    output_gif_path = r"C:\MyUserName\Temp_animation.gif"
    imageio.mimsave(output_gif_path, [imageio.imread(fp) for fp in figure_paths], duration=0.48, subrectangles=True)

With these lines of code you should be able to create a nice animation out of your plots!
