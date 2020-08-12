.. index:: numpy, maths, array

``numpy`` -- numerical routines for python
==========================================

For numerical calculation, based on notion of arrays (which include matrices). The ``array`` object has several key attributes, including:

- ``array.shape`` attribute, which reflects the dimensions of the array. This can be derived from the input data.
- ``array.dtype`` attribute, which specifies the data type. This can also be determined by the input data, or by using the ``dtype`` argument.

.. jupyter-execute::
    :linenos:

    import numpy

    data = numpy.array([0, 1, 2, 3], dtype=int)
    data

.. jupyter-execute::
    :linenos:

    data.shape

.. jupyter-execute::
    :linenos:

    data.dtype

Once created, you cannot extend an array, i.e. it's total number of elements is immutable. However, the array "shape" can be changed and the value at individual coordinate can be changed.

.. jupyter-execute::
    :linenos:

    data.resize((2, 2))
    data

.. jupyter-execute::
    :linenos:

    data[0][0] = 42
    data

Conversion to standard python data types
----------------------------------------

.. jupyter-execute::
    :linenos:

    raw = data.tolist()
    raw

.. index::
    pair: matrix; numpy

Specifying matrices
-------------------

These can be specified on construction. ``array``'s can be constructed from normal python data types.

.. jupyter-execute::
    :linenos:

    data = numpy.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    data, data.shape

Or, other arrays [1]_. 

.. [1] I've used the ``numpy.arange()`` function, which returns an ``array`` object.

.. jupyter-execute::
    :linenos:

    a = numpy.arange(4)
    a

.. jupyter-execute::
    :linenos:

    b = numpy.arange(4, 8)
    b

.. jupyter-execute::
    :linenos:

    # from the above numpy arrays
    m = numpy.array([a, b])
    m

.. index:: scalar

Scalar operations on arrays
---------------------------

A major convenience for arrays is the ability to express element-wise operations as a single statement, instead of having to use a ``for`` loop.

Here's an element-wise addition using a standard for loop on the ``raw`` nested list data structure.

The laborious (and slow) way
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::
    :linenos:

    for i in range(len(raw)):
        for j in range(len(raw[i])):
            raw[i][j] += 20
    raw

And here it is on the numpy array equivalent.

.. jupyter-execute::
    :linenos:

    data += 20
    data

Standard mathematical operations on arrays
------------------------------------------

If two or more arrays have the same shape, then element-wise operations between corresponding elements is also very simply expressed.

.. jupyter-execute::
    :linenos:

    print("Before:", a, b)
    c = a * b
    print("After:", c)

If they do not have the same shape, an exception is raised.

.. jupyter-execute::
    :linenos:
    :raises:

    d = numpy.arange(5)
    a * d

Array iteration
---------------

.. jupyter-execute::
    :linenos:

    for e in data:
        print(e)

.. index::
    pair: indexing; numpy
    pair: slicing; numpy

indexing and slicing
--------------------

We can select an individual element using the standard looking slice notation.

.. jupyter-execute::
    :linenos:

    data[0][1]

or using the numpy extended slicing notation, which allows combining the slice notation into one set of ``[]``.

.. jupyter-execute::
    :linenos:

    data[0, 1]

The slicing capabilities of arrays is rich and very useful! We can slice a matrix for a single column across all rows

.. jupyter-execute::
    :linenos:

    data[:, 1]  # the [1] column

or a single row across all columns. In both cases the `:` represents the complete set.

.. jupyter-execute::
    :linenos:

    data[1, :]  # the [1] row

Array assignment
----------------

.. jupyter-execute::
    :linenos:

    data[1, 2] = -99
    data

.. index::
    pair: evaluation; numpy

Evaluation operations
---------------------

.. jupyter-execute::
    :linenos:

    indices = data < 0
    indices

You can use the resulting ``bool`` array to slice, and for assignment.

.. jupyter-execute::
    :linenos:

    data[indices] = 1000
    data

.. jupyter-execute::
    :linenos:

    data[data > 100] = 999
    data

.. index::
    pair: axis; numpy

The numpy array axis
--------------------

This is akin to specifying whether a method / function operates on rows (``axis=0``) or columns (``axis=1``).

.. jupyter-execute::
    :linenos:

    data.sum(axis=0)

.. index::
    pair: mean; numpy
    pair: standard deviation; numpy


Getting useful quantities
-------------------------

.. jupyter-execute::
    :linenos:

    # Overall mean, all elements
    data.mean()

.. jupyter-execute::
    :linenos:

    # Unbiased estimate of standard deviation, all elements
    data.std(ddof=1)

.. jupyter-execute::
    :linenos:

    # Column means, operating on rows
    data.mean(axis=0)

.. jupyter-execute::
    :linenos:

    # Row means, operating on columns
    data.mean(axis=1)

.. index::
    pair: matrix multiply; numpy

Linear algebra -- matrix multiplication
---------------------------------------

.. jupyter-execute::
    :linenos:

    data1 = numpy.array([0, 1, 2, 3])
    data2 = numpy.array([4, 5, 6, 7])

    ip = numpy.inner(data1, data2)
    ip

.. index::
    pair: conditionals; numpy
    pair: any; numpy
    pair: all; numpy

Conditionals on arrays
----------------------

Conditional operations on ``numpy`` arrays are important. We illustrate the utility of these operations with some simple examples.

.. jupyter-execute::
    :linenos:

    data = numpy.array([[1, 2, 1, 9], [9, 1, 1, 3]])
    matched = data > 3
    matched

The above expression is evaluated element wise and returns a numpy array of type ``bool``.

.. index:: method chaining

.. code:: python
    
    # conditionals using arrays

    if (data > 100).any():
        print("Yes")
    else:
        print("No")

    # conditionals using arrays

    if 1000 in data:
        print("Yes")
    else:
        print("No")
    
    # conditionals using arrays

    if (data == 1000).all():
        print("Yes")
    else:
        print("No")

.. index::
    pair: logical operations; numpy
    pair: array comparisons; numpy

Comparisons of multiple arrays
------------------------------

- `numpy` provides tools for element-wise comparisons
- this is more complicated than just using the standard python syntax

.. jupyter-execute::
    :linenos:
    :raises:

    x = numpy.array([True, False, False, True], dtype=bool)
    y = numpy.array([False, False, False, True], dtype=bool)
    x or y

.. jupyter-execute::
    :linenos:

    numpy.logical_or(x, y)

.. jupyter-execute::
    :linenos:

    numpy.logical_and(x, y)

.. index::
    pair: count; numpy

Using the result of array comparisons to count
----------------------------------------------

Scenario, you want to count (from multiple arrays that consist of a continuously distributed random variable) the number of times a specific threshold is reached for each "position" on a reference coordinate system.

.. jupyter-execute::
    :linenos:

    data = [
        numpy.array([0.923, 0.022, 0.360, 0.970, 0.585]),
        numpy.array([0.480, 0.282, 0.055, 0.873, 0.960]),
    ]

    # create an array that will be used to count how often
    # a certain threshold is met
    counts = numpy.zeros((5,), dtype=int)
    counts

.. jupyter-execute::
    :linenos:

    print(data[0] > 0.5)
    for da in data:
        counts[da > 0.5] += 1

    counts

.. jupyter-execute::
    :linenos:

    data = numpy.array(data)

    (data > 0.5).sum(axis=0)

Exercises
=========

**1.** ``bool`` data types can be summed. Create an array with ``dtype=bool`` and try it.