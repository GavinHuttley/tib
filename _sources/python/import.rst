.. index:: import, modules

.. _import_module:

Extending capabilities using ``import``
=======================================

In Python, the capabilities of the core name space is relatively stripped down. Much of the power of the language comes from the availability of modules. For instance, the ``math`` module is part of what is referred to as the Python *standard library*, i.e. it comes standard with all Python installations. How we gain access to these is through the ``import`` statement. ``math`` contains many basic mathematical operations, e.g. ``log()`` or ``sqrt()``, as functions. We get access to those using the ``.`` notation.

.. jupyter-execute::

    import math

    math.sqrt(4)

Modules have their own type.

.. index::
    pair: module; types

.. jupyter-execute::

    type(math)

Just like standard Python objects, you can see what capabilities a module has using ``dir()`` [1]_ and ``help()`` works too.

.. margin::
  
    .. [1] The ``dir()`` command returns a list. I'm truncating that to just display a small listing of what's in ``math``.

.. jupyter-execute::

    dir(math)[:10]

.. jupyter-execute::

    math.log10(10)

.. jupyter-execute::

    math.log(10)

You can also import a specific module function using the keyword ``from``

.. jupyter-execute::

    from math import sqrt
    
    sqrt(4)

or multiple functions by separating them with a ``,``.

.. index::
    pair: log2; maths

.. jupyter-execute::

    from math import sqrt, log2
    
    log2(4)

Modules also serve to allow simplification of code. This enable putting logically related functions into a single file. They facilitate reuse of those functions in different programs, thus reducing redundancy and increasing the robustness of software.

Modules can be organised hierarchically, meaning that some modules are nested within others. How Python achieves this is actually dead simple, the name of a directory containing some Python scripts becomes the import name [2]_. For instance, the Python standard library includes (among a multitude of goodies) the ``os`` module which is used for handling operating system related calls. Inside this module is another one called ``path`` that contain useful functions, among which is the ``dirname()`` function. Using ``.`` notation, we full specify that function as ``os.path.dirname``.

.. jupyter-execute::

    import os
    
    os.path.dirname("data/nested_dir/somefile.txt")

We can also import just that function

.. jupyter-execute::

    from os.path import dirname
    
    dirname("data/nested_dir/somefile.txt")

You can renamed imported modules using the :index:`as` keyword.

.. jupyter-execute::

    from math import sqrt as msqrt
    
    msqrt(16)

.. margin::
  
    .. [2] Since Python version 3.3, having a python file ``bar.py`` inside a directory ``foo`` means you can use the `from foo import bar` statement. Prior to version 3.3, it was necessary to have a special file ``__init__.py`` inside ``foo``.

"third party" libraries
-----------------------

.. index:: 3rd party libraries, third party libraries

An even greater appeal of Python is the availability of highly sophisticated modules written by others.

Of particular note is numpy_ (numerical Python). This library is arguably the main reason Python is so popular in science. Numpy provides critical routines in numerical mathematics, particularly linear algebra. But it's very broadly useful, being ~10x faster than straight Python implementations. It also allows succinct expressions for arrays and provides very useful methods on arrays.

Other invaluable libraries for science are Scipy, Pandas, Matplotlib, IPython and biology specific libraries (such as cogent3_).

We will cover ``numpy`` in a separate section.

Why use libraries written by others?
------------------------------------

- Widely scrutinised, so less chance of code errors
- Typically better performance
- May provide algorithms that are simply too difficult to write yourself!

There are an increasing number of Biology specific libraries. My own lab produces a number of open sourced library for genomic biology (e.g. cogent3_, which we will use later in the course).

Writing your own modules
------------------------

Since a Python script is a module, then all you have to do is write your code in a python script. If that script is on what is called the *python path*, then it can be imported and any functions within can be used.

The python path refers to the places on your computer that Python will look for modules. The first is the directory from which the Python executable was started. The second is the "installed packages" location, typically a directory called ``site-packages`` which is "within" Python itself. The third is a custom location which you have to tell Python about, for instance using a special `PYTHONPATH <https://docs.python.org/3/using/cmdline.html?highlight=pythonpath#envvar-PYTHONPATH>`_ environment variable.
