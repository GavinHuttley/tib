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

.. topic:: You Try
    
    Converting that mathematical expression into a Python expression.

Measuring entropy for a simple alignment
----------------------------------------

Here's the simple alignment from the previous section ::
    
    TCAGA
    TTCCA
    TTCCA
    TTTTC
    TTTTC

and here's the entropy calculation. ::

    Applying Shannon entropy to the sample alignment above gives:

    Pos.   0     1     2     3     4
           T     C     A     G     A
           T     T     C     C     A
           T     T     C     C     A
           T     T     T     T     C
           T     T     T     T     C
    Ent.   0    0.72  1.52  1.52  0.97

In the previous section, the display of coloured letters describing sequences that bind to TBP is referred to as a sequence logo [1]_. That representation is computed using position-wise entropy.

.. [1] *Schneider & Stephens (1990). Sequence logos: a new way to display consensus sequences. Nucleic Acids Research, 18(20), 6097–100.*

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

    * - .. image:: /images/CtoT_MI.png
            :scale: 50 %
      - .. image:: /images/CtoT_RE.png
            :scale: 50 %

These results originated from the honours research project of Ms Yicheng Zhu, published in [2]_.

.. [2] *Zhu, Neeman, Yap, Huttley (2017). Statistical Methods for Identifying Sequence Motifs Affecting Point Mutations. Genetics, 205, 843–856*
