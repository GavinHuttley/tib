.. _assignment:

Variables and assignment
========================

Consider the equation :math:`h^2=a^2+b^2`. This mathematical expression is familiar (Pythagoras, of course!) and exactly the sort of thing we'd like to use computers to calculate. But expressing this as an algorithm requires defining variables and breaking the problem into smaller steps. But before we can even do this, we need to define both what a variable is and what is meant by assignment.

In the above equation *h*, *a*, *b* are *pro-numerals*, symbols that represent a numeral (number). In programming, we call these *variables*. We create variables "on the fly" in Python by the process of "assignment" and, in doing so, we need to obey some simple rules.

.. index::
    pair: naming; variable
    pair: variable; syntax

Naming variables
----------------

.. note:: Allowed characters are ``_``, ``0-9``, ``a-z``, ``A-Z``. Variable names MUST not start with a number.

Valid variable names: ``record``, ``Record``, ``record1``, ``_seqs``.

Invalid variable names: ``1a``, ``a record``, ``:funky_name``.

.. note:: ``CaseMatters`` is different to ``casematters``!

Define them before you use them
-------------------------------

Often, this simply means before you use them (i.e. closer to the top of the file). So, we can, for instance do the following:

.. jupyter-execute::

    x = 3
    y = 4
    h = (x ** 2 + y ** 2) ** (1 / 2)
    h

It's noteworthy that this is not a general algorithm -- we have an explicit solution that works for just these values of ``x`` and ``y``. If we want to evaluate different values of these two variables. we have to edit the lines defining the variables ``x`` and ``y`` and rerun the program.

Compare this expression to the original mathematical equation. Clearly, we have rewritten it so we have solved the equation already.

.. index:: assignment, assignment unpacking, unpacking

The assignment statement
------------------------

As illustrated above, an assignment statement is creation of a named reference (the variable) to some data. They are characterised by 3 components:

1. the variable name
2. a **single** ``=``
3. the value (or data)

Assignment unpacking
--------------------

Sometimes, its useful to do multiple variable assignments in one go. Which value maps to which variable? (You can answer that definitively by trying it.)

.. jupyter-execute::

    x, y = 3, 4

Exercises
=========

#. Enter the following. What happens? Why?

    .. code-block:: python

        h = (a ** 2 + b ** 2) ** (1 / 2)
        a = 3
        b = 4
        print(h)

    Fix it!

#. Consider the following two variables

    .. code-block:: python

        a = 4
        b = 6

    Do these assignments on a single line (without using a ``;``).

#. Consider execution of the following

    .. code-block:: python

        a = "2.2"
        a = 2.2

    What type is ``a``?

#. Define a variable using invalid syntax, i.e. your code should generate a ``SyntaxError``.
