Reading data from a file
========================

Our first task in this week's lesson is to learn how to read data from
files. In Python this comprises two tasks: (1) Opening the file to be
able to read in the contents, and (2) reading in the contents of the
file. In terms of how the data is read in Python, there are many and we
will focus on one simple form. Later in the course you will be
introduced to more sophisticated libraries that can help with reading
data files, but for now we will focus on the traditional way in which
data files can be read in Python.

The data used in this part of the exercise is from the `Smithsonian
Institution's volcano database <http://volcano.si.edu/>`__.

Topics
------

1. `Downloading and extracting the
   data <#downloading-and-extracting-the-data>`__
2. `Preparing to read the data files in
   **Spyder** <#preparing-to-read-the-data-files-in-spyder>`__
3. `Reading an entire file at once <#reading-an-entire-file-at-once>`__
4. `Interacting with our file data <#interacting-with-our-file-data>`__
5. `Skipping file headers and other unwanted
   data <#skipping-file-headers-and-other-unwanted-data>`__
6. `Pro tips <#pro-tips>`__

Downloading and extracting the data
-----------------------------------

1. You can start by downloading the `volcano data zip
   file <https://github.com/Python-for-geo-people/Lesson-5-Reading-Writing/raw/master/Data/volcano-data.zip>`__
   we will be using for this part of the lesson.

-  The Firefox browser will likely download the file to the
   ``Downloads`` directory in the home directory of your computer
   instance. If so, you should move the file into the home directory
   using the file browser.

2. Once you have moved the ``volcano-data.zip`` file into your home
   directory, you can unzip the file using the ``unzip`` command in the
   Terminal window.

   .. code:: bash

       $ cd $HOME
       $ unzip volcano-data.zip
       $ ls volcano-data
       GVP-Volcano-Lat-Lon-Elev.csv GVP-Volcano-List.csv

   You should now have a directory titled ``volcano-data`` in your home
   directory. It contains two files based on `version 4.5.1 of the
   Smithsonian Institution's Holocene volcano database (updated
   23.9.2016) <http://volcano.si.edu/list_volcano_holocene.cfm>`__:

-  ``GVP-Volcano-List.csv``: The first 100 lines of the Holocene volcano
   database file in ``.csv`` format and with header lines. **Note**:
   Values are separated by semicolons (``;``) in this version of the
   file rather than commas (``,``).
-  ``GVP-Volcano-Lat-Lon-Elev.csv``: The volcano ID, latitude, longitude
   and elevation for the first 10 volcanoes in the Holocene volcano
   database. There are no headers in this file and values are separated
   by commas (``,``).

Preparing to read the data files in **Spyder**
----------------------------------------------

1. Let's start by opening **Spyder** by either double clicking on its
   icon on the Desktop or typing ``spyder`` in the Terminal window.
2. In order to use the data in the downloaded files, we need to change
   the working directory in **Spyder** to be the ``volcano-data``
   directory in your home directory. This can be done by clicking on the
   **File explorer** tab in the upper right pane of the **Spyder**
   window and navigating to the ``volcano-data`` directory.
3. After navigating to that directory, you should see the two data
   files. However, you also need to tell the IPython window in
   **Spyder** that the ``volcano-data`` directory is where we will be
   working. This can be done by clicking on the button shown below to
   set the console's working directory to the one selected in the **File
   explorer**.

   |Setting the Spyder directory|\  *Setting the working directory for
   IPython in Spyder*.

We should now be ready to continue and start working with our data
files.

Reading an entire file at once
------------------------------

There are several ways in which data can be read from a file in Python,
but some are more common (or better in some cases) than others. We will
focus on two ways to read files that can be easily used for many types
of data files.

1. We will begin by reading an entire file into a Python list. To start
   we need to open the file for reading by typing the following into the
   **Spyder** editor:

   .. code:: python

       with open("GVP-Volcano-Lat-Lon-Elev.csv", "r") as infile:
           <commands to read file...>

   Here we are using the ``open()`` function in combination with the
   ``with`` statement in Python. I suppose an explanation is required.

-  The general format used for opening files in Python is
   ``open(<filename>, <mode>)``, where ``filename`` is the name of the
   file and ``mode`` is either ``"r"`` for reading a file or ``"w"`` for
   writing to a file. In our case, we open our file
   (``"GVP-Volcano-Lat-Lon-Elev.csv"``) to be read (``"r"``).
-  In addition, we are using the ``with`` statement. What this does is
   open our file and assign access to the file to a variable
   (``infile``). Thus, using the variable ``infile`` we can access the
   file contents anywhere within the indented block of code beneath the
   ``with`` statement. For instance, we will see how to read the file in
   the next point.
-  The main advantage of using the ``with`` statement is that normally
   you need to manually close file access in Python (using the
   ``file.close()`` method), but when using the ``with`` statement the
   file is automatically closed at the end of the indented block. This
   ensures you don't forget to close it yourself. Closing files is
   important because sometimes the final changes made to a file will not
   be written until the file is closed, for example.

2. With our file open, we can now proceed to read the file.

   .. code:: python

       """
       readall.py

       A simple script for reading the entire contents of a file.

       dwhipp - 2.10.2016
       """

       # Read entire data file
       with open("GVP-Volcano-Lat-Lon-Elev.csv", "r") as infile:
           data = infile.read()
           print(data)

   So what we have done here is to use the ``file.read()`` *method* to
   read in the entire file as one long character string. What does that
   mean? Well, this means that we now have a variable ``data`` that
   contains the entire contents of our data file
   (``GVP-Volcano-Lat-Lon-Elev.csv``). Thus, if we save the script above
   as ``readall.py`` and run it in **Spyder**, we should see the
   following output to the IPython window:

   .. code:: python

       210010,50.17,6.85,600
       210020,45.775,2.97,1464
       210030,42.17,2.53,893
       210040,38.87,-4.02,1117
       211001,43.25,10.87,500
       211003,42.6,11.93,800
       211004,41.73,12.7,949
       211010,40.827,14.139,458
       211020,40.821,14.426,1281
       211030,40.73,13.897,789

   No surprises here, this looks like the contents of the
   ``GVP-Volcano-Lat-Lon-Elev.csv`` data file. If you want to confirm,
   you're welcome to open that file in the **Spyder** editor. Note that
   you may have to set **Files of type** to be "All files (\*)" in the
   **Open file** window to see the data files.
3. As mentioned, ``file.read()`` is a *method* for file objects that
   reads all data in as a single (potentially very long) character
   string. You can confirm this using the ``type()`` function.

   .. code:: python

       >>> type(data)
       str

   Obviously, it is nice to read the entire file at once, but this may
   be a problem for very large data files that may not fit in memory on
   the computer.
4. To convert our character string ``data`` into a more usable format in
   which each line is a separate value in a Python list, we can use the
   ``str.splitlines()`` method. Thus, we can create a list ``datalist``
   that contains each line of the file as follows:

   .. code:: python

       """
       readall.py

       A simple script for reading the entire contents of a file.

       dwhipp - 2.10.2016
       """

       # Read entire data file, separate lines in a list
       with open("GVP-Volcano-Lat-Lon-Elev.csv", "r") as infile:
           data = infile.read()
           datalist = data.splitlines()
           print(datalist)

   Now each line of the data file will be a character string in the list
   ``datalist``. We can confirm this by running the example above, which
   should output the following to the IPython console:

   .. code:: python

       ['210010,50.17,6.85,600', '210020,45.775,2.97,1464', '210030,42.17,2.53,893', '210040,38.87,-4.02,1117', '211001,43.25,10.87,500', '211003,42.6,11.93,800', '211004,41.73,12.7,949', '211010,40.827,14.139,458', '211020,40.821,14.426,1281', '211030,40.73,13.897,789']

   We are now ready to start interacting with our file data.

Interacting with our file data
------------------------------

We currently have a Python list ``datalist`` that contains our data file
contents. A common task in Python is to separate the values on each line
into separate Python lists that can be manipuated independently. Below,
we will create a set of 4 Python lists, one for each column in our data
file, and fill them with the values from the 10 lines of our file.

1. We will first need to create our empty lists for storing the data
   file values. We can do this by creating empty lists beneath the
   indented block for reading the file.

   .. code:: python

       """
       readall.py

       A simple script for reading the entire contents of a file.

       dwhipp - 2.10.2016
       """

       # Read entire data file, separate lines in a list
       with open("GVP-Volcano-Lat-Lon-Elev.csv", "r") as infile:
           data = infile.read()
           datalist = data.splitlines()

       # Create empty lists to store file data
       VolcanoID = []
       Latitude = []
       Longitude = []
       Elevation = []

   **Note**: These empty lists are not indented as part of the file
   reading block.
2. With the empty lists created, we now need to go through each line of
   the file, separate the values on each line, and add them to the lists
   we've created. We can do this using the ``str.split()`` method and a
   ``for`` loop.

   .. code:: python

       """
       readall.py

       A simple script for reading the entire contents of a file.

       dwhipp - 2.10.2016
       """

       # Read entire data file, separate lines in a list
       with open("GVP-Volcano-Lat-Lon-Elev.csv", "r") as infile:
           data = infile.read()
           datalist = data.splitlines()

       # Create empty lists to store file data
       VolcanoID = []
       Latitude = []
       Longitude = []
       Elevation = []

       # Loop over lines in file, append to lists 
       for line in datalist:
           splitline = line.split(",")
           VolcanoID.append(splitline[0])
           Latitude.append(splitline[1])
           Longitude.append(splitline[2])
           Elevation.append(splitline[3])

   So, what happened?

-  First, we have used a ``for`` loop to go over each value in the list
   ``datalist``, assigning each line to the variable ``line`` in the
   loop.
-  Second, we have created a new variable ``splitline`` that is itself a
   Python list. In this case, ``line.split(",")`` separates all of the
   values in the line at each comma (``,``) and stores the split values
   in a list (``splitline``). You can see this list for the final line
   in the data file by typing ``print(splitline)`` in the IPython
   console.
-  Lastly, since each of the four values in each line of the data file
   have been separated, we can add the values to the lists we've created
   earlier using the ``list.append()`` method. In this case, we append
   the corresponding values in the list ``splitline`` by using their
   index values. This may seem complicated, but if you look at the code
   line by line, we're not really doing too many new things here.

Skipping file headers and other unwanted data
---------------------------------------------

In our example above, we had a data file with 10 lines, and each line
had 4 values separated by commas. It is more typical to deal with data
files that include *headers*, which describe the data in the file but
are not necessarily data that might be manipulated in a Python script.
Often we simply want to ignore these lines when creating variable lists
with data to manipulate. How headers are handled generally falls into
two categories.

Headers of a known number of lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In many cases, the header in a data file will occupy the top few lines
of a data file and we can simply skip over the header by not storing
header data in the lists used for other file data. We can see and
example of how to do this by using the other data file for this part of
the lesson (``GVP-Volcano-List.csv``).

1. Let's start by editing the ``readall.py`` script we created above to
   read the other data file (``GVP-Volcano-List.csv``) and saving the
   modified file as ``headread.py``.

   .. code:: python

       """
       headread.py

       A simple script for reading the entire contents of a file and skipping the header.

       dwhipp - 2.10.2016
       """

       # Read entire data file, separate lines in a list
       with open("GVP-Volcano-List.csv", "r") as infile:
           data = infile.read()
           datalist = data.splitlines()

       # Create empty lists to store file data
       VolcanoID = []
       Latitude = []
       Longitude = []
       Elevation = []

       # Loop over lines in file, append to lists 
       for line in datalist:
           splitline = line.split(";")
           VolcanoID.append(splitline[0])
           Latitude.append(splitline[8])
           Longitude.append(splitline[9])
           Elevation.append(splitline[10])

   So this looks a bit different than our earlier script. We've made
   three significant changes to this point:

-  The script now opens the data file ``GVP-Volcano-List.csv``, which
   contains the first 100 lines of `version 4.5.1 of the Smithsonian
   Institution's Holocene volcano database (updated
   23.9.2016) <http://volcano.si.edu/list_volcano_holocene.cfm>`__.
-  Lines are split using the semicolon (``;``), rather than comma
   (``,``) since the semicolon is used in this data file.
-  The index values of ``splitline`` have been changed to reflect the
   fact that the latitude, longitude, and elevation data are in
   different locations in this data file.

2. At this point, we know the first two lines of the data file are the
   header, and these lines should be skipped when filling the lists of
   the VolcanoID, etc. We can skip over the header lines by changing the
   ``for`` loop used to split each line in the file as follows:

   .. code:: python

       """
       headread.py

       A simple script for reading the entire contents of a file and skipping the header.

       dwhipp - 2.10.2016
       """

       # Read entire data file, separate lines in a list
       with open("GVP-Volcano-List.csv", "r") as infile:
           data = infile.read()
           datalist = data.splitlines()

       # Create empty lists to store file data
       VolcanoID = []
       Latitude = []
       Longitude = []
       Elevation = []

       # Loop over lines in file, append to lists, skip first 2 lines of file
       for i in range(2,len(datalist)):
           line = datalist[i]
           splitline = line.split(";")
           VolcanoID.append(splitline[0])
           Latitude.append(splitline[8])
           Longitude.append(splitline[9])
           Elevation.append(splitline[10])

   Here we have made two key changes.

-  First, instead of having a ``for`` loop that loops over each line in
   ``datalist``, we not use the ``range()`` function to start at line 3
   (index 2) and split lines in the file from there to the end of the
   file, the index value corresponding to the length of the ``datalist``
   list.
-  Second, since we are now using the index variable ``i`` in the
   ``for`` loop, we need to explicitly define the variable ``line`` for
   each iteration in the loop. In this case, we simply set ``line`` to
   be equal to the value at index ``i`` in the ``datalist`` list.

Headers beginning with a certain character
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another common form of file header is one that starts with a specific
character, such as ``#``. In this case we don't need to know the number
of lines occupied by the header, but simply to ignore any line starting
with ``#``, for example.

1. We can start by taking a copy of the first example of the
   ``headread.py`` script above and saving it as ``charheadread.py``.

   .. code:: python

       """
       charheadread.py

       A simple script for reading the entire contents of a file and skipping a header starting with
       a specific character.

       dwhipp - 2.10.2016
       """

       # Define starting character for headers/comments
       headchar = "#"

       # Read entire data file, separate lines in a list
       with open("GVP-Volcano-List.csv", "r") as infile:
           data = infile.read()
           datalist = data.splitlines()

       # Create empty lists to store file data
       VolcanoID = []
       Latitude = []
       Longitude = []
       Elevation = []

       # Loop over lines in file, append to lists 
       for line in datalist:
           splitline = line.split(";")
           VolcanoID.append(splitline[0])
           Latitude.append(splitline[8])
           Longitude.append(splitline[9])
           Elevation.append(splitline[10])

   Here all we have done is change the documentation string at the top
   of the script and define the character ``headchar`` that should be
   used to identify the start of a header (or comment) line in the data
   file.
2. Now we can modify the script within the ``for`` loop for processing
   the lines of the file to ignore any line starting with ``headchar``.

   .. code:: python

       """
       charheadread.py

       A simple script for reading the entire contents of a file and skipping a header starting with
       a specific character.

       dwhipp - 2.10.2016
       """

       # Define starting character for headers/comments
       headchar = "#"

       # Read entire data file, separate lines in a list
       with open("GVP-Volcano-List.csv", "r") as infile:
           data = infile.read()
           datalist = data.splitlines()

       # Create empty lists to store file data
       VolcanoID = []
       Latitude = []
       Longitude = []
       Elevation = []

       # Loop over lines in file, append to lists 
       for line in datalist:
           # Append data only for lines that do not start with headchar
           if line[0] != headchar:
               splitline = line.split(";")
               VolcanoID.append(splitline[0])
               Latitude.append(splitline[8])
               Longitude.append(splitline[9])
               Elevation.append(splitline[10])

   The change in this case is simple. We have added an ``if`` statement
   to test if the first character of a given line is not equal to
   ``headchar``. If that condition is met, the line will be processed
   normally. In this way, we will simply ignore lines starting with
   ``headchar``.

Pro tips
--------

Spliting lines separated by other characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reading an entire file line-by-line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example we've seen above will work nicely for small files, but often
it is easier to read file data line-by-line and not require storing the
entire file in memory. This is particularly beneficial in cases where
you extract only a small amount of the data in a file. Here we'll
explore reading data from a file line by line.

We can start by using a similar template to that used earlier for
opening a file, but rather than using the ``file.read()`` method to read
the entire file, we will use a ``for`` loop to go over each line in the
file.

.. code:: python

    """
    readlines.py

    A simple script for reading the contents of a file line by line in Python.

    dwhipp - 2.10.2016
    """

    # Read entire data file, separate lines in a list
    with open("GVP-Volcano-Lat-Lon-Elev.csv", "r") as infile:
        datalist = []
        for line in infile:
            datalist.append(line)

Here we start by adding a new empty list ``datalist`` to which we will
append each line of the file that is read. The ``for`` loop that follows
will read each line in the file ``infile`` and allow us to manipulate
them one by one. In this way we could, for example, split each line as
it is read and store only some part of each line in the list
``datalist``. Depending on the size of data you encounter, this may be
the only way to handle your datasets.

**Next**: `Reading multiple data files <reading-multiple-files.md>`__\ 
**Home**: `Lesson 5 main
page <https://github.com/Python-for-geo-people/Lesson-5-Reading-Writing>`__\ 
**Previous**: `Summary of early course feedback <midterm-feedback.md>`__

.. |Setting the Spyder directory| image:: ../img/Spyder-directory.png

