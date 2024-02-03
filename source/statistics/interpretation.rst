.. jupyter-execute::
    :hide-code:

    import set_working_directory


Step 4 -- Interpretation and looking past the |pvalue|
======================================================

In the :ref:`listing of 4 essential steps <essential_steps>` for data analysis, the final listing concerns interpreting the results of our analysis with respect to our original question.

Case Study 1
------------

I reproduce below the result from analysis of :ref:`case study 1 <case_study_1>` sequence.

.. jupyter-execute::
    :hide-code:

    from book_code import case_studies as cs

    seq = cs.get_seq("data/case_study1.fasta")
    cs1_ccounts = cs.to_4x4(cs.to_dinucs(str(seq)))
    cs1_chi_test = cs1_ccounts.chisq_test()
    cs1_chi_test.statistics

As explained earlier, the |pvalue| measures the probability that ``seq`` originated from a process whereby nucleotides occur independently. A |pvalue|\ :math:`\approx`\ 0.007 indicates this is a rare occurrence. Adopting the conventional threshold of |alpha|\ =0.05 as our cutoff for declaring we have obtained a "significant" result, we reject that null model as a likely explanation for ``seq``. This leads us to the view that nucleotides actually occur in a dependent manner. That seems OK, but we need to challenge our own interpretation.

Simply drawing a conclusion about our data based on the |pvalue| can be misleading. The amount of data has a direct effect on the power of a statistical test. This translates to |pvalues| being very sensitive to sample size. For instance, what if we had an enormously long sequence? The :index:`statistical power` in such a case is so high that we would almost certainly wind up with a tiny |pvalue| [#]_. We might be able to convince ourselves that this is not the case here since the sequence is only 600bp long (as distinct from billions of nucleotides long in the case).

.. margin::

    .. [#] A difference in nucleotide frequency at the 3rd decimal place proved highly significant when the whole vertebrate genome sequences of Mouse and Rat were compared :cite:`2004.Cooper`! How meaningful is such a result? That's a good question for which there is no simple answer.

A more valuable measure is to consider how the data depart from the expectation of the null hypothesis. For categorical data analysis, as we have done here, one very informative quantity are the model :index:`residuals`. A residual is a scaled measure of the difference between the observed and expected quantities.

.. jupyter-execute::
    :hide-code:

    residuals = cs1_chi_test.residuals.to_table()
    residuals.set_repr_policy(show_shape=False)
    residuals.title = "Residuals"
    residuals

The other merit of examining residuals is that we move from saying that our data differs from the null to demonstrating how that difference occurs. In the above case, the largest absolute residual is -2.7 for the CG dinucleotide. That the residual is negtaive indicates a striking deficit in our data compared to what our null model predicts. This matches up with published data about mutagenesis. Namely, that the CG (or more precisely CpG) dinucleotide is the sequence context within which C becomes methylated (to produce 5-methyl-cytosine, or 5mC). It has been demonstrated that the mutation rate of :math:`5mC\rightarrow T` is ~10x the mutation rate of :math:`C\rightarrow T`. This mutagenic mechanism thus predicts a deficit of the CpG dinucleotide. So in this case, we have a result which is consistent with evidence from independent studies :cite:`1998.Krawczak.000`.

Case Study 2
------------

By now you've probably been wondering why I bothered even having the second case study. Fear not, its time has finally come!

:ref:`Case Study 2 <case_study_2>` was selected because it is nearly the reverse of a conventional statistical analysis. Typically, the scientist secretly hopes their statistical analysis will have provided evidence (i.e. a |pvalue|) that enables them to conclude their null model is unlikely. Thus, their interest in the outcome is maximised when the null is rejected. Recall that our null model for this case study is that a query sample is drawn from the same distribution as our reference sample which is the *V. cholerae* 16S gene. If the test returns a |pvalue|\ >0.05 we face the unpleasant prospect of dealing with an outbreak of cholera. In other words, our interest is maximised when the null is accepted.

There are a multitude of reasons why this approach to detecting cholera is super bad and should never be used. In order to explore these we need to think about what underpins our choices. We could reasonably expect that the DNA sequence of *V. cholera* encodes the pathogenicity of this bacteria. In order to fit that genomic sequence into a conventional statistical analysis we have adopted an extreme data reduction approach -- we selected a single gene and we reduced that gene into just the counts of nucleotides. In doing such a radical data transformation we are assuming that we can uniquely identify a pathogenic cholera bacterium purely from this approach.

The test we employed required the assumption that the genome of cholera exhibits a distinctive nucleotide composition to the sequences of other bacteria. Not only do we require all other bacteria to be markedly different to cholera, we also require all pathogenic cholera to *not* differ markedly from one another. Ultimately, the mechanism that causes species to differ in the nucleotide abundance is mutagenesis. As our first case study highlighted, mutagenesis is a process in which interactions amongs neighbouring bases can play a profound influence. But the analysis we employed assumed this influence does not exist.

In brief, we should not be confident in the results we obtain from this approach. Clearly, the model used is seriously wrong. In the next section we will demonstrate how model choice can profoundly affect your results.

------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha

