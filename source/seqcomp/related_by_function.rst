.. _experimental_data:

Experimental procedures for detecting functionally related sequences
====================================================================

Sequences that a possess a shared functional property (e.g. protein binding) will share sequence features in common. For instance, the sequences that are able to bind TBP. How can we identify where something binds DNA? We need to obtain a sample of sequences that have this property in common.

Here's a fuller description of the experimental procedures [4]_, albeit a bit of out date.

.. [4] `Geertz and Maerkl <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3080775/>`_

SELEX -- Systematic evolution of ligands by exponential enrichment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /images/selex.png
    :scale: 50 %
    
    A synthetic sequence assessment procedure.

ChIP -- chromatin immunoprecipitation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /images/chipseq.png
    :scale: 50 %
    
    An empirical survey of naturally occurring DNA [5]_.

.. [5] `Wikipedia entry <https://en.wikipedia.org/wiki/ChIP-sequencing>`_

With the sequence data from those experimental procedures
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

identifying a dominant motif requires a way of summarising features across a collection of sequences. For instance, we can "align" fragments and employ a majority rule consensus approach. This just picks the most frequent state in a column of *aligned* sequences. ::

    01234 <-- the "index" or position
    TCAGA
    TTCCA
    TTCCA
    TTTTC
    TTTTC

    TTCTA <-- the majority consensus

Challenges to this approach include handling the case of equally abundant states (a random choice at positions 2 and 3), and masking the possible importance of other states. An alternate approach to handling this issue of multiple characters is to use `IUPAC ambiguity characters <https://en.wikipedia.org/wiki/Nucleic_acid_notation>`_ to capture all states at a column. ::

    01234
    TCAGA
    TTCCA
    TTCCA
    TTTTC
    TTTTC

    TYHBM <-- the IUPAC consensus

.. note:: In the above, ``Y`` is either ``C`` or ``T``.

.. _pssm-origins:

Transformation of the data for analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From an experimental procedure, we ultimately seek to obtain a curated set of "aligned" sequences. 

.. todo:: fix width of tables in display

.. jupyter-execute::
    :hide-code:

    from numpy import array
    from cogent3 import make_table

    header = ['Label \\ Position', '0', '1', '2', '3', '4', '5', '6']
    data = {'Label \\ Position': array(['seq-0', 'seq-1', 'seq-2', 'seq-3', 'seq-4', 'seq-5', 'seq-6',
       'seq-7', 'seq-8', 'seq-9'], dtype='<U5'), '0': array(['A', '.', 'T', 'T', '.', '.', '.', '.', '.', '.'], dtype='<U1'), '1': array(['T', '.', '.', '.', '.', '.', '.', '.', '.', '.'], dtype='<U1'), '2': array(['T', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'], dtype='<U1'), '3': array(['T', '.', '.', 'A', 'A', '.', '.', 'A', 'A', '.'], dtype='<U1'), '4': array(['A', '.', '.', '.', '.', '.', '.', '.', '.', 'T'], dtype='<U1'), '5': array(['T', 'A', 'A', 'A', '.', '.', 'G', 'A', '.', '.'], dtype='<U1'), '6': array(['G', 'A', 'A', '.', '.', '.', '.', 'A', 'C', 'A'], dtype='<U1')}
    data = {k: array(data[k], dtype='U') for k in data}
    table = make_table(header, data=data, title="Hypothetical sequence data from an enrichment experiment",
    legend="Position -- alignment position; label -- sequence identifier. The value '.' indicates the nucleotide is identical to that of the first sequence.")
    table

This is converted to a table of counts by simply counting occurrences of bases in each alignment column.

.. jupyter-execute::
    :hide-code:

    from numpy import array
    from cogent3 import make_table

    header = ['Base \\ Position', '0', '1', '2', '3', '4', '5', '6']
    data = {'Base \\ Position': array(['T', 'C', 'A', 'G'], dtype='<U1'), '0': array(['2', '0', '8', '0'], dtype='<U1'), '1': array(['10', '0', '0', '0'], dtype='<U2'), '2': array(['1', '0', '9', '0'], dtype='<U1'), '3': array(['6', '0', '4', '0'], dtype='<U1'), '4': array(['1', '0', '9', '0'], dtype='<U1'), '5': array(['5', '0', '4', '1'], dtype='<U1'), '6': array(['0', '1', '4', '5'], dtype='<U1')}
    data = {k: array(data[k], dtype='U') for k in data}
    table = make_table(header, data=data, title="PWM", legend="position specific weights matrix")
    table


