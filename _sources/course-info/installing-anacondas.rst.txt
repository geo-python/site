Installing Python
=================

**It is possible to do programming with Python on your own computer**, but first you need to install Python. The purpose of this page is to help you to
install Python and different Python packages into your own computer. Even though it is possible to install Python from their `homepage <https://www.python.org/>`_,
**we highly recommend using** `Anaconda <https://www.continuum.io/anaconda-overview>`_ which is an open source distribution of the Python and R programming
languages for large-scale data processing, predictive analytics, and scientific computing, that aims to simplify package management and deployment. In short,
it makes life much easier when installing new tools to your Python.

Install Python on Windows
-------------------------

Following steps have been tested to work on Windows 7 and 10 with Anaconda3 version 4.2.0 (19th November 2016).

`Download Anaconda installer (64 bit) <https://repo.continuum.io/archive/Anaconda3-4.2.0-Windows-x86_64.exe>`_ for Windows.

Install Anaconda to your computer by double clicking the installer and install it into a directory you want (needs admin rights).
Install it to **all users** and use default settings.

.. note::

    Note for University of Helsinki workers: you need to set the installation location as ``C:\HYapp`` so that it can be used easily by anyone without the need to
    pass admin credentials all the time. If you don't have ``C:\HYapp`` -folder, create one with admin rights.


Test that the Anaconda´s package manage called ``conda`` works by
`opening a command prompt as a admin user <http://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/>`_
and running command ``conda --version``. If the command returns a version number of conda (e.g. ``conda 4.3.23``) everything is working correctly.


Install Python on Linux / Mac
-----------------------------

The following have been tested on Ubuntu 16.04. Might work also on Mac (not tested yet).

**Install Anaconda 3 and add it to system path**

.. code::

    # Download and install Anaconda
    sudo wget https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh
    sudo bash Anaconda3-4.1.1-Linux-x86_64.sh

    # Add Anaconda installation permanently to PATH variable
    nano ~/.bashrc

    # Add following line at the end of the file and save (EDIT ACCORDING YOUR INSTALLATION PATH)
    export PATH=$PATH:/PATH_TO_ANACONDA/anaconda3/bin:/PATH_TO_ANACONDA/anaconda3/lib/python3.5/site-packages

How to find out which conda -command to use when installing a package?
----------------------------------------------------------------------

The easiest way
~~~~~~~~~~~~~~~

The first thing to try when installing a new module ``X`` is to run in a command prompt (as admin) following command (here we try to install a hypothetical
module called X)

.. code::

    conda install X

In most cases this approach works but sometimes you get errors like (example when installing a module called shapely):

.. code::

    C:\WINDOWS\system32>conda install shapely
    Using Anaconda API: https://api.anaconda.org
    Fetching package metadata .........
    Solving package specifications: .
    Error: Package missing in current win-64 channels:
      - shapely

    You can search for packages on anaconda.org with

        anaconda search -t conda shapely

In this case conda was not able to find the shapely module from the typical channel it uses for downloading the module.


Alternative way to install packages if typical doesn't work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If ``conda install`` command was not able to install the package you were interested in there is an alternative way to do it by taking advantage of different conda distribution channels that
are maintained by programmers themselves. An easy way to find the right command to install a package from these alternative conda distribution channels is to Google it.

Let's find our way to install the Shapely module by typing following query to Google:

.. image:: img/google_query_conda.PNG

Here, we can see that we have different pages showing how to install ``Shapely`` using conda package manager.

**Which one of them is the correct one to use?**

We need to check the operating system banners and if you find a logo of the operating system of your computer,
that is the one to use! Thus, in our case the first page that Google gives does not work in Windows but the second one does, as it has Windows logo on it:

.. image:: img/conda_shapely_windows.PNG

From here we can get the correct installation command for conda and it works!

.. image:: img/install_shapely.PNG

You can follow these steps similarly for all of the other Python modules that you are interested to install.




