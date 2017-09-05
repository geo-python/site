Anaconda, our Python distribution
=================================

For the exercises in this course we'll be using the Anaconda Python
distribution. There are several different Python distributions available
that include various Python tools and libraries, but Anaconda is easy to
install, free and up to date. Feel free to install a copy on your
personal computer to use Python wherever you please.

Downloading and installing Anaconda on Windows
----------------------------------------------

TODO.

Downloading and installing Anaconda on Mac / Linux
--------------------------------------------------

The Anaconda installation process on the laboratory computers will need
to be done once for the course, but it is quite slow.

1. If you don't still have the download, you can start by `downloading
   Anaconda <http://repo.continuum.io/archive/Anaconda3-2.5.0-Linux-x86_64.sh>`__.
   This is the 64-bit version based on Python 3.5.
2. After the download completes, open a new Terminal window by clicking
   on the Dash Home icon at the top left corner of the screen, typing
   ``terminal`` into the search box, and clicking on the Terminal icon.
3. You can now start the installation process

   .. code:: bash

       $ cd ~/Downloads
       $ bash Anaconda3-2.5.0-Linux-x86_64.sh

   Note the ``$`` symbol represents the command prompt in the Terminal
   window.
4. You will be first asked to agree to the license agreement. Press
   **Enter** to review the license. You can press space several times to
   get to the bottom of the agreement and then type in ``yes`` and press
   **Enter**.
5. Next, you are asked about the installation location. Simply press
   **Enter** to install in the default location.
6. Installation may take 30-45 minutes (!), so we can leave the
   installation running in the background. NOTE: You can safely ignore
   any error messages about not being able to create links.
7. Once the installation has completed, you will be asked a final
   question about the installation PATH. Type ``yes`` and press
   **Enter**.

What if it fails?
-----------------

If your Anaconda install fails, please type the following in your
terminal window.

.. code:: bash

    $ cd
    $ rm -rf anaconda3

You can then return to step 3 above and try to install again.
