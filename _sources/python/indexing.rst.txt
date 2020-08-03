Indexing and Slicing
====================

.. index:: index

Indexing
--------

This works equivalently for python strings, tuples and lists. There are similarities to indexing other data types, and differences.

An index refers to the order number of an element in a series. Elements from instances of a series data type (e.g. `str` and `list`) can be referenced by their index number.

For all data types, the `[]` are used to specify the indices.

.. note:: Python indexes start at `0`.

.. jupyter-execute::
    :linenos:

    #       0123...
    data = "ACGTACGTACGT"
    print(data[1])

Indexing is also used for assignment.

.. jupyter-execute::
    :linenos:

    more_data = ["some text", 4, 23.4]
    more_data[0] = -2
    print(more_data)

But assignment is not possible with an immutable data type like a string.

.. jupyter-execute::
    :linenos:
    :raises:

    data[0] = "T"

Indexing beyond the length of a series causes an exception. Here is a little gotcha. Although ``more_data`` is 3 elements long, there is no element at index 3. That's because Python indexes start at 0.

.. jupyter-execute::
    :linenos:
    :raises:

    print(more_data[3])

Indexing in multiple-dimensions
-------------------------------

Using the list of lists I created earlier.

.. jupyter-execute::
    :linenos:

    seq_records = [["label 1", "AA"], ["label 2", "TT"]]
    seq_records[0]

.. jupyter-execute::
    :linenos:

    seq_records[0][1]

.. jupyter-execute::
    :linenos:

    seq_records[1][1]

.. index:: slice

Slicing
-------

.. index::
    pair: start; slice
    pair: stop; slice
    pair: stride; slice

Slicing is just an indexing operation that refers to a range of elements. A slice operation allows you to select a sequential ordering of elements. The syntax for a slice is ``[start:end:stride]``, but some of these terms are optional.

- ``start`` refers to the first index from which elements will be sampled. Defaults to 0.
- ``end`` refers to the index up (but not including) to which the elements will be sampled. Defaults to the length of the series.
- ``stride`` refers to the separation between selected elements. Defaults to 1.

.. jupyter-execute::
    :linenos:

    data
    codon1 = data[0:3]
    codon1

.. note:: I omitted the ``start`` and just used the `":"`. Python interpreted this as "slice from the start of the string up to (but not including) index 3".

.. index::
    pair: negative; slice

Negative slicing works from the *end*.

.. jupyter-execute::
    :linenos:

    data[-3:]

You can even specify a *stride*, which causes the slice to occur in steps of the specified length. Below I set the stride `=3` (which is what you would do if you wanted to select 1st codon positions, for example).

.. jupyter-execute::
    :linenos:

    data[0:9:3]

Slicing to beyond the length of a series does not cause an exception.

.. jupyter-execute::
    :linenos:

    data[:15]

Exercises
=========

**1.** Consider the ``dict`` defined below

.. jupyter-execute::
    :linenos:

    d = {0: "value for 0", ("a-key",): "funky key"}

Get each value of ``d`` using ``index`` notation [1]_.

.. [1] This is actually not indexing, because elements in a dict are not ordered. But the notation for "getting" an item from a ``dict`` is the same as for other data types (i.e. you use ``[]``). The difference is the "index" does not need to be an integer.

-----

Answer the following questions using this simple list of numbers.

.. jupyter-execute::
    :linenos:

    nums = [0, 1, 2, 3, 4]


**2.** What does ``nums[::-1]`` do?

-----

Answer the following questions using this simple protein coding DNA sequence ``ATGATGATG`` [2]_.

.. [2] In the standard genetic code, this corresponds to 3 repeats of the methionine codon

.. jupyter-execute::
    :linenos:

    seq =  "ATGATGATG"

**3.** Use a slice to extract the first codon. Do the same for the last codon.

**4.** Use a slice operation to obtain the first nucleotide of each codon [3]_, i.e. you should produce ``["A", "A", "A"]``. Do this for the second codon position (producing ``["T", "T", "T"]``) and then the third codon position.

.. [3] DNA encodes amino acid sequences using 3 consecutive bases. This unit is referred to as a :index:`codon`.

**5.**  Split the sequence ``ATGAAATAA`` into codons (non-overlapping letter triples). (The most succinct solution uses a list comprehension.)

