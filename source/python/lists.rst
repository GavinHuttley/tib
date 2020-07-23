.. index:: list, container objects

Using lists
===========

.. jupyter-execute::
    :linenos:

    data = []
    print(data)

.. jupyter-execute::
    :linenos:

    data.append("AA")
    print(data)

.. jupyter-execute::
    :linenos:

    data.append("TTTT")
    print(data)

.. index:: len()

.. jupyter-execute::
    :linenos:

    len(data)  # to find out what len does, do help(len)

Lists within lists
------------------

One feature of lists (and some other Python data types), is the ability to create objects that have multiple dimensions.

For instance, you can have a list whose elements are also lists.

.. note:: If creating a list of multiple elements from scratch, you must separate the elements using ``","``.

.. jupyter-execute::
    :linenos:

    seq_records = []
    seq_records.append(["label 1", "AA"])
    print(seq_records)

.. jupyter-execute::
    :linenos:

    seq_records.append(["label 2", "TT"])
    print(seq_records)
