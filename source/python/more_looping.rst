.. index::
    pair: nested for loop; loops

More on looping
===============

So far, all the looping has been quite simple -- iterating over a one dimensional series. This means we have used a single ``for`` statement. But it's not uncommon to have (at least) a 2-dimensional array of numbers (for example). How can we iterate over all elements in such a case?

Let's illustrate this problem with a constructed example.

.. jupyter-execute::
    :linenos:

    two_d = [[0, 4, 1, 9, 5],
             [1, 4, 7, 1, 3]]

``two_d`` is a list of lists. It has 2 "rows" and 5 "columns". So rows is the first dimension, columns the second. First let's recap some standard Python operations. First, we will index the first row.

.. jupyter-execute::
    :linenos:

    two_d[0]

The second row, second column.

.. jupyter-execute::
    :linenos:

    two_d[1][1]

.. sidebar:: Differences between cartesian and array coordinates

    It's worth pointing out a significant distinction between :index:`"cartesian coordinates"` and what I'll refer to as :index:`"array coordinates"`. The former is what you know and love from graphing data where coordinates are expressed as :math:`x, y` in that order, where the :math:`x`-value occurs first and represents a position on a horizontal axis -- increasing from left to right. The :math:`y`-value comes second and represents a position on the vertical axis -- increasing from bottom to top. Array coordinates are totally different -- they are expressed as in :math:`row, column` order. The value for column is analogous to the :math:`x` values (representing horizontal position and increases left to right). However, the value for ``row`` occurs first and it represents the vertical position. Row values also increases top to bottom! Hence, the ``two_d[1]`` refers to the second row which is at the bottom. This is exactly same numbering pattern as you see in spreadsheet programs. The distinction matters when you try and accumulate array based points for plotting.

Knowing, in this case, that we have 2 rows and 5 columns we can generate all possible indices with nested for loops combined with the builtin ``range()`` function.

.. jupyter-execute::
    :linenos:

    for i in range(2):
        for j in range(5):
            pass

In the above, for each step through the "outer most loop" (``for i in ...``) we execute the entire "inner most loop". I'll demonstrate this by just adding a print statement.

.. jupyter-execute::
    :linenos:

    for i in range(2):
        for j in range(5):
            print(f"i={i}, j={j}")

These ``for`` loops have only generated series of integers. These are useful, in the context of ``two_d``, in that we can use these to obtain the corresponding values using indexing, like so.

.. jupyter-execute::
    :linenos:

    for i in range(2):
        for j in range(5):
            print(two_d[i][j])

We can also combine these loops with conditional statements so that we can selectively do operations only when we encounter a value that matches some condition. I'll just display the row and column indices when we the value is 4.

.. jupyter-execute::
    :linenos:

    for i in range(2):
        for j in range(5):
            if two_d[i][j] == 4:
                print(f"i={i}, j={j}")

Exercises
=========

**1.** Consider the following two-dimension list

.. code-block:: text
    
    [[0, 4, 1],
     [1, 7]]

The number of "columns" is different between the first and second rows. Write a nested foor loop that prints the row index, column index and the value fof every element in that list.

It should produce output like:

.. code-block:: text
    
    row=0 col=0 val=0
    row=0 col=1 val=4
    ...

**2.** Construct a list of lists that contains different data types, some ints, some floats, some strings. Then using nested iteration, record the row and column coordinates (in separate lists) when the value is a string. For instance, if I used ``[[0, "data", 3.1]]`` and I would produce ``[0], [1]``.
