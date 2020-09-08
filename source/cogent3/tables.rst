.. jupyter-execute::
    :hide-code:

    import set_working_directory

.. _tables:

Tabular data
============

The ``cogent3`` Table_ data type provides methods for manipulating tabular data. Here we summarise the basic capabilities. One important point to make is that tables are immutable, in that once a column has been created you cannot modify individual elements. But you can modify what columns a table has, their name and order. Table columns themselves are just numpy arrays.

.. index::
    pair: make table; cogent3

Making a Table from standard Python objects
-------------------------------------------

I want to produce a Table that has two columns, base 1 and base2 of a dinucleotide. We will construct this using a sequence from one of the alignment files.

.. jupyter-execute::
    :hide-code:

    from cogent3 import load_aligned_seqs

    seqs = load_aligned_seqs("data/brca1.fasta", moltype="dna").degap()
    seq = seqs.named_seqs["Wombat"]

.. jupyter-execute::

    seq

We split into the separate positions using the builtin ``zip()`` [1]_.

.. [1] By prefacing the argument with ``*``, we do an unzip operation.

.. jupyter-execute::

    dinucs = seq.get_in_motif_size(2, log_warnings=False)
    base1, base2 = list(zip(*dinucs))

From a column-oriented dict
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We convert the above into a column based ``dict`` -- the keys will become the column names and the values the column.

.. jupyter-execute::

    data = {"base1": base1, "base2": base2}

and then we import a utility function for making tables.

.. jupyter-execute::

    from cogent3 import make_table

    table = make_table(data=data)
    table

From a header and a list of lists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I'm going to make a list of lists from ``dinucs`` by just convert each dinucleotide into a list.

.. jupyter-execute::

    rows = [list(dinuc) for dinuc in dinucs]
    rows[:4]

In this instance, I need to specify the column names using the argument ``header``.

.. jupyter-execute::

    table = make_table(header=["base1", "base2"], data=rows)
    table

.. index::
    triple: load from file; table; cogent3

Loading a table from a file
---------------------------

We load a tab separated data file using the ``load_table()`` function. The format is inferred from the filename suffix and you will note, in this case, it's not actually a `csv` file.

.. jupyter-execute::

    from cogent3 import load_table

    stats = load_table("data/edge_stats.tsv")
    stats

Getting summary using ``Table.head()`` or ``Table.tail()``
----------------------------------------------------------

These display the top or bottom of a table.

.. jupyter-execute::

    stats.head()

.. jupyter-execute::

    stats.tail()

Slicing a Table
---------------

Tables are "row oriented", so the first index concerns rows, the column.

.. jupyter-execute::

    stats[:4]

Getting a column
----------------

Tables have a ``column`` attribute.

.. jupyter-execute::

    stats.columns

This has ``dict`` like properties and supports you getting a column using the column header,

.. jupyter-execute::

    stats.columns["kappa"]

or, using an ``int`` like it's a series – in this case indexes are defined by the ``column.order`` attribute.

.. jupyter-execute::

    stats.columns.order

.. jupyter-execute::

    stats.columns[0]

.. index::
    triple: filter; table; cogent3

Filtering a table to include rows by value
------------------------------------------

In our dinucleotide table, we only want rows where both bases are in the canonical set ``{A, C, G, T}``. We do this via a filter step using a ``lambda`` function and a ``set`` object consisting of these bases. The ``filtered()`` method calls the ``lambda`` with each row. Only if the ``lambda`` returns ``True`` will the row be included in the new ``Table``. In our case, our ``lambda`` will return true if the set of elements in the row is a subset of all the basses.

.. jupyter-execute::

    table = table.filtered(lambda x: set(x) <= {"A", "C", "G", "T"})
    table

.. note:: I did not specify which columns because the default is to use all columns.

Counting unique values
----------------------

This method returns counts of the unique combinations of values from the specified columns. The result is a ``cogent3`` type, a ``CategoryCounter`` instance, which has some useful properties. Principal being that it behaves like a ``dict``.

.. jupyter-execute::

    unique = table.count_unique()
    unique

To categorical count
^^^^^^^^^^^^^^^^^^^^

Another being that it can produce ``CategoryCount`` object

.. jupyter-execute::

    cat_counts = unique.to_categorical()
    cat_counts

which supports statistical testing of categorical data. For instance

.. jupyter-execute::

    cat_counts.chisq_test()

.. index::
    triple: index column; table; cogent3

Generating categorical counts from a Table
------------------------------------------

We can also get a ``CategoryCount`` object via ``Table.to_categorical()``. In this case, the counts must be fully specified prior to constructing the table. (Meaning you've already done the counting part.) In addition, we also need to specify a column whose values are the row categories. The latter is achieved setting ``make_table(index=<column name>)``. In this case, I specify the column name of the index is an empty string.

.. jupyter-execute::

    data = {
        "A": (158, 110, 113, 59),
        "C": (66, 81, 65, 57),
        "G": (142, 15, 69, 87),
        "T": (81, 72, 63, 58),
        "": ["A", "C", "G", "T"],
    }

    table = make_table(data=data, index="")
    table

.. jupyter-execute::

    cat_counts = table.to_categorical()
    cat_counts

.. todo:: add some exercises
