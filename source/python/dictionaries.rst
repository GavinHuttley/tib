.. index::
    pair: dict; types

.. _dicts:

Dealing with dictionaries
=========================

The ``dict`` type is a mutable collection data structure that is extraordinarily useful. They provide super fast lookups of items and allow a more natural specification of how things are stored and retrieved. In general, a dictionary consists of key/value pairs [1]_. The value is the object of interest and the key is how you retrieve it from a dictionary instance. This means that dictionaries are not "ordered", i.e. you can't rely on the first element in always appearing "first" if you start to loop over

.. [1] When discussing dictionaries, a key/value pair is referred to as an "item".

.. note you cannot have duplicate keys

Creating an empty ``dict``
--------------------------

There are two approaches to defining a ``dict``, the first uses "empty" curly braces [2]_.

.. [2] A dict is empty if you don't specify any key/value pairs. So having blank spaces, or tab characters within the braces has no impact.

.. jupyter-execute::

    x = {}
    x

Or by calling the builtin ``dict()`` without any arguments.

.. jupyter-execute::

    x = dict()
    x

Dictionaries have a length, which in this case is 0.

.. jupyter-execute::

    len(x)


Creating a non-empty ``dict``
-----------------------------

The syntax differs between the two different approaches. In the case of using ``{}``, you separate keys from values using the ``:`` and from the next key/value pair using a ``,``.

.. jupyter-execute::

    names = {"first": "GAVIN", "last": "Huttley"}
    names

.. note:: Only immutable data types can be used for dictionary keys.

Using the ``dict()`` function allows a quite different approach that can only be applied if the keys are going to be strings. In this approach, the keys become argument names to ``dict()`` and the values are assigned to them in the function call. In the following, notice that we use what a standard keyword argument statement within a function call -- we remove the quotes from the key and use ``=`` to assign the value.

.. jupyter-execute::
    :raises:

    names = dict(first="GAVIN", last="Huttley")
    names

.. warning:: This approach only works if the string can be a valid python variable. For instance "first_name" would work, but "first name" would not.

.. note:: Dictionary keys are always unique. If you make successive assignments to a dict with the same key name, you are simply overwriting the previous value for that key.

.. index::
    pair: KeyError; Exceptions

Retrieving values from a ``dict`` by "indexing"
-----------------------------------------------

We obtain values from a ``dict`` instance using the key. Using the ``names`` instance, we can get the value corresponding to the key ``"first"`` using the standard looking indexing syntax (i.e. using ``[]``).

.. jupyter-execute::

    f = names["first"]
    f

If you try to get a key that does not exist, Python raises a ``KeyError``.

.. jupyter-execute::
    :raises:

    f = names["first name"]


``KeyError`` exception

Retrieving values from a ``dict`` using the ``get()`` method
------------------------------------------------------------

The ``get()`` method is an alternate to indexing using ``[]``. If a key does not exist, it defaults to return ``None`` instead of raising a ``KeyError``.

.. jupyter-execute::

    v = names.get("first name")
    type(v), v

You can provide your own "default" value for when a key is missing. If we were using a dict to record counts of nucleotides, for instance, we can define a default value of 0 (for an alternate approach to counting).

.. jupyter-execute::

    counts = {}
    seq = "ACGGCCG"
    for nucleotide in seq:
        counts[nucleotide] = counts.get(nucleotide, 0) + 1
    
    counts

.. margin:: Counting without using a dict
    :name: no_dict
    
    It's worth showing building counts if you don't use a dict. Let's say we want to use a list instead. Here's one approach.
    
    .. jupyter-execute::
    
        nucleotides = "ACGT"
        seq = "ACGGCCG"
        ordered_counts = [seq.count(nuc) for nuc in nucleotides]
        ordered_counts

    This is compact but does not have the nice association of a count with it's corresponding nucleotide. Hence, looking up the counts of "A" requires getting its index in ``nucleotides`` and using that value to get the count from ``ordered_counts``. This is fragile since it relies on the ordering of both always being the same (not guaranteed for a list). It also doesn't scale well for counting larger length strings (e.g. all dinucleotides or trinucleotides, etc...) since every state must be evaluated.

Looping over a dict
-------------------

The ``dict`` object is an iterable data type. This means you can loop over it. This process returns the keys of the instance.

.. jupyter-execute::

    for k in counts:
        # printing both the key and it's value
        print(k, counts[k])

Seeing if a ``dict`` contains a key
-----------------------------------

This is done using the ``in`` operator.

.. jupyter-execute::

    has_a = "A" in counts
    has_a

.. jupyter-execute::

    has_t = "T" in counts
    has_t

Displaying all the keys or all the values or all the items of a ``dict``
------------------------------------------------------------------------

Getting all the keys
^^^^^^^^^^^^^^^^^^^^

To find what keys are present  in a dict, we use the aptly named ``keys()`` method. This returns a custom type [3]_, which can be iterated over.

.. jupyter-execute::

    v = counts.keys()
    type(v)

You can use that to get the keys as a different data type, e.g. a tuple or list, using the respective builtin functions.

.. jupyter-execute::

    keys = tuple(counts.keys())
    keys

But you can get the same thing by passing the ``dict`` instance itself. This works because the ``tuple()`` and ``list()`` functions take an iterable as their argument and, as we showed above, iterating over a dict returns the keys.

.. jupyter-execute::

    keys = tuple(counts)
    keys

Getting all the values
^^^^^^^^^^^^^^^^^^^^^^

This is what the ``values()`` method does! It returns a custom data type [3]_ which can be iterated over.

.. jupyter-execute::

    counts.values()

Getting all the key/value pairs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can achieve this by using the ``items()`` method which, again, returns a custom data type [3]_.

.. jupyter-execute::

    counts.items()

A common usage pattern for the ``items()`` method is for looping with :index:`assignment unpacking`.

.. jupyter-execute::

    for key, value in counts.items():
        print(f"key={key} and value={value}")

.. [3] These custom types can all be iterated over and/or used to create one of the other standard data types by using their builtin functions, e.g. ``list()``, ``tuple()``.

Adding new items to a ``dict``
------------------------------

Adding a new item to an existing dict is just an assignment.

.. jupyter-execute::

    counts["T"] = 0

Updating an existing item
-------------------------

But where dicts become really valuable is when you need to dynamically update a value. We've shown this above in the case of constructing our dict of nucleotide counts (the counts are incremented). But consider the case when we have a mutable data type, such as a ``list``, as the value. Let's consider the following data

.. jupyter-execute::

    data = [['FlyingFox', '8.57'],
            ['DogFaced', '7.66'],
            ['edge.0', '4.66']]

Say we want to convert the second column to floats. We can do this by iterating over the rows and only convert the index ``1``. Another approach is to construct separate lists for each column and convert the entire column [4]_. We start by defining our dictionary with the keys assigned values of empty lists. (I'm using assignment unpacking again.)

.. [4] I know this is a little contrived, but it's the best example I can come up with right now. The point is how we can update the value of a mutable object!

.. jupyter-execute::

    by_column = {"name": [], "stat": []}
    for name, stat in data:
        by_column["name"].append(name)
        by_column["stat"].append(stat)
    
    by_column

In the above, the ``by_column[<key name>]`` returns the value for that key. We can then directly access methods on that returned object using the ``.`` syntax (in this case, the ``append()`` method) which we use, appending a new value to.  This is an example of :index:`method chaining` (see :ref:`method_chaining`).

We can now apply our casting to the numerical column only.

.. jupyter-execute::

    by_column["stat"] = [float(v) for v in by_column["stat"]]
    by_column

This pattern of modifying the value associated with a key based on its current value is extremely useful.
