Writing your own Python scripts
===============================

As you may be noticing by now, it isn't that convenient to type in all of the commands you would like to use in the IPython console.
An alternative to typing in all of the commands you would like to run is the list them in a Python *script file*.
A Python script file is simple a file containing a list of the command you would like to run, with one command per line, and formatted in the same way as if you were to type them in.
Python script files traditionally use the ``.py`` file extension in their names.

The general concept of a ``.py`` script file
--------------------------------------------

A Python script file is simply a list of commands that you might otherwise type into the IPython console.
As such, we can quite easily create a basic script file and test things out.

1. You should already have the **Spyder** editor open, and in this part of the lesson we will be working with the IPython console panel you have been using, but also with the Spyder editor panel.

   .. figure:: img/Spyder-editor.png
    :width: 600px
    :align: center
    :alt: The Spyder editor

    The Spyder editor

   Start by copying and pasting the text below into your **Spyder** editor panel.

   .. code:: python

    stationName = 'Helsinki Kaivopuisto'
    stationLat = 60.15
    print("The", stationName, "station is located at", stationLat, "N")

2. Save this script file as ``stationinfo.py`` somewhere in your home directory, such as a directory called ``Geo-Python-Lesson-2``.
   This can be done by clicking on the disk icon in the toolbar at the top of the window.
   Enter the file name as ``stationinfo.py`` and click the ``Save`` button on the lower right of the window to save the file.

3. To run your script in **Spyder**, you simply click on the green play button in the toolbar above the editor panel.
   You may be prompted about some options related to running the script, and you can simply click on the **Run** button on the window that pops up.

   .. figure:: img/Spyder-play-button.png
    :width: 400px
    :align: center
    :alt: Running a script with Spyder

    Running a script in Spyder

   Running the script should produce the following output in the IPython console, exactly as if you had typed the commands into the console.

   .. code::

    The Helsinki Kaivopuisto station is located at 60.16 N

4. Now let's make a small change to the script.
   Edit the script so that it now reads

   .. code:: python

    stationName = 'Helsinki Kaivopuisto'
    stationLat = 60.15
    stationLong = 24.96
    print("The", stationName, "station is located at", stationLat, "N,", stationLong, "E")

   Save your changes.

5. Run the script again and you should see your changes.

   .. code::

    The Helsinki Kaivopuisto station is located at 60.16 N, 24.96 E

Writing our scripts the "right" way
-----------------------------------

The script above works, but one of the big advantages of using scripts is including features that make the code easier to read and understand.
These include *comments* in the code, which explain what the code does, but are not executed when the code is run.
As your programs get longer and more complicated, features such as comments will become essential.
Below are some suggestions to make sure your code is formatted nicely and easy to understand.

Inline comments
~~~~~~~~~~~~~~~

*Inline comments* are comments within the code that explain what certain lines of the code do.
To your, it may seem obvious how the code works, but if you share it with another person perhaps they will not feel the same way.
It is a very good idea to make the code as easy to read as possible for people.

.. code:: python

    # Finnish Meterological Institute observation station name and location data
    # Station name for the station in Kaivopuisto, Helsinki, Finland
    stationName = 'Helsinki Kaivopuisto'
    # Station latitude and longitude - Latitude is north, longitude is east
    stationLat = 60.15
    stationLong = 24.96
    # Print station name and location to the screen
    print("The", stationName, "station is located at", stationLat, "N,", stationLong, "E")

Here, we have provided a a bit more information about the data in this script by adding *inline comments*.
Inline comments begin with a ``#`` (number sign or hash), and all characters that follow on that line will be ignored by Python.
Adding comments to scripts is essential for scientists like ourselves to both help us remember how a script works and to make it easier to share with colleagues.
It is best to get into the habit of adding comments as you write.

Use line breaks wisely
~~~~~~~~~~~~~~~~~~~~~~

*Line breaks*, or blank lines, in your scripts can greatly improve readability, and help divide different sections of the script.
Perhaps it is obvious, but Python will ignore blank lines in a script.

.. code:: python

    # Finnish Meterological Institute observation station name and location data

    # Station name for the station in Kaivopuisto, Helsinki, Finland
    stationName = 'Helsinki Kaivopuisto'

    # Station latitude and longitude - Latitude is north, longitude is east
    stationLat = 60.15
    stationLong = 24.96

    # Print station name and location to the screen
    print("The", stationName, "station is located at", stationLat, "N,", stationLong, "E")

Use a docstring
~~~~~~~~~~~~~~~

A *docstring* is a form of *block comment* at the start of your program that clearly states its purpose and how to run the program.
A *block comment* is similar to the inline comments above, but starts with ``'''`` and comments out all code between the start and another closing set of ``'''``.
You can also include your name, and possibly add licensing information in the docstring.

.. code:: python

    '''Prints information about an FMI observation station to the screen.

    Usage:
        ./stationinfo.py

    Author:
        David Whipp - 10.9.2017
    '''

    # Finnish Meterological Institute observation station name and location data

    # Station name for the station in Kaivopuisto, Helsinki, Finland
    stationName = 'Helsinki Kaivopuisto'

    # Station latitude and longitude - Latitude is north, longitude is east
    stationLat = 60.15
    stationLong = 24.96

    # Print station name and location to the screen
    print("The", stationName, "station is located at", stationLat, "N,", stationLong, "E")

   In this example the script is simple, but many Python programs have optional values that can be used by the code when it is run, making the usage statement crucial.

Advanced topics
---------------

Adding a license
~~~~~~~~~~~~~~~~

Depending on what you aim to do with your script, you may want to include a formal software license in the docstring to state the conditions under which the code can be used or modified.
There are many helpful web resources to `teach you about software licenses <https://tldrlegal.com/>`__ and `how to choose a license <http://choosealicense.com/>`__.
In most cases my preference is the `MIT License <https://opensource.org/licenses/MIT>`__, which is simple and allows software use by anyone.
An example is below.

.. code:: python

    '''Prints information about an FMI observation station to the screen.

    Usage:
        ./stationinfo.py

    License:
        MIT License

        Copyright (c) 2017 David Whipp

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
    '''

    # Finnish Meterological Institute observation station name and location data

    # Station name for the station in Kaivopuisto, Helsinki, Finland
    stationName = 'Helsinki Kaivopuisto'

    # Station latitude and longitude - Latitude is north, longitude is east
    stationLat = 60.15
    stationLong = 24.96

    # Print station name and location to the screen
    print("The", stationName, "station is located at", stationLat, "N,", stationLong, "E")

In this case I have taken the license information directly from an `online software license template <http://choosealicense.com/licenses/mit/>`__.
Software licensing is an important consideration when posting your software in online repositories such as GitHub.
It is one way to protect your intellectual property from being used in ways you do not wish.

Starting with a shebang
~~~~~~~~~~~~~~~~~~~~~~~

Starting with a *shebang* is another thing to consider doing with your scripts.
Why?
Well, without going into too much detail, it makes it easier for users to run your script directly from a terminal, rather than needing to use **Spyder** or open an IPython console first.
If this doesn't make a great deal of sense, you can get a bit more information on `Wikipedia <https://en.wikipedia.org/wiki/Shebang_(Unix)>`__.

Starting with a shebang means that the first line of your program starts with the characters ``#!`` followed by the location of a program that will run the Python software installed on the computer.
An example is below.

.. code:: python

    #!/usr/bin/env python3
    '''Prints information about an FMI observation station to the screen.

    Usage:
        ./stationinfo.py

    Author:
        David Whipp - 10.9.2017
    '''

    # Finnish Meterological Institute observation station name and location data

    # Station name for the station in Kaivopuisto, Helsinki, Finland
    stationName = 'Helsinki Kaivopuisto'

    # Station latitude and longitude - Latitude is north, longitude is east
    stationLat = 60.15
    stationLong = 24.96

    # Print station name and location to the screen
    print("The", stationName, "station is located at", stationLat, "N,", stationLong, "E")

We'll leave it at that for now, but if you have questions let us know.

Page summary
------------

As we continue in the course we will be creating more advanced Python scripts that include more complex code logic and other features we've not yet learned.
With these, we'll also learn a few tips for incorporating them in our scripts.
However, an expectation in this course is that you stick to the general template described above when writing your code, which means including appropriate use of inline comments, blank lines, and a docstring.