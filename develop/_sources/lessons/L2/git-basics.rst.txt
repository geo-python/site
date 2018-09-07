Meet Git
==================

This page will guide you through step-by-step how to clone a repository from GitHub, modify its contents, and push changes back online. These materials have been adapted for the geo-python course from `GitHubClassroom Campus Advisors -resources <https://github.com/Campus-Advisors>`_, and inspired by other online resources such as https://git-scm.com/about/.


.. figure:: img/Git_illustration.png

    Different stages of version control using Git and Github (adapted from `Git webpages <https://git-scm.com/about/>`__)


After going trough this tutorial, you should be aware of at least the following git-commands:

1. **git clone [url]** - download a project from GitHub
2. **git add [file]** or **git add .** - add a snapshot of changes to the staging area
3. **git status** - review the status of your repository (use this command often at every stage!)
4. **git commit -m "[informative message]"** - record changes permanently in version history
5. **git pull** - download and incorporate changes. Always pull before you push (especially when working in a shared repository)!
6. **git push** - upload local commits to GitHub

For other useful git commands, you can refer to the `GIT CHEAT SHEET <https://education.github.com/git-cheat-sheet-education.pdf>`__


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

We will **clone an existing repository from GitHub and start modifying it**. A repository, or a "repo", is a location for storing files. In general, it is recommended that each project, library or discrete piece of software should have it's own repository.
In this course each exercise has it's own repository.

We will clone Exercise-1 repository from week 1 for practicing how to work with Git and GitHub. Navigate to your personal exercise-1 repository in https://github.com/Geo-Python-2018/ and copy the web URL which you can find under the **Clone or download** -button:

.. figure:: img/GitHub_clone_link.png

Clone the repository into JupyterLab using the `git clone` command:

.. code-block:: bash

    $ git clone [paste your URL here]

.. note::

    You can paste text on the terminal trough Shift + Right Click --> paste

List directory contents in the terminal using the `ls` command:

.. code-block:: bash

    $ ls

You should now see the exercise repository in the list! **Navigate to the repository** using the `cd`command:

.. code-block:: bash

    $ cd exercise-1-username

List all files inside the repository using the `ls` command, and include hidden files using the -al command

.. code-block:: bash

    $ ls -al

**Check the status of your repository** using  the `git status` command, which provides change information about the repository (this is the most common git command - use it often!):

.. code-block:: bash

    $ git status

At this stage, your terminal window should look something like this:

.. figure:: img/Terminal_git_status1.png

Make changes
---------------

**Create an empty markdown-file** `test.md` under the exercise-1 repository. You can either create the file manually (do this if you are using windows!), or in the terminal using the `touch` -command:

.. code-block:: bash

    $ touch test.md

List all files inside the repository (you should see the new file listed in the terminal)

.. code-block:: bash

    $ ls

check the status of the repository:

.. code-block:: bash

    $ git status

**Add a snapshopt of your changes to the 'staging area'**. The staging area is an index that prepares content for the next commit.

.. code-block:: bash

    $ git add test.md

check again the status of the repository

.. code-block:: bash

    $ git status

**Commit your changes** to the repository **and include a message** to accompany the change:

.. code-block:: bash

    $ git commit -m "added a test file"

Check the status of your repository

.. code-block:: bash

    $ git status

Synchronize changes
--------------------

Next, we want to synchronize our changes with the remote repository on GitHub. First, it's good to use `git pull` to double check for remote changes before contributing your own changes.

.. code-block:: bash

    $ git pull

During this course you don't have to worry much about branches, but it is good to know that master branch is always the default branch. You can read more about branches `here <https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is>`__.

Let's make a network call and send data to branch 'master' in the remote repository.

.. code-block:: bash

    $ git push origin master

or just simply

.. code-block:: bash

    $ git push

Now, you should see the updates in GitHub (go and have a look)!

If you want to double check that you have a remote location, you can use the `git remote` command (v stands for 'verbose' which prints out more details):

.. code-block:: bash

    $ git remote -v



That's all you need to know for know :)











