Dotplot -- Alignment of sequences related by descent from a common ancestor
===========================================================================

This very neat approach to establishing the relatedness between biological sequences was invented here at ANU, by Gibbs and McIntyre :cite:`Gibbs:1970aa`.

.. sidebar:: The original dotplot

    .. image:: /_static/images/seqcomp/dotplot_pub.png
        :scale: 50%
    
    After :cite:`Gibbs:1970aa`.

Below is a subset of Figure 1 of Gibbs and McIntyre. Dotplot of cytochrome C amino acid sequences from Human to: Rhesus macaque, Tuna fish. (The N-terminus is at the top left, which corresponds to the "translation start" the protein.) Each dot indicates where the amino acid is identical between the two sequences.

Long stretches of identity form a diagonal. A break -- existence of multiple diagonals -- can arise from changes in "state" (the amino acids differ, but the flanking amino acids are the same), or insertions / deletions (new sequence inserted or existing sequence removed) that have occurred. The latter are frequently referred to as "indels".

.. note:: When analysing two sequences, it is typically not possible to establish whether it was a deletion or an insertion.

.. sidebar:: Comparison of cytochrome C

    .. image:: /_static/images/seqcomp/dotplot_fig1ab.png
        :scale: 75%
    
    After :cite:`Gibbs:1970aa`.

The original dotplot algorithm
------------------------------

Consider two sequences, ``X`` and ``Y`` with lengths ``n`` and ``m`` respectively. We establish the matches between them using the following algorithm (written as `pseudocode <https://en.wikipedia.org/wiki/Pseudocode>`_) [1]_:

.. code-block:: text
    :name: dotplot_algorithm
    
    create a matrix of ones, matches, with dimensions n x m
    for i in 1 ... n:
        for j in 1 ... m:
            if X[i] == Y[j] then
                matches[i, j] = 0

.. note:: I am *not* using Python indexing here! This is, in effect, a :math:`k`-mer matching algorithm where :math:`k=1`.

.. [1] Because of the Plotly colour scale, we use values of 0 to indicate a match which will display as black, 1 means a mismatch which will be white. For the two sample sequences ``"AGCGT"`` and ``"AT"`` we construct by hand the resulting.

.. code-block:: python
    :name: dotplot_matrix

    #           A  G  C  G  T
    matches = [[0, 1, 1, 1, 1],  #  A
               [1, 1, 1, 1, 0]]  #  T

.. jupyter-execute::
    :hide-code:

    matches = [[0, 1, 1, 1, 1],  #  A
               [1, 1, 1, 1, 0]]  #  T

.. jupyter-execute::

    import plotly.express as px

    fig = px.imshow(
        matches,
        range_color=[0.0, 1.0],
        color_continuous_scale="gray",
    )

We make some adjustments to simplify the display.  First, suppress a colour bar.

.. jupyter-execute::

    fig = fig.update_layout(coloraxis_showscale=False)

We want to place a box around the matrix and specify a font size for both the |xaxis| and |yaxis| text, which we define as a ``dict``.

.. jupyter-execute::

    common_settings = dict(
        linewidth=2, linecolor="black", mirror=True, tickfont={"size": 28}
    )

.. index:: **kwargs 

This one object can then be provided as the keyword arguments for a method calls using a ``**kwargs`` idiom. We also set the sequence text as the tick text on their respective axes.

.. jupyter-execute::

    fig.update_xaxes(
        ticktext=["A", "G", "C", "G", "T"], tickvals=[0, 1, 2, 3, 4], **common_settings
    )
    fig.update_yaxes(ticktext=["A", "T"], tickvals=[0, 1], **common_settings)
    fig.show()

I draw your attention to the fact that array coordinates (see :ref:`explanation on array coordinates <array_coordinates>`) are used in both this display and that presented in the original publication.

Exercises
=========

#. Implement the simple dotplot algorithm. Write a function that takes the following two sequences and returns an array with 1 where the sequences do not match and 0 where they do.

    .. jupyter-execute::

        seq1 = "CCTCTGAATAGGAGACAAGACCATGCAGGCATACTAGGTGGCGCACATAGATTT"
        seq2 = "CCTCTGAATAGGCGACGAAGACAAGACCATGCAGGCATAGGTGGCGCACATAGATTT"

#. Write a function that returns :ref:`cartesian coordinates <array_coordinates>` for the same sequences, but with the :math:`x` and :math:`y` components separated.

    .. tabbed:: For this data
    
        Using a smaller data set like the below, you can check your algorithm performs correctly.
    
        .. jupyter-execute::
    
            seq1 = "CCAAA"
            seq2 = "CCTCAG"

    .. tabbed:: Expected Output

        .. jupyter-execute::
            :hide-code:
    
            def get_cartesian_coords(s1, s2):
                coords = []
                for x, b1 in enumerate(s1):
                    for y, b2 in enumerate(s2):
                        if b1 == b2:
                            coords.append((x, y))
                return list(zip(*coords))
    
            x, y = get_cartesian_coords(seq1, seq2)
            print(f"x={x}\ny={y}")

#. Plot the cartesian coordinates using a scatter plot, with axis labels representing the sequence names.

.. todo:: get short examples of DNA sequences with repeats and and short examples of amino acid sequences, make generating dotplot using those an exercise and get them to interpret

------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha
