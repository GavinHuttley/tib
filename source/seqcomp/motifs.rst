|kmers| and Motifs
==================

.. index:: k-mers

|kmers|
-------

One way of describing DNA sequences is simply counting the occurrences of DNA words of a fixed size. Such words are often referred to as |kmers| where :math:`k` refers to the word length. If we set :math:`k=1`, then the complete set of possible 1-mers is the listing of the nucleotides, i.e. ``{A, C, G, T}``.

But why do it? Why is knowing |kmers| informative? There are a multitude of ways in which |kmer| counting is used in bioinformatics. One concerns evolutionary relatedness, and another concerns functional encoding. Before we tackle those, let's go ahead and define |kmers| in more detail.

We define the set of possible |kmers| as the full enumeration of characters in a state space. In English, since DNA has four letters there are :math:`4^k` distinct |kmers|. So for :math:`k=2`, that's :math:`4^2=16`. These are all the possible dinucleotides.

.. jupyter-execute::
    :hide-code:

    from itertools import product
    
    print(", ".join(["".join(pair) for pair in product("ACGT", "ACGT")]))

Setting :math:`k=3`, we have 64 possible trinucleotides, for :math:`k=4`, we have 256 tetranucleotides and so on.

We typically define the |kmer| distribution of a biological sequence as the counts of all possible occurrences of each |kmer|. Consider the following 11bp long DNA sequence.

.. jupyter-execute::
    :hide-code:
    
    seq = "ACGGTGCCAGG"
    seq

The distribution of |kmers| for :math:`k=1` is

.. jupyter-execute::
    :hide-code:

    from collections import Counter
    
    dict(Counter(seq))

Each value in the ``dict`` corresponds to the number of occurrences of that nucleotide.

The distribution of |kmers| for :math:`k=2` is

.. jupyter-execute::
    :hide-code:

    dinucs = [seq[i:i+2] for i in range(len(seq)-1)]
    c = dict(Counter(dinucs))
    print(c)

where each value corresponds to the number of occurrences of that dinucleotide. If you sum the values you get 10, from a sequence of length 11. Wait, what ... how does that work! Surely there are only 5 dinucleotides in a sequence of length 11!

We derive a |kmer| distribution by considering **all possible words** of length :math:`k`, Let's simplify the problem by working on just the first 3 nucleotides, ``ACG``. This has two possible dinucleotides -- ``AC`` and ``CG``. Thus, we slide the start position along the sequence by 1 and take the :math:`k` nucleotides from that position (:ref:`see Sliding window <kmers>`).

.. margin:: Sliding window
    :name: kmers
    
    ::
        
        Index      012
        Sequence   ACG
        Index 0    AC
        Index 1     CG
    
    To identify all dinucleotides (:math:`k=2`), we iterate over all indices, slice the sequence from the current index to be length 2. Clearly, we need to make sure to get the last |kmer| correct, i.e. it must also be of length 2.

So how do |kmers| get used? They are used as a measure of evolutionary relatedness. The "distance" between |kmer| distributions of closely related species is typically smaller than the distance between distantly related species. The genomic signature statistics of `Karlin and colleagues <https://pubmed.ncbi.nlm.nih.gov/9294192/>`_ are related to these measures. Moreover, |kmers| are `employed in machine learning algorithms <https://www.genetics.org/content/215/1/25>`_ such as that of Zhu et al (from my own lab).

.. index:: motif

Motifs
------

Another application of |kmers| is in how they relate to the concept of motifs. A motif is a short sequence that occurs multiple times in a DNA, RNA or protein sequence. The phrase can also be applied quite generally. For instance, the ``"ATG"`` motif corresponds to the start codon of protein coding genes. The phrase is typically applied to sequences that have some functional association. Arguably, this notion is exemplified by sequence logos, a statistical method used for visualisation of motifs. The DNA binding motif of the TBP protein is visually represented by a :ref:`sequence logo <Binding to DNA>`. A related visualisation technique was developed by Zhu et al (from my own lab) for identifying `sequence motifs associated with mutation processes <https://pubmed.ncbi.nlm.nih.gov/27974498>`_.

As the start codon example illustrates, motifs represent a fundamental concept in the description of information encoding by DNA sequences.

Exercises
=========

#. Consider the sequence ``seq``. How many |kmers| are there for :math:`k=1,2,3`?

    .. jupyter-execute::
    
        seq = "ACG"

#. For a sequence of length 7, how many |kmers| are there for :math:`k=1,2,3`?

#. Write an equation for the number of |kmers| in a sequence of length :math:`n`. When you set :math:`n=3, 7` and :math:`k=1, 2, 3` you should get the same answers as above.

#. Write an algorithm that produces all the dinucleotides for ``seq``.

#. Then do it for all the trinucleotides in ``seq``.

#. The Python standard library has lots of very useful goodies. Investigate the ``Counter`` class from ``collections`` and apply it to your result from (4) and (5) to determine the |kmer| counts. (Use google!)
