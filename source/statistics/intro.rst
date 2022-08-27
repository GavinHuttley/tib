******************************
Evidence based decision making
******************************

.. sidebar:: The 4 essential steps for correct data analysis!
    :name: essential_steps

    What a click-bait title! Whatever, here's the steps:

    #. State the biological problem or question
    #. Decide what measurement you will use from your data that will allow you to answer the question
    #. Write the algorithm that performs the measurement
    #. Interpret!

Hypothesis testing is a conventional application of using statistics to arrive at a decision. I'm going to present hypothesis testing principally by focussing on the null hypothesis (denoted |Ho|). This corresponds most closely with the approach for data analysis advocated by Fisher (see :cite:`Perezgonzalez:2015aa`).

In the Fisherian approach, the null corresponds to some notion of how we think the data may be distributed. In the upcoming case studies, we will pose the null hypothesis that two sequences are from the same distribution. To quantify this, we will select our statistical procedure and decide, *a priori*, on our significance threshold (often referred to as the |alpha| level and typically set as 0.05). We will compute our test-statistic and obtained the corresponding |pvalue| from the theoretical distribution. Based on the relationship between those two quantities, a decision will be made.

Central to this approach is the chosen significance threshold as it governs what decision to make for a given |pvalue|. It is a value decided on by the scientist for when to reject the null hypothesis as an acceptable explanation for the data. It is often described as being how often the scientist is prepared to be wrong. In the Fisherian approach, which does not formalise the role of an alternate hypothesis, this is a sufficient basis for pursuing additional experimental avenues. Dues to the very definition of a |pvalue| (coming up in the next section), it cannot be proof that a null hyothesis is wrong.

The notion of an alternate hypothesis (denoted |Ha|) originates from the framework of Neyman-Pearson. There are overlaps in outcome with the approach of Fisher, but significant differences too (again, see :cite:`Perezgonzalez:2015aa` for an accessible summary). You will also encounter the Neyman-Pearson approach in these notes.

So how does this hypothesis testing paradigm fit with the "4 essential steps"? It is in effect all 4 steps. However, hypothesis testing is not the only approach to statistical analysis and the |pvalue| is not the only measure on which to base decisions.


------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha

