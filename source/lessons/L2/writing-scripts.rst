Writing your own Python scripts
===============================

As you may be noticing by now, it isn't that convenient to type in all
of the commands you would like to use in the IPython interpreter window.
An alternative to typing in all of the commands you would like to run is
the list them in a Python script file. A Python script file is simple a
file containing a list of the command you would like to run, with one
command per line, and formatted in the same way as if you were to type
them in. Python script files traditionally use the ``.py`` file
extension in their names.

Getting started
---------------

1. To start creating and editing our Python script file, we'll need to
   open a text editor. In our case, we'll be using the **gedit** basic
   editor, which can be launched by double clicking on the **Text
   editor** icon on the desktop of your computer instance.
2. The **gedit** window will appear shortly after double clicking, and
   it should open a new (blank) document by default. You're now ready to
   proceed.

The general concept of a ``.py`` script file
--------------------------------------------

A Python script file is simply a list of commands that you might
otherwise type into the IPython interpreter window. As such, we can
quite easily create a basic script file and test things out.

1. Start by copying and pasting the text below into your **gedit**
   window.

   .. code:: python

       SampleID = "DW-NP-48-16"
       SampleWeightLbs = 6.89
       print("Sample", SampleID, "weighs", SampleWeightLbs, "pounds")

2. Save this script file as ``sampleinfo.py`` in your home directory
   ``/home/geo`` by clicking on **File -> Save** in the menu bar of the
   **gedit** window. Click on the **Home** icon on the top left of the
   **Save As** window that appears, and enter the file name as
   ``sampleinfo.py``. Click the ``Save`` button on the lower right of
   the window to save the file.
3. Return to your IPython interpreter window (or start a new one if you
   have closed it), change the directory in IPython to the home
   directory by typing ``cd``, and run the script using the ``%run``
   magic command in IPython. Before pressing **Enter** on the second
   line, **what do you expect to see as output when the script runs**?

   .. code:: python

       >>> cd
       >>> %run sampleinfo.py
       Sample DW-NP-48-16 weighs 6.89 pounds

   No surprises here. The script simply executes the commands exactly as
   you would have if you had typed them in to the IPython interpreter.
4. Now let's make a small change to the script. Go back to **gedit** and
   edit the script so that it now reads

   .. code:: python

       SampleID = "DW-NP-48-16"
       SampleWeightLbs = 6.89
       SampleRockType = "Mica schist"
       print("Sample", SampleID, "is a", SampleWeightLbs, "pound chunk of", SampleRockType)

   Save your changes.
5. Once again, go back to the IPython interpreter and use the ``%run``
   magic command to run the modified script. Don't worry, we'll cover a
   much better way to edit and test scripts later in today's lesson.

   .. code:: python

       >>> %run sampleinfo.py
       Sample DW-NP-48-16 is a 6.89 pound chunk of Mica schist

Writing our scripts the "right" way
-----------------------------------

The script above works, but one of the big advantages of using scripts
is the ability to include comments that describe what the code does. As
your programs get longer and more complicated, comments and other
changes to how you write the code will help make sure you (and other
users) can understand what the code does. Below are some suggestions to
make sure your code is easy to understand.

1. **Add inline comments to the code to explain what different sections
   do**. It may seem obvious how the code should work, but if you share
   it with another person perhaps they will not feel the same way. It is
   a very good idea to make the code as easy to read as possible for
   people.

   .. code:: python

       # Information for sample 48 from the 2016 Nepal (NP) field excursion collected by Dave Whipp (DW)
       # Sample 48 was from the footwall of the MCT just north of where the Nyadi river joins the Marsyandi
       # Basic sample information
       SampleID = "DW-NP-48-16"
       SampleRockType = "Mica schist"
       # Sample weight given in pounds (sorry, most of the world)
       SampleWeightLbs = 6.89
       # Print basic information about this sample to the screen
       print("Sample", SampleID, "is a", SampleWeightLbs, "pound chunk of", SampleRockType)

   Here, we have provided a great deal more information about the data
   in this script by adding *inline comments*. Comments in Python are
   not executed by the computer, but provide useful information for
   people reading the script. Inline comments begin with a ``#`` (number
   sign or hash), and all characters that follow on that line will be
   ignored by Python. Adding comments to scripts is essential for
   scientists like ourselves to both help us remember how a script works
   and to make it easier to share with colleagues. It is best to get
   into the habit of adding comments as you write.
2. **Use blank lines to visually divide your script**. Perhaps it is
   obvious, but Python will ignore blank lines in a script. They don't
   matter to Python, but they are very helpful to users.

   .. code:: python

       # Information for sample 48 from the 2016 Nepal (NP) field excursion collected by Dave Whipp (DW)
       # Sample 48 was from the footwall of the MCT just north of where the Nyadi river joins the Marsyandi

       # Basic sample information
       SampleID = "DW-NP-48-16"
       SampleRockType = "Mica schist"

       # Sample weight given in pounds (sorry, most of the world)
       SampleWeightLbs = 6.89

       # Print basic information about this sample to the screen
       print("Sample", SampleID, "is a", SampleWeightLbs, "pound chunk of", SampleRockType)

   Dividing even a short script into section using blank lines makes it
   much easier to read the code.
3. **Add a block comment section at the start of the script to state its
   purpose, how it is run, who wrote it, and possibly some licencing
   information**. In contrast to the inline comments above that describe
   the different sections of the code, a *block comment* at the top of
   the script is intended to help users run the code and be aware of its
   author (and licensing restrictions stated by the author). At the
   minimum, you should include what the script does, your name, and the
   date in the block comments at the start of script files. Let's add
   some of this basic information.

   .. code:: python

       '''sampleinfo.py

       A simple Python script to print information for a rock sample on the screen.

       Usage: ./sampleinfo.py

       David Whipp - 12.9.2016
       '''

       # Information for sample 48 from the 2016 Nepal (NP) field excursion collected by Dave Whipp (DW)
       # Sample 48 was from the footwall of the MCT just north of where the Nyadi river joins the Marsyandi

       # Basic sample information
       SampleID = "DW-NP-48-16"
       SampleRockType = "Mica schist"

       # Sample weight given in pounds (sorry, most of the world)
       SampleWeightLbs = 6.89

       # Print basic information about this sample to the screen
       print("Sample", SampleID, "is a", SampleWeightLbs, "pound chunk of", SampleRockType)

   Here we have added the basic information to the top of our script
   file using *block comments*. Block comments start with ``'''`` and
   end with ``'''``. Everything between the triple quotes will be
   ignored when the script is run, even if the text is spread over
   multiple lines. In our case, the script is simple, but many Python
   programs have optional values that can be used by the code when it is
   run, making the usage statement crucial. Another example to consider
   is using a formal software license in the code to state the
   conditions under which the code can be used or modified. There are
   many helpful web resources to `teach you about software
   licenses <https://tldrlegal.com/>`__ and `how to choose a
   license <http://choosealicense.com/>`__. In most cases my preference
   is the `MIT License <https://opensource.org/licenses/MIT>`__, which
   is simple and allows software use by anyone. An example is below.

   .. code:: python

       '''sampleinfo.py

       A simple Python script to print information for a rock sample on the screen.

       Usage: ./sampleinfo.py

       MIT License

       Copyright (c) 2016 David Whipp

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

       # Information for sample 48 from the 2016 Nepal (NP) field excursion collected by Dave Whipp (DW)
       # Sample 48 was from the footwall of the MCT just north of where the Nyadi river joins the Marsyandi

       # Basic sample information
       SampleID = "DW-NP-48-16"
       SampleRockType = "Mica schist"

       # Sample weight given in pounds (sorry, most of the world)
       SampleWeightLbs = 6.89

       # Print basic information about this sample to the screen
       print("Sample", SampleID, "is a", SampleWeightLbs, "pound chunk of", SampleRockType)

   In this case I have taken the license information directly from an
   `online software license
   template <http://choosealicense.com/licenses/mit/>`__. Software
   licensing is an important consideration when posting your software in
   online repositories such as GitHub. It is one way to protect your
   intellectual property from being used in ways you do not wish.
4. **Start with a shebang**. This part gets a bit more complicated, but
   we can add one line above our first block comment to help make the
   script easier to run for users. Here, we add a line at the very top
   of the script that starts with ``#!`` (often referred to as shebang).
   The meaning of this line is given below the script.

   .. code:: python

       #!/usr/bin/env python3
       '''sampleinfo.py

       A simple Python script to print information for a rock sample on the screen.

       Usage: ./sampleinfo.py

       David Whipp - 12.9.2016
       '''

       # Information for sample 48 from the 2016 Nepal (NP) field excursion collected by Dave Whipp (DW)
       # Sample 48 was from the footwall of the MCT just north of where the Nyadi river joins the Marsyandi

       # Basic sample information
       SampleID = "DW-NP-48-16"
       SampleRockType = "Mica schist"

       # Sample weight given in pounds (sorry, most of the world)
       SampleWeightLbs = 6.89

       # Print basic information about this sample to the screen
       print("Sample", SampleID, "is a", SampleWeightLbs, "pound chunk of", SampleRockType)

   Basically, this additional line allows users to run the script in a
   terminal window without having to use the ``%run`` magic command from
   within IPython or explicitly launch a new Python interpreter. The
   line states that when the script is executed in a terminal it should
   use the default system Python 3 interpreter. We'll leave it at that
   for now, but if you have questions let us know.

Page summary
------------

As we continue in the course we will be creating more advanced Python
scripts that include more complex code logic and other features we've
not yet learned. With these, we'll also learn a few tips for
incorporating them in our scripts. However, an expectation in this
course is that you stick to the general template described above when
writing your code, which means including appropriate use of inline
comments, blank lines, block comments, and starting with a shebang.

**Next**: `Working on the assignments <working-on-assignment.md>`__\ 
**Home**: `Lesson 2 main
page <https://github.com/Python-for-geo-people/Lesson-2-Data-types-Lists>`__\ 
**Previous**: `Some basic elements of Python, part
1 <python-basic-elements1.md>`__
