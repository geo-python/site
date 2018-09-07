Meet Git
==================

These materials have been adapted for the geo-python course from `GitHubClassroom Campus Advisors -resources <https://github.com/Campus-Advisors>`_ Modules 1 and 2.

**Check to see if you have git installed:**

Type this command in the terminal window:

.. code-block:: bash

    $ git -- version

Anything above version 2 is just fine.

**Configure user information**

Check git user configuration:

.. code-block:: bash

    $ git config user.name

    $ git config user.email

If these commands return nothing it means that user information has not been configured.
Configure git to recognize you. The user name you set will be attached to your commits:

.. code-block:: bash

    $ git config user.name "Mona Lisa"

    $ git config --global user.email "email@example.com"


**Clone a repository from GitHub**

A repository, or a "repo", is a location for storing files. In general, it is recommended that each project, library or discrete piece of software should have it's own repository
In this course each exercise has it's own repository. We will repository for Exercise-1 for practicing how to work with Git and GitHub.

Go to GitHub and copy the web URL of your exercise-1 repository

Clone the repository into JupyterLab using this command in the terminal:

.. code-block:: bash

    $ git clone [paste your URL here]


(note: you can paste text on the terminal trough Shift + Right Click --> paste)

navigate to the repository:

.. code-block:: bash

    $ cd exercise-1-GITHUBUSERNAME

List all files inside the repository using the ls command, and include hidden files using the -al command

.. code-block:: bash

    $ ls -al

Check the status of your repository (this is the most common git command - use it often!) Git status provides change information about the repository.

.. code-block:: bash

    $ git status

**Edit content**

Create an empty markdown-file `test.md`. You can either create the file manually (do this if you are using windows!), or in the terminal using the `touch` -command:

.. code-block:: bash

    $ touch test.md

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

Modify the file, add for example a few lines of text. Save your changes (Ctrl + S)

check again the status of the repository

.. code-block:: bash
    $ git status

Snapshot the file again

.. code-block:: bash
    $ git add test.md

.. code-block:: bash

    $ git status

Commit your changes to the repository and include a message to accompany the change

.. code-block:: bash

    $ git commit -m 'added a test file

Check the status

.. code-block:: bash

    $ git status

**Push your changes to GitHub**


Let's make a network call and send data to branch 'master'

.. code-block:: bash
    $ git push origin master

Now, you should see the updates in github! (go and have a look)

Link the remote with the local in a bookmark (in the future, you can just call git push)

.. code-block:: bash
    $ git push -u origin maste

If you want to double check that you have a remote location, you can type in:

.. code-block:: bash
    $ git remote

This tells you that a remote location exists. Note: origin is just a default name, you can change this if you wish! The exact address of the remote is shown using the following command.

Check remote locations with -v (=verbose)

.. code-block:: bash
    $ git remote -v



*








