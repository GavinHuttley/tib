*********
Resources
*********

.. todo:: Find some youtube channels and other learning python resources

Reading
=======

Here's an awesome |text_book|_, you can get it for free as a pdf, browse the web version or buy a hard copy. Be sure and read the preface about the history of this book!

.. _setup:

Setting up your own computer
============================

I encourage you to download `VS Code`_ [*]_, a free programmers text editor [1]_ that has a sophisticated debugger. Debuggers are extremely useful for understanding program flow and fixing errors. Before you can use it you need to install Python3.10 on your computer (see below).

.. [*] In past years I have recommended installation of `WingIDE <https://wingware.com>`_. While I personally still use this application a lot, its usage is not as widespread as that of VS Code and there are less resources available for it. Plus Microsoft is putting massive resources into making VS Code a top notch integrated development environment for Python and its feature set improves with every release.

.. [1] This is provided by Microsoft and is available for all operating systems.

Once you have installed Python 3.10, open VS Code. Open the Extensions section and type in ``Python``. Select the Python package distributed by Microsoft and click on the install button. That extension provides a bunch of super useful tools including the aforementioned debugger.

Install Python3.10 on macOS
--------------------------

There are multiple ways to install Python on a mac, what I'm recommending will allow you to remove this installation of Python easily after the course has finished (if you should want to do that).

**Step 1** -- open the Terminal.app.

You can use Spotlight (typically invoked using command+<space bar>) to find it, or navigate to ``/Applications/Utilities/Terminal.app``. Once it's open, click anywhere in the Terminal window and you should see your cursor as a grey box following a "prompt" character [2]_. Enter the following text and press the return key::

    xcode-select --install

and follow the prompts [3]_.

.. [2] Typically this is a single ``$`` or ``>`` character.
.. [3] It will ask for your password and install some essential command line tools.

**Step 2** -- Install `Homebrew <https://brew.sh>`_

Homebrew is a "package manager", a command line tool to make installing other command line tools easy. Follow the install instructions. When completed, enter the following text and press the return key::

    brew install python@3.10

When that is completed, you have Python 3.10 installed.

Install Python3.10 on Windows
----------------------------

See the `information here <https://docs.python.org/3/using/windows.html#windows-store>`_.

Adding support for Jupyter notebooks
------------------------------------

As we use these heavily in the course, having the capacity to create and run them on your own machine may prove useful. I'm assuming you have already successfully installed Python, VS Code and the Python extension. Open the command palette (View > Command Palette, or ⌘+⇧+p on macOS, ⌃+⇧+p on Windows?), type "Jupyter" and select "Jupyter: Create New Blank Notebook" from the list of options. This should lead to a prompt to install ``ipykernel``. Follow the prompts to allow installation. (This may require entering your user password to authorise installation.) After this completes the ``print("hello world")`` example should execute in the notebook.

Podcasts
========

These are not explicitly aimed at beginners, but podcasts that I find informative on multiple levels and quite polished. |python_bytes|_, is a weekly 30' podcast with an overview of interesting Python things. |test_n_code|_ is a longer format that covers all things related to testing code -- a critical topic for scientists. |talkpython|_ is a longer format interview of various individuals doing interesting things. Data science is increasingly covered by these podcasts.

Do you know any more?
=====================

If you know of any more useful resources, please click the "Edit on GitHub" link above, add them to the appropriate section and make a pull request. For more information on this, read the :ref:`contribute` section to learn how to become a contributor.
