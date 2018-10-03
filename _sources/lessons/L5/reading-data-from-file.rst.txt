Reading data from a file
========================

The instructions here are for reading files in the traditional Python way.
**We do not recommend doing this**, as it is more challenging and often more difficult to understand.
That said, the info is here if you're curious.
We're assuming below that you have downloaded a copy of the Kumpula weather data file from the :doc:`Exploring data using Pandas lesson <pandas-basics>`.
If not, do that before proceeding.

Reading an entire file at once
------------------------------

There are several ways in which data can be read from a file in Python, but some are more common (or better in some cases) than others.
Here we will focus on a common way to read files that can be easily used for many types of data files.

1. We will begin by reading an entire file into a Python list.
   To start we need to open the file for reading by typing the following into the **Spyder** editor:

   .. code:: python

    with open('Kumpula-June-2016-w-metadata.txt', 'r') as infile:
        <commands to read file...>

   Here we are using the ``open()`` function in combination with the ``with`` statement in Python.
   I suppose an explanation is required.

   - The general format used for opening files in Python is ``open(<filename>, <mode>)``, where ``filename`` is the name of the file and ``mode`` is either ``"r"`` for reading a file or ``"w"`` for writing to a file.
     In our case, we open our file (``'Kumpula-June-2016-w-metadata.txt'``) to be read (``'r'``).
   - In addition, we are using the ``with`` statement.
     What this does is open our file and assign access to the file to a variable (``infile``).
     Thus, using the variable ``infile`` we can access the file contents anywhere within the indented block of code beneath the ``with`` statement.
     For instance, we will see how to read the file in the next point.
   - The main advantage of using the ``with`` statement is that normally you need to manually close file access in Python (using the ``file.close()`` method), but when using the ``with`` statement the file is automatically closed at the end of the indented block.
     This ensures you don't forget to close it yourself.
     Closing files is important because sometimes the final changes made to a file will not be written until the file is closed, for example.

2. With our file open, we can now proceed to read the file.

   .. code:: python

    #!/usr/bin/env python3
    '''Reads the contents of a file at once.

    Usage:
        ./readall.py

    Author:
        David Whipp - 2.10.2017
    '''

    # Read entire data file
    with open('Kumpula-June-2016-w-metadata.txt', 'r') as infile:
        data = infile.read()

   So what we have done here is to use the ``file.read()`` *method* to read in the entire file as one long character string.
   What does that mean?
   Well, this means that we now have a variable ``data`` that contains the entire contents of our data file (``Kumpula-June-2016-w-metadata.txt``).
   Thus, if we save the script above as ``readall.py`` and run it in **Spyder**, we should see the following output to the IPython console when we print out the contents of ``data``:

   .. ipython:: python
    :suppress:

        import os
        fp = os.path.join(os.path.abspath('data'), 'L5', "Kumpula-June-2016-w-metadata.txt")
        with open(fp, 'r') as infile:
            data = infile.read()
            dataList = data.splitlines()

        # Create empty lists to store file data
        date = []
        meanTemp = []
        maxTemp = []
        minTemp = []

        # Loop over lines in file, append to lists 
        headerLines = 8
        for line in range(len(dataList)):
            if line > headerLines:
                splitLine = dataList[line].split(',')
                date.append(splitLine[0])
                meanTemp.append(splitLine[1])
                maxTemp.append(splitLine[2])
                minTemp.append(splitLine[3])

   .. ipython:: python

    print(data)

   No surprises here, this looks like the contents of the ``Kumpula-June-2016-w-metadata.txt`` data file.
   If you want to confirm, you're welcome to open that file in the **Spyder** editor.
   Note that you may have to set **Files of type** to be "All files (\*)" in the **Open file** window to see the data files.

3. As mentioned, ``file.read()`` is a *method* for file objects that reads all data in as a single (potentially very long) character string.
   You can confirm this using the ``type()`` function.

   .. ipython:: python

    type(data)

   Obviously, it is nice to read the entire file at once, but this may be a problem for very large data files that may not fit in memory on the computer.

4. To convert our character string ``data`` into a more usable format in which each line is a separate value in a Python list, we can use the ``str.splitlines()`` method.
   Thus, we can create a list ``datalist`` that contains each line of the file as follows:

   .. code:: python

    #!/usr/bin/env python3
    '''Reads the contents of a file at once.

    Usage:
        ./readall.py

    Author:
        David Whipp - 2.10.2017
    '''

    # Read entire data file
    with open('Kumpula-June-2016-w-metadata.txt', 'r') as infile:
        data = infile.read()
        dataList = data.splitlines()

   Now each line of the data file will be a character string in the list ``dataList``.
   We can confirm this by running the example above and printing out the contents of dataLits, which should output the following to the IPython console:

   .. ipython:: python

    print(dataList)

   We are now ready to start interacting with our file data.

Dealing with headers of known length
------------------------------------

In many cases, the *header* in a data file will occupy the top few lines the file and we can simply skip over the header by not storing header data.
We currently have a Python list ``dataList`` that contains our data file contents.
A common task in Python is to separate the values on each line into separate Python lists that can be manipuated independently.
Below, we will create a set of 4 Python lists, one for each column in our data file, and fill them with the values from the lines of our file.

1. We will first need to create our empty lists for storing the data file values.
   We can do this by creating empty lists beneath the indented block for reading the file.

   .. code:: python

    #!/usr/bin/env python3
    '''Reads the contents of a file at once.

    Usage:
        ./readall.py

    Author:
        David Whipp - 2.10.2017
    '''

    # Read entire data file
    with open('Kumpula-June-2016-w-metadata.txt', 'r') as infile:
        data = infile.read()
        dataList = data.splitlines()

    # Create empty lists to store file data
    date = []
    meanTemp = []
    maxTemp = []
    minTemp = []

   **Note**: These empty lists are not indented as part of the file reading block.

2. With the empty lists created, we now need to go through each line of the file, separate the values on each line, and add them to the lists we've created.
   We can do this using the ``str.split()`` method and a ``for`` loop.
   Don't forget, we want to skip over the *header*.

   .. code:: python

    #!/usr/bin/env python3
    '''Reads the contents of a file at once.

    Usage:
        ./readall.py

    Author:
        David Whipp - 2.10.2017
    '''

    # Read entire data file
    with open('Kumpula-June-2016-w-metadata.txt', 'r') as infile:
        data = infile.read()
        dataList = data.splitlines()

    # Create empty lists to store file data
    date = []
    meanTemp = []
    maxTemp = []
    minTemp = []

    # Loop over lines in file, append to lists 
    headerLines = 8
    for line in range(len(dataList)):
        if line > headerLines:
            splitLine = dataList[line].split(',')
            date.append(splitLine[0])
            meanTemp.append(splitLine[1])
            maxTemp.append(splitLine[2])
            minTemp.append(splitLine[3])

   So, what happened?

   - First, we have used a ``for`` loop to go over each value in the list ``dataList``, assigning each line to the variable ``line`` in the loop.
   - Second, we have used an ``if`` statement to only deal with lines below the headers (index 9 and up).
   - Third, we have created a new variable ``splitline`` that is itself a Python list.
     In this case, ``line.split(',')`` separates all of the values in the line at each comma (``,``) and stores the split values in a list (``splitline``).
     You can see this list for the final line in the data file by typing ``print(splitline)`` in the IPython console.
   - Lastly, since each of the four values in each line of the data file have been separated, we can add the values to the lists we've created earlier using the ``list.append()`` method.
     In this case, we append the corresponding values in the list ``splitline`` by using their index values.
     This may seem complicated, but if you look at the code line by line, we're not really doing too many new things here.

Headers of a known number of lines - Alternative approach
---------------------------------------------------------

1. Let's start by editing the ``readall.py`` script we created above to read the other data file (``Kumpula-June-2016-w-metadata.txt``) and saving the modified file as ``headread.py``.

   .. code:: python 

    #!/usr/bin/env python3
    '''Reads the contents of a file at once.

    Usage:
        ./headread.py

    Author:
        David Whipp - 2.10.2017
    '''

    # Read entire data file
    with open('Kumpula-June-2016-w-metadata.txt', 'r') as infile:
        data = infile.read()
        dataList = data.splitlines()

    # Create empty lists to store file data
    date = []
    meanTemp = []
    maxTemp = []
    minTemp = []

    # Loop over lines in file, append to lists 
    for line in range(9,len(dataList)):
        splitLine = dataList[line].split(',')
        date.append(splitLine[0])
        meanTemp.append(splitLine[1])
        maxTemp.append(splitLine[2])
        minTemp.append(splitLine[3])

   - So this looks almost exactly the same as before, but we're starting the range at ``9``, rather and ``0``.
     This means we don't need to have the ``if`` statement to only append below the header.

More options
------------

If you'd like to see a few other options for reading files the Pythonic way, you can also check out the `materials from the 2016 version of this course <https://github.com/Python-for-geo-people/Lesson-5-Reading-Writing/blob/master/Lesson/reading-data-from-file.md>`__.