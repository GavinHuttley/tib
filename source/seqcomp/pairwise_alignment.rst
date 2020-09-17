Global Pairwise Alignment Using Dynamic Programming
===================================================

The transmission of genetic information from one generation to the next is imperfect. DNA sequences can differs from their parent in a number of ways due to mutations. There are different categories of mutations. Large scale rearrangements, such as translocations, inversions, duplications are important features of genome evolution and are (in humans) contributors to disease. Smaller scale changes such as those affecting individual mutations -- referred to as point mutations -- as are small deletions or insertions.

Comparisons of related DNA sequences that have been subjected to such processes are performed using alignment algorithms where the goal is to identify those positions in two (or more) sequences that have descended from a common ancestor. Consider the following case where we have an ancestral sequence with two descendants, one of whom experienced a deletion event.

::

                  |
       +--------ACAGT--------+     Ancestor
       |                     |
       |                   AxxxT   3 bp deletion
       |                     |
     ACAGT                  AT     Sampled sequences

     seq1                  seq2

What we typically observe, as in this case, is the outcomes of the process.

::
    seq1  ACAGT
    seq2  AT

As the "history" is hidden, we must infer an *alignment* that can then be applied to deduce what happened. There are 2 possibilities in this instance.

::

    seq1  ACAGT
    seq2  A---T

OR

::

    seq1  ACAGT
    seq2  --A-T

Making inferences regarding historical relatedness underpins much of how we utilise biological sequence data. So how can we decide which positions in two (or more) sequences are related? There are optimally efficient algorithms available for pairwise alignment. We first tackle the problem of *global alignment* [1]_ :cite:`Needleman:1970aa`.

.. [1] Global here means aligning the entire sequences. This contrasts with a "local" alignment, which computes the best aligned segment for a pair of sequences. That is solved using another dynamic programming algorithm referred to as Smith-Waterman, which we don't address.

Needleman and Wunsch (NW)
-------------------------

A more elaborate case is presented in the dotplot below. There are obvious diagonal lines here which I will refer to as a "path".

.. jupyter-execute::
    :hide-code:

    from cogent3 import make_aligned_seqs

    aln = make_aligned_seqs(data=
    {'A': 'CCTCTGAATAGG------AGACAAGACCATGCAGGCATACTAGGTGGCGCACATAGATTT',
     'B': 'CCTCTGAATAGGCGACGAAGACAAGACCATGCAGGCATA---GGTGGCGCACATAGATTT'}, moltype="dna")
    fig = aln.degap().dotplot(name1="A", name2="B", window=9, threshold=9, title="")
    fig.layout.showlegend = False
    fig.show()

When the path breaks and starts again higher up, that means there is some sequence missing from ``"A"``. This will be represented by hyphens in ``"A"`` in the final alignment. When it breaks and starts again to the right, it means that there is some sequence "missing" from sequence ``"B"``. In the final alignment, that will be represented by the hyphen (`"-"` character) in ``"B"``.

The aim of an alignment algorithm is to find this path efficiently (in terms of time) given biological input sequences like.

.. code-block:: text

    A    CCTCTGAATAGGAGACAAGACCATGCAGGCATACTAGGTGGCGCACATAGATTT
    B    CCTCTGAATAGGCGACGAAGACAAGACCATGCAGGCATAGGTGGCGCACATAGATTT

The resulting alignment will look like the following.

.. code-block:: text

    A    CCTCTGAATAGG------AGACAAGACCATGCAGGCATACTAGGTGGCGCACATAGATTT
    B    CCTCTGAATAGGCGACGAAGACAAGACCATGCAGGCATA---GGTGGCGCACATAGATTT

In this result, each column of this alignment corresponds to characters that have descended from a common ancestor.

Compared to the dotplot approach, it allows for more sophisticated "match", i.e. the sequence state may be different but still considered a match. It is also efficient in terms of computation and identifies the optimal path [2]_ through the matrix.

.. [2] The use of the word optimal in this case means given a specific model, which we will define. There can, however, be multiple solutions (paths) that are equal in terms of the alignment score. In this instance, there are multiple optimal solutions.

The NW algorithm works via building an alignment from solutions of smaller alignments. Instead of a graph, we now think in terms of a matrix. This matrix shares the row and column labelling as that for :ref:`the dotplot  <dotplot_matrix>` but has some differences.

In the dotplot matrix, elements in the matrix simply reflect presence absence of a match between the two sequences. For NW, the values correspond to *the score of the optimal alignment up to that point*.

We need 4 things for the NW algorithm  [3]_:

.. [3] I'm presenting the algorithm of :cite:`Gotoh:1982aa`.

- a scoring system
- a matrix of "path scores"
- a corresponding matrix of "path choices"
- a way of recovering the alignment from the path choices

.. index::
    pair: indel; insertion deletion

The scoring system
^^^^^^^^^^^^^^^^^^

.. note:: To simplify the following discussion, I will only refer to DNA states for my examples but emphasise that the same reasoning applies to protein sequences.

For any pair of sequence states [4]_ (nucleotides) we define a score function :math:`s(i, j)`, where :math:`i, j` are the nucleotides being compared from sequences ``A`` and ``B``. This function :math:`s()` returns a score that the two nucleotides are a "match". Typically there are distinct values for when the two states are the same (:math:`i=j`), compared to when the states are different (:math:`i\neq j`). For our purpose, we start by using the exact same scoring function as NW :cite:`Needleman:1970aa`. I their case :math:`s(i, j)` returns 1 when :math:`i=j` and -1 otherwise. We also define a gap introduction score, :math:`\delta=-1` [5]_.

.. [4] The word "state" refers to a single character in the corresponding biological alphabet. For instance, for DNA, the valid states are A, C, G and T.
.. [5] This is a linear gap score, meaning that each additional gap character has the same score.

A matrix of path scores
^^^^^^^^^^^^^^^^^^^^^^^

We illustrate the notion of the path matrix (which we denote :math:`\mathcal{P}`), by considering the calculation of the score in the cell :math:`\mathcal{P}[i, j]`.

.. csv-table:: The path scores matrix :math:`\mathcal{P}`. The 3 possible paths leading to cell :math:`\mathcal{P}[i, j]`. :math:`i, j` refer to positions within sequence ``A``, ``B`` respectively.
    :name: path_table
    :header: ``A`` |backslash| ``B``, ..., G\ :sub:`j-1`,A\ :sub:`j`

    ..., , ,
    G\ :sub:`i-1`, ,":math:`[i-1,j-1]`",":math:`[i-1,j]`"
    G\ :sub:`i`, ,":math:`[i,j-1]`", ":math:`\leftarrow \nwarrow \uparrow`"

As indicated in the table, there are 3 different ways of arriving at the alignment score ending at this cell. In the case of either a :math:`\leftarrow, \uparrow`, the best alignment leading to :math:`\mathcal{P}[i, j]` was from a gap. In the case of :math:`\leftarrow`, the gap is in ``A`` and in the case of :math:`\uparrow` the gap is in ``B``. The :math:`\nwarrow` indicates a diagonal move and corresponds to an alignment path coming from a match. The selection of which direction gives the optimal alignment path to :math:`i, j` stems from the following function

.. math::
    :name: path_score

    \mathcal{P}[i, j] = \max
    \begin{cases}
    \mathcal{P}[i-1, j-1] + score(A[i], B[j])\\
    \mathcal{P}[i-1, j] + \delta\\
    \mathcal{P}[i, j-1] + \delta\\
    \end{cases}

where :math:`score(A[i], B[j])` is the *score* for the match of position :math:`i` and :math:`j` from sequences ``A`` and ``B`` respectively. Being able to choose amongst these possible paths requires that the scores for all 3 possible input cells (:math:`\mathcal{P}[i-1,j]`, :math:`\mathcal{P}[i-1,j-1]`, :math:`\mathcal{P}[i,j-1]`) already exist. And if we tried to compute the score for any of those cells we would discover that we needed the scores of their 3 input cells, and so on. This is a recursive function, which we address below.

The path choices matrix
^^^^^^^^^^^^^^^^^^^^^^^

If we want to recover the optimal alignment path through the matrix, we need to be recording at every cell, which of the possible input directions was chosen. We will refer to this :math:`\mathcal{T}` and it's a companion matrix to :math:`\mathcal{P}`, with exactly the same dimensions.

Handling the recursion
^^^^^^^^^^^^^^^^^^^^^^

We have to start somewhere, and the first issue we encounter is a need to handle the boundaries. If we are on the top row, :math:`i=0`. We are restricted to a single possible input path (:math:`\leftarrow`, the others are undefined). As a consequence, these boundary elements consist of an alignment of one sequence to a prefix of only gaps. With this notion in place, we then introduce the beginning state row/column into the :math:`\mathcal{P, T}` matrices. Thus these matrices both have dimensions :math:`n+1, m+1` where :math:`n, m` are the lengths of sequences ``A`` and ``B`` respectively. Given the form of :ref:`equation <path_score>`.

Demonstrating NW on an example
------------------------------

We apply NW to the following two sequences, gradually building up the algorithmic components in Python. We will use ``numpy`` arrays to implement this algorithm.

.. jupyter-execute::

    seq1 = "GGTAC"
    seq2 = "GAGTAC"

Create the data structures we need
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because of the boundary condition, the dimensions of our matrices are +1 that of the sequence lengths.

.. jupyter-execute::

    dim_r = len(seq1) + 1
    dim_c = len(seq2) + 1

We next define the ``path_scores`` matrix (which represents :math:`\mathcal{P}`). We will specify this as a float array populated with zeros to start.

.. jupyter-execute::

    import numpy

    path_scores = numpy.zeros((dim_r, dim_c), dtype=float)

As described above, every boundary cell has only one possible entry path. We define index ``r`` as the row index, and ``c`` as the column index. Then for every boundary cell where :math:`r=0, c`, the only possible path into it is from :math:`r=0, c-1`. (The same applies to the other boundary, but noting in that case :math:`c=0`). In this case, the scores for the boundary cells can be pre-computed as simply the index multiplied by :math:`\delta`. We represent the latter parameter in python as ``delta`` and apply this operation to the ``path_scores`` matrix across both boundaries.

.. jupyter-execute::

    delta = -1

    for r in range(dim_r):
        path_scores[r, 0] = delta * r

    for c in range(dim_c):
        path_scores[0, c] = delta * c

    path_scores

We define a ``path_choices`` matrix (which represents :math:`\mathcal{T}`). We specify this as an ``object`` array since we want to store tuples inside it. Specifically, we will store the :math:`r, c` coordinates for the optimal alignment leading into the current cell. Using ``numpy``, we initialise the matrix as being empty.

.. jupyter-execute::

    path_choices = numpy.empty((dim_r, dim_c), dtype=object)

We then address the boundary conditions. Since boundary cells can have only one input path, and since the ``path_choices`` array records that path, we can easily initialise the array. But note that we need to point into the *previous cell*, so we must start our loops from the value ``1``, not ``0``. We also set the special value of ``(0, 0)`` for the vert first cell.

.. jupyter-execute::

    path_choices[0, 0] = (0, 0)

    for r in range(1, dim_r):
        path_choices[r, 0] = (r - 1, 0)

    for c in range(1, dim_c):
        path_choices[0, c] = (c - 1, 0)

    path_choices

All the cells with the value ``None`` will be completed during the calculation of the scores.

The scoring function
^^^^^^^^^^^^^^^^^^^^

We write this as a function since it will be called for every comparison of sequence states.

.. jupyter-execute::

    def score_match(a, b):
        if a == b:
            val = 1
        else:
            val = -1
        return val

    score_match("A", "C")

.. jupyter-execute::

    score_match("A", "A")

Computing the best score and path for a particular comparison
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I write a function that corresponds to the algorithmic implementation of `equation <path_score>`_. In this case, I'm anticipating what information I need -- the ``path_scores`` matrix, the coordinates of the current cell, the score for the states represented by that cell and the gap penalty (``delta``).

.. jupyter-execute::

    def get_best_score_path(path_scores, r, c, score, delta):
        match_path = (r - 1, c - 1)
        match_score = path_scores[match_path] + score

        left_path = (r, c - 1)
        left_score = path_scores[left_path] + delta

        up_path = (r - 1, c)
        up_score = path_scores[up_path] + delta

        # call max on lists with [score, path coord]
        # This function will select based on score first, then break ties using
        # path coord

        best_score_path = max(
            [match_score, match_path], [left_score, left_path], [up_score, up_path]
        )

        return best_score_path

Populating the ``path_scores`` and ``path_choices`` matrices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    for r, base1 in enumerate(seq1, 1):
        for c, base2 in enumerate(seq2, 1):
            score = score_match(base1, base2)
            best_score, best_path = get_best_score_path(path_scores, r, c, score, delta)
            path_scores[r, c] = best_score
            path_choices[r, c] = best_path

    path_scores

The following table uses bold font to emphasise the path choices that are made to produce the alignment and provides the indices to make it clearer how the path is interpreted.

.. csv-table:: The completed score matrix
    :header: ``seq1[r]`` |backslash| ``seq2[c]``,:math:`\\mathbf \\delta_0`,G\ :sub:`1`,A\ :sub:`2`,G\ :sub:`3`,T\ :sub:`4`,A\ :sub:`5`,C\ :sub:`6`

    ":math:`\delta_0`",          "**0**",       "-1",       "-2",       "-3",       "-4",       "-5",       "-6"
    **G**  :sub:`1`,              "-1",    "**1**",    "**0**",       "-1",       "-2",       "-3",       "-4"
    **G**  :sub:`2`,             "-2",        "0",        "0",    "**1**",        "0",       "-1",       "-2"
    **T**  :sub:`3`,              "-3",       "-1",       "-1",        "0",    "**2**",        "1",        "0"
    **A**  :sub:`4`,              "-4",       "-2",        "0",       "-1",        "1",    "**3**",        "2"
    **C**  :sub:`5`,              "-5",       "-3",       "-1",       "-1",        "0",        "2",    "**4**"

.. jupyter-execute::

    path_choices

The exciting bit -- the Viterbi algorithm!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The NW algorithm is a solution to the complex challenge of finding the optimal global alignment. Up to now it's been quite mundane and very conventional. The elegance and efficiency of NW stems from this step -- the traceback. This part is referred to as the Viterbi algorithm, which is a :index:`dynamic programming` solution for efficiently tracing back the optimal path through the matrix. It's referred to as a traceback since the final path score is at the very end of the matrix.

We will solve this using a ``while`` loop since we don't know precisely how many steps this will take. Our ``while`` loop exit condition will be based on having reached a ``path_choices`` cell whose value is ``(0, 0)``. Since we are tracing back the alignment, our initial coordinate for ``path_choices`` is the very last cell.

.. jupyter-execute::

    r = len(seq1)
    c = len(seq2)

We then define two lists which we will use to hold the aligned sequences as they are built.

.. jupyter-execute::

    aligned_1 = []
    aligned_2 = []

.. jupyter-execute::

    while (r, c) != (0, 0):
        # the next step backwards
        r_next, c_next = path_choices[r, c]
        base1 = "-" if r_next == r else seq1[r - 1]
        base2 = "-" if c_next == c else seq2[c - 1]
        aligned_1.append(base1)
        aligned_2.append(base2)

        r, c = r_next, c_next

So that didn't fail -- awesome! But our sequences are actually in reverse order (we did start at the end of the alignment after all). So to recover them in their correct orientation, we simply reverse the lists and transform them into a string.

.. jupyter-execute::

    aligned_1.reverse()
    aligned_1 = "".join(aligned_1)

    aligned_2.reverse()
    aligned_2 = "".join(aligned_2)

    print(f"seq1: {aligned_1}", f"seq2: {aligned_2}", sep="\n")

Aligning the sequences from the dotplot example
-----------------------------------------------

So how well does our algorithm go in aligning the sequences we used for the doplot example at the top? If you try it, you will likely see the following.

.. code-block:: text

    A: CCTCTGAATAGG - -A - GA - --CAAGACCATGCAGGCATACTAGGTGGCGCACATAGATTT
    B: CCTCTGAATAGGCGACGAAGACAAGACCATGCAGGCATA - --GGTGGCGCACATAGATTT

This is not the same. The single large gap in ``A`` from the above has now been fragmented into multiple smaller gaps. This illustrates a limitation of the linear gap score. Examination of real biological sequences indicates that indels tend to affect multiple adjacent positions. For instance, in a protein coding gene indels sizes are products of 3. This has the effect of maintaining the reading frame. A more advanced indel (e.g. an affine gap) model is used to represent this property. We don't address that here aside from saying this is just one of the ways alignment algorithms have improved since the original NW publication.

Exercises
=========

#. Convert the above code into functions so that you can align any pair of sequences you like.

#. Write some tests of your functions to make sure they are working correctly. For instance, if you give two sequences that are completely different (e.g. "AAAA" and "TTTT"), what should you see? Does the algorithm generate that?

#. Modify the scoring function to be more tuned to DNA sequences. Specifically, allow transitions (changes between pyrimidines or between purines) to have a higher match score than transversions, but less than a perfect match.

------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha

.. |backslash| replace:: \\

