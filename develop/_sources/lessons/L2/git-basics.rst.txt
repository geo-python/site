Meet Git
=========

Overview and preparations
-----------------------------
Let's go trough the basics of using git. Before working on this tutorial, please go and accept exercise 2 on GitHub Classroom from the  :doc:`Exercise-2 landing page <exercise-2>`.
Also, open a JupyterLab session in order follow this tutorial hands-on.

.. image:: https://img.shields.io/badge/launch-binder-red.svg
   :target: https://mybinder.org/v2/gh/Geo-Python-2019/Binder/master?urlpath=lab

.. image:: https://img.shields.io/badge/launch-CSC%20notebook-blue.svg
   :target: https://notebooks.csc.fi/#/blueprint/d71cd2d26d924f48820dc22b67a87d8e

We will cover the very basics of version control using Git and GitHub:

1. `Configuration`_
2. `Clone a repository from GitHub`_
3. `Add changes to the staging area`_
4. `Commit changes`_
5. `Publish your local commits to GitHub`_

There are many different ways to use Git. We will first go trough the basics of using Git from the command line, and then we will learn to repeat these steps using a plugin in JupyterLab.
These materials have been adapted for the geo-python course from `GitHubClassroom Campus Advisors -resources <https://github.com/Campus-Advisors>`_, and inspired by other online resources such as https://git-scm.com/about/.

Key concepts and tools
-----------------------

.. figure:: img/Git_illustration.png

    Different stages of version control using Git and Github (adapted from `Git webpages <https://git-scm.com/about/staging-area>`__)

.. figure:: img/pull-push-illustration.png

    Always pull before you push (especially when working in a shared repository)!

.. note::
    After going trough this tutorial, you will be familiar with the following git-commands:

    1. **git clone [url]** - retrieve a repository from a remote location (often from GitHub)
    2. **git status** - review the status of your repository (use this command often!)
    3. **git add [file]** or **git add .** - add files to the next commit (add files to the staging area)
    4. **git commit -m "[descriptive message]"** - commit staged files as a new snapshot
    5. **git pull** - bring the local branch up to date (fetch and merge changes from the remote)
    6. **git push** - transmit local branch commits to the remote repository

    Check out other commonly used git commands from `the GIT CHEAT SHEET <https://education.github.com/git-cheat-sheet-education.pdf>`__

Using Git from the command line
-------------------------------
You will need to know a couple of basic command line commands in order to use Git. Code Academy's `list of command line commands <https://www.codecademy.com/articles/command-line-commands>`__ provides
a good overview of commonly used commands for navigating trough files in the Terminal. The instructions below are compatible with the Linux terminal (which is available in :doc:`the course environment <course-environment-components>`).

Start a new Terminal session in JupyterLab (using the icon on the Launcher, or from File > New > Terminal)

.. figure:: img/terminal-icon.png

**check if you have git installed** by typing :code:`git --version` in the terminal window:

.. code-block:: bash

    $ git --version

Anything above version 2 is just fine.


Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Configuring Git by storing your Git username and email can be useful especially if working from own computer as you do not
need to fill these information every time when you are e.g. pulling or pushing from remote repository.
The username you set, will be attached to your commits:

.. code-block:: bash

    $ git config --global user.name "[Your Name]"

    $ git config --global user.email "[email@example.com]"

You can check existing user information with these commands:

.. code-block:: bash

    $ git config user.name

    $ git config user.email

We can also tell Git to remember our GitHub username and password using a credential helper (see instructions for other operating systems than linux `here <https://help.github.com/en/articles/caching-your-github-password-in-git<`__:

.. code-block:: bash

    $ git config --global credential.helper 'cache --timeout=3600'

.. note::

    You will need to cache your credentials in order to use the Git plugin in JupyterLab.

Clone a repository from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will **clone an existing repository from GitHub and start modifying it**. A repository, or "Git project", or a "repo", is a location for storing files.
A repo contains all the files and folders associated with a project and the revision history of each entity. In general, it is recommended that each project, library or discrete piece of software should have it's own repository.
In this course each exercise has it's own repository.

First we need to navigate to the correct folder in the Terminal. Type in ``ls`` to check the contents of the current directory:

.. code-block:: bash

    $ ls

In case you are working in the CSC notebooks environment, you should see two directories (folders) in the work-directory: ``exercises`` and ``notebooks``.
The notebooks folder contains all the lesson materials (each time you launch an instance, Git automatically pulls changes from https://github.com/geo-python/notebooks! ).

The exercises folder is an empty folder where you can start working with the exercise materials.
Let's *change directory* to the exercise directory using the ``cd`` command:

.. code-block:: bash

    $ cd exercises

Now we are ready to start cloning. For this, we need a url for the remote repository. Go to https://github.com/geo-python-2019/ and navigate to your personal Exercise-2 folder (for example, Vuokko would go to https://github.com/geo-python-2019/exercise-2-VuokkoH ).
On GitHub, find the button **Clone and download** and copy the url under *Clone with HTTPS* (for example; https://github.com/geo-python-2019/exercise-1-VuokkoH.git ).

.. figure:: img/GitHub_clone_link.png

Clone the repository into JupyterLab using the :code:`git clone` command:

.. code-block:: bash

    $ git clone [paste your URL here]

for instance:

.. code-block:: bash

    $ git clone https://github.com/geo-python-2019/exercise-1-VuokkoH.git

.. note::

    You can paste text on the terminal using :code:`Ctrl + V` or :code:`Shift + Right Click --> paste`

After running ``git clone`` Git will prompt you for GitHub username and password:

.. code-block:: bash

    Cloning into 'exercise-1-VuokkoH'...
    Username for 'https://github.com': VuokkoH
    Password for 'https://VuokkoH@github.com':
    remote: Counting objects: 9, done.
    remote: Compressing objects: 100% (5/5), done.
    remote: Total 9 (delta 1), reused 9 (delta 1), pack-reused 0
    Unpacking objects: 100% (9/9), done.

Once cloning is completed, check what happened in the current directory by listing directory contents in the terminal using the :code:`ls` command:

.. code-block:: bash

    $ ls

You should now see the exercise repository listed in the terminal (as well as in the File Browser).
**Navigate to the exercise directory** using the :code:`cd` command:

.. code-block:: bash

    $ cd exercise-1-username

List all files in the directory, this time including all hidden files using the :code:`ls -a` (on Windows, use :code:`dir /a`):

.. code-block:: bash

    $ ls -a

Tada! You now have a local version of your exercise-2 repository! You should see ``.git`` listed on the screen - this is a hidden folder that contains all the information that Git needs for version control.
**Check the status of your local git repository** usin the :code:`git status` command, which provides change information about the repository (this is the most common git command - use it often!):

.. code-block:: bash

    $ git status

As we didn't make any changes yet, git should tell that the project is up to date.
At this stage, your terminal window should look something like this:

.. figure:: img/Terminal_git_status1.png

Git status also tells that you are on branch master. **During this course you don't have to worry much about branches**, but it is good to know that master branch is always the default branch.
A branch is a parallel version of a repository which can be developed separately before merging the changes to the primary version. You can read more about branches `here <https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is>`__.

.. note::
    In case you would be starting a new project from the scratch, you could create a new repository using ``git init`` command (https://git-scm.com/docs/git-init).
    During this course, however, we always start working by cloning an existing repository. In case you want to create new files on the command line using git, you can use ``git touch``.


Add changes to the staging area
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's start making changes in the repository! For example, open the Readme.md -file of the exercise repository and type in something.

After saving your changes, check the status of the repository:

.. code-block:: bash

    $ git status


Git should tell you that it detected changes that have not been "staged for commit:"

.. code-block:: bash

    On branch master
    Your branch is up to date with 'origin/master'.

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

            modified:   README.md

As you can see, you could use ``git checkout README.md`` to discard the changes you made.
In case you are happy with your changes, go ahead and ``git add README.md to add the changes to the staging area:

.. code-block:: bash

    $ git add README.md

check the status of your repository:

.. code-block:: bash

    $ git status

Git now tells you that there are changes that are ready to be committed:

.. code-block:: bash

    On branch master
    Your branch is up to date with 'origin/master'.

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            modified:   README.md

Here, git tells you how you can unstage the changes using ``git reset HEAD <file>...``. Doing this would not revert the changes, just unstage them back to the working directory.
You might want to "reset HEAD", for example, in case you had added many files to the staging area, but decide to commit them separately. For now, we are happy with the changes made,
and are ready to commit them.

Commit changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before recording your changes, check again the status of your repository:

.. code-block:: bash

    $ git status

All files listed under "Changes to be committed" will be included in the next commit - a record changes to the repository.

Commit the changes using ``git commit -m [message]``. **Pay attention that you write an informative commit message!**

.. code-block:: bash

    $ git commit -m "modified README.md"

Check the status:

.. code-block:: bash

    $ git status

Git status tells that your branch is ahead of the remote repository's master branch by 1 commit, and tells you to use :code:`git push` to publish the local changes:

.. code-block:: bash

    $ git status
    On branch master
    Your branch is ahead of 'origin/master' by 1 commit.
      (use "git push" to publish your local commits)


Publish your local commits to GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next, we want to synchronize our local changes with the remote repository on GitHub. First, it's good to use :code:`git pull` to double check for remote changes before contributing your own changes.

.. code-block:: bash

    $ git pull

Git should tell you that the repository is **"Already up-to-date"**. Now we are ready to push the local changes to GitHub using :code:`git push`:

.. code-block:: bash

    $ git push origin master

or just simply

.. code-block:: bash

    $ git push

Git will prompt you for username and password before pushing the changes online:

.. code-block:: bash

    jovyan@jupyter-geo-2dpython-2d2018-2dbinder-2d63pkzqdt:~/exercise-1-VuokkoH$ git push
    Username for 'https://github.com': VuokkoH
    Password for 'https://VuokkoH@github.com':
    Counting objects: 3, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 316 bytes | 316.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/Geo-Python-2018/exercise-1-VuokkoH.git
       b33a43a..c4be7c3  master -> master

Now, you should see the updates in GitHub (go and have a look at your personal repository in https://github.com/Geo-Python-2019/ )!

Using the JupyterLab Git plugin
-------------------------------

For your convenience, we have also installed a plugin in JupyterLab which has buttons for completing most of the version control tasks we need during this course.
Even if using the plugin, you need to clone the repository and cache your username and password on the command line:

Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ git config --global credential.helper 'cache --timeout=3600'

Clone a repository from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    $ git clone [paste your URL here]

After caching the credentials and cloning the repo, you can do the rest using the plugin.


Add changes to the staging area
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- modify README.md and save the file. The git plugin should detect the changes
- stage all changes using the plugin

Commit changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- add a descriptive commit message in the text box
- click on the commit-button
- check commit history under the history-tab

Publish your local commits to GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First, press "Pull" to check that the local repo is up to date
- Then, press "Push"

.. warning::
    In case you get an error message, you have not successfully cashed your credentials.
    In this case, you can run git pull and git push from the command line.


If everything else fails...
------------------------------------

Remember, that you can always download your files on your own computer, and upload them manually to GitHub like we did in exercise 1!

.. image:: https://imgs.xkcd.com/comics/git.png
    :alt: https://xkcd.com/1597/

Remotes
------------------------------------

If you want to double check that you have a remote location, you can use the :code:`git remote` command (v stands for 'verbose' which prints out more details):

.. code-block:: bash

    $ git remote -v

Check once more the status of your repository:

.. code-block:: bash

    $ git status


That's all you need to know about Git for know :)



