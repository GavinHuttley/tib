.. _intro_to_version_control:

###############################
Introduction to version control
###############################

.. sectionauthor:: Gavin Huttley

"Version control" refers to software tools that are designed to efficiently keep track of changes to your plain text files. As the phrase implies, the support relates to recording different versions of files. Here, the word version is not limited to a release version [#]_.

.. [#] For example, the *version* of your operating system is a release version.

While used predominantly for programming [#]_, they can be applied to any application that uses plain text files [#]_. Familiarity with version control is thus crucial for bioinformaticians. Here's just a short list of some advantages from using it:

- makes it easier to experiment with different solutions to a problem
- makes it easier to collaborate with other people
- makes moving your code between computers easier
- makes it easier to ensure the reproducibility of your work

.. [#] Plain text files are the medium for recording programs in nearly all programming languages.
.. [#] For example, many data files from genomics are plain text files.

As a budding professional computational scientist, writing code is your core business so anything that makes that job easier is a good thing!

In this topic I provide a functional introduction [#]_ to the version control tool :index:`git <pair: git; version control>`. ``git`` is a sophisticated (and very complex) command line tool with extensive capabilities. It is not the only such tool available [#]_. You will become familiar with using it in a terminal. Note that some IDE's expose a sophisticated graphical user interface to using ``git`` that make using it much easier.

.. [#] Only the bare minimum necessary to use basic capabilities of git.
.. [#] I personally use mercurial, but ``git`` is way more popular.

.. how to revert a change (see https://github.com/sympy/sympy/wiki/Git-hg-rosetta-stone)

Getting set up
==============

These instructions are focussed on having a repository (see :ref:`version_glossary` for definitions) that is hosted at GitHub and for which there will be a clone on a computer that you will use for writing your code. If you don't already have one, sign up for a GitHub_ account.

You also need ``git`` installed on the machine where you will be writing / running the code [#]_.

.. [#] If you are doing my course, ``git`` has already been installed on the class server.

On your developer machine you need to inform ``git`` what your user name and email address are. These details are used to "sign" every commit you make. This is your attribution and informs others who made what changes. On your developer machine, in the terminal

.. code-block:: bash
    
    $ git config --global user.name "Your Name"
    $ git config --global user.email "YourEmail@example.com"

I also strongly recommend to change the log message editor from the default (``vim``) to ``nano`` [#]_.

.. [#] Which reminds me of a joke -- "How do you generate a random string? Put a first year Computer Science student in ``vim`` and ask them to save and exit."

.. code-block:: bash
    
    $ git config --global core.editor nano

A demo project
==============

Create a demo project on GitHub
-------------------------------

Once your account is setup, create a new repository. For the purpose of demonstration, I'm going to assume you name it ``demo``.

.. sidebar:: Creating a new repository

    .. figure:: /_static/images/version_control/github-create-repo.png
        :scale: 50%
    
Check the "Add a README file" option. Check the "Add .gitignore" option and select python from the popup. Check the "Choose a license" option and pick whichever one you like.

Cloning the repository to your development computer
---------------------------------------------------

In this case, you will clone onto the machine where you will be developing your code. I assume you have gone through the process of creating an ssh key and followed GitHub's instructions for adding that to your account [#]_.

.. [#] You will make life easier for yourself if you upload a SSH key to your GitHub account. This requires you create a SSH key. See `instructions here <https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_ for doing both of these things.

.. code-block:: bash

    $ git clone git@github.com:YourUserName/YourRepo.git

This creates a directory named ``YourRepo`` on the system.

Add a python file to your repository
------------------------------------

You first need to change into the directory that contains your repository. In the terminal, this is

.. code-block:: bash
    
    $ cd YourRepo

When you list all [#]_ the contents of this directory you will see the ``.git`` directory

.. [#] ``ls -a``, which shows hidden files and folders too.

Now create a python file that contains just a print statement

.. code-block:: bash
    
    $ echo 'print("Hello World")' > demo.py

add it to your repository,

.. code-block:: bash
    
    $ git add demo.py

and commit the change.

.. code-block:: bash
    
    $ git commit -m "Added a demo python script"

Look at the history of your repository
--------------------------------------

.. code-block:: bash
    
    $ git log

Push your change to GitHub
--------------------------

.. code-block:: bash
    
    $ git push

Tips for effective use of version control
-----------------------------------------

Do
^^

- track text files
- commit changes that are logically related
- think of log messages as your lab notebook entries to help you (and others) to understand what you were thinking when changed the files
- write meaningful log messages
- commit often
- push to GitHub often [#]_

.. [#] It's your backup!

Do NOT
^^^^^^

- add really big files to a repository
- add binary files to a repository
- add secrets [#]_ to a repository!
- include a massive number of changes in one commit

.. [#] Any type of information that would allow someone to cause you trouble! For example, passwords, application tokens, account names.

.. _version_glossary:

Glossary of key version control terms
=====================================

:index:`add <pair: add; version control>`
    Adding a file to a your repository.

:index:`clone <pair: clone; version control>`
    An independent copy of a repository. It is not required to be identical to the original.
    
:index:`commit <pair: commit; version control>`
    The act of recording changes to a file by version control software.

:index:`config <pair: config; version config>`
    Configure the version control software.

:index:`conflict <pair: conflict; version control>`
    Where someone else has made a change to a repository affecting the same lines as your change.

:index:`diff <pair: diff; version control>`
    A comparison of contents of two files / directories that shows only the differences.

:index:`.gitignore <pair: .gitignore; version control>`
    A file that contains patterns that match files you **do not** want to be included in the repository.

:index:`log <pair: log; version control>`
    Command to show the history of commits.

:index:`log message <pair: log message; version control>`
    Text that describes the purpose of the changes being committed to a repository.

:index:`manifest <pair: manifest; version control>`
    Listing of files that are being tracked in a repository.

:index:`merge <pair: merge; version control>`
    The step of resolving conflicting repository versions.

:index:`repository <pair: repository; version control>`
    Short for software repository. This is a directory of (typically plain text source code) files pertaining to a project.

:index:`repo <pair: repo; version control>`
    See repository.

:index:`tracked <pair: tracked; version control>`
    Refers to files whose contents are being recorded by version control software.

:index:`pull <pair: pull; version control>`
    Updating a repository by pulling changes from another (possibly on another computer) repository.

:index:`push <pair: push; version control>`
    Pushing changes recorded locally to another (possibly on another computer) repository.

:index:`reset <pair: reset; version control>`
    See revert.

:index:`revert <pair: revert; version control>`
    To remove all changes made to the working copy of a file.

:index:`stage <pair: stage; version control>`
    Staging a file means informing ``git`` that changes to that file are to be included on the next commit step.

:index:`working copy <pair: working copy; version control>`
    The files in a repository that are visible (they are not under the ``.git`` directory).

