.. jupyter-execute::
    :hide-code:

    import set_working_directory


.. _PSSMs:

Position Specific Scoring Matrices (PSSMs)
==========================================

.. index::
    pair: PSSM; Position Specific Scoring Matrix

A Position Specific Scoring Matrix, or PSSM, is a matrix of :index:`log-odds ratios` per position of a sequence motif. (PSSMs are also called :index:`profiles`.) They provide a means for computing the match odds for any new sequence. They are typically applied to finding transcription factor binding sites (TFBS) but are also used to characterise protein domains.

See :ref:`experimental_data` for how the counts data are derived. To illustrate the transformation of those counts data into a PSSM, we will start with a simple worked example. First we take the counts table presented in :ref:`pssm-origins`.

We convert the :ref:`PWM <pssm-origins>` into a PPM, but I'm restricting the examples to just 4 positions.

.. jupyter-execute::
    :hide-code:

    from book_code import pssm_calc

    pssm_calc.calc_ppm()


A worked example
----------------

Calculating the Expected Under the Background
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's use the sequence

.. jupyter-execute::

    seq1 = "GTAT"

We define a background distribution as one where all bases are equally frequent. In the above case, we then obtain the :math:`p(seq1|background)` as

.. jupyter-execute::

    seq_len = len(seq1)
    p_seq1_background = 0.25 ** seq_len
    print(f"{p_seq1_background:.6f}")

Calculating the Expected Under the Alternate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case, I'm just doing this "manually". First, note the base order is T, C, A, G [1]_. Here's a pseudo-code algorithm describing this calculation:

.. [1] This ordering of nucleotides is chemical (pyrimidines, then purines) and is the ordering used in some software.

.. code-block:: rest

    PPM is a 2D matrix with rows corresponding to bases, columns to positions
    define the index order of bases as T at index 0, C index 1, A index 2, G index 3
    prob_of_seq = 1.0
    for seq_index in sequence
        set base as the character at seq_index
        set base_index as the index of base in bases
        probability_of_base_at_position equals PPM[base_index, seq_index]
        prob_of_seq  = prob_of_seq * probability_of_base_at_position
        if prob_of_seq is 0, exit the loop

At sequence position ``0``, we have base ``G``. This has the value of 0.0, so we stop.

This raises the question of whether a ``G`` at index ``[0]`` is truly impossible? More likely, the 0 is due to the sample size of the experiment. One approach is to add a "small" number to all elements. (This is akin to imagining the next observation would have been of the unobserved type.) This number is referred to as a pseudocount and typically, a pseudocount ≤ 1 is chosen.

Adjusting the PWM with a pseudocount
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We add a pseudocount of 0.5 to the PWM and then convert to a PPM as before, producing

.. jupyter-execute::
    :hide-code:

    from cogent3 import make_table
    from numpy import array

    header = ["Base \\ Position", "0", "1", "2", "3"]
    data = {
        "Base \\ Position": array(["T", "C", "A", "G"], dtype="<U1"),
        "0": array(["0.208", "0.042", "0.708", "0.042"], dtype="<U5"),
        "1": array(["0.875", "0.042", "0.042", "0.042"], dtype="<U5"),
        "2": array(["0.125", "0.042", "0.792", "0.042"], dtype="<U5"),
        "3": array(["0.542", "0.042", "0.375", "0.042"], dtype="<U5"),
    }
    data = {k: array(data[k], dtype="U") for k in data}
    table = make_table(
        header,
        data=data,
        title="PPM",
        legend="Position specific probability matrix after adding 0.5 to the PWM cells",
    )
    table

This now leads to the following elements being taken from the table ``0.042, 0.875, 0.792, 0.542``, leading to

.. math::
     
     p(seq1|alternate)=0.042\times0.875\times0.792\times0.542\approx0.015775

The odds-ratio
^^^^^^^^^^^^^^

We can form an odds-ratio as

.. math::

    OR = \frac{p(seq1|alternate)}{p(seq1|null)}\approx4.0384

How should you interpret this? Look at the OR equation!

Computing the PSSM
^^^^^^^^^^^^^^^^^^

The PSSM is a log-odds matrix, i.e. it's the log of the odds ratio matrix. Because we assume a background distribution of 0.25, we can compute this very simply as ``log2(ppm)-log2(0.25)``.

.. sidebar:: Maths with logarithms, recall that

    :math:`\log(a/b)=\log(a) - \log(b)`
    
    and
    
    :math:`\log(a \times b) = \log(a) + \log(b)`
    
    Note that we use log base 2 (:math:`\log_2`), by convention.

.. jupyter-execute::
    :hide-code:

    from cogent3 import make_table
    from numpy import array

    header = ["Base \\ Position", "0", "1", "2", "3"]
    data = {
        "Base \\ Position": array(["T", "C", "A", "G"], dtype="<U1"),
        "0": array([-0.263, -2.585, 1.503, -2.585]),
        "1": array([1.807, -2.585, -2.585, -2.585]),
        "2": array([-1.000, -2.585, 1.663, -2.585]),
        "3": array([1.115, -2.585, 0.585, -2.585]),
    }
    data = {k: array(data[k]) for k in data}
    table = make_table(header, data=data, digits=3)
    table

Computing the PSSM score for the sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We now select elements from the PSSM, just as we did above from the PPM -- we use the sequence position number to specify the column of the PSSM, and the base at that position to specify the row. With that, for the sequence "GTAT", we select the following log-odds scores: ``-2.585, 1.807, 1.663, 1.115``.

From these, the log-odds of ``seq1`` being derived from the experimental sample instead of the bacgkround is:

.. math::

    score = -2.585 + 1.807 + 1.663 + 1.115 = 2

For more on the interpretation of odds ratios, see :ref:`odds-ratios`.

Exercises
=========

#. What does an OR equal 1 mean? What about an OR > 1? Or, an OR<1?

#. What does a log-odds ratio > 1 mean? What about a log-odds ratio equal to 0?

#. Write a function that takes a numpy array of odds-ratios and returns their :math:`\log_2`.

#. Write a function that takes a numpy array of log odds-ratios (assume the base is 2, i.e. :math:`log_2`) and returns their odds ratios.
