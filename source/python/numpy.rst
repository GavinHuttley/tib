.. index::
    pair: install; numpy

.. sidebar:: Installing ``numpy`` on your computer
    :name: numpy_install

    If you want to use ``numpy`` on your own computer you will need to install it. How to do so will depend very much on how you have setup Python. If you are not using ``conda``, then the following is the safest approach.
    
    In the terminal (either macOS terminal, or the one included with `VS Code`_)
    
    .. code-block::
        
        $ python3 -m pip install --user numpy


.. index:: numpy, maths, array

.. _using_numpy:

``numpy`` -- numerical routines for python
==========================================

.. todo:: visual demonstration of numpy http://jalammar.github.io/visual-numpy/

.. todo:: numpy docs https://numpy.org/devdocs/user/absolute_beginners.html

.. todo:: do a screencast on the fundamentals, how you don't need loops

The numpy_ library is the foundation of the vast majority of scientific computing packages that use Python. It is popular because it provides a greatly simplified interface to complicated algorithms that have fast implementations. Conventional wisdom holds that converting a standard Python program to use ``numpy`` will deliver a 10x speedup. In fact, it can be much faster than that. But that's not the focus of this extremely brief summary of ``numpy``. Instead, we introduce you to the major capabilities and usage patterns that ``numpy`` enables. In short, using ``numpy`` objects can often eliminated the need for loops entirely. As a consequence, this greatly simplify the algorithms you have to write. So it's truly worthwhile becoming familiar with this library [#]_.

.. [#] For a visual representation of how operations on arrays work, `see the excellent visual guide by Jay Alammar <http://jalammar.github.io/visual-numpy/>`_.

``numpy`` is designed for numerical calculation and the primary object the library provides is an array. The ``array`` [#]_ object has several key attributes, including:

.. [#] Strictly speaking, ``numpy`` arrays have type ``ndarray`` but they are predominantly created using a top-level ``array`` function.

- ``array.ndim`` attribute, which indicates how many dimensions the array has
- ``array.shape`` attribute, which indicates the number of elements on each dimension.
- ``array.dtype`` attribute, which indicates the numpy data type [#]_. This can also be determined by the input data, or by using the ``dtype`` argument.

.. [#] ``numpy`` extends the range of possible data types, e.g. 8-bit integers, 64-bit floats. `See the numpy docs <https://numpy.org/doc/stable/user/basics.types.html>`_ for more details.

Creating an array from existing data
------------------------------------

.. jupyter-execute::

    import numpy

    data = numpy.array([0, 1, 2, 3], dtype=int)
    data

.. jupyter-execute::

    data.ndim

.. jupyter-execute::

    data.shape

.. jupyter-execute::

    data.dtype

Once created, you cannot extend an array, i.e. it's total number of elements is immutable. However, the array "shape" (and thus dimensions) can be changed and the value at individual coordinates can be changed.

.. jupyter-execute::

    data.resize((2, 2))
    data

.. jupyter-execute::

    data[0][0] = 42
    data

Conversion to standard python data types
----------------------------------------

.. jupyter-execute::

    raw = data.tolist()
    raw

.. index::
    pair: matrix; numpy

Conversion to a different ``dtype``
-----------------------------------

There is a method on arrays for converting an array of one type into an array of a different type. For instance

.. jupyter-execute::

    x = numpy.array(["0.12", "0.33"])
    x.dtype, x

.. jupyter-execute::

    cast = x.astype(float)
    cast.dtype, cast

So ``numpy`` has converted an array of strings into an array of 64-bit precision floats, in one line. Sweet!

Implicit type casting
---------------------

The ``dtype`` of an array instance dictates what assignment operations mean. For example, say we have an integer array

.. jupyter-execute::

    data.dtype, data

If we try to assign a ``float`` to the first element, it will not work because the value is implicitly cast to the ``dtype`` of the instance. In this example, only the integer component of the float 5.92132 is assigned.

.. jupyter-execute::

    data[0, 0] = 5.92132
    data

.. warning:: Implicit type casting is never what you want! Because ``numpy`` does not raise an exception for this case, it is up to the programmer (you) to ensure the array ``dtype`` is appropriate. For this example, if you want to be able to assign floats to ``data`` you should convert it with ``astype(float)``.

Constructing matrices
---------------------

Matrices can be specified on construction by providing, for example, lists of lists. In this example we use a list consisting of two lists, each with 4 elements. This results in a :math:`2\times4` array.

.. jupyter-execute::

    data = numpy.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    data.shape

.. jupyter-execute::

    data

Or, by combining other arrays [1]_.

.. [1] I've used the ``numpy.arange()`` function, which returns an ``array`` object.

.. jupyter-execute::

    a = numpy.arange(4)
    a

.. jupyter-execute::

    b = numpy.arange(4, 8)
    b

.. jupyter-execute::

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

    for i in range(len(raw)):
        for j in range(len(raw[i])):
            raw[i][j] += 20
    raw

The simple and fast ``numpy`` way
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    data += 20
    data

Nice!

Standard mathematical operations on arrays
------------------------------------------

If two or more arrays have the same shape, then element-wise operations between corresponding elements is also very simply expressed.

.. jupyter-execute::

    print("Before:", a, b, sep="\n")
    c = a * b
    print("After:", c, sep="\n")

If they do not have a compatible shape, a ``ValueError`` exception is raised and the text indicates "... operands could not be :index:`broadcast <pair: broadcast; numpy>` together with shapes...".

.. jupyter-execute::
    :raises:

    d = numpy.arange(5)
    a * d

Array iteration
---------------

Behaves the same as iterating over a standard Python list (or tuple) with the same dimensions. This corresponds to :ref:`iterating over axis=0 <numpy_axes>`.

.. jupyter-execute::

    for e in data:
        print(e)

.. index::
    pair: indexing; numpy
    pair: slicing; numpy

Indexing and slicing
--------------------

In the following, we are working on this array.

.. jupyter-execute::
    :hide-code:

    data

We can select an individual element using the standard looking slice notation.

.. jupyter-execute::

    data[0][1]

Note that each dimension requires successive ``[]`` pairs. The ``numpy`` extended slicing notation allows using one set of ``[]``.

.. jupyter-execute::

    data[0, 1]

The slicing capabilities of arrays is rich and very useful! We can slice a matrix for a single column across all rows

.. jupyter-execute::

    data[:, 1] # the [1] column

or a single row across all columns. In both cases the ``:`` represents the complete set.

.. jupyter-execute::

    data[1, :] # the [1] row

.. index::
    pair: broadcasting; numpy

Ensuring array shapes are compatible for mathematical operations
----------------------------------------------------------------

There are rules that ``numpy`` uses to determine how arrays are broadcast together. The best resource to understanding this is `the official documentation on broadcasting <https://numpy.org/doc/stable/user/basics.broadcasting.html>`_. That said, here's a very condensed explanation.

When the array shapes are not the same, ``numpy`` compares the shapes element wise **from right to left**. The dimensions of two arrays are considered compatible when they are same or one of them is 1. Consider the arrays ``x`` and ``y``

.. jupyter-execute::

    x = numpy.array([[0, 1], [2, 3], [4, 5], [6, 7]])
    x

.. jupyter-execute::
    
    x.shape

.. jupyter-execute::

    y = numpy.array([1, 5, 9, 13])
    y
    
.. jupyter-execute::
    
    y.shape

Applying the broadcast rule, these are incompatible.

.. jupyter-execute::
    :linenos:
    :raises:

    x * y

This is because, the first value read from the right of ``x.shape`` is 2 and from the right of ``y.shape`` is 4.

For our example, one solution that ensures the result of the ``*`` operation has the same shape as ``x`` is to add a "new axis" to ``y``. This can be done via a combination of slicing and using ``numpy.newaxis``

.. index::
    pair: newaxis; numpy

.. jupyter-execute::

    x * y[:, numpy.newaxis]

or, equivalently, by explicitly reshaping ``y``.

.. jupyter-execute::

    x * y.reshape((4,1))

We could also solve this using the :index:`transpose <pair: transpose; numpy>` ``x`` (which flips the matrix, reversing it's dimensions)

.. jupyter-execute::

    x.T * y

but this has the effect of meaning the result is also transposed with respect to the original orientation, which is typically inconvenient.

.. index::
    pair: assignment; numpy

Array assignment
----------------

Consider the following data.

.. jupyter-execute::

    a = numpy.array([[38, 28, 93], [96, 95, 70]])
    l = a.tolist()

Assignment to individual elements of an array is more flexible than the comparable standard python objects. For instance, to assign ``0`` to all values of ``a`` is simply

.. jupyter-execute::

    a[:] = 0
    a

Trying that on a list, however, raises an exception.

.. jupyter-execute::
    :linenos:
    :raises:

    l[:] = 0

As the exception indicates, looping is required.

We can assign to an individual element using the ``numpy`` notation.

.. jupyter-execute::

    data[1, 2] = -99
    data

.. index::
    pair: evaluation; numpy
    pair: bool array; numpy

Evaluation operations
---------------------

Using standard python evaluation operations on ``numpy`` arrays returns element wise ``bool`` arrays. We show uses for these below.

.. jupyter-execute::

    indices = data < 0
    indices

.. index::
    pair: bool array; numpy
    pair: advanced indexing; numpy
    pair: boolean indexing; numpy
    pair: integer indexing; numpy

Advanced indexing
-----------------

There are two types of advanced indexing, boolean and integer.

Boolean indexing
^^^^^^^^^^^^^^^^

This applies when the object being used to slice the array is of type ``bool``. These typically result from some array comparison operation.

.. jupyter-execute::

    m = numpy.array([[1, 2], [-3, 4], [5, -6]])
    m

Let's identify all elements that are :math:`<0`.

.. jupyter-execute::

    negative = m < 0
    negative

The result is an array with boolean elements indicating whether the corresponding value in ``m`` satisfied (indicated by ``True``) or not (indicated by ``False``) the condition (:math:`<0`). We can use bool arrays to slice the others with the same shape.

.. jupyter-execute::

    m[negative]

As this shows, using a ``bool`` array for indexing on the original returns just those elements as a flat array. If you want your operation to generate a result with the same shape you need to "index in place". For instance, you can use the index to restrict specific operations to just those elements represented by the index such as this assignment statement.

.. jupyter-execute::

    m[negative] = 0
    m

Integer indexing
^^^^^^^^^^^^^^^^

This involves as many series of integers as there are dimensions to the array (e.g. 2 in the case of ``m``).

Before we start using actual integer series, I'll start by using conventional indexing to get the value of a single item. Specifically, I select row ``1``, column ``1``.

.. jupyter-execute::

    row_index = 1
    col_index = 1
    m[row_index, col_index]

We now enclose those indices in lists, such that each successive value corresponds to another row, another column. As such these sequential arrays correspond to array coordinates and thus must have the same dimension (length in our example below).

.. jupyter-execute::

    row_indices = [1, 2, 0]
    col_indices = [1, 0, 1]
    m[row_indices, col_indices]

This corresponds to the following array coordinates: (1, 1), (2, 0), (0, 1). Thus, the returned value from advanced indexing is an array with same length as the indexing array length (3 in our case).

.. index::
    pair: axis; numpy

The ``numpy`` array axis
------------------------

.. sidebar:: Numpy arrays and their axis.
    :name: numpy_axes
    
    .. figure:: /_static/images/numpy-axes.png
        :scale: 20%
        
    An array with ``shape=(3,2)``, ``ndim=2``. Elements and their array indices are shown as e\ :math:`_{i,j}`. Many array methods have an ``axis`` argument that applies to arrays with ``ndim>1``. In the illustrated example, setting ``axis=0`` would apply that method along the corresponding axis and generate a result with 2 elements. Setting ``axis=1`` would generate a result with 3 elements.

:ref:`As illustrated <numpy_axes>`, the ``axis`` argument specifies whether a method / function operates on rows or columns [2]_.

.. [2] You can many more than 2-dimensions with arrays. More dimension means you have more axes and thus larger values of ``axis`` may be required.

Working on this array.

.. jupyter-execute::
    :hide-code:

    data

.. jupyter-execute::

    data.sum(axis=0)

.. index::
    pair: mean; numpy
    pair: standard deviation; numpy

Getting useful statistical quantities
-------------------------------------

.. jupyter-execute::

    # Overall mean, all elements
    data.mean()

.. jupyter-execute::

    # Unbiased estimate of standard deviation, all elements
    data.std(ddof=1)

.. jupyter-execute::

    # Column means, operating on rows
    data.mean(axis=0)

.. jupyter-execute::

    # Row means, operating on columns
    data.mean(axis=1)

.. index::
    pair: matrix multiply; numpy

.. index::
    pair: matrix multiplication; numpy

Linear algebra -- matrix multiplication
---------------------------------------

`Matrix multiplication <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ is a fundamental operation in linear algebra and is central to many statistical procedures (e.g. fitting linear models, taking the exponential of a matrix, likelihood of a phylogeny).

.. jupyter-execute::

    data1 = numpy.array([0, 1, 2, 3])
    data2 = numpy.array([4, 5, 6, 7])

    ip = numpy.inner(data1, data2)
    ip

The ``@`` symbol also serves as a special operator for matrix multiplication.

.. index::
    pair: @; operators

.. jupyter-execute::

    data1 @ data2

.. index::
    pair: conditionals; numpy
    pair: any; numpy
    pair: all; numpy

Conditionals on arrays
----------------------

Conditional operations on ``numpy`` arrays are important. We illustrate the utility of these operations with some simple examples.

.. jupyter-execute::

    data = numpy.array([[1, 2, 1, 9], [9, 1, 1, 3]])
    matched = data > 3
    matched

The above expression is evaluated element wise and returns a ``numpy`` array of type ``bool``.

We use the standard Python ``in`` operator.

.. jupyter-execute::

    if 3 in data:
        print("Yes")
    else:
        print("No")

We apply a conditional to an array and use the ``any()`` method, which will return ``True`` if any single element satisfied this condition.

.. index:: method chaining

.. jupyter-execute::

    if (data > 3).any():
        print("Yes")
    else:
        print("No")

Using the ``all()`` method, which will return ``True`` only if **all** elements satisfied the condition.

.. jupyter-execute::

    if (data > 3).all():
        print("Yes")
    else:
        print("No")

.. index::
    pair: logical operations; numpy
    pair: array comparisons; numpy

Comparisons of multiple arrays
------------------------------

``numpy`` provides tools for element-wise comparisons. This is more complicated than just using the standard python syntax.

.. jupyter-execute::

    x = numpy.array([True, False, False, True], dtype=bool)
    y = numpy.array([False, False, False, True], dtype=bool)

Applying equivalence operators to arrays can result in exceptions because the result is ambiguous.

.. jupyter-execute::
    :raises:

    x or y

Instead, you should use special functions which will operate element wise. Here's a couple of examples.

.. jupyter-execute::

    numpy.logical_or(x, y)

.. jupyter-execute::

    numpy.logical_and(x, y)

.. index::
    pair: count; numpy

Using the result of array comparisons to count
----------------------------------------------

Scenario, you want to count (from multiple arrays that consist of a continuously distributed random variable) the number of times a specific threshold is reached for each "position" on a reference coordinate system.

.. jupyter-execute::

    data = [
        numpy.array([0.923, 0.022, 0.360, 0.970, 0.585]),
        numpy.array([0.480, 0.282, 0.055, 0.873, 0.960]),
    ]

    # create an array that will be used to count how often
    # a certain threshold is met
    counts = numpy.zeros((5,), dtype=int)
    counts

.. jupyter-execute::

    print(data[0] > 0.5)
    for da in data:
        counts[da > 0.5] += 1

    counts

.. jupyter-execute::

    data = numpy.array(data)

    (data > 0.5).sum(axis=0)

Exercises
=========

#. Create a list of 10 positive integers and convert it into a ``numpy`` array. Use ``array`` methods to compute the total. Divide the original array by the total to produce a normalised array, which you assign to a variable ``freqs``. Using ``numpy`` logical operations to show that all elements are between 0 and 1. Use array methods to show the array sum is 1.

#. Many methods on ``numpy`` arrays have an ``axis`` argument, one of which is ``sum()``. Construct a 2-dimensional (2D) array that has the same number of rows and columns, e.g.

    .. code-block:: text

        [[0, 0],
         [0, 0]]

    is a 2D array. Assign values that make it easy to distinguish operations that operate across rows versus those which operate across columns [#]_. Demonstrate this matrix serves that purpose using ``sum()``.

#. ``bool`` data types can be summed. Create a sample array with ``dtype=bool`` and show that the sum of this array equals the number of occurrences of ``True``.

#. Look at the array ``data`` and identify the array coordinates where the values equal 9. Now use advanced array indexing to extract those coordinates in a single line statement.

    .. jupyter-execute::

        data = numpy.array([[1, 9, 0, 3, 9],
                            [9, 2, 8, 2, 1],
                            [3, 1, 9, 9, 5]])

    The result should be

    .. jupyter-execute::
        :hide-code:

        data[data == 9]

#. Same as the previous question except in a single line statement extract the values ≠9. The result should be

    .. jupyter-execute::
        :hide-code:

        data[data != 9]

#. Use boolean array indexing to assign -3 to all values of ``data`` less than 2. The result should be

    .. jupyter-execute::
        :hide-code:

        numpy.array([[-3, 9, -3, 3, 9],
                     [9, 2, 8, 2, -3],
                     [3, -3, 9, 9, 5]])

#. For the following boolean array ``indices``, what is the result of ``~indices``?

    .. jupyter-execute::

        indices = numpy.array([1, 1, 0, 1], dtype=bool)


#. Convert the following code into using ``numpy`` -- without ``for`` loops. After converting ``counts`` to a ``numpy`` array, my solution is 3 lines long.

    .. jupyter-execute::

        from math import log10
    
        counts = [[-4, 3, 4, -3, 4],
                  [4, -1, -2, -3, 4],
                  [-4, -1, 2, 0, 3],
                  [2, -2, -2, -4, -5]]
        result = []
        for i in range(4):
            row = []
            for j in range(4):
                val = counts[i][j]
                val = 0 if val <= 0 else log10(val)
                row.append(val)
            result.append(row)
        
        result
    
    The expected result from conversion is
    
    .. jupyter-execute::
        :hide-code:

        c = numpy.array(counts, dtype=float)
        indices = c > 0
        c[indices] = numpy.log10(c[indices])
        c[~indices] = 0
        c
    

#. What happens when you slice the following 1D array using ``newaxis`` on the first axis, or the second axis

    .. jupyter-execute::
    
        x = numpy.array([1, 9, 0, 3, 9])

#. Comparing performance of pure Python and ``numpy`` implementations. Investigate usage of ``numpy.where()`` to obtain the row and column coordinates of a 2D array where the value equals ``1`` (that's a one). Write a function called ``np_where()`` that takes a matrix as an argument and returns the row coordinates and column coordinates.

    First, use the following code to generate a random square matrix.

    .. jupyter-execute::

        from numpy.random import randint
    
        dim = 5
        mat = randint(0, 2, size=dim * dim)
        mat.resize(dim, dim)
        mat

    Compare ``np_where()`` to the performance of a function implemented using only pure python called ``py_where()`` that takes the matrix as an argument and returns the ``<row coordinates>, <column coordinates>`` as lists. For ``mat``, it should return the following.

    .. jupyter-execute::
        :hide-code:

        def py_where(matrix):
            row_coords, col_coords = [], []
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    if matrix[i][j] == 1:
                        row_coords.append(i)
                        col_coords.append(j)
            return row_coords, col_coords
    
        coords = py_where(mat)
        print(coords)

    Use the "magic" ``%timeit`` command builtin to Jupyter to assess performance of each function on the same value of ``mat``.

    .. jupyter-execute::

        %timeit py_where(mat)

    Then try setting ``dim=20`` and repeat. Which is faster, and by how much?

#. Do some googling for testing ``numpy`` arrays using ``assert_allclose``. Then use this to check your array ``freqs`` created above sums to 1.

.. [#] You want the sum of rows to be different to the sum of columns, that way you know when you have used ``axis`` correctly.