.. index::
    pair: set; type
    pair: frozenset; type

The ``set`` data type
=====================

This data type represents the mathematical object of a set. A set stores *unique values*, no matter how the object was initialised. They also cannot be indexed (or subscripted) since that has no meaning. The elements in a set are also unordered.

Sets are defined either explicitly using ``{}`` with different members separated by commas.

.. jupyter-execute::

    a = {0, 1, 1, 3, 1}
    a

or by calling the builtin function ``set()`` passing the data in as a series.

.. jupyter-execute::

    a = set([0, 1, 1, 3, 1])
    a

As the latter expression indicates, the input to ``set()`` must be an iterable. This matters! The latter two **are not** equivalent.

.. jupyter-execute::

    a = {"ABC"}
    a

The former states explicitly that the string "ABC" is a set member and the set has one member.

But using the builtin function states the items in "ABC" are set members.

.. jupyter-execute::

    b = set("ABC")
    b

To have the latter correspond with the former requires placing the string inside another iterable.

.. jupyter-execute::

    b = set(["ABC"])
    b

The ``set`` type is iterable.

.. jupyter-execute::
    
    dinucs = {"AA", "CG", "GA"}
    for item in dinucs:
        print(item)

Only immutable data types can be members of sets (so not lists etc..)

.. jupyter-execute::
    :raises:

    {"ABC", []}

The great power of this data type is the ability to do very succinct comparisons. These use :ref:`bitwise operators <bitwise_operators>`. For instance, we identify the overlap between two sets using the bitwise ``&`` character (bitwise AND).

.. jupyter-execute::

    a = set("ACGGCCT")
    b = set("ACGGAAA")
    a & b

We can establish that one set is a subset of another using the ``in`` logical operator

.. jupyter-execute::

    bases = {"A", "C", "G", "T"}
    a in bases

We can compute the difference (what nucleotides is ``b`` missing) using the standard ``-`` operator

.. jupyter-execute::

    bases - b

Or a "symmetric" difference using the ``^`` character (bitwise exclusive OR, analogous to NOT)

.. jupyter-execute::

    bases ^ b

We can take the union of two sets using the ``|`` character (bitwise inclusive OR).

.. jupyter-execute::

    a = {0, 2, 3}
    b = {1, 4}
    
    a | b

These operations are also available as methods on the ``set`` instances.

Having created a set, you can add new elements using the ``add()`` method.

.. jupyter-execute::

    a.add(22)
    a

Or remove elements using the ``remove()`` method.

.. jupyter-execute::

    a.remove(22)
    a

Given that a ``set`` is mutable, you cannot have sets as part of sets. Python provides an ``immutable`` set type, ``frozenset`` that can be. This is defined using the builtin function of that name.

.. jupyter-execute::

    f = frozenset("ABCD")
    f

.. jupyter-execute::

    a.add(f)
    a

.. note:: Once created, a ``frozenset`` instance cannot be changed.

.. todo:: add some exercises
