Basic elements of Python (part I)
=================================

In this lesson we will revisit data types, learn how data can be stored in Python lists, and about the concept of objects in programming.
If you have not already started **Spyder** you should do so now.
You can find :doc:`directions on how to open Spyder at the start of Lesson 1<../L1/A-taste-of-Python>`.

Sources
-------

Like the previous lesson, this lesson is inspired by the `Programming with Python lessons <https://swcarpentry.github.io/python-novice-inflammation/>`__ from the `Software Carpentry organization <http://software-carpentry.org/>`__.

Data types revisited
--------------------

1. We saw a bit about variables and their values in the lesson last week, and we continue today with some variables related to `FMI observation stations in Finland <http://en.ilmatieteenlaitos.fi/observation-stations>`__.
   For each station, a number of pieces of information are given, including the name of the station, an FMISID, its latitude, its longitude, and the station type.
   We can store this information and some additional information for a given station in Python as follows:

   .. ipython:: python

    stationName = 'Helsinki Kaisaniemi'
    stationID = 100971
    stationLat = 60.18
    stationLong = 24.94
    stationType = 'Weather stations'

   Here we have 5 values assigned to variables related to a single observation station.
   Each variable has a unique name and they can store different types of data.

2. We can explore the different types of data stored in variables using the ``type()`` function.

   .. ipython:: python

    type(stationName)
    type(stationID)
    type(stationLat)

   As expected, we see that the ``stationName`` is a character string, the ``stationID`` is an integer, and the ``stationLat`` is a floating point number.

   .. note::
    Remember, the data types are important because some are not compatible with one another.

   .. ipython:: python

    stationName + stationID

   Here we get a ``TypeError`` because Python does not know how we are expected to combine a string of characters (``stationName``) with an integer value (``stationID``).

3. It is not the case that things like the the ``stationName`` and ``stationID`` cannot be combined at all, but in order to combine a character string with a number we need to perform a data *type conversion*.
   For example, we can could convert the ``stationID`` into a character string using the ``str()`` function.

   .. ipython:: python

    stationIDStr = str(stationID)
    type(stationIDStr)
    print(stationIDStr)

   As you can see, ``str()`` converts a numerical value into a character string with the same numbers as before.

   .. note::
    Similar to using ``str()`` to convert numbers to character strings, ``int()`` can be used to convert strings or floating point numbers to integers and ``float()`` can be used to convert strings or integers to floating point numbers.

   .. attention::
    **Poll pause - Questions 2.1, 2.2**

    Please visit the `class polling page <https://geo-python.github.io/poll>`__ to participate (*those present in lecture only*).

4. Although most mathematical operations operate on numerical values, a common way to combine character strings is using the addition operator ``+``.

   .. ipython:: python

    stationNameAndID = stationName + ": " + str(stationID)
    print(stationNameAndID)

   Note that here we are converting ``stationID`` to a character string using the ``str()`` function within the assignment to the variable ``stationNameAndID``.
   Alternatively, we could have simply added ``stationName`` and ``stationIDStr``.

Lists and indices
-----------------

As we've seen above, my recent field excursion involved collecting (at
least) 48 rock samples. Rather than having individual variables for each
of those samples, we can store many related values in a *collection*.
The simplest type of *collection* in Python is a **list**.

1. Let's first create a list of selected ``SampleID`` values.

   .. code:: python

       >>> SampleIDs = ['DW-NP-03-16', 'DW-NP-12-16', 'DW-NP-33-16', 'DW-NP-48-16']
       >>> print(SampleIDs)
       ['DW-NP-03-16', 'DW-NP-12-16', 'DW-NP-33-16', 'DW-NP-48-16']
       >>> type(SampleIDs)
       list

   Here we have a list of 4 ``SampleID`` values in a list called
   ``SampleIDs``. As you can see, the ``type()`` function recognizes
   this as a list. Lists can be created using the square brackets (``[``
   and ``]``), with commas separating the values in the list.
2. To access an individual value in the list we need to use an **index
   value**. An **index value** is a number that refers to a given
   position in the list. Let's check out the first value in our list as
   an example:

   .. code:: python

       >>> print(SampleIDs[1])
       'DW-NP-12-16'

   Wait, what? This is the second value in the list we've created, what
   is wrong? As it turns out, Python (and many other programming
   languages) start values stored in collections with the index value 0.
   Thus, to get the value for the first item in the list, we must use
   index 0.

   .. code:: python

       >>> print(SampleIDs[0])
       'DW-NP-03-16'

   OK, that makes sense now, but it may take some getting used to...
3. We can find the length of a list using the ``len()`` function.

   .. code:: python

       >>> len(SampleIDs)
       4

   Just as expected, there are 4 values in our list and
   ``len(SampleIDs)`` returns a value of 4.
4. If we know the length of the list, we can now use it to find the
   value of the last item in the list, right?

   .. code:: python

       >>> print(SampleIDs[4])
       ---------------------------------------------------------------------------
       IndexError                                Traceback (most recent call last)
       <ipython-input-34-946b174fe444> in <module>()
       ----> 1 print(SampleIDs[4])

       IndexError: list index out of range

   What, an ``IndexError``? That's right, since our list starts with
   index 0 and has 4 values, the index of the last item in the list is
   ``len(SampleIDs) - 1``. That isn't ideal, but fortunately there's a
   nice trick in Python to find the last item in a list.

   .. code:: python

       >>> print(SampleIDs)
       ['DW-NP-03-16', 'DW-NP-12-16', 'DW-NP-33-16', 'DW-NP-48-16']
       >>> print(SampleIDs[-1])
       'DW-NP-48-16'
       >>> print(SampleIDs[-4])
       'DW-NP-03-16'

   Yes, in Python you can go backwards through lists by using negative
   index values. Index -1 gives the last value in the list and index
   ``-len(SampleIDs)`` would give the first. Of course, you still need
   to keep the index values within their ranges.

   .. code:: python

       >>> print(SampleIDs[-5])
       ---------------------------------------------------------------------------
       IndexError                                Traceback (most recent call last)
       <ipython-input-38-ac2327014588> in <module>()
       ----> 1 print(SampleIDs[-5])

       IndexError: list index out of range

5. Another nice feature of lists is that they are *mutable*, meaning
   that the values in a list that has been defined can be modified.
   Consider a list of the rock types corresponding to the sample IDs in
   the ``SampleIDs`` list.

   .. code:: python

       >>> SampleRockTypes = ['Augen gneiss', 'Leucogranite', 'Quartzite', 'Mica schst']
       >>> print(SampleRockTypes)
       ['Augen gneiss', 'Leucogranite', 'Quartzite', 'Mica schst']

   Now as we saw before, the rock types for sample DW-NP-48-16 should be
   'Mica schist', not 'Mica schst'. Fortunately, this is an easy fix. We
   simply replace the value at the corresponding location in the list
   with the correct definition.

   .. code:: python

       >>> SampleRockTypes[3] = 'Mica schist'
       >>> print(SampleRockTypes)
       ['Augen gneiss', 'Leucogranite', 'Quartzite', 'Mica schist']

6. Lists also do not need to have only one type of data. Let's consider
   that in addition to having a list of each sample ID, sample number,
   rock type, etc. we would like to have a list of all of the values for
   sample 'DW-NP-48-16'.

   .. code:: python

       >>> Sample48 = [SampleID, SampleNumber, SampleWeightLbs, SampleRockType]
       >>> print(Sample48)
       ['DW-NP-48-16', 48, 6.89, 'Mica schist']

   Here we have one list with 3 different type of data in it. We can
   confirm this using the ``type()`` function.

   .. code:: python

       >>> type(Sample48)
       list
       >>> type(Sample48[0])    # The sample ID
       str
       >>> type(Sample48[1]     # The sample number
       int
       >>> type(Sample48[2])    # The sample weight
       float

7. Finally, we can add and remove values from lists to change their
   lengths. Let's consider that we no longer want to include the first
   value in the ``SampleIDs`` list.

   .. code:: python

       >>> print(SampleIDs)
       ['DW-NP-03-16', 'DW-NP-12-16', 'DW-NP-33-16', 'DW-NP-48-16']
       >>> del SampleIDs[0]
       >>> print(SampleIDs)
       ['DW-NP-12-16', 'DW-NP-33-16', 'DW-NP-48-16']

   ``del`` allows values in lists to be removed. It can also be used to
   delete values from memory in Python. If we would instead like to add
   a few samples to the ``SampleIDs`` list, we can do so as follows.

   .. code:: python

       >>> SampleIDs.append('DW-NP-27-16')
       >>> SampleIDs.append('DW-NP-51-16')
       >>> print(SampleIDs)
       ['DW-NP-12-16', 'DW-NP-33-16', 'DW-NP-48-16', 'DW-NP-27-16', 'DW-NP-51-16']

   As you can see, we add values one at a time using
   ``SampleIDs.append()``. ``list.append()`` is called a *method* in
   Python, which is a function that works for a given data type (a list
   in this case). We'll see a bit more about these below.

The concept of objects
----------------------

Python is one of a number of computer programming languages that are
called "object-oriented languages". It took me quite some time to
understand what this meant, but the simple explanation is that we can
consider the variables that we define to be "objects" that can contain
both data known as *attributes* and a specific set of functions
(*methods*). The previous sentence could take quite some time to
understand by itself, but using an example the concept of "objects" is
much easier to understand.

1. Let's consider our list ``SampleIDs``. As we know, we already have
   data in the list ``SampleIDs``, and we can modify that data using
   built-in *methods* such as ``SampleIDs.append()``. We can also do
   other things such as count the number of times a value occurs in a
   list, or where it occurs.

   .. code:: python

       >>> SampleIDs.count('DW-NP-27-16')    # The count method counts the number of occurences of a value
       1
       >>> SampleIDs.index('DW-NP-27-16')    # The index method gives the index value of an item in a list
       3

   The good news here is that our selected sample ID is only in the list
   once. Should we need to modify it for some reason, we also now know
   where it is in the list (index ``3``).
2. There are two other common methods for lists that we need to see.
   First, there is the ``.sort()`` method, used to sort values in a
   list. As you can see from when we appended the additional two sample
   IDs earlier, our list no longer has sample IDs in increasing order.
   We can fix that.

   .. code:: python

       >>> SampleIDs.sort()
       >>> print(SampleIDs)
       ['DW-NP-12-16', 'DW-NP-27-16', 'DW-NP-33-16', 'DW-NP-48-16', 'DW-NP-51-16']

   Yay, it works! A common mistake when sorting lists is to do something
   like ``SampleIDs = SampleIDs.sort()``. **Do not do this!** When
   sorting with ``.sort()`` the ``None`` value is returned (this is why
   there is no screen ouput when running ``SampleIDs.sort()``). If you
   then assign the output of ``SampleIDs.sort()`` to ``SampleIDs`` you
   will sort the list, but then overwrite its contents with the returned
   value ``None``. This means you've deleted the list contents (!).
3. The ``.reverse()`` method works the same way.

   .. code:: python

       >>> SampleIDs.reverse()   # Notice no output here...
       >>> print(SampleIDs)
       ['DW-NP-51-16', 'DW-NP-48-16', 'DW-NP-33-16', 'DW-NP-27-16', 'DW-NP-12-16']

   As you can see, the list has been reversed using the ``.reverse()``
   method, but there is no screen output when this occurs. Again, if you
   were to assign that output to ``SampleIDs`` the list would get
   reversed, but the contents would then be assigned ``None``.
4. We won't discuss any list *attributes* because as far as I know there
   aren't any, but we'll encounter some very useful *attributes* of
   other data types in the future.
