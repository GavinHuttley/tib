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
---------

**1.**

Do the hello world example yourself.

**2.**

Compute the square root of ``16``. What ``type`` is ``16``? What ``type`` is the result?

**3.**

Order of operations rules. Compute the following expressions

.. code-block:: python

    (10 + 2) * 2
    
and

.. code-block:: python

    10 + 2 * 2

