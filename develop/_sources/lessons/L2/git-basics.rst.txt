Meet Git
==================

These materials have been adapted for the geo-python course from `GitHubClassroom Campus Advisors -resources <https://github.com/Campus-Advisors>`_ Modules 1 and 2.


Gonfiguration
-----------------

Before starting to work, **check if you have git installed** by typing this command in the terminal window:

.. code-block:: bash

    $ git --version

Anything above version 2 is just fine.

Next, **configure user information for local repositories**. The user name you set will be attached to your commits:

.. code-block:: bash

    $ git config --global user.name "Your Name"

    $ git config --global user.email "email@example.com"

You can check existing user information with these commands:

.. code-block:: bash

    $ git config user.name

    $ git config user.email

Cloning
---------

We will clone an existing repository from GitHub and start modifying it. A repository, or a "repo", is a location for storing files. In general, it is recommended that each project, library or discrete piece of software should have it's own repository
In this course each exercise has it's own repository. We will clone Exercise-1 repository from week 1 for practicing how to work with Git and GitHub.

Navigate to your personal exercise-1 repository in https://github.com/Geo-Python-2018/ and copy the web URL of your exercise-1 repository:

.. figure:: img/GitHub_clone_link.png

Clone the repository into JupyterLab using the `git clone` command:

.. code-block:: bash

    $ git clone [paste your URL here]

.. note::

    You can paste text on the terminal trough Shift + Right Click --> paste

List directory contents in the terminal using the `ls` command:

.. code-block:: bash

    $ ls

You should now see the exercise repository in the list! Navigate to the repository usind the `cd`command:

.. code-block:: bash

    $ cd exercise-1-username

List all files inside the repository using the `ls` command, and include hidden files using the -al command

.. code-block:: bash

    $ ls -al

Check the status of your repository using  the `git status` command, which provides change information about the repository (this is the most common git command - use it often!):

.. code-block:: bash

    $ git status

Make changes
---------------

Create an empty markdown-file `test.md` under the exercise-1 repository. You can either create the file manually (do this if you are using windows!), or in the terminal using the `touch` -command:

.. code-block:: bash

    $ touch test.md


You can also edit the file contents and save your changes (Ctrl + S).
List all files inside the repository (you should see the new file listed in the terminal)

.. code-block:: bash

    $ ls

check the status of the repository
.. code-block:: bash

    $ git status

**Add and commit changes**

Add a snapshopt of your changes to the 'staging area'. The staging area is an index that prepares content for the next commit.

.. code-block:: bash

    $ git add test.md

check again the status of the repository

.. code-block:: bash

    $ git status

Commit your changes to the repository and include a message to accompany the change

.. code-block:: bash

    $ git commit -m "added a test file"

Check the status of your repository

.. code-block:: bash

    $ git status

Synchronize changes
--------------------

Let's make a network call and send data to branch 'master' in the remote repository

.. code-block:: bash

    $ git push origin master

Now, you should see the updates in GitHub! (go and have a look)

Link the remote with the local in a bookmark (after doing this, you can just call `git push`)

.. code-block:: bash

    $ git push -u origin master

If you want to double check that you have a remote location, you can use the `git remote` command (v stands for 'verbose' which prints out more details):

.. code-block:: bash

    $ git remote -v










