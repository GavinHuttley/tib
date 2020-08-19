:math:`k`-mers and Motifs
=========================

.. index:: k-mers

:math:`k`-mers
--------------

One way of describing DNA sequences is simply counting the occurrences of DNA words of a fixed size. Such words are often referred to as :math:`k`-mers where :math:`k` refers to the word length. If we set :math:`k=1`, then the complete set of possible 1-mers is the listing of the nucleotides, i.e. ``{A, C, G, T}``.

But why do it? Why is knowing :math:`k`-mers informative? There are a multitude of ways in which :math:`k`-mer counting is used in bioinformatics. One concerns evolutionary relatedness, another concerns functional encoding. Before we tackle those, lets go ahead and define :math:`k`-mers in more detail.

We define the set of possible :math:`k`-mers as the full enumeration of a characters in a state space. In English, since DNA has four letters there are :math:`4^k` distinct :math:`k`-mers. So for :math:`k=2`, that's :math:`4^2=16`. These are all the possible dinucleotides.

.. jupyter-execute::
    :hide-code:

    from itertools import product
    
    print(", ".join(["".join(pair) for pair in product("ACGT", "ACGT")]))

Setting :math:`k=3`, we have 64 possible trinucleotides, for :math:`k=4`, we have 256 tetranucleotides and so on.

We define the :math:`k`-mer distribution of a biological sequence typically as the counts all possible occurrences of each :math:`k`-mer. Consider the following DNA sequence.

.. jupyter-execute::
    :hide-code:

    seq = "ACGGTGCCAGG"
    seq

The distribution of :math:`k`-mers for :math:`k=1` is

.. jupyter-execute::
    :hide-code:

    from collections import Counter
    
    dict(Counter(seq))

Each value in the ``dict`` corresponds to the number of occurrences of that nucleotide.

The distribution of :math:`k`-mers for :math:`k=2` is

.. jupyter-execute::
    :hide-code:

    dinucs = [seq[i:i+2] for i in range(len(seq)-1)]
    c = dict(Counter(dinucs))
    print(c)

where each value corresponds to the number of occurrences of that dinucleotide. If you sum the values you get 10, from a sequence of length 11.

Wait, what! How does that work! Surely there are only 5 dinucleotides in a sequence of length 11!

We derive a :math:`k`-mer distribution by considering all possible words of length :math:`k`. Let's simplify the problem by working on just the first 3 nucleotides, ``ACG``. This has two possible dinucleotides -- ``AC`` and ``CG``. Thus, we slide the start position along the sequence by 1 and take the :math:`k` nucleotides from that position.

So how do :math:`k`-mers get used? They are used as a measure of evolutionary relatedness. The "distance" between :math:`k`-mer distributions of species that are closely related to each other is typically smaller that the distance between more distantly related species. The genomic signature statistics of `Karlin and colleagues <https://pubmed.ncbi.nlm.nih.gov/9294192/>`_ are related to these measures. Moreover, they are `employed in machine learning algorithms <https://www.genetics.org/content/215/1/25>`_ such as that of Zhu et al (from my own lab).

.. index:: motif

Motifs
------

Another application of :math:`k`-mers is in how they relate to the concept of motifs. A motif is a short sequence that occurs multiple times in a DNA, RNA or protein sequence. The phrase can also be applied quite generally. For instance, the ``"ATG"`` motif corresponds to the start codon of protein coding genes. The phrase is typically applied to sequences that have some functional association. Arguably, this notion is exemplified by sequence logos, a statistical method used for visualisation of motifs. The DNA binding motif of the TBP protein is visually represented by a `sequence logo <Binding to DNA>`_. A related visualisation technique was developed by Zhu et al (from my own lab) for identifying `sequence motifs associated with mutation processes <https://pubmed.ncbi.nlm.nih.gov/27974498>`_.

As the start codon example illustrates, motifs represent a fundamental concept in the description of information encoding by DNA sequences.

Exercises
=========

**1.** Write an algorithm that produces all possible dinucleotides for ``seq``.

**2.** Then do it for all possible trinucleotides in ``seq``.

**3.** The Python standard library has lots of very useful goodies. Investigate the ``Counter`` class from ``itertools`` and apply it to your result from (1) and (2) to determine the :math:`k`-mer distribution. (Use google!)
