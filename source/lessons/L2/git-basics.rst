Meet Git
==================

These materials have been adapted for the geo-python course from `GitHubClassroom Campus Advisors -resources <https://github.com/Campus-Advisors>`_ Modules 1 and 2.

**1. Check to see if you have git installed:**

Type this command in the terminal window:

`git -- version`

Anything above version 2 is just fine.

**2. Git configuration**
*(is there any point in doing this on the cloud computers....?)*

Check git user configuration:

`git config user.name`
`git config user.email`

If not set, configure git to recognize you:

`git config user.name "Mona Lisa"`
`git config --global user.email "email@example.com"`

**3. Create a repository**

A repository, or a "repo", is a location for storing files. In general, it is recommended that each project, library or discrete piece of software should have it's own repository
(in this course each exercise has it's own repository!).

Initiate an empty repository with git init -command:
`git init exercise-1`

navigate to the repository:
`cd exercise-1`

List all files inside the repository using the ls command, and include hidden files using the -al command
`ls -al`

Check the status of your repository (this is the most common git command - use it often!) Git status provides change information about the repository.
`git status`

**4. Add content**

Create an empty markdown-file `readme.md`. You can either create the file manually (do this if you are using windows!), or in the terminal using the `touch` -command:

`touch readme.md`

check the status of the repository
`git status`

**4. Add and commit changes**
edit your readme file (in a text editor).

check again the status of the repository
`git status`

Add a snapshopt of your changes to the 'staging area'. The staging area is an index that prepares content for the next commit.
`git add readme.md`

Check the status
`git status`

Commit your changes to the repository and include a message to accompany the change
`git commit -m 'initialized exercise 1`

Check the status
`git status`

**5. Host the repository on github**

Next, set up a place to host your code online.

Create a repo in github [maybe the students have to activate a github classroom repo
copy the URL-of your github repo to the clipboard

On the terminal, check if check if this local repository has a remote location
`git remote`

(If the command retuns nothing there is no remote location assigned)

add a bookmark for a remote repository
`git remote add origin [paste url]`

Check again for the remote location
`git remote`

(Note: origin is just a default name, you can change this if you wish!)

Note: yet, no network activity has happened. Everything we did so far with git has happened inside the computer instance (or your local computer).

Let's make a network call and send data to branch 'master'
`git push origin master`

Now, you should see the updates in github!

Link the remote with the local in a bookmark (in the future, you can just call git push)
`git push -u origin master`

check remote locations with -v (=verbose)
`git remote -v`

...












