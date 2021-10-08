.. jupyter-execute::
    :hide-code:

    import set_working_directory


.. sidebar:: Substitution models
    
    .. index::
        pair: Substitution models; screencasts
    
    .. raw:: html
    
        <video width="50%" height="50%" controls>
          <source src="https://cloudstor.aarnet.edu.au/plus/s/HwpLTt8oZxyCP7N/download" type="video/mp4">
          Your browser does not support the video tag.
        </video>

Substitution models
===================

As we demonstrated, calculating a likelihood requires a matrix of substitution probabilities. We can define such matrices in two ways. In the first, we simply specify a matrix of probabilities which we have denoted |P|. This corresponds to a discrete-time Markov process. This class of Markov process (substitution model) is not widely used because every possible exchange requires a separate probability and this means the number of free parameters in the model is proportional to the square of the matrix dimensions multiplied by the number of edges on a phylogenetic genetic tree.

The second approach uses an instantaneous transition rate matrix which we denote |Q|. This is a mathematical precursor to |P| that corresponds to a continuous-time Markov process. In this class of model, we do not define a matrix of probabilities but instead define a matrix of instantaneous rates. This is the most commonly used category of substitution models for molecular evolutionary analyses. Their popularity stems in part because they enable an intuitive measurement of elapsed time (described below) and because they can be defined with a very small number of parameters. Their construction can also be related to chemical and or biochemical properties of DNA. We will focus on this category from now on.

.. index::
    pair: rate matrix; substitution model
    pair: Q; substitution model

Time reversible continuous-time substitution models
---------------------------------------------------

.. todo:: analytical solutions for some processes

Recall the following equation.

.. math::

    P_t = \exp^{Q}

This shows how the substitution probabilities needed to compute a likelihood are obtained from a rate matrix |Q|. The properties of |P| are that all elements are valid probabilities and the row sums are 1. There are constraints on the construction of |Q| such that it can be used to generate a valid |P|. Those constraints are:

- off-diagonal elements are positive
- row sums are 0

The following is an example of such a matrix. The constraint that rows sum to 0 is achieved by setting the diagonal element as equal to the negative of the sum of the remaining elements.

.. jupyter-execute::
    :hide-code:

    from cogent3 import make_table

    data = {
        "": ["T", "C", "A", "G"],
        "T": [
            -0.015739182237141117,
            0.004976556304570878,
            0.004976556304570878,
            0.004976556304570878,
        ],
        "C": [
            0.0036135504377138856,
            -0.01710218810399811,
            0.0036135504377138856,
            0.0036135504377138856,
        ],
        "A": [
            0.007763525366856285,
            0.007763525366856285,
            -0.012952213174855709,
            0.007763525366856285,
        ],
        "G": [
            0.004362106432570946,
            0.004362106432570946,
            0.004362106432570946,
            -0.01635363210914105,
        ],
    }

    Q = make_table(data=data, index_name="", title="Q")
    Q.set_repr_policy(show_shape=False)
    Q

It is typically the case that the Markov process is assumed to be :index:`time-reversible`. This means that, the probability of the forward and reverse substitutions are equal. For example, for a given time period |t|, a |CtoT| occurs with the same probability as |TtoC|.

.. jupyter-execute::
    :hide-code:

    data = {
        "T": [0.2402306967984934],
        "C": [0.17443502824858756],
        "A": [0.3747645951035782],
        "G": [0.21056967984934086],
    }
    pi = make_table(data=data, title="π")
    pi.set_repr_policy(show_shape=False)
    pi

.. jupyter-execute::

    from_t = pi[0, "T"] * Q["T", "C"]
    to_t = pi[0, "C"] * Q["C", "T"]
    from_t, to_t

.. note:: These values are not identical due to the limits of numerical precision.

.. _jc69:

The Jukes-Cantor substitution model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Jukes-Cantor 1969 model (abbreviated JC69) :cite:`Jukes:1969aa` was the first published substitution model. It assumes all bases are equally frequent and that all substitutions occur at the same rate, irrespective of the identify of the bases being exchanged.

.. math::

    \begin{matrix}
     & \begin{matrix} {\bf A}\; & {\bf C}\; & {\bf G}\; & {\bf T} \end{matrix} \\
    Q = \begin{matrix} {\bf A} \\[1mm] {\bf C} \\[1mm] {\bf G} \\[1mm] {\bf T} \end{matrix} &
          \begin{bmatrix}
                \frac{-3}{4} &  \frac{1}{4} &   \frac{1}{4} &  \frac{1}{4}\\
                \frac{1}{4}  & \frac{-3}{4} &   \frac{1}{4} &  \frac{1}{4}\\
                \frac{1}{4}  &  \frac{1}{4} & \frac{-3}{4}  &  \frac{1}{4}\\
                \frac{1}{4}  &  \frac{1}{4} &   \frac{1}{4} &  \frac{-3}{4}\\
           \end{bmatrix}
        \end{matrix}

.. _f81:

F81
^^^

Described by Felsenstein in his seminal 1981 paper :cite:`Felsenstein:1981aa`. This matrix is time reversible and, therefore, stationary. The |pi| elements correspond to the stationary nucleotide frequencies. F81 allows nucleotide frequencies to differ (e.g. :math:`\pi_A \neq \pi_C`) but assumes all exchanges otherwise occur at the same rate.

.. note:: In the following definition, "\ :math:`-`\ " is being used for diagonal elements to simplify the expression. Those elements are computed as the negative sum of the remaining elements on the row.

.. math::

    \begin{matrix}
     & \begin{matrix} {\bf A}\; & {\bf C}\; & {\bf G}\; & {\bf T} \end{matrix} \\
    Q = \begin{matrix} {\bf A} \\ {\bf C} \\ {\bf G} \\ {\bf T} \end{matrix} &
      \begin{bmatrix}
            - & \pi_C  &  \pi_G  &  \pi_T \\
        \pi_A &   -    &  \pi_G  &  \pi_T \\
        \pi_A & \pi_C  &  -      &  \pi_T \\
        \pi_A & \pi_C  &  \pi_G  &  -\\
      \end{bmatrix}
    \end{matrix}

.. _hky85:

HKY85
^^^^^

Named after its authors :cite:`Hasegawa:1985aa`, the Hasegawa-Kishino-Yano (HKY or HKY85) model includes an additional exchangeability parameter [#]_ |kappa|. This parameter is within matrix cells that correspond to :index:`transition substitutions`. Because the parameter is applied multiplicatively in the matrix (discussed below), it is the ratio of transition / transversion substitution rates.

.. [#] I use the term "exchangeability parameter" to refer to a parameter in a rate matrix that is not an element of |pi|.

.. math::

    \begin{matrix}
     & \begin{matrix} {\bf A}\quad & {\bf C}\quad & {\bf G}\quad & {\bf T} \end{matrix} \\
    Q = \begin{matrix} {\bf A} \\ {\bf C} \\ {\bf G} \\ {\bf T} \end{matrix} &
      \begin{bmatrix}
            -         &    \pi_C        &  \pi_G {\color{blue}\bf\kappa} &  \pi_T \\
        \pi_A         &               - &  \pi_G        &  \pi_T {\color{blue}\bf\kappa}\\
        \pi_A {\color{blue}\bf\kappa}  &    \pi_C        &        -      &  \pi_T \\
        \pi_A         &  \pi_C {\color{blue}\bf\kappa}   &  \pi_G        &  -\\
      \end{bmatrix}
    \end{matrix}

The rate matrix of the HKY85 model illustrates a fundamental structure shared with all time-reversible Markov processes. Namely, that the exchangeability parameters are symmetric across the diagonal. As a consequence, time-reversible matrices can be expressed as the product of a diagonal matrix of the |pi| terms and a symmetric matrix consisting of the exchangeability terms.

.. _gtr:

GTR
^^^

GTR stands for General Time Reversible :cite:`Lanave:1984aa`. It is the most general nucleotide substitution model that is time-reversible. This model contains 6 additional parameters: |alpha|, |beta|, |gamma|, |delta|, |epsilon| and |zeta|. This model is saying that all of the possible nucleotide exchanges have distinctive rates.

.. math::

    \begin{matrix}
     & \begin{matrix} {\bf A}\quad & {\bf C}\quad & {\bf G}\quad & {\bf T} \end{matrix} \\
    Q = \begin{matrix} {\bf A} \\ {\bf C} \\ {\bf G} \\ {\bf T} \end{matrix} &
      \begin{bmatrix}
            -         &    \pi_C \alpha &   \pi_G \beta &  \pi_T \gamma\\
        \pi_A \alpha  &               - &  \pi_G \delta &  \pi_T \epsilon\\
        \pi_A \beta   &    \pi_C \delta &        -      &  \pi_T \zeta\\
        \pi_A \gamma  &  \pi_C \epsilon &  \pi_G \zeta  &  -\\
      \end{bmatrix}
    \end{matrix}

Notice again that the exchangeability parameters are symmetric across the diagonal.

.. index::
    triple: stationary; stationarity; Markov process

Stationarity – base frequencies constant through time
-----------------------------------------------------

A |P| matrix specifies the probabilities of changing from one base into another for a specific time period. So what will the base frequencies be at the end of that time period?

Let us set |pi|\ :math:`(0)` as the base frequencies at the beginning of our time interval and |P|\ :math:`(t)` as the substitution probability matrix for time |t|. We then obtain the base frequencies at time |t| as

.. math::

     {\mathbf \pi}(t) = {\mathbf \pi}(0) \cdot {\mathbf {\rm P}}(t)

where ":math:`\cdot`" is |matmul|_ [#]_. If |pi|\ :math:`(0)` equals |pi|\ :math:`(t)` then the base frequencies have not changed and we can state that |pi|\ :math:`(0)` is the stationary frequency vector of |P|. This is the condition of stationarity. For simplicity, we just denote this stationary vector as |pi|.

.. [#] Matrix multiplication is also often referred to as a "dot product". This is available in ``numpy`` as ``numpy.dot()`` or using the  ``@`` symbol, e.g. ``pi @ Q``.

In the case of a continuous-time Markov process, we can operate directly on the rate matrix |Q| without needing to specify a time period. Recall that the rate matrix specifies the instantaneous rates of exchanges between states. If |pi| is the stationarity frequency vector, then there will be *no* exchanges and we expect a vector of zeros. Thus,

.. math::

    {\mathbf \pi} \cdot {{\mathbf\rm Q}} = \mathbf{0}

where :math:`\mathbf{0}` is a vector of zeros and indicates that |pi| is the stationary frequency vector of |Q|.

All time-reversible substitution models are stationary Markov processes. However, not all stationary Markov processes are time-reversible.

.. _exchangeability:

The behaviour of parameters in |Q|
----------------------------------

For the models I'm presenting, exchangeability parameters are applied "multiplicatively" in the rate matrix. By this I mean the parameters in a "rate matrix cell" are multiplied together [#]_. From the definition of a rate matrix, the only constraint operating on exchangeability parameters is that they are ≥0. This construction means that setting an exchangeability parameter value to 1 means it has no effect on the instantaneous rate of change. Setting :math:`\kappa=1` in HKY85 simplifies the expression to produce the F81 rate matrix definition.

.. [#] This is not a strict requirement of continuous-time Markov processes.

The multiplicative construction of the rate matrices also provides guidance for interpreting parameter estimates from a model. Parameters whose estimate is <1 are reducing the instantaneous rate of change for the substitutions they influence compared to the remainder. The converse applies when they are > 1.

As you will see below, we typically define one exchangeability parameter as the reference parameter, setting it to the value 1. This effectively means that all other exchangeability parameters are relative to this term. Which parameter is chosen to be the reference is arbitrary. This strategy is used to allow including a time parameter in our models of sequence evolution.

*Time* in molecular evolution
-----------------------------

What we call "time" in molecular evolution is not chronological time as we know it in our daily lives, but a measure of sequence change. Recall that Kimura showed the rate of substitution is equal to the neutral mutation rate for neutrally evolving genetic variants. Time comes into this via the neutral mutation rate as this quantity is measured as the probability of mutation *per generation*.

.. index::
    pair: branch length; expected number of substitutions

In molecular evolutionary analyses, we measure time (|t|) as the *expected number of substitutions* per position. This is a product of the amount of elapsed chronological time and the mutation rate. For a stationary Markov process, we obtain the expected number of substitutions by multiplying the base frequencies by the *flow* away from the base (the diagonal element of |Q|) [#]_.

.. [#] For a non-stationary Markov process, the calculation is trickier :cite:`Kaehler:2015aa`.

.. math::

    t=-\sum_{i=1}^4\pi_i Q_{i,i}

Although it is not possible to extract chronological time from just sequence divergence data alone, methods exist that use datings from the fossil record to facilitate estimation of chronological times.

.. index::
    pair: calibration; rate matrix

.. _calibration:

Calibrating rate matrices to facilitate estimation of time on a tree
--------------------------------------------------------------------

In order to estimate the expected number of substitutions on all the branches on a tree, molecular evolutionary software often employs a trick. It uses a rate matrix that has been calibrated such that |t|\ =1.

The calibration step involves calculating |t| for a given |Q| according to the equation above and dividing both sides by it.

There is a major computational advantage of this approach. Specifically, the eigendecomposition_ algorithm for matrix exponentiation allows us to do the algorithmically "hard part" once for an entire tree and store the next to final step in the computation :cite:`Schranz:2008aa`. That final step — producing the different substitution probability matrices for edges with different |t| (|P|\ :math:`(t)`) — is very efficiently obtained by applying the corresponding branch length to this intermediate product.

By specifying time as a parameter in our models, we must eliminate another parameter to avoid over specifying the model [#]_. This is achieved by selecting a reference exchangeability parameter and setting it to 1.

.. [#] This basically means adding more parameters than the model can possibly accomodate.

.. _eigendecomposition: https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix

Assumptions of substitution process
-----------------------------------

time-reversible
    That the rate of forward substitutions is equal to their reverse rate. The consequence is that evolution looks the same going forwards or backwards.

stationary
    The sequence composition, or frequencies of the states, is the same across the data set. An assumption of all time-reversible models and some others too. This becomes less likely with increasing time since species shared a common ancestor.

time-homogeneous
    The substitution process remains the same *along* each branch. Translated, this means the same intrinsic dynamics governing mutation, and therefore substitution, operate across the entire branch for every branch that we might be analysing. If the lineages aren't too long then this seems a pretty reasonable assumption. If we assume a single rate matrix for the entire tree we are further assuming the mutation and substitution processes have not changed between the different edges. As you increase the time depth of your sample, this assumption can be more problematic since the potential for changes affecting mutation increase. Accordingly, in such circumstances this property should be checked for :cite:`Verbyla:2013aa`.

Exercises
=========

#. What constraints would you impose on HKY85 to make it F81?
#. Assume I have a rate matrix cell :math:`q_{i,j}=r_j\theta`. Holding :math:`r_j` fixed, what will be the effect on the magnitude of :math:`q_{i,j}` if

    a.) :math:`\theta<1`?
    b.) :math:`\theta>1`?
    c.) :math:`\theta=1`?

Advanced exercises
------------------

#. Show that JC is a time-reversible process.
#. Scale the JC matrix such that :math:`t=1`.
#. With |pi|

    .. jupyter-execute::

        pi = {
            "T": 0.2402306967984934,
            "C": 0.17443502824858756,
            "A": 0.3747645951035782,
            "G": 0.21056967984934086,
        }

    is the following a calibrated matrix?

    .. jupyter-execute::
        :hide-code:

        from cogent3 import make_table

        Q = make_table(
            data={
                "": ["T", "C", "A", "G"],
                "T": [
                    -0.8501619185546586,
                    0.7306386623954628,
                    0.13118318481801372,
                    0.13118318481801372,
                ],
                "C": [
                    0.5305274363890622,
                    -1.0502731445610591,
                    0.09525403228823925,
                    0.09525403228823925,
                ],
                "A": [
                    0.20464833927513754,
                    0.20464833927513754,
                    -0.8668647364719968,
                    1.1398106325659745,
                ],
                "G": [
                    0.11498614289045887,
                    0.11498614289045887,
                    0.6404275193657437,
                    -1.3662478496722275,
                ],
            },
            index_name="",
            digits=6,
        )
        Q.set_repr_policy(show_shape=False)
        Q

#. Test if the following orthologous sequences have been generated by the same stationary process.

.. jupyter-execute::

    seq1 = (
        "TCCAAGTGCCTAACTACAGTAAGTACTTACAGTCAAGCATCAGTATGAAT"
        "TTGGTCCAAGATGTTTCGTGAAAGTGAGACAGTTATTATTTGAAATCCTG"
        "ATTGGTCATTAGATTTCATTGGTAATCAATTAGCTATGATATTTTAGAAC"
        "AGCTTTTGTAATATAATCCAAAGTTACAATGACTGGGACCCCACTATATA"
        "TAAATTTGAGAAAGTCCATAAGTAGATAACTTTGTTCGAATGATAGTTAG"
        "ATGATCAGGGTTAGGTTTTTTTGTAAATTTTGTGATTCAAAACAAATTCA"
        "GATATACCTACTGACAATCCTAAATAGTGGGGGTTCGTTTGTAAACTATA"
        "CATTTTAGATTTTTCTAGAGAAGCCAGACGCCACAACGATATATACGGTC"
        "GATAGATAATCCTTCAGGGAATATTTTTGTATCTATAATCTTCTAAAAAA"
        "GAAAATATTACCAGATAAGTGATAATAGTCTTAGATTTTTCTGATCGAGA"
    )

    seq2 = (
        "TCTAATTACCTAGCCACAGTAAGTACCTACAGTCAAGCAGCTCTATGAAT"
        "CTGCATCTGGTGGTCTTGTGGACAGGGGGCTGCTATTGCGTACAGACCTG"
        "ATTGGACATTCTACTTCCCTGCTGGCAGGTTCAATGTCAGATTCTTGGTC"
        "AGTCCTTTCGATGTAACTCGTAACTATAATAACTGAGATCTTGTTATACG"
        "TTATGTTTCGCTAGTCACCGAGTAAGCATCGGTGTCCGGGCTATCACTAG"
        "ATCTTCATCAACAGGCGTCTTTGGACATTTAGAGATTGAAGTGGAACTCA"
        "TAAGTATCCACTGGTAATTATCAGAAACGGGGGTACGCCTTTGCATTACA"
        "CTTTGTAGGCTCTCCTAGAGAATTAGGACACCAGTGGAAAATGTACGGCT"
        "GATCAAAATTCTATCAAAAAACGTCTTTCTATTTGTAGATCCTCAAAATA"
        "GCGAACACCACATGCGTAGGGATAACAACGGTGGTTTTTGCTGCTCAGTA"
    )

------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha
