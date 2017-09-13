Basic elements of Python
========================

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

    stationName = 'Helsinki Kaivopuisto'
    stationID = 132310
    stationLat = 60.15
    stationLong = 24.96
    stationType = 'Mareographs'

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
    **Poll pause - Questions 2.2, 2.3**

    Please visit the `class polling page <https://geo-python.github.io/poll>`__ to participate (*those present in lecture only*).

4. Although most mathematical operations operate on numerical values, a common way to combine character strings is using the addition operator ``+``.

   .. ipython:: python

    stationNameAndID = stationName + ": " + str(stationID)
    print(stationNameAndID)

   Note that here we are converting ``stationID`` to a character string using the ``str()`` function within the assignment to the variable ``stationNameAndID``.
   Alternatively, we could have simply added ``stationName`` and ``stationIDStr``.

Lists and indices
-----------------

Above we have seen a bit of data related to one of several FMI observation stations in the Helsinki area.
Rather than having individual variables for each of those stations, we can store many related values in a *collection*.
The simplest type of *collection* in Python is a **list**.

1. Let's first create a list of selected ``stationName`` values.

   .. ipython:: python

    stationNames = ['Helsinki Harmaja', 'Helsinki Kaisaniemi', 'Helsinki Kaivopuisto', 'Helsinki Kumpula']
    print(stationNames)
    type(stationNames)

   Here we have a list of 4 ``stationName`` values in a list called ``stationNames``.
   As you can see, the ``type()`` function recognizes this as a list.
   Lists can be created using the square brackets (``[`` and ``]``), with commas separating the values in the list.

2. To access an individual value in the list we need to use an **index value**.
   An **index value** is a number that refers to a given position in the list.
   Let's check out the first value in our list as an example:

   .. ipython:: python

       print(stationNames[1])

   Wait, what?
   This is the second value in the list we've created, what is wrong?
   As it turns out, Python (and many other programming languages) start values stored in collections with the index value 0.
   Thus, to get the value for the first item in the list, we must use index 0.

   .. ipython:: python

       print(stationNames[0])

   OK, that makes sense, but it may take some getting used to...

3. As it turns out, index values are extremely useful, very commonly used in many programming languages, yet often a point of confusion for new programmers.
   Thus, we need to have a trick for remembering what an index value is and how they are used.
   For this, we need to be introduced to Bill.

   .. figure:: img/bill-the-vending-machine.png
    :width: 800px
    :align: center
    :alt: Bill the vending machine

    Bill, the vending machine.

   As you can see, Bill is a vending machine that contains 6 items.
   Like Python lists, the list of items available from Bill starts at 0 and increases in increments of 1.

   The way Bill works is that you insert your money, then select the location of the item you wish to receive.
   In an analogy to Python, we could say Bill is simply a *list* of food items and the buttons you push to get them are the *index values*.
   For example, if you would like to buy a taco from Bill, you would push button ``3``.
   The equivalent operation in Python would simply be

   .. ipython:: python
    :suppress:

    Bill = ["Lollypop", "Cookie", "Hamburger", "Taco", "Ice cream cone", "Beer"]

   .. ipython:: python

    print(Bill[3])

4. We can find the length of a list using the ``len()`` function.

   .. ipython:: python

    len(stationNames)

   Just as expected, there are 4 values in our list and ``len(stationNames)`` returns a value of 4.

5. If we know the length of the list, we can now use it to find the value of the last item in the list, right?

   .. ipython:: python

    print(stationNames[4])

   What, an ``IndexError``?
   That's right, since our list starts with index 0 and has 4 values, the index of the last item in the list is ``len(SampleIDs) - 1``.
   That isn't ideal, but fortunately there's a nice trick in Python to find the last item in a list.

   .. ipython:: python

    print(stationNames)
    print(stationNames[-1])
    print(stationNames[-4])

   Yes, in Python you can go backwards through lists by using negative index values.
   Index -1 gives the last value in the list and index ``-len(SampleIDs)`` would give the first.
   Of course, you still need to keep the index values within their ranges.

   .. ipython:: python

    print(stationNames[-5])

   .. attention::
    **Poll pause - Question 2.4**

    Please visit the `class polling page <https://geo-python.github.io/poll>`__ to participate (*those present in lecture only*).

6. Another nice feature of lists is that they are *mutable*, meaning that the values in a list that has been defined can be modified.
   Consider a list of the observation station types corresponding to the station names in the ``stationNames`` list.

   .. ipython:: python

    stationTypes = ['Weather stations', 'Weather stations', 'Weather stations', 'Weather stations']
    print(stationTypes)

   Now as we saw before, the station type for Helsinki Kaivopuisto should be 'Mareographs', not 'Weather stations'.
   Fortunately, this is an easy fix.
   We simply replace the value at the corresponding location in the list with the correct one.

   .. ipython:: python

    stationTypes[2] = 'Mareographs'
    print(stationTypes)

7. Lists also do not need to have only one type of data.
   Let's consider that in addition to having a list of each station name, FMISID, latitude, etc. we would like to have a list of all of the values for station 'Helsinki Kaivopuisto'.

   .. ipython:: python

    stationHelKaivo = [stationName, stationID, stationLat, stationLong, stationType]
    print(stationHelKaivo)

   Here we have one list with 3 different type of data in it.
   We can confirm this using the ``type()`` function.

   .. ipython:: python

    type(stationHelKaivo)
    type(stationHelKaivo[0])    # The station name
    type(stationHelKaivo[1])    # The FMISID
    type(stationHelKaivo[2])    # The station latitude

8. Finally, we can add and remove values from lists to change their lengths.
   Let's consider that we no longer want to include the first value in the ``stationNames`` list.

   .. ipython:: python

    print(stationNames)
    del stationNames[0]
    print(stationNames)

   ``del`` allows values in lists to be removed.
   It can also be used to delete values from memory in Python.
   If we would instead like to add a few samples to the ``stationNames`` list, we can do so as follows.

   .. ipython:: python

    stationNames.append('Helsinki lighthouse')
    stationNames.append('Helsinki Malmi airfield')
    print(stationNames)

   As you can see, we add values one at a time using ``stationNames.append()``.
   ``list.append()`` is called a *method* in Python, which is a function that works for a given data type (a list in this case).
   We'll see a bit more about these below.

The concept of objects
----------------------

Python is one of a number of computer programming languages that are called 'object-oriented languages'.
It took me quite some time to understand what this meant, but the simple explanation is that we can consider the variables that we define to be 'objects' that can contain both data known as *attributes* and a specific set of functions (*methods*).
The previous sentence could take quite some time to understand by itself, but using an example the concept of 'objects' is much easier to understand.

1. Let's consider our list ``stationNames``.
   As we know, we already have data in the list ``stationNames``, and we can modify that data using built-in *methods* such as ``stationNames.append()``.
   We can also do other things such as count the number of times a value occurs in a list, or where it occurs.

   .. ipython:: python

    stationNames.count('Helsinki Kumpula')    # The count method counts the number of occurences of a value
    stationNames.index('Helsinki Kumpula')    # The index method gives the index value of an item in a list

   The good news here is that our selected station name is only in the list once.
   Should we need to modify it for some reason, we also now know where it is in the list (index ``2``).

2. There are two other common methods for lists that we need to see.
   First, there is the ``.reverse()`` method, used to reverse the order of items in a list.

   .. ipython:: python

    stationNames.reverse()
    print(stationNames)

   Yay, it works!
   
   .. caution::
    A common mistake when sorting lists is to do something like ``stationNames = stationNames.reverse()``.
    **Do not do this!**
    When reversing lists with ``.reverse()`` the ``None`` value is returned (this is why there is no screen ouput when running ``stationNames.reverse()``).
    If you then assign the output of ``stationNames.reverse()`` to ``stationNames`` you will reverse the list, but then overwrite its contents with the returned value ``None``.
    This means you've deleted the list contents (!).

3. The ``.sort()`` method works the same way.

   .. ipython:: python

    stationNames.sort()   # Notice no output here...
    print(stationNames)

   As you can see, the list has been sorted alphabetically using the ``.sort()`` method, but there is no screen output when this occurs.
   Again, if you were to assign that output to ``stationNames`` the list would get sorted, but the contents would then be assigned ``None``.

   .. note::
    As you may have noticed, ``Helsinki Malmi airfield`` comes before ``Helsinki lighthouse`` in the sorted list.
    This is because alphabetical sorting in Python places capital letters before lowercase letters.

4. We won't discuss any list *attributes* because as far as I know there aren't any, but we'll encounter some very useful *attributes* of other data types in the future.
