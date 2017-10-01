Writing data to a file
======================

Topics
------

-  `Writing to a new file <#Writing-to-a-new-file>`__
-  `Appending to a file <#append>`__
-  `(Not) overwriting data files <#overwrite>`__
-  `Useful functions related to filepaths <#useful-functions>`__
-  `Copying contents from a file into another <#copying-files>`__

Writing to a new file
---------------------

`Previous materials <reading-multiple-files.md>`__ focused on reading
data from file(s) but for sure it is as important to know how to write
contents into a file. Writing data into a file uses the same ``open``
-function that we used for reading the data but when writing we use the
``w`` -mode.

1. When filepath is opened in write mode (``mode=w``), Python will
   create a file into that location. Let's create a file called
   ``test.txt`` into our home -folder:

\`\`\`python # Let's store the filepath of the new file into a variable
>>> out\_file = '/home/geo/test.txt'

# This will open the file in write -mode and create it at the same time
>>> w = open(out\_file, 'w') \`\`\`

Now the test.txt -file has appeared into our home -folder:

.. figure:: ../img/new-file-writing.PNG
   :alt: New file was created

   New file was created

2. We can of course write content into that file using ``.write()``
   -function. Let's write a single line of text into our test file, and
   let's use the ``with`` -statement for opening the file [0].

``python   # Open the file in write -mode    >>> with open(out_file, 'w') as w:           # Write a line of text into that file           my_line = "This is my first line of text written in Python!"           w.write(my_line)``

Now our test.txt file contains the line of text that we just wrote:

.. figure:: ../img/first-line-of-text.PNG
   :alt: First line of text

   First line of text

3. We can also add stuff to already existing file using append -mode
(``a``) in the open statement:

``python   # Open the file in append -mode    >>> with open(out_file, 'a') as w:           # Write a second line of text into our file           second_line = "This is my SECOND line of text written in Python!"           w.write(second_line)``

Now our test.txt file contains the following:

.. figure:: ../img/second-line-of-text.PNG
   :alt: Second line of text

   Second line of text

Hey, but wait a second. The text that we just added did not go to a new
line! This happens because we did not say to the computer to add a new
line after our write -statement. For doing that we need to add the
``\n`` -newline character at the end of each line that we write. Let's
fix this.

4. We can overwrite the old contents of a file by opening it again in
write -mode. **Notice:** this really does delete all the earlier
contents of the file, so be careful! Let's write those two lines now
with adding the new-line character at the end:

``python   # This will now overwrite the old contents of the existing test.txt -file   >>> with open(out_file, 'w') as w:           # Write the first line of text but now with new-line character at the end           my_line = "This is my first line of text written in Python!\n"           w.write(my_line)           # Write the SECOND line of text but now with new-line character at the end           second_line = "This is my SECOND line of text written in Python!\n"           w.write(second_line)``

Now our test.txt file looks correct:

.. figure:: ../img/second-line-of-text-fixed.PNG
   :alt: Second line of text, correct

   Second line of text, correct

Now the each sentence are correctly written in separate lines.

5. There is also another function called ``.writelines()`` that writes a
list of texts into a file where each list item will be written into the
output file. Let's add another two lines at once into our test.txt -file
using writelines -function:

\`\`\`python # Open the file in append -mode >>> with open(out\_file,
'a') as w: # Third and fourth lines of texts third\_line = "This is my
THIRD line of text written in Python!:raw-latex:`\n`" fourth\_line =
"This is my FOURTH line of text written in Python!:raw-latex:`\n`"

::

          # Write both of those lines at once
          w.writelines([third_line, fourth_line])

\`\`\`

Now we have four lines in our test.txt file:

.. figure:: ../img/third-line-of-text.PNG
   :alt: 3-4 lines

   3-4 lines

 Useful functions related to filepaths
--------------------------------------

When dealing with file paths in Python there are several useful
functions available in a sub-module called
**`os.path <https://docs.python.org/3/library/os.path.html>`__**.

For instance when creating output filepaths it is common that you have a
common folder where all the output files will be created. In such cases,
you need to combine the path to the folder and the output filename for
each output file that you produce, os-module can help with such an
operation.

1. It is possible to parse the filename of a file (without folder
   information):

``python  >>> import os  >>> filename = os.path.basename("/home/geo/data/test.txt")   >>> print(filename)  test.txt``

2. One typical example that you might need to do sometime is to copy a
   part of file into a new file in another folder. Let's create a new
   folder called ***Results*** to the home -folder of our computer
   instance using specific command called ``os.makedirs()`` but ONLY if
   it does not exist already (we can take advantage of
   ``os.path.exists()`` -function):

\`\`\`python >>> import os >>> result\_dir = "/home/geo/Results"

# Check if folder does NOT exist >>> if not os.path.exists(result\_dir):
# If folder didn't exist create one os.makedirs(result\_dir) \`\`\`

Now we have a new folder called Results in our home folder:

.. figure:: ../img/result-folder.PNG
   :alt: New folder created

   New folder created

3. Now we can combine the filename (test.txt) and our new folder using
   ``os.path.join()`` -function:

``python  >>> new_output_file = os.path.join(result_dir, filename)  >>> print(new_output_file)  /home/geo/Results/test.txt``

 Copying selected lines of (multiple) files into a new location
---------------------------------------------------------------

1. Let's take our previous exercise (reading multiple files) as a
   starting point and copy the first line of each inflammation csv-file
   and save them into new files using the same filenames but located
   into our new Results folder. We will use ``os.path.basename()``
   -function to find out the filename of the input files and
   ``os.path.join()`` -function to create the new output filepaths that
   will be saved into the new Results folder:

| \`\`\`python >>> import glob # List inflammation data files from the
  source directory
| >>> source\_dir = "/home/geo/data" >>> inflammation\_paths =
  glob.glob(source\_dir + "/inflammation\*.csv")

# As a reminder our result directory >>> result\_dir =
"/home/geo/Results"

# Iterate over the files >>> for fp in inflammation\_paths: # Parse the
filename of the input file and print it as information for the user
filename = os.path.basename(fp) print(filename)

::

         # Open the source file in read mode
         with open(fp, 'r') as f:
             # Parse the output file name, combine the result_dir folder-path and the filename of the input file
             output_fp = os.path.join(result_dir, filename)
             
             # Open and create the output file in write mode 
             with open(output_fp, 'w') as w:
             
                # Read the first line of the source file
                first_line = f.readline()
                
                # Write it to the output file
                w.write(first_line)

\`\`\`

Now we have copied the inflammation files in our Results -folder:

.. figure:: ../img/copy-files-1-line.PNG
   :alt: Results

   Results

And each of those files have the first line as content:

.. figure:: ../img/copy-files-1-line-content.PNG
   :alt: Results

   Results

Footnotes
---------

-  [0]: When reading / writing in Python, it is best to use the ``with``
   -statement as it takes care of closing your file after you have
   read/written something into your file. *Closing* the file takes care
   of saving the data into that file. If the file is not closed after
   writing something into it, the contents won't be saved into that
   file. It is similar idea than when thinking of writing something into
   a Word template document but without saving it anywhere. You can find
   more info about how to write data without ``with`` -statement, and
   how to close files from
   **`here <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>`__**.

**Next**: `Exercise 5: Analysing NOAA climate
data <https://classroom.github.com/assignment-invitations/17f0f2ee87873cb1bcb2c6a9ec228c42>`__\ 
**Home**: `Lesson 5 main
page <https://github.com/Python-for-geo-people/Lesson-5-Reading-Writing>`__\ 
**Previous**: `Reading multiple data
files <reading-multiple-files.md>`__
