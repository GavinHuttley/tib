Finding motifs
==============

So how do we find occurrences of a motif that is "noisy"? If we use the consensus approach, it's trivial --  exact string match. For the IUPAC ambiguity case, it's also quite trivial -- we could use a regular expression, e.g.

.. jupyter-execute::

    import re

    re.findall("T[CT][ACT][GCT][AC]", "AGCGTTTCTCAGATGCA")

In the above, I've used the regular expression module (``re``) that's distributed with python.

Alternatively, we could use a "probabilistic model" [1]_. That's what we're going to do now.

.. [1] A probabilistic model is one where a specific outcome is quantified via explicit probability calculation.

Simple probability model for generating sequences
-------------------------------------------------

Assume the probabilities of nucleotides are :math:`p_A=0.1`, :math:`p_C=0.2`, :math:`p_G=0.3`  and :math:`p_T=0.4`. We can calculate the probability of observing the following sequence as

.. jupyter-execute::

    seq = "AGGTC"
    probs = dict(A=0.1, C=0.2, G=0.3, T=0.4)
    p_seq = 1.0
    for base in seq:
        p_seq *= probs[base]
    p_seq

For this probability to be an accurate reflection of the true expected frequency of ``seq`` requires that nucleotides occur independently of each other. Hence, we can just use the product of the individual nucleotide probabilities. (The alternate is a Markov process with order ≥ 1.)

When we consider modelling a sequence motif, however, we use position specific probabilities, i.e. there would be a distinct ``probs`` for each position of a motif. This is the foundation of PSSMs.

PSSMs: Position Specific Scoring Matrices
-----------------------------------------

Among the simplest probabilistic approaches are PSSMs. A PSSM is a matrix of log-odds ratios per position of a sequence motif. They are also referred to as profiles. They provide a means for computing the match odds for any new sequence. They are typically applied to finding transcription factor binding sites (TFBS) but also used to characterise protein domains.

Great, where can I get one? Well ... recall JASPAR (the open access database of TFBS profiles) [2]_.

.. [2] *Sandelin et al (2004). JASPAR: an open-access database for eukaryotic transcription factor binding profiles. Nucleic Acids Research, 32(90001), 91D–94*

Below is the TATA box position weight matrix from JASPAR. ::

    A  [ 61  16 352   3 354 268 360 222 155  56  83  82  82  68  77 ]
    C  [145  46   0  10   0   0   3   2  44 135 147 127 118 107 101 ]
    G  [152  18   2   2   5   0  20  44 157 150 128 128 128 139 140 ]
    T  [ 31 309  35 374  30 121   6 121  33  48  31  52  61  75  71 ]

In this case, the PSSM has length 15. This motif is on display at `JASPAR <http://jaspar.genereg.net/cgi-bin/jaspar_db.pl?ID=MA0108.2&rm=present&collection=CORE>`_ (but note their web server can be quite slow).

Formal definition of the probability model
------------------------------------------

We now layout the equations for computing the probability of a sequence. To start, we make some simplifying assumptions. Namely, we assume a counts matrix reflects the true underlying probabilities of bases per position of a motif; that each base in a motif occurs independently of the other bases. We can compute the probability under the PPM (position probability matrix) model `M` of a sequence `x` with length `L` as:

.. math::
    P(x|M)=\Pi_{i=0}^L p_i(x_i)

where :math:`x_i` is the base at position `i`. This probability can also be referred to as the *odds* of observing the sequence given the model `M`.

.. note::  the :math:`\Pi` symbol means "take the product of the series". So what :math:`\sum` is to addition, :math:`\Pi` is for multiplication.

A worked example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Consider the following hypothetical matrix ::

    A  [ 61  16 389   3 ]
    C  [145  46   0  10 ]
    G  [152  18   0   2 ]
    T  [ 31 309   0 374 ]

which produces the following position specific probability matrix ::

    A [ 0.16  0.04  1.00  0.01 ]
    C [ 0.37  0.12  0.00  0.03 ]
    G [ 0.39  0.05  0.00  0.01 ]
    T [ 0.08  0.79  0.00  0.96 ]

The conditional probability of the sequence:

*1.* ``GTAT``, is :math:`0.39 \times 0.79 \times 1.0 \times 0.96 \approx 0.3`

*2.* ``GTCT``, is :math:`0.39 \times 0.79 \times 0.0 \times 0.96 = 0.0`

The latter case is potentially real -- binding only happens with A at the 3rd position -- but most likely due to a finite sized training data set. In other words, if the training set had been much larger we may have observed the other bases at that position.

Pseudo-counts -- handling missing data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Handling small sample sizes is a substantial problem [3]_. The easiest way to tackle it, which we will use here, is to employ a pseudo-count. A pseudo-count is a "synthetic observation" that is added to all the elements in the counts matrix. It eliminates 0 counts and thus precludes cases such as (2) above, where a sequence is otherwise considered impossible. I'll illustrate that using the above example.

.. [3] When sample sizes are large, the effect of adding a pseudo-count is small.

.. jupyter-execute::

    from numpy import array

    counts = array(
        [[61, 16, 389, 3], [145, 46, 0, 10], [152, 18, 0, 2], [31, 309, 0, 374]]
    )

Then we add our pseudo-count.

.. jupyter-execute::

    counts += 1
    counts

We determine our new columns sums

.. jupyter-execute::

    col_sums = counts.sum(axis=0)
    col_sums

and produce a revised position specific probability matrix

.. jupyter-execute::

    ppm = counts / col_sums
    ppm

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to assess whether a sequence might be consistent with a PSSM, we need a way of scoring them. This is done by converting a the Position specific Probability Matrix (PPM) to a log-odds ratio. In short, we compare the odds of observing a base compared to its odds from a background distribution.

For convenience, define the background distribution of sequence states to be equally frequent. Then the odds ratio is:

.. math::

    OR(x|M)=\Pi_{i=0}^L \frac{p_i(x_i)}{0.25}

Which is expressed as a log-odds score `S`:

.. math::
    S=\sum_{i=0}^L \log p_i(x_i) - \log 0.25

We then interpret the values of `S` as

- if S=0, the sequence is equally likely in the PSSM and background
- if S<0, the sequence is less likely under the PSSM than background
- if S>0, the sequence is more likely under the PSSM than background

PSSM limitations
^^^^^^^^^^^^^^^^

- if the training data is limited, we need to handle zero counts which may introduce bias
- we assume bases in a sequence are independent of each other
