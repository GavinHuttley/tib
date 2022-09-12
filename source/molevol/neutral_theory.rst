.. sidebar:: Variation in proteins seems to accumulate linearly with time
    :name: molecular_clock

    .. image:: /_static/images/molevol/molecular_clock.png
        :scale: 50%
    
    Number of amino acid differences versus species divergence time. The former were estimated allowing for multiple changes, the latter derived from paleontological studies. Mean error in estimate of amino acid differences are indicated by the vertical bars [1]_. Figure from :cite:`Dickerson:1971aa`.

.. [1] Amusingly, there is no such uncertainty portrayed for the paleontological estimates.

*****************************************
The neutral theory of molecular evolution
*****************************************

If the complete DNA sequence of an organism (its genome) encodes that organism then, under Darwin's theory of evolution by natural selection, the attributes that distinguish that organism will also distinguish its DNA from that of others.

While Darwin's theory provides our guidance, including that natural selection is the fundamental driving force underpinning adaptation, it is incomplete. It turns out that evolution also happens entirely by chance and, in fact, this may be the dominant force underpinning the divergence between species. The seeds of this rather remarkable (and simultaneously banal) amendment to Darwin's work originated principally with the population genetic empirical and theoretical work of |Sewall_Wright|_.

Examination of genetic divergence
=================================

We start our exploration of this idea by looking at early results from comparisons of molecular sequences. As displayed in :ref:`the figure <molecular_clock>`, there appeared to be a linear relationship between chronological time and the accumulation of differences in amino acid sequences between species.

This result was difficult to reconcile under a model in which most genetic variation was under the scrutiny of natural selection. In 1968, 2 seminal papers provided an elegant mathematical and conceptual basis for understanding these clock-like behaviours. They also provide the critical framework from within which to examine and understand the forces affecting the distribution of genetic variation, both within and between species.

The Neutral Theory of Molecular Evolution
=========================================

This theory proposes that most genetic variation, both within and between species, has not been affected by natural selection, but instead reflects the influence of chance events on new mutations. The theory was dominantly developed by Motoo Kimura :cite:`Kimura:1968aa` but independently proposed by King and Jukes :cite:`King:1969aa`.

.. sidebar:: Neutral variation
    :name: neutral_variation

    .. digraph:: neutrality

        layout=twopi
        node [shape="circle"];

        R [fontcolor="white" color="blue" style=filled];
        D [fontcolor="white" color="blue" style=filled];
        E [fontcolor="white" color="blue" style=filled];
        H [fontcolor="white" color="blue" style=filled];
        K [fontcolor="white" color="blue" style=filled];
        A [color="#33333555" style=filled];
        G [color="#33333555" style=filled];
        P [color="#33333555" style=filled];
        Q [color="#33333555" style=filled];
        W [color="#33333555" style=filled];
        ellipsis [label="…" color="#33333555" style=filled];
        R -> D;
        R -> E;
        R -> H;
        R -> K;
        R -> A [style=dotted arrowhead=none];
        R -> G [style=dotted arrowhead=none];
        R -> P [style=dotted arrowhead=none];
        R -> Q [style=dotted arrowhead=none];
        R -> W [style=dotted arrowhead=none];
        R -> ellipsis [style=dotted arrowhead=none];

    Each node represents an amino acid (not all amino acids are shown). Hydrophilic amino acids are shown in :blue:`blue`.

A simplified example of neutral evolution
=========================================

Let us begin by making the simplistic assumption that the actual probability of a mutation (in a single generation) to any of the amino acids is equal. We denote this :math:`p(a, b)=\epsilon` where :math:`a, b` are two different amino acids. For a sequence position where any amino acid is allowed, the total probability an existing amino acid changes is :math:`19\epsilon` [2]_.

.. [2] There are 19 amino acids that can be changed into.

Now let us consider an extreme scenario of a specific position in a hypothetical human protein sequence that only tolerates hydrophilic amino acids and any other type is recessive lethal before birth. I have illustrated this hypothetical sequence as having an arginine (``R``, see :ref:`Neutral variation <neutral_variation>`). If we watch that sequence through time, we can never see any changes other than those which generate another hydrophilic amino acid because of natural selection. For this position, the actual total probability of mutation is the same as above. But if viewed from a longer time depth, after natural selection has operated, there can only be 5 hydrophilic amino acids. Thus, the probability of a mutation that is not lethal is :math:`4\epsilon`.

Now imagine we view variation in this protein at the population level. At our strictly hydrophilic position, only other hydrophilic amino acids can exist because they exhibit no difference with respect to natural selection. In this sense, we say they are "neutral" with respect to natural selection (not to be confused with chemically neutral). Now let us examine a different position in our hypothetical protein where, for instance, all amino acids are equivalent. We will see many more distinct variants and, as for the hydrophilic position, all such variants are neutral with respect to natural selection.

.. the fixation probability will be less and ditto for the substitution rate.

What does "neutral" mean?
=========================

A genetic variant is considered selectively neutral, or just neutral, if it is "invisible" to natural selection.
For neutral variation, the evolutionary dynamics (changes in frequency) are dictated by random genetic drift and mutation only (these are the "neutral processes"). But, as Kimura showed, the designation of neutral is a moving target.

.. note:: Random genetic drift is the fluctuation in allele frequencies between generations that occurs due to random sampling of gametes.

Some important results from Kimura
==================================

One important result from Kimura, often referred to as his "rule of thumb", is that natural selection is only effective against random genetic drift when :math:`4N_e s >> 1` where :math:`N_e` is the effective population size and :math:`s` is the selection coefficient. What this means is that, as population size shrinks, the magnitude of natural selection must increase in order overcome the stochastic fluctuations of random genetic drift. Very bad news for endangered species, since deleterious genetic variants can become fixed [3]_.

.. [3] Fixation is the condition in which a genetic variant achieves a frequency of 1.0 (all population members have it). It becomes a substitution when that frequency applies to all members of the species.

Another striking result is that the neutral substitution rate :math:`k` **is** the number of mutations per site per generation :math:`\mu` for strictly neutral variation. Irrespective of population size. This elegant result provides the foundation for why a molecular clock can exist.

Perhaps the most crucial corollary from this body of theory is the theoretical foundations establish how what goes on within a species shapes what we see between species.

Finally, returning to our simplistic example of how variation can be neutral but natural selection can be operated, the following conjecture by King and Jukes provides another key perspective on how this body of work applies to modern day genomics.

.. epigraph::

    “..functionally less important molecules or parts of a molecule evolve faster than more important ones..”

    King and Jukes :cite:`King:1969aa`

Summary
-------

The great value of the neutral theory is as a null hypothesis. Models have been developed for explicitly testing for departure from neutrality for both population genetic and molecular evolutionary analyses. When we can reject the null convincingly, we are able to state that a specific genomic location encodes critical information for the organism. 

While that seems all beautiful, be aware that, as with many other difficult problems, Kimura's theory rests on a number of very restrictive assumptions about biology that are known to be incorrect. Understanding how important those are remains a highly active area of research by many, including myself.

Exercises
---------

#. Use the :ref:`thought experiment <neutral_variation>` to explain the King and Jukes conjecture.

#. Construct an example alignment that illustrates how the King and Jukes conjecture will manifest on real data (don't limit yourself to protein coding DNA sequences). Explain what features of your synthetic alignment relate to the King and Jukes conjecture and why.

#. The characteristic influence of natural selection thus far has been to consider it as a "negative" or "purifying" force. These terms refer to the elimination of a subset of genetic variants due to their deleterious influence on phenotype. What other type of natural selection is there and provide an example showing how that would manifest in real data.

------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha
