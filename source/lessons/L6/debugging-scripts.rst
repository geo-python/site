Debugging Python scripts
========================

Debugging your scripts can be time consuming, and probably already uses most of the time you devote to working on them.
There is no way to avoid spending time fixing bugs, especially when you're learning to program and simply may not yet know how to solve a given programming problem.
That said, there are ways to be more effective when debugging, which can save you time and frustration.
Below, we review some tips for debugging.

Source
------

This lesson is based in part on the `Software Carpentry group's lesson on debugging <http://swcarpentry.github.io/python-novice-inflammation/09-debugging/>`__.

Test your code with known outputs
---------------------------------

One of the biggest challenges to debugging your code once you solve the syntax issues is knowing whether or not the code actually works like it should.
In order to be able to assess this, we need to know the "answer" the code should produce.
In many cases this means *some form* of calculating a known value using simplified data or test cases.

Testing with a simplified data file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's consider an example of calculating the maximum difference in daily temperature in Helsinki using observations for the past 50 years.
First off, we don't know the answer in advance so we cannot simply work on the code until it gives the expected temperature difference.
Secondly, we can expect that we should have more than 18 000 observations in our data file for the past 50 years, so it will be hard to confirm we get the right answer because of the size of the dataset.
One thing that can be helpful here is to test your program using some small subset of the data.
For instance, we could take the top 5 lines of data from the file, which might look like the following:

.. code::

    STATION           ELEVATION  LATITUDE   LONGITUDE  DATE     PRCP     TAVG     TMAX     TMIN     
    ----------------- ---------- ---------- ---------- -------- -------- -------- -------- -------- 
    GHCND:FIE00142080         51    60.3269    24.9603 19520101 0.31     37       39       34       
    GHCND:FIE00142080         51    60.3269    24.9603 19520102 -9999    35       37       34       
    GHCND:FIE00142080         51    60.3269    24.9603 19520103 0.14     33       36       -9999    
    GHCND:FIE00142080         51    60.3269    24.9603 19520104 0.05     29       30       25       
    GHCND:FIE00142080         51    60.3269    24.9603 19520105 0.06     27       30       25     

From this, we know two things:

- We should expect the code to be able to handle no data values equal to -9999, and to not include days with no data values when calculating the maximum temperature difference (``TMAX`` - ``TMIN``).
- The maximum temperature difference in if we test our code with this data file should be 5°

In this case, we now know that if we can get our code to return the correct answer with the small test file, perhaps the same can be done for the full dataset.
In other cases, we may actually know the expected answer, in which case debugging should be a bit easier.

Make your code crash quickly and regularly
------------------------------------------

This may sound silly, but it is a good thing when your code crashes the same way every time you run it.
If you have different behaviors when you run your code several times without making changes to the code, it will be much more difficult to isolate the problem.
What we ideally want in a code is to see behavior that is **consistent**.

In addition, if you expect to debug your program efficiently, you can't afford to wait 30 minutes every time you run it in order for it to crash.
If your code crashes when processing a massive data file, you can consider testing with some smaller part of the file.
Does the code still crash?
If not, why not?
Are there some parts of the code that seem to run just fine every time?
If you can reduce the time needed for a crash, and isolate where in the code the problem lies (perhaps in memory if you're dealing with really large datasets), you will save yourself time debugging.

Make small changes and track them
---------------------------------

We're teaching you to use `GitHub.com <https://github.com/>`__ to store your work, and to commit your changes regularly.
This is for two reasons.
First, by keeping track of the changes, you will have a better chance of isolating a problem if you find that suddenly your code doesn't work.
You can simply go back to a version of the code that worked and look at what has changed in the version that doesn't work.
**This is probably the greatest thing about version control**.
Secondly, if you make small changes to the code it is easier to see exactly what changed and where.
When it comes to debugging, this is one of the keys to finding problems quickly.

It is worth noting that often we don't keep track and commit every single small change to our codes, but rather commit when things are working as we expected.
This means that when you debug, you might not keep track of every little change you make.
This is fine, but it is important when you are debugging that you make small changes in one part of the code, then re-test.
You should change one thing at a time, test the code, and make more changes if needed.
Changing several things at once might be appealing, but it will make it harder to see exactly what is causing the problem because you can't isolate the issue to a single line of the program.