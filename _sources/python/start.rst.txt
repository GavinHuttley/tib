.. sidebar:: Executing Python using a REPL
    :name: REPL

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

But seriously, I strongly recommend using an IDE [2]_ as these incorporate tools to facilitate debugging, a very useful capability (you can see a demo of this in :ref:`debugging`). (See :ref:`setup` for installing one on your computer.)

Writing scripts has two steps for running the program (illustrated in the executing python from a text file video): (1) write the script, (2) running the script in a terminal.

Code and output in these notes is from Jupyter
==============================================

The blocks of computer code, and associated output, displayed in these notes are derived from running the code in a Jupyter notebook. Running the same code in the standard python interpreter inside a terminal will generate different looking output. The difference is most obvious on what is called the representation (or ``repr()``) of an object. In Jupyter, the output can be "styled" (e.g. bold font, coloured tables) whereas in a conventional interpreter the output will appear as plain text (see :ref:`Demonstration of using Jupyter<REPL>`).

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
    pair: division remainder; maths
    pair: modulo operator; maths
    pair: divmod(); maths
    pair: %; maths

Division remainder
------------------

While integer division (``a // b``) returns how many times ``b`` goes into ``a``, the modulo operation returns the remainder. This is denoted by the ``%`` symbol in Python (and many other languages). In the example, 3 goes into 20 6 times, with 2 remainder. The modulo operation only returns the latter.

.. jupyter-execute::

    20 % 3

The builtin ``divmod()`` returns both parts.

.. jupyter-execute::

    divmod(20, 3)

The remainder is zero when ``b`` is a factor of ``a``, (for example ``20 % 2``). 

.. index::
    pair: exponents; maths
    pair: powers; maths

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

#. Do the hello world example yourself.

#. Order of operations rules. Compute the following expressions

    .. code-block:: python

        (10 + 2) * 2
    
    and

    .. code-block:: python

        10 + 2 * 2

    Hopefully, the conventional rules of mathematics apply!
