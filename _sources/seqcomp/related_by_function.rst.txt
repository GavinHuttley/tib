.. _experimental_data:

Experimental procedures for detecting functionally related sequences
====================================================================

Sequences that a possess a shared functional property (e.g. protein binding) will share sequence features in common. For instance, the DNA sequences that are able to bind TBP. What sort of experiments can be conducted that allow identifying whether there is a particular diagnostic DNA sequence motif to which a protein binds? Whatever the nature of the experiment, we need a means for isolating a collection of sequences that are enriched for those that bind to the protein of interest. The experiment also needs to be able to identify individual sequences that have bound. Once that data exists we enter the world of computation and statistical analysis.

There are a variety experimental procedures that can used for this purpose :cite:`Geertz:2010aa`. I will discuss just two of those here.

.. index:: SELEX

SELEX -- Systematic evolution of ligands by exponential enrichment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This procedure is entirely *in vitro*. The inputs are a substantial amount of enriched protein [1]_ which is bound to a bead. Also required is a library of synthetically produced double stranded DNA of a precise fragment size. These two substrate are then incubated together under conditions favourable to binding of the DNA and protein. By eluting the unbound DNA fragments, you wind up with beads that have bound DNA. Those DNA fragments are then dissociated from the beads and amplified using PCR. This new DNA pool is then reintroduced to bead-bound protein and the process is repeated. (Only a few a rounds are done.) At the end of these iterations, the bound DNA is isolated again and the collection of DNA fragments is sequenced.

.. [1] The requirement for a lot of protein limits the utility of this technique.

.. figure:: /_static/images/seqcomp/selex.png
    :scale: 50 %
    
    A synthetic sequence assessment procedure.

.. index:: ChIP-seq

ChIP -- chromatin immunoprecipitation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ChIP-seq is an *in vivo* process. A precursor for this technique is availability of an antibody with high specificity for the protein of interest. With this in place, the cellular material of interest is exposed to formaldehyde which causes formation of cross linking (via covalent bonds) between DNA and whatever else is bound to it. The cells are then lysed and the DNA protein mix extracted and sheared [2]_ to a size suitable for the sequencing technology that will be used. You then expose the sheared DNA+protein mixture to the antibody and precipitate bound complexes. This step is followed by chemistry that reverses the cross linking, the protein is removed and the collection of DNA fragments are sequenced.

.. [2] Sonication being one approach.

.. figure:: /_static/images/seqcomp/chipseq.png
    :scale: 50 %
    
    An empirical survey of naturally occurring DNA [5]_.

.. [5] `Wikipedia entry <https://en.wikipedia.org/wiki/ChIP-sequencing>`_

With the sequence data from those experimental procedures
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Identifying a dominant motif requires a way of summarising features across a collection of sequences. For instance, we can "align" fragments and employ a majority rule consensus approach. This just picks the most frequent state in a column of *aligned* sequences.

.. code-block:: text

    01234 <-- the "index" or position
    TCAGA
    TTCCA
    TTCCA
    TTTTC
    TTTTC

    TTCTA <-- the majority consensus

Challenges to this approach include handling the case of equally abundant states (a random choice at positions 2 and 3), and masking the possible importance of other states. An alternate approach to handling this issue of multiple characters is to use `IUPAC ambiguity characters <https://en.wikipedia.org/wiki/Nucleic_acid_notation>`_ to capture all states at a column.

.. code-block:: text

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


------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha
