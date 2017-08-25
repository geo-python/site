Using the course environment
============================

Principles of the course environment
------------------------------------

-  You will launch a new cloud computer instance every time you're
   working in a lecture or doing the exercises.

-  You will **ALWAYS** download the course materials from the course
   GitHub repository for the week.

-  You will **ALWAYS** save everything you have done (codes, figures,
   data, etc.) on your private GitHub account because files cannot be
   saved permanently to the cloud computers.

-  There is a fixed 'life-time' allocated (**6 hours**) for each
   computer instance

-  After finishing your work, you should always 'destroy' your course
   environment by yourself from the `Pebbles
   Dashboard <https://pb.geo.helsinki.fi>`__.
-  **Note**: We have tried to design the cloud computers to have
   reminders to save your work, or that you session will soon end.
   However, when the life-time of the computer instance is finished the
   system will automatically 'destroy' your Computer Instance and you
   **will lose EVERYTHING in it** if you have not updated your files on
   Github.


We'll start using the course environment by creating and activating your
account on the Computing Dashboard, and launching our first Computer
Instance. Then we will download course materials from GitHub to your
cloud computer, do some work, and save your work back on GitHub.

.. note::

    The first time you use the computing environment, you must :doc:`create and activate your account on the Computing Dashboard <activate-pb-account>`.
    **You only need to do this once**.

Here are the remaining steps that you will follow during each lecture.
You will do steps 1-4 below repeatedly during the course, so it will
become familiar to you after a few weeks.

1. `Log into the Computing Dashboard and launch a Computer
   Instance <launch-instance.md>`__

2. `Connect to Computer Instance from your local
   computer <connect-to-instance.md>`__

3. `Use Git and GitHub to download the course materials and save your
   work <intro-to-github.md>`__

4. `When finished working, destroy the Computer
   Instance <destroy-instance.md>`__


Launching a new computer instance
---------------------------------

Launching a new computer instance is a straightforward procedure that is
done from the Computing Dashboard. These instructions will help you
first launch a new Computer Instance and then open a port to it from
your local computer's IP address (steps 5-6). A port in a computer is a
somewhat similar to the idea of having a door in a house: you cannot
access the house without having an open door. In this analogy, the
default computing instance will have all the doors closed until you open
one for yourself.

.. admonition:: Step 1

    **Navigate with a web browser to** https://pb.geo.helsinki.fi.

    *You might want to bookmark this page in your web browser as we are going to this address often.*

.. admonition:: Step 2

    **Sign in to the Computing Dashboard**

    .. figure:: img/7_log_in.PNG
       :alt: Login to Computing Dashboard
       :align: center

.. admonition:: Step 3

    ``Launch new`` **computer instance**

    .. figure:: img/8_launch_instance.PNG
       :alt: Launch a new computer instance
       :align: center

.. admonition:: Step 4

    **Wait until the instance is ready.** You will first see a spinning gear
    under the **State**, the instance is ready when the gear turns into a
    checkmark. Now go to instance details.

    .. figure:: img/9_go_to_instance_details.PNG
       :alt: Go to instance details
       :align: center

.. admonition:: Step 5

    **Click on the** ``Query client IP`` **button** to find out the IP address of your local computer.

    .. figure:: img/10_query_client_IP.PNG
       :alt: Go to instance details
       :align: center

.. admonition:: Step 6

    **Click on the** ``Change client IP`` **button** to open a port in the cloud computer for your local computer. When done successfully the IP address should appear under the
    ``Client IP`` text as shown below.

    .. figure:: img/11_change_client_IP.PNG
       :alt: Go to instance details
       :align: center

.. admonition:: Step 7

    **Done! You have a remote computer running that you can access now from your local computer.**
    Go back to the Dashboard tab by pressing ``Back`` button.


Connecting to the computer instance
-----------------------------------

There are basically two steps that you need to do for being able to
connect to a remote (cloud) computer instance: (1) Find the IP address
of the (running) cloud computer instance and (2) connect to it with
remote desktop software on your local computer.

How you connect to the computer instance will depend on

-  the operating system that you have on your local computer
   (`Windows <#connect-to-computer-instance-on-windows>`__ /
   `MacOS <#connect-to-computer-instance-on-macos>`__ /
   `Linux <#connect-to-computer-instance-on-linux>`__)
-  The remote desktop software (or protocol) that you are using

Below are instructions how to access the computer instance on different
systems (follow the one that you have).

Copy the IP address of your computer instance
---------------------------------------------

Everyone will need to do this.

You can find the IP address from the Computing Dashboard under the
**'Access'** heading. Select and copy only the numbers. We won't be
using the rest of the information mentioned there. That information is
used for taking a specific type of connection (SSH) to the computer
using the command prompt.

.. figure:: img/13_copy_access_IP_address.PNG
   :alt: Copy IP address of the computer instance
   :align: center

   Copy IP address of the computer instance

Connect with Windows
--------------------

On Windows we have two different ways and pieces of software that can be
used for connecting the remote computer: **'TightVNC Viewer'** and the
**'Remote Desktop Connection'** tool (in finnish 'Etätyöpöytäyhteys').
`The TightVNC Viewer <http://www.tightvnc.com/>`__ is freely available
and is an open source remote desktop software that has some nice
features, and it is smooth to use. We will be using this tool in the GIS
labs where it is installed on the computers. If you want, you can also
`download <http://www.tightvnc.com/download.php>`__ and install this
tool to your own computer.

`The Remote Desktop Connection <https://support.microsoft.com/en-us/help/17463/windows-7-connect-to-another-computer-remote-desktop-connection>`__
tool is another remote desktop software that comes with every Windows
computer. It is more simple, but has slightly less smooth user
experience when compared to TightVNC. However, it is highly
recommendable option since it can be used from any Windows computer
(e.g., from the computers in the University's libraries or your own
Windows computer) without any additional software installation.

Details on how to connect with both pieces of software are given below.

1. `Connecting with the TightVNC Viewer software <connect-win-vnc.md>`__
2. `Connecting with the Remote Desktop Connection
   tool <connect-win-rdp.md>`__

Connect with MacOS
------------------

The preferred way to connect to the computer instances on MacOS is to
use the built-in connection tool in **Finder**.

.. figure:: ../img/connect-to-server.png
   :alt: Connect to server

   Connect to server

Once the **Connect to Server** window appears, enter the address of the
computer instance to connect in the format
``vnc://XXX.XXX.XXX.XXX:5901``, replacing the ``XXX.XXX.XXX.XXX`` with
the numbers you selected and copied above in the Computing Dashboard.

.. figure:: ../img/enter-server-info.png
   :alt: Enter server info

   Enter server info

At this point you can click **Connect** and enter the password for the
connection when prompted (``geoman``). Now you should see the desktop of
your cloud computer!

.. figure:: ../img/cloud-desktop-mac.png
   :alt: Cloud desktop Mac

   Cloud desktop Mac

Connect with Linux
------------------

If there are users running Linux, let us know if you're not aware of how
to use VNC on your machine and we can help get you connected.




