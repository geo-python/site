Exercise 7
==========

.. warning::

    Please note that **we provide assignment feedback only for students enrolled in the course at the University of Helsinki**.

.. admonition:: Start your assignment

    .. note::

        **Pandas**

        **You can start working on your copy of Exercise 7 (Pandas version) by** accepting the `GitHub Classroom assignment <https://classroom.github.com/a/nFG7H5VK>`__

        **Exercise 7 is due by 16:00 on 28.10**.

        You can also take a look at the open course copy of `Exercise 7 in the course GitHub repository <https://github.com/Geo-Python-2018/Exercise-7P>`__ (does not require logging in).
        Note that you should not try to make changes to this copy of the exercise, but rather only to the copy available via GitHub Classroom.

Hints for Exercise 7
--------------------

Labels and legends
------------------

In the plot for Problem 3 you're asked to include a line legend for each subplot.
To do this, you need to do two things:

1. You need to add a ``label`` value when you create the plot using the ``plt.plot()`` function.
   This is as easy as adding a parameter that say ``label='some text'`` when you call ``plt.plot()``.
2. You'll need to display the line legend, which can be done by calling ``plt.legend()`` for each subplot.

Saving multiple plots into a directory
--------------------------------------

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

Creating an animation from multiple images
------------------------------------------

In Problems 3 and 4 the aim was to plot multiple images on a predefined folder. An optional task
was to create an animation out of those figures. Animating the figures in Problems 3 and 4 is fairly
straightforward task to do in Python. All you need to do is to install a module called ``imageio`` and
run couple lines of code that I show below.

But, first you need to install ``imageio`` module.

Installing the module can be done by running following command **from the command prompt / terminal** with **admin rights**:

.. code:: bash

    $ conda install -c conda-forge imageio


.. note::

    If everything works fine you should not see any errors coming into the screen. If you receive an error, the most typical
    one is that you did not have **admin rights** when trying to install the module. In such case, you should open command prompt
    with admin rights (Command prompt --> right click --> Run as administrator..)

When you have imageio installed you should be able to import it, in Spyder:

.. ipython:: python

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

.. code:: python

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
