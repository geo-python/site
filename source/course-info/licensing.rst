License and using our materials
===============================

It is our hope that the materials provided here will be helpful for others.
Thus, we share all the lesson materials openly, and our source codes and lesson materials are openly available `from GitHub <https://github.com/geo-python/site>`__.
If you would like to create your own copy of the course online, you can also find :ref:`information about how to do that below<Getting started hosting your own version of the course>`.

If you modify the lesson materials we request that you also share your materials openly (e.g., on GitHub), where everyone could benefit from your work in the same way that we provide these materials for you.
We also welcome collaboration and ideas of how to improve the materials on these pages.
Contact us via :doc:`email <course-info>` or fork the docs on **GitHub**.

**Our materials and code snippets are licensed** as explained below:

Instructional materials
-----------------------

.. raw:: html

    <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /></a>

All the instructional material is made available under the **Creative Commons Attribution-ShareAlike 4.0 International licence** . See the `full licence <https://creativecommons.org/licenses/by-sa/4.0/legalcode>`_.

In short as a human-readable version of the license:

You are free to
~~~~~~~~~~~~~~~

- **Share** - copy and redistribute the material in any medium or format
- **Adapt** - remix, transform, and build upon the material

for any purpose, even commercially. The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms
~~~~~~~~~~~~~~~~~~~~~~~~~

- **Attribution** - You must give appropriate-credit_, provide a link to the license, and indicate_ if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **ShareAlike** - If you remix, transform, or build upon the material, you must distribute your contributions under the same-license_ as the original.

**No additional restrictions** — You may not apply legal terms or technological-measures_ that legally restrict others from doing anything the license permits.

Notices
~~~~~~~

You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception_ or **limitation**.

No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity_, privacy,
or moral rights may limit how you use the material.

.. admonition:: Footnotes

    .. _appropriate-credit:

    **Appropriate credit**: If supplied, you must provide the name of the creator and attribution parties, a copyright notice, a license notice, a disclaimer notice, and a link to the material. CC licenses prior to Version 4.0 also require you to provide the title of the material if supplied, and may have other slight differences.

    .. _indicate:

    **Indicate changes**: In 4.0, you must indicate if you modified the material and retain an indication of previous modifications. In 3.0 and earlier license versions, the indication of changes is only required if you create a derivative.

    .. _same-license:

    **Same license**: You may also use a license listed as compatible at `https://creativecommons.org/compatiblelicenses <https://creativecommons.org/compatiblelicenses>`_.

    .. _technological-measures:

    **Technological measures**: The license prohibits application of effective technological measures, defined with reference to Article 11 of the WIPO Copyright Treaty.

    .. _exception:

    **Exception or limitation**: The rights of users under exceptions and limitations, such as fair use and fair dealing, are not affected by the CC licenses.**

    .. _publicity:

    **Publicity, privacy, or moral rights**: You may need to get additional permissions before using the material as you intend.


Code snippets / software
------------------------

Except where otherwise noted, the example programs, code snippets and other software provided by the Geo-Python course are made available under the **GNU GPLv3 license** (read the licence `here <https://www.gnu.org/licenses/gpl.html>`_).

Getting started hosting your own version of the course
------------------------------------------------------

Below are some instructions about how to create your own copy of the Geo-Python course materials and host it online using `Read the Docs <https://about.readthedocs.com>`__.
In essence, this allows you to easily copy and customize the course materials for your use.

Preparations
~~~~~~~~~~~~

#. If you do not already have one, create a GitHub user account at https://github.com. You can find instructions for this as part of `Exercise 1 in the course <https://geo-python-site.readthedocs.io/en/latest/lessons/L1/exercise-1.html#part-1-sign-up-for-github>`__.

#. If you do not already have one, create a "Read the Docs Community" account on Read the Docs at https://about.readthedocs.com. You can click **Sign up** to get started, and we recommend that you use the "Sign up with GitHub" option on the sign up page.

Copying and deploying the course
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Create your copy of the course materials in GitHub by visiting the `Geo-Python course GitHub repository <https://github.com/geo-python/site>`__ and clicking on the **Fork** button on the top right side of the page. It is fine to leave the "Copy the master branch only" option ticked. This will make a copy of the course materials for your GitHub account, but keep the connection to the original course repository.

#. Sign in to Read the Docs at https://about.readthedocs.com and then click **Import a Project**. You may need to click the refresh button to get a list of available projects, but you should then see "yourusername/site" in the list (where "yourusername" is your GitHub username), which you can select by clicking on the **+** button.

   * You can edit the **Name**, but otherwise leave the project details as they are and click **Next**.
   
   * We already have a ``.readthedocs.yaml`` configuration file in the repository, so you can click **Finish** on the next screen.
   
#. After importing, click on **Build version** to build and deploy the course website. This will take a few minutes.

#. Once the page builds and is deployed, you can view the course online by clicking the **View Docs** button on the top right of the Read the Docs page.

Making changes to the materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this point your page should be online and to make changes to the materials, simply visit your GitHub repository with the forked course materials and edit the materials on GitHub.com or locally on your computer if you have cloned them.
You will find all of the website content in the ``source`` directory of the Geo-Python course repository.

Every time you push changes to the course materials to your forked copy the website will automatically rebuild and be updated online within a few minutes.
We hope this will be helpful in getting your version of the course up and running smoothly!