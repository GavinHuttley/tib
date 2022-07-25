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

We can establish whether an object is a member of a set using the ``in`` logical operator

.. jupyter-execute::

    "X" in a

or whether one set is a subset of another using the ``<`` logical operator

.. jupyter-execute::

    bases = {"A", "C", "G", "T"}
    b < bases

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

Exercises
=========

#. For the following data, create a set using either ``set()`` or a set comprehension.

    .. jupyter-execute::

        data = ['GC', 'CA', 'AA', 'AG', 'GG', 'GA', 'AG',
                'GC', 'CC', 'CA', 'AA', 'AC', 'CA', 'AT',
                'TA', 'AA', 'AC', 'CA', 'AG']

#. How many unique dinucleotides are there in ``data``?

#. Create a set from the following and compare it to the set you created from ``data``. How big is the intersection of the two sets? How big is the set of symmetric differences?

    .. jupyter-execute::
    
        data2 = ['GC', 'CA', 'AA', 'AG', 'GG', 'GC', 'CG',
                 'GC', 'CC', 'CA', 'AA', 'AC', 'CA', 'AG',
                 'GA', 'AG', 'GC', 'CA', 'AG']
    
#. Provide an example that a ``frozenset()`` can be applied to but a ``set()`` cannot. In showing this, include any errors and explain why they occur.

#. For the following data, you want to create a set that excludes dinucleotides containing a non-canonical DNA character (see Expected Output). Solve this problem in two different ways. (a) by creating the set of unique dinucleotides and creating the correct set from that. (b) by creating an empty set, iterating over dinucleotides in ``data`` and adding them only if they consist of canonical nucleotides. Which algorithm is faster and why?

    .. tabbed:: Data

        .. jupyter-execute::

            data = ['GC', 'CA', 'AA', 'NG', 'GG', 'GA', 'AG',
                    'GC', 'CC', 'CR', 'AA', 'AC', 'CA', 'NN',
                    'TA', 'AA', 'AY', 'CA', 'AG']

    .. tabbed:: Expected Output
    
        .. jupyter-execute::
            :hide-code:
        
            data = set(data)
            nucs = set("ACGT")
            data = {d for d in data if set(d) <= nucs}
            print(data)
