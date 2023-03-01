.. jupyter-execute::
    :hide-code:

    import set_working_directory

.. wrong_models:

Acknowledging the limits of an analysis
=======================================

.. epigraph::

    “Since all models are wrong the scientist must be alert to what is importantly wrong.”

    --- Professor George Box, :cite:`Box1976`

The impact of model choice
--------------------------

It's easy to claim all models are wrong and that we should be cautious, but nothing beats a demonstration of how a seemingly simple analysis can be prove remarkably misleading. In this spirit, I have generated :download:`synthetic sequences </data/wrong_model.fasta>` based on the reference *V. cholerae* genome.

.. tab-set::
    
    .. tab-item:: Comparing nucleotide frequencies

        We use the |chisq| test for homogeneity on nucleotide counts on the two synthetic sequences. With a |pvalue|\ :math:`\approx`\ 0.69, we cannot reject the null.

        .. jupyter-execute::
            :hide-code:

            from cogent3 import load_unaligned_seqs

            def get_test_result(seqs, motif_length=1):
                c = seqs.counts_per_seq(motif_length=motif_length)
                t = c.to_table().to_categorical()
                return t.chisq_test()

            seqs = load_unaligned_seqs("data/wrong_model.fasta", moltype="dna")
            nuc_result = get_test_result(seqs, motif_length=1)
            nuc_result.statistics

    .. tab-item:: But, using a different model!

        We employ the same test, but we apply it to *dinucleotide* counts of the two synthetic sequences (rather than nucleotide counts). The resulting |pvalue| is so small, it is below the limits of my computers precision to compute it.

        .. jupyter-execute::
            :hide-code:

            dinuc_result = get_test_result(seqs, motif_length=2)
            dinuc_result.statistics

This example was deliberately constructed to demonstrate that applying different models to the same data can result in contradictory outcomes. In this case, because I generated the data I knew this problem existed. I can say that analogous situations do arise in the analysis of real data too.

So how do you address such a possibility when analysing real data? You must employ your expert knowledge of the scientific domain. Specifically, based on what you understand about the experimental procedures, biological and/or chemical properties of the system you are examining, is the model you have used reasonable? Has it been used by others [#]_? In our first case study we demonstrated that nucleotides do not occur randomly, a property demonstrated as characteristic of our own genome and which has been argued to originate from mechanisms of mutagenesis :cite:`Simon2020`.

The most critical step you can take is in acknowledging the uncertainty present in any analysis. Your conclusions are based on the assumptions required by the model and if those are incorrect, your conclusion may be also.

.. [#] Presumably if a method has been used by other scientists, they have established its suitability. Unfortunately, that is not always correct.

------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha

