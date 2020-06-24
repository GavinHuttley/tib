Pairwise alignment using dynamic programming
============================================

There are optimally efficient algorithms available for pairwise alignment. We first tackle the problem of *global alignment*.

Needleman and Wunsch (NW) [1]_
------------------------------

Compared to the dotplot approach, it allows for more sophisticated "match", i.e. the sequence state may be different but still considered a match. It efficiently (in terms of computation) identifies the optimal "path" through the matrix.

The scoring system
^^^^^^^^^^^^^^^^^^

We will start by using the exact same *scoring matrix* as NW [1]_:

- states matched, score = 1
- states mismatched, score = -1
- gap insertion / deletion (:math:`\delta`), score = -1

.. note:: This is a linear gap score

Scored match / mismatch
^^^^^^^^^^^^^^^^^^^^^^^

We construct a matrix :math:`F`, such that :math:`F[i, j]` is the score for the *best* alignment up to :math:`i,j`. :math:`F` is built recursively using the following cases:

.. math::
    F[i,j] = \max 
    \begin{cases}
    F[i-1, j-1] + score(S_1[i], S_2[j])\\
    F[i-1, j] + \delta\\
    F[i, j-1] + \delta\\
    \end{cases}

where :math:`score(S_1[i], S_2[j])` is the *score* for the match of position :math:`i` and :math:`j` from sequences :math:`S_1` and :math:`S_2` respectively.

If we set :math:`i=1,j=1`, then the possible alignment paths leading to cell :math:`X[i,j]` are:

- :math:`(i,j-1)`, from :math:`\leftarrow`
- :math:`(i-1,j)`, from :math:`\uparrow`
- :math:`(i-1,j-1)`, from :math:`\nwarrow`

We arrive at :math:`F[1, 1]`, :math:`X`, by adding :math:`\delta` to the :math:`F` from each of the possible flanking cells and take the maximum of these. (:math:`\delta` is the mismatch and gap insertion penalties equal :math:`-1`.)

.. csv-table:: The 3 possible paths leading to cell :math:`F[i, j]`
    :header: "seq1 / seq2", ":math:`\\delta`", "**G** (j=0)","**A** (j=1)"

    :math:`\delta`, 0, ,
    **G** (i=0), ,":math:`[i-1,j-1]`",":math:`[i-1,j]`"
    **G** (i=1), ,":math:`[i,j-1]`", ":math:`\leftarrow \nwarrow \uparrow`"

Demonstrating NW on an example
------------------------------

We apply NW to the two sequences: ``GAGTAC`` and ``GGTAC`` gradually building up the algorithmic components in Python. We first define the scoring function:

.. jupyter-execute::
    :linenos:

    def score_func(a, b):
        if a == b:
            val = 1
        else:
            val = -1
        return val

    score_func("A", "A")
    score_func("A", "C")
    score_func("-", "A")

.. csv-table:: The completed score matrix
    :header: "",":math:`\\mathbf \\delta(x=0)`","G :math:`(x=1)`","A :math:`(x=2)`","G :math:`(x=3)`","T :math:`(x=4)`","A :math:`(x=5)`","C :math:`(x=6)`"
    
    ":math:`\delta(y=0)`",          "**0**",       "-1",       "-2",       "-3",       "-4",       "-5",       "-6"
    "**G** :math:`(y=1)`",              "-1",    "**1**",    "**0**",       "-1",       "-2",       "-3",       "-4"
     "**G** :math:`(y=2)`",             "-2",        "0",        "0",    "**1**",        "0",       "-1",       "-2"
    "**T** :math:`(y=3)`",              "-3",       "-1",       "-1",        "0",    "**2**",        "1",        "0"
    "**A** :math:`(y=4)`",              "-4",       "-2",        "0",       "-1",        "1",    "**3**",        "2"
    "**C** :math:`(y=5)`",              "-5",       "-3",       "-1",       "-1",        "0",        "2",    "**4**"

.. [1] Needleman & Wunsch (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. Journal of Molecular Biology, 48: 443–453
