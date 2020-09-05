.. _shannon_entropy:

Measuring information using Shannon's entropy
=============================================

We can measure the information content of "something" using a measurement called "entropy" (like a scale for information). The core unit is the "bit", called a measure of surprise, which is the answer to a yes/no question.

Consider a state space containing only the letter ``A``. We can never be "surprised" by the outcome of drawing a new letter from this space as it can only be of one type. So our entropy, in this case is 0. Add another letter and we have a chance to be "surprised". So in general, as predictability goes up, entropy goes down.

As it turns out, entropy is a very fundamental quantity. You will see numerous expressions in statistics that relate to this. Given that the very purpose of genetical systems is to contain all the information sufficient to specify a living thing, application of statistical techniques built around the notion of "information" as a fundamental quantity seems quite natural.

There is a formal definition for entropy.

.. math::
    H = -\sum_{i=0}^n p_i \log_2(p_i)

where :math:`H` is Shannon entropy, `p` is a series of probabilities with `n` members and :math:`p_i` the probability of state `i`. In words, entropy is calculated as the sum of :math:`p_i\log_2(p_i)`. Further, in words the latter can be described as multiplying a probability by the log base 2 of itself.

.. note:: :math:`\sum_{i=0}^n` means take the sum of the series starting at index 0 and ending at index `n`.

Measuring entropy for a simple alignment
----------------------------------------

Here's the simple alignment from the previous section.

.. code-block:: text
    
    TCAGA
    TTCCA
    TTCCA
    TTTTC
    TTTTC

Applying Shannon entropy to the sample alignment above gives:

.. code-block:: text
    
    Pos.   0     1     2     3     4
           T     C     A     G     A
           T     T     C     C     A
           T     T     C     C     A
           T     T     T     T     C
           T     T     T     T     C
    Ent.   0    0.72  1.52  1.52  0.97

In the previous section, the display of coloured letters describing sequences that bind to TBP is referred to as a sequence logo :cite:`Schneider:1990aa`. That representation is computed using position-wise entropy.

.. _information:

Information at a position
-------------------------

.. math::
    R_i=\log(n) - H_i

where :math:`R_i` is the information at position `i`, `n` is the number of possible states (4 for DNA), :math:`\log(n)` is the maximum possible entropy, and :math:`H_i` is the Shannon entropy for position `i`.

In this display, the letter height at a position is :math:`p_{i,l} R_i`.

Problems with sequence logo
---------------------------

The background genomic distribution is assumed to be equally frequent nucleotides. Replacing :math:`\log(n)` with the entropy of the genome can lead to :math:`R<0`.

Using relative entropy as an alternate
--------------------------------------

Relative entropy (`RE`) is defined as

:math:`RE_i = \sum_{i=0}^n p_i \log(p_i / q_i)`

where :math:`q_i` is the background (e.g. genome) frequency of `i`.

An illustration of the difference -- identifying neighbouring base effects on mutation
--------------------------------------------------------------------------------------

:math:`C\rightarrow T` mutations in vertebrates typically arise from deamination of 5-methyl-cytosine. The latter modification is typically applied to `5'-CpG-3'`. Hence, there is a striking association of `3'G` and this point mutation direction.

If we sample sequences that share this mutation in common, aligning them centred on the mutated position, we can assess which statistic better captures the neighbouring base association. What we *should* see is that the 3' position should have high information which arises from the base `G`.

.. todo:: use latest images from mutation motif

.. list-table::

    * - .. image:: /_static/images/seqcomp/CtoT_MI.png
            :scale: 50 %
      - .. image:: /_static/images/seqcomp/CtoT_RE.png
            :scale: 50 %

These results originated from the honours research project of Ms Yicheng Zhu :cite:`Zhu:2017aa`.

Exercises
=========

Defining a short sequence for use below.

.. jupyter-execute::

    seq = "AGCCATTGCAAA"

#. Write a function that converts ``seq`` into counts of nucleotides. (Use the standard library ``collections.Counter`` class.)

#. Write a function that takes a dict like object (e.g. the counter you've just created from (1)) of counts and converts it to numpy array whose length is 4.

    You should consider it critical that your function always returns arrays where the counts for each nucleotide are always in the same position. For instance, if you define the state order as T, C, A, G then the counts for T are always at index 0 -- even if a T was not observed.

#. Write a function that converts these counts into a frequencies.

#. Converting the mathematical expression for entropy into a Python function. Apply it to the results from applying the functions you wrote for (1-3) to ``seq``.

#. Apply the functions you've written to the following randomly generated sequence.

    .. jupyter-execute::
        :hide-code:

        from random import choices
    
        rand_seq = "".join(choices("AAACCGGGG", k=50))
        rand_seq

    What do you observe? Why is it happening?

#. Modify your function for answer (3) so, if there are zero values, it adds a pseudocount to **all** of the array elements before converting to frequencies. Set a default pseudocount of 0.5.

    Make sure your frequencies sum to 1.

    Is there another approach to solving this issue?

------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha
