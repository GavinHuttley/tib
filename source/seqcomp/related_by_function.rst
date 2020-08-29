.. _experimental_data:

Experimental procedures for detecting functionally related sequences
====================================================================

Since DNA sequences can encode function, it holds that different sequences demonstrated to encode a comparable property should be similar. For instance, different sequences that are able to bind a specific protein (e.g. TBP) will share sequence features in common. This perspective motivates development of experimental and statistical techniques to uncover how such functional information is encoded.

What sort of experiments can be conducted that allow identifying whether there is a particular diagnostic DNA sequence motif to which a protein binds? Whatever the nature of the experiment, we need a means for isolating a collection of sequences that are enriched for those that bind to the protein of interest. The experiment also needs to be able to identify the sequence of DNA molecules that have bound. Once that data exists we enter the world of computation and statistical analysis.

There are a variety of experimental procedures that can used for this purpose :cite:`Geertz:2010aa`. I will discuss just two of those here.

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

ChIP-seq is an *in vivo* process. A precursor for this technique is the availability of an antibody with high specificity for the protein of interest. With this in place, the cellular material of interest is exposed to formaldehyde which causes formation of cross linking (via covalent bonds) between DNA and whatever else is bound to it. The cells are then lysed and the DNA protein mix extracted and sheared [2]_ to a size suitable for the sequencing technology that will be used. You then expose the sheared DNA+protein mixture to the antibody and precipitate bound complexes. This step is followed by chemistry that reverses the cross linking, the protein is removed and the collection of DNA fragments are sequenced.

.. [2] Sonication being one approach.

.. figure:: /_static/images/seqcomp/chipseq.png
    :scale: 50 %
    
    An empirical survey of naturally occurring DNA [3]_.

.. [3] `Wikipedia entry <https://en.wikipedia.org/wiki/ChIP-sequencing>`_

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

From an experimental procedure, we ultimately seek to obtain a curated set of "aligned" sequences. I illustrate a hypothetical such case below [4]_.

.. [4] Positions displaying a ``.`` have the same nucleotide as ``"seq-0"`` for that column.

.. todo:: fix width of tables in display

.. jupyter-execute::
    :hide-code:

    from cogent3 import make_aligned_seqs

    seqs = {'seq-0': 'ATTTATG', 'seq-1': 'ATATAAA', 'seq-2': 'TTATAAA', 'seq-3': 'TTAAAAG', 
            'seq-4': 'ATAAATG', 'seq-5': 'ATATATG', 'seq-6': 'ATATAGG', 'seq-7': 'ATAAAAA',
            'seq-8': 'ATAAATC', 'seq-9': 'ATATTTA'}
    aln = make_aligned_seqs(data=seqs, moltype="dna")
    aln.set_repr_policy(ref_name="seq-0")
    aln

.. index::
    pair: PWM; Position Specific Weights Matrix

This is converted to a table of nucleotide counts per aligned column, resulting in a Position specific Weights Matrix (or PWM).

.. jupyter-execute::
    :hide-code:

    c = aln.counts_per_pos()
    c = c.to_table()
    tr = c.transposed(r"Base \ Position", select_as_header="", index=r"Base \ Position",
                      title="PWM", legend="position specific weights matrix")
    tr

This table becomes the primary source for defining :ref:`PSSMs <PSSMs>`.

------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha
