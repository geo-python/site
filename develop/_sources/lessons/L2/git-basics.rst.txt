Meet Git
==================

This page will guide you through step-by-step how to clone a repository from GitHub, modify its contents, and push changes back online.

These materials have been adapted for the geo-python course from `GitHubClassroom Campus Advisors -resources <https://github.com/Campus-Advisors>`_, and inspired by other online resources such as https://git-scm.com/about/.


.. figure:: img/Git_illustration.png

    Different stages of version control using Git and Github (adapted from `Git webpages <https://git-scm.com/about/staging-area>`__)


After going trough this tutorial, you should be aware of at least the following git-commands:

1. **git clone [url]** - download a project from GitHub
2. **git add [file]** or **git add .** - add a snapshot of changes to the staging area
3. **git status** - review the status of your repository (use this command often at every stage!)
4. **git commit -m "[informative message]"** - record changes permanently in version history
5. **git pull** - download and incorporate changes. Always pull before you push (especially when working in a shared repository)!
6. **git push** - upload local commits to GitHub

For other useful git commands, you can refer to the `GIT CHEAT SHEET <https://education.github.com/git-cheat-sheet-education.pdf>`__

**We will use git from the command line** in this tutorial and throughout the course. Code Academy's `list of command line commands <https://www.codecademy.com/articles/command-line-commands>`__ provides
a good overview of commonly used commands for navigating trough files in the Terminal. The instructions below are compatible with the Linux terminal (which is available in :doc:`the course environment <course-environment-components>`).

At this point, you should launch JupyterLab and open a terminal window, for example trough Binder:

.. image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/Geo-Python-2018/Binder/master?urlpath=lab

.. figure:: img/open-terminal.png

Gonfiguration
-----------------

First, **check if you have git installed** by typing this command in the terminal window:

.. code-block:: bash

    $ git --version

Anything above version 2 is just fine.

Next, **configure user information for local repositories**. The user name you set will be attached to your commits:

.. code-block:: bash

    $ git config --global user.name "[Your Name]"

    $ git config --global user.email "[email@example.com]"

You can check existing user information with these commands:

.. code-block:: bash

    $ git config user.name

    $ git config user.email

Cloning
---------

We will **clone an existing repository from GitHub and start modifying it**. A repository, or "Git project", or a "repo", is a location for storing files. A repo contains all the files and folders associated with a project and the revision history of each entity.
In general, it is recommended that each project, library or discrete piece of software should have it's own repository.
In this course each exercise has it's own repository.

We will clone Exercise-1 repository from week 1 for practicing how to work with Git and GitHub. Navigate to your personal exercise-1 repository in https://github.com/Geo-Python-2018/ and copy the web URL which you can find under the **Clone or download** -button:

.. figure:: img/GitHub_clone_link.png

Clone the repository into JupyterLab using the :code:`git clone` command:

.. code-block:: bash

    $ git clone [paste your URL here]

.. note::

    You can paste text on the terminal trough :code:`Shift + Right Click --> paste`

Git will prompt you for GitHub username and password:

.. code-block:: bash

    Cloning into 'exercise-1-VuokkoH'...
    Username for 'https://github.com': VuokkoH
    Password for 'https://VuokkoH@github.com':
    remote: Counting objects: 9, done.
    remote: Compressing objects: 100% (5/5), done.
    remote: Total 9 (delta 1), reused 9 (delta 1), pack-reused 0
    Unpacking objects: 100% (9/9), done.

Once cloning is completed, check what happened by listing directory contents in the terminal using the :code:`ls` command (if you are working on a windows machine, use :code:`dir` instead):

.. code-block:: bash

    $ ls

You should now see the exercise repository listed in the terminal (and also in the navigation pane in JupyterLab). **Navigate to the repository** using the :code:`cd` command:

.. code-block:: bash

    $ cd exercise-1-username

List all files inside the repository using the :code:`ls` command, and include hidden files in a long format using the :code:`ls -a` (on Windows, use :code:`dir /a`):

.. code-block:: bash

    $ ls -a

**Check the status of your repository** using  the :code:`git status` command, which provides change information about the repository (this is the most common git command - use it often!):

.. code-block:: bash

    $ git status

As we didn't make any changes yet, git should tell that the project is up to date.
At this stage, your terminal window should look something like this:

.. figure:: img/Terminal_git_status1.png

Git status also tells that you are on branch master. **During this course you don't have to worry much about branches**, but it is good to know that master branch is always the default branch. A branch is a parallel version of a repository which can be developed separately before merging the changes to the primary version. You can read more about branches `here <https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is>`__.


Make changes
---------------

**Create an empty markdown-file** `test.md` under the exercise-1 repository. You can either create the file manually (do this if you are using windows!), or in the terminal using the :code:`touch` -command:

.. code-block:: bash

    $ touch test.md

List all files inside the repository (you should see the new file listed in the terminal)

.. code-block:: bash

    $ ls

check the status of the repository:

.. code-block:: bash

    $ git status


Git should tell you that it detected untracked files.

.. code-block:: bash

    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    Untracked files:
        (use "git add <file>..." to include in what will be committed)

            .ipynb_checkpoints/
            test.md

    nothing added to commit but untracked files present (use "git add" to track)


**Start tracking the file with git** uing the command :code:`git add`:

.. code-block:: bash

    $ git add test.md

check again the status of the repository

.. code-block:: bash

    $ git status

Git status shows that there is a new file under the "Changes to be committed" -heading:

.. code-block:: bash

    $ git add test.md
    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            new file:   test.md

Next, edit the contents of the test.md -file (you can do this manually! Open up the file and add a few lines of text):

.. figure:: img/edit-testMD.png

check the status of your repository:

.. code-block:: bash

    $ git status

Git now tells you that there are changes that are ready to be committed (the new file), and changes that have not yet been staged for commit:

.. code-block:: bash

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            new file:   test.md

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

            modified:   test.md


**Add a snapshopt of your changes to the 'staging area'** using the :code:`git add`:
.. code-block:: bash

    $ git add test.md

The staging area is an index that prepares content for the next commit.

Commit changes
------------------

Before committing your changes, check again the status of your repository:

.. code-block:: bash

    $ git status

Git status tells you that 1 new file (test.md) is ready to be committed:

.. code-block:: bash
    $ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            new file:   test.md

**Commit your changes** to the repository **and include a message** to accompany the change:

.. code-block:: bash

    $ git commit -m "added a test file"

Check the status:

.. code-block:: bash

    $ git status


Synchronize changes
--------------------

Next, we want to synchronize our changes with the remote repository on GitHub. First, it's good to use :code:`git pull` to double check for remote changes before contributing your own changes.

.. code-block:: bash

    $ git pull

Git should tell you that the repository is **"Already up-to-date"**.

Let's make a network call and send data to branch 'master' in the remote repository.

.. code-block:: bash

    $ git push origin master

or just simply

.. code-block:: bash

    $ git push

Now, you should see the updates in GitHub (go and have a look at your repository in https://github.com/Geo-Python-2018/ )!

If you want to double check that you have a remote location, you can use the :code:`git remote` command (v stands for 'verbose' which prints out more details):

.. code-block:: bash

    $ git remote -v

Check once more the status of your repository:

.. code-block:: bash

    $ git status


Your master branch should be now up to date in all location! That's all you need to know about Git for know :)











