Variables and assignment
========================

Consider the equation :math:`h^2=a^2+b^2`. This mathematical expression is familiar (Pythagoras, of course!) and exactly the sort of thing we'd like to use computers to calculate. But expressing this as an algorithm requires defining variables and breaking the problem into smaller steps. But before we can even do this, we need to define what a variable is.

In the above equation *h*, *a*, *b* are *pro-numerals*, symbols that represent a numeral (number). In programming, we call these *variables*. We create variables "on the fly" in Python and, in doing so, we need to obey some simple rules.

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

    a = 3
    b = 4
    h = (a ** 2 + b ** 2) ** (1 / 2)
    h

It's noteworthy that this is not a general algorithm -- we have an explicit solution that works for just these values of ``a`` and ``b``. If we want to evaluate different values of these two variables. we have to edit the lines defining the variables ``a`` and ``b`` and rerun the program.

Compare this expression to the original mathematical equation. Clearly, we have rewritten it so we have solved the equation already.

.. topic:: You Try
    
    Rewrite this so the equation is the first line. What happens? Why?

Assignment unpacking
--------------------

Sometimes, functions return multiple objects. If you know a certain number of objects will be returned then knowing how to do a multiple assignment can be useful.

It can also be applied in other contexts. One particularly useful context is in looping. In the following example, I'm looping over pairs of integers and assigning the results to separate variables. Note the use of the ``","`` in the ``for`` statement.

The tedious way
^^^^^^^^^^^^^^^

.. jupyter-execute::

    # here is a tedious way
    coordinates = [(0, 1), (0, 2), (0, 3)]
    for coord in coordinates:
        x = coord[0]  # grabbing each integer by it's index
        y = coord[1]
        print(x, y)

The succinct way
^^^^^^^^^^^^^^^^

.. jupyter-execute::

    # This is more succinct
    coordinates = [(0, 1), (0, 2), (0, 3)]
    for x, y in coordinates:
        print(x, y)
