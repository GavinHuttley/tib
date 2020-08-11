.. sidebar:: Executing Python using a REPL

    .. index::
        pair: Executing Python using a REPL; screencasts

    .. raw:: html
    
        <video width="50%" height="50%" controls>
          <source src="https://cloudstor.aarnet.edu.au/plus/s/SgZ6vLqa40dje1e/download" type="video/mp4">
          Your browser does not support the video tag.
        </video>


.. sidebar:: Executing Python from a text file

    .. index::
        pair: Executing Python from a text file; screencasts

    .. raw:: html
    
        <video width="50%" height="50%" controls>
          <source src="https://cloudstor.aarnet.edu.au/plus/s/drRX6w0PffFDGyI/download" type="video/mp4">
          Your browser does not support the video tag.
        </video>

Computing environments
======================

There are 2 main ways in which you can write, and execute, Python code. The first involves using a REPL [1]_, which I illustrate in the REPL video. This environment is most useful for experimenting with small pieces of code and, in the case of Jupyter notebooks, for interactive analyses.

The second approach is based on writing Python scripts. A script is just a plain text file. These can be written using any program capable of saving as plain text. However, you're strongly advised to use a "programmers editor". There's a multitude of these, and it's a topic about which programmers are sufficiently opinionated as to create cartoons...

.. [1] Stands for Read Evaluate Print Loop. Python interactive terminals belong to this class, including when using Jupyter.
.. [2] Stands for Integrated Development Environment.

.. raw:: html
    
    <figure style="padding: 4px;">
    <img src="https://imgs.xkcd.com/comics/real_programmers.png" style="height: auto; max-width=75%" alt="Editor Wars">
    <figcaption>From <a href="https://xkcd.com/378/">XKCD</a></figcaption>
    </figure>

But seriously, I strongly recommend using an IDE [2]_ as these incorporate tools to facilitate debugging, a very useful capability (you can see a demo of this in :ref:`debugging`). Writing scripts has two steps for running the program (illustrated in the executing python from a text file video): (1) write the script, (2) running the script in a terminal.

Everyones first program in Python
=================================

.. jupyter-execute::

    print("Hello World!")

Now that we've got that out of the way, let's first treat Python as just a calculator.

Basic arithmetic operations
===========================

.. index::
    pair: plus; maths
    pair: add; maths

Addition
--------

.. jupyter-execute::

    1 + 9

.. index::
    pair: minus; maths
    pair: subtract; maths

Subtraction
-----------

.. jupyter-execute::

    1 - 9

.. index::
    pair: multiply; maths

Multiplication
--------------

.. jupyter-execute::

    2 * 20

.. index::
    pair: divide; maths
    pair: integer divide; maths

Division (including integer division)
-------------------------------------

Standard division uses a single ``/``

.. jupyter-execute::

    20 / 3

Integer division uses ``//``

.. jupyter-execute::

    20 // 3

.. index::
    pair: exponents; maths
    pair: powers; maths

.. todo:: add modulo operator, index with % symbol, maths

Exponents / Powers
------------------

.. jupyter-execute::

    2 ** 4

.. index::
    pair: roots; maths

Roots
-----

.. jupyter-execute::

    4 ** (1 / 2)

The ``math`` module
-------------------

More sophisticated mathematical routines are included in the `math` module. We will discuss modules later.

Exercises
=========

**1.** Do the hello world example yourself.

**2.** Order of operations rules. Compute the following expressions

.. code-block:: python

    (10 + 2) * 2
    
and

.. code-block:: python

    10 + 2 * 2

Hopefully, the conventional rules of mathematics apply!
