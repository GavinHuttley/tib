.. index:: numpy, maths, array

.. _using_numpy:

``numpy`` -- numerical routines for python
==========================================

The numpy_ library is the foundation of the vast majority of scientific computing packages that use Python. It is popular because it provides a greatly simplified interface to complicated algorithms that have fast implementations. Conventional wisdom holds that converting a standard Python program to use ``numpy`` will deliver a 10x speedup. In fact, it can be much faster than that. But that's not the focus of this extremely brief summary of ``numpy``. Instead, we introduce you to the major usage patterns that ``numpy`` enables. These patterns greatly simplify the algorithms you have to write. So it's truly worthwhile becoming familiar with this library.

.. _numpy: https://numpy.org

``numpy`` is designed for numerical calculation and the primary object the library provides is an array. The ``array`` object has several key attributes, including:

- ``array.ndim`` attribute, which indicates how many dimensions an array has
- ``array.shape`` attribute, which reflects indicates the number of elements on each. This can be derived from the input data.
- ``array.dtype`` attribute, which specifies the data type. This can also be determined by the input data, or by using the ``dtype`` argument.

.. jupyter-execute::
    :linenos:

    import numpy

    data = numpy.array([0, 1, 2, 3], dtype=int)
    data

.. jupyter-execute::
    :linenos:

    data.ndim

.. jupyter-execute::
    :linenos:

    data.shape

.. jupyter-execute::
    :linenos:

    data.dtype

Once created, you cannot extend an array, i.e. it's total number of elements is immutable. However, the array "shape" (and thus dimensions) can be changed and the value at individual coordinates can be changed.

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

Constructing matrices
---------------------

Matrices can be specified on construction by providing, for example, lists of lists. In this example we use a list consisting of two lists, each with 4 elements. This results in a :math:`2\times4` array.

.. jupyter-execute::
    :linenos:

    data = numpy.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    data.shape

.. jupyter-execute::
    :linenos:

    data

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

Nice!

Standard mathematical operations on arrays
------------------------------------------

If two or more arrays have the same shape, then element-wise operations between corresponding elements is also very simply expressed.

.. jupyter-execute::
    :linenos:

    print("Before:", a, b, sep="\n")
    c = a * b
    print("After:", c, sep="\n")

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

Indexing and slicing
--------------------

In the following, we are working on this array.

.. jupyter-execute::
    :hide-code:

    data

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

or a single row across all columns. In both cases the ``:`` represents the complete set.

.. jupyter-execute::
    :linenos:

    data[1, :]  # the [1] row

.. index::
    pair: advanced indexing; numpy
    pair: bool indexing; numpy

.. index::
    pair: assignment; numpy

Array assignment
----------------

.. jupyter-execute::
    :linenos:

    data[1, 2] = -99
    data

.. index::
    pair: evaluation; numpy

.. index::
    pair: bool array; numpy

Evaluation operations
---------------------

Using standard python evaluation operations on ``numpy`` arrays returns element wise ``bool`` arrays. We show uses for these below.

.. jupyter-execute::
    :linenos:

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
    :linenos:

    m = numpy.array([[1, 2], [-3, 4], [5, -6]])
    m

Let's identify all elements that are :math:`<0`.

.. jupyter-execute::
    :linenos:

    negative = m < 0
    negative

The result is an array with boolean elements indicating whether the corresponding value in ``m`` satisfied (indicated by ``True``) or not (indicated by ``False``) the condition (:math:`<0`). We can use bool arrays to slice the others with the same shape.

.. jupyter-execute::
    :linenos:

    m[negative]

This can be used, for instance, to do specific operations on just those elements such as an assigning a distinct value.

.. jupyter-execute::
    :linenos:

    m[negative] = 0
    m

Integer indexing
^^^^^^^^^^^^^^^^

This involves as many series of integers as there are dimensions to the array (e.g. 2 in the case of ``m``).

Before we start using actual integer series, I'll start by using conventional indexing to get the value of a single item. Specifically, I select row ``1``, column ``1``.

.. jupyter-execute::
    :linenos:

    row_index = 1
    col_index = 1
    m[row_index, col_index]

We now enclose those indices in lists, such that each successive value corresponds to another row, another column. As such these sequential arrays correspond to array coordinates and thus must have the same dimension (length in our example below).

.. jupyter-execute::
    :linenos:

    row_indices = [1, 2, 0]
    col_indices = [1, 0, 1]
    m[row_indices, col_indices]

This corresponds to the following array coordinates: (1, 1), (2, 0), (0, 1). Thus, the returned value from advanced indexing is an array with same length as the indexing array length (3 in our case).

.. index::
    pair: axis; numpy

The numpy array axis
--------------------

This is akin to specifying whether a method / function operates on rows (``axis=0``) or columns (``axis=1``) [2]_.

.. [2] You can many more than 2-dimensions with arrays. More dimension means you have more axes and thus larger values of ``axis`` may be required.

Working on this array.

.. jupyter-execute::
    :hide-code:

    data

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

.. index::
    pair: matrix multiplication; numpy

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

We use the standard Python ``in`` operator.

.. jupyter-execute::
    :linenos:

    if 3 in data:
        print("Yes")
    else:
        print("No")

We apply a conditional to an array and use the ``any()`` method, which will return ``True`` if any single element satisfied this condition.

.. index:: method chaining

.. jupyter-execute::
    :linenos:

    if (data > 3).any():
        print("Yes")
    else:
        print("No")

Using the ``all()`` method, which will return ``True`` only if **all** elements satisfied the condition.

.. jupyter-execute::
    :linenos:

    if (data > 3).all():
        print("Yes")
    else:
        print("No")

.. index::
    pair: logical operations; numpy
    pair: array comparisons; numpy

Comparisons of multiple arrays
------------------------------

`numpy` provides tools for element-wise comparisons. This is more complicated than just using the standard python syntax.

.. jupyter-execute::
    :linenos:

    x = numpy.array([True, False, False, True], dtype=bool)
    y = numpy.array([False, False, False, True], dtype=bool)

Applying equivalence operators to arrays can result in exceptions because the result is ambiguous.

.. jupyter-execute::
    :linenos:
    :raises:

    x or y

Instead, you should use special functions which will operate element wise. Here's a couple of examples.

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

**1.** Create a list of 10 positive integers and convert it into a ``numpy`` array. Use ``array`` methods to compute the total. Divide the original array by the total to produce a normalised array, which you assign to a variable ``freqs``. Using ``numpy`` logical operations to show that all elements are between 0 and 1. Use array methods to show the array sum is 1.

**2.** Many methods on ``numpy`` arrays have an axis argument, one of which is sum. Construct a 2-dimensional (2D) array that has the same number of rows and columns, e.g.

.. code-block:: text

    [[0, 0],
     [0, 0]]

is a 2D array. Assign values that make it easy to distinguish operations that operate across rows versus those which operate across columns. Demonstrate this matrix serves that purpose using ``sum()``.

**3.** ``bool`` data types can be summed. Create a sample array with ``dtype=bool`` and show that when you sum that you get the expected answers (what you expect is the sum will equal the number of occurrences of ``True``).

-----

Use the following array to answer the next question.

.. jupyter-execute::
    :linenos:

    data = numpy.array([[1, 9, 0, 3, 9],
                        [9, 2, 8, 2, 1],
                        [3, 1, 9, 9, 5]])


**4.** Look at the array ``data`` and identify the array coordinates where the values equal 9. Now use advanced array indexing to extract those coordinates in a single statement. The result should be

.. jupyter-execute::
    :hide-code:

    numpy.array([9, 9, 9, 9, 9])

**5.** Use boolean array indexing to assign -3 to all values of ``data`` less than 2. The result should be

.. jupyter-execute::
    :hide-code:

    numpy.array([[-3, 9, -3, 3, 9],
                 [9, 2, 8, 2, -3],
                 [3, -3, 9, 9, 5]])

**6.** Comparing performance of pure Python and numpy implementations. Investigate usage of ``numpy.where()`` to obtain the row and column coordinates of a 2D array where the value equals ``1`` (that's a one). Write a function called ``np_where()`` that takes a matrix as an argument and returns the row coordinates and column coordinates.

First, use the following code to generate a random square matrix.

.. jupyter-execute::
    :linenos:

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
    :linenos:

    %timeit py_where(mat)

Then try setting ``dim=20`` and repeat. Which is faster, and by how much?

**7.** Do some googling for testing ``numpy`` arrays using ``assert_allclose``. Then use this to check your array ``freqs`` created above sums to 1.
