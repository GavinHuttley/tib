.. jupyter-execute::
    :hide-code:

    import set_working_directory

.. _case_studies:

************
Case studies
************

We will develop a perspective on statistical analysis through addressing two different problems. In these case studies, I'm describing the problem in a very procedural way, focussing on the :ref:`essential steps <essential_steps>` to deliver a |pvalue|. I am taking this approach because many of the students (and in fact many of the scientists) I have interacted with believe that this is all statistical analysis entails.

The point of this topic is explain **why** this a manifestly superficial approach to statistical analysis. In subsequent sections I develop our interpretation of the analysis results I obtain here.

.. todo:: proceed from the last back to the first, discovery is never complete!

.. _case_study_1:

Case study 1 – do nucleotides occur randomly in a DNA sequence?
===============================================================

Much of my own research concerns understanding organisation [#]_ of DNA sequences and the mechanisms by which those properties arise. Inevitably, this leads me to asking questions about the role that mutation plays in creating patterns in DNA. This particular case study is focussed on a fundamental property of DNA that has important implications for a large number of fields, including molecular evolutionary analyses such as phylogenetics, and cancer genetics. We now follow the 4-step procedure.

.. [#] By organisation I mean the ordering of nucleotides in a DNA sequence, e.g. does eukaryotic :ref:`DNA organisation <organisation_dna>` manifest in periodic base patterns? I consider understanding such properties as essential to understanding how DNA encodes life.

Step 1 - the biological problem
-------------------------------

.. sidebar:: Data for case study 1
    :name: case_study_1_data
    
    .. jupyter-execute::
        :hide-code:
    
        from book_code import case_studies as cs
        
        seq = cs.get_seq("data/case_study1.fasta")
        seq[:10]

    A 10bp snippet of the sample sequence. Click to download the :download:`sequence data </data/case_study1.fasta>`.

For the :ref:`single DNA sequence <case_study_1_data>`, we want to evaluate whether nucleotides occur randomly along the sequence [#]_. In other words, given a nucleotide ``C``, is its 3'- neighbour a random draw from all 4 nucleotides?

.. [#] We are referring to nucleotides on a single strand of the double-helix.

Step 2 - selecting the measurement
----------------------------------

DNA sequences are represented by the *discrete series* of symbols [#]_ which we can view as categories. As I'm interested in asking whether these symbols occur randomly, my measurement needs to allow me to distinguish between randomness and non-randomness.

In the statistical parlance of categorical analysis, the synonyms for randomness and non-randomness are independence and dependence respectively. These synonyms help me identify the |chisq| test of independence as the test I will use. (Selecting this statistical test means we have selected a model for the null distribution, but more on that when we get to the Interpretation step.)

.. [#] These symbols are the letters of the DNA alphabet `A, C, G, T`.

That all sounds great, but how can I transform my data in such a way that it can be used for this analysis? 

Step 3 - writing the algorithm
------------------------------

In short, we need to produce what's referred to as a contingency-table. This is just a table of counts of the number of occurrences of each possibility. Consider the nucleotide ``A``. For ``seq``, how many times does that occur as: ``AA``, ``AC``, ``AG``, ``AT``? For the nucleotide ``C``, we need to count the number of occurrences of ``CA``, ``CC``, ``CG``, ``CT``. Then for ``G`` and ``T``. The pattern here is we need to count dinucleotides!

Awesome, I need to write an algorithm to convert a sequence into dinucleotides. For example, ``'ATGAAT'`` should be converted to ``['AT', 'GA', 'AT']``. The next part is to convert that series of dinucleotides into a :math:`4\times 4` table with the row labels corresponding to the first (the 5'-) nucleotide of the dinucleotide and the column labels corresponding to the second (3'-) nucleotide of the dinucleotide.

Applying my algorithm to ``seq`` I get

.. jupyter-execute::
    :hide-code:

    result = cs.to_4x4(cs.to_dinucs(str(seq)))
    obs = result.observed.to_table()
    obs.set_repr_policy(show_shape=False)
    obs

Further applying the |chisq| test to this data produces the following *result*, a |chisq| :index:`test statistic`, associated degrees-of-freedom and |pvalue|. (We will expand on these later.)

.. jupyter-execute::
    :hide-code:

    stats = result.chisq_test().statistics[0]
    stats.title = None
    stats.set_repr_policy(show_shape=False)
    stats

.. note:: What we do with this result corresponds to the last of the :ref:`essential steps <essential_steps>`, which we do later.

.. _case_study_2:

Case study 2 – evaluate whether a query sequence belongs to a pathogen
======================================================================

.. sidebar:: Data for case study 2
    :name: Data for case study 2
    
    .. jupyter-execute::
        :hide-code:

        table = cs.get_table("data/ncbi_dataset/vibrio_cholera/v_cholera_16SrRNA.tsv")

        ref = table.filtered(lambda x: x, columns="is_ref")
        ref = ref[:, :-1]
        ref.title = "Reference"
        ref.set_repr_policy(show_shape=False)
        ref

    .. jupyter-execute::
        :hide-code:
    
        query = table.filtered(lambda x: not x, columns="is_ref")
        query.title = "Query samples"
        query[:, :-1]
        
    Nucleotide counts from the 16S rRNA gene of the reference and query genomes.

The properties of DNA are often used for identification purposes. In this case study we are interested in the detection of the cholera pathogen in amplicon sequence data. A standard approach in analyses of microbial communities is to use the DNA sequence from the :index:`16S rRNA` gene (hereafter abbreviated 16S) as a species marker. These can be sampled from an environment by PCR amplification and subsequent high-throughput DNA sequencing.

Step 1 - the biological problem
-------------------------------

Our question is whether a "query" 16S DNA sequence could be a member of *Vibrio cholerae* (some strains of which cause cholera).

If the query sequence belongs to *V. cholerae*, then its DNA sequence should be very similar to the reference [#]_ *V. cholerae* pathogen 16S sequence. 

.. [#] We use the NCBI defined reference for *V. cholerae*.

Step 2 - selecting the measurement
----------------------------------

As for :ref:`Case study 1 <case_study_1>`, because DNA sequences are our basic data type we are dealing with categorical data. We can measure the similarity between DNA sequences in a very large number of ways. One computationally efficient way is to just compare nucleotide counts. If the query belongs to a different species than the reference sequence, we expect the abundance of nucleotides will be less similar than if it is from the same species. In other words, I'm expressing this measurement problem as one of establishing whether a query *is not* *V. cholerae*.

Conveniently, this problem can also be evaluated using a |chisq| test. In this case, it is a homogeneity test [#]_.

.. [#] Which tests whether the query comes from the same population as the reference.

Step 3 - writing the algorithm
------------------------------

The first part of the algorithm here is quite simple. For each sequence, we count the number of ``A``, ``C``, ``G`` and ``T``. The result of this is displayed in the case study :ref:`data overview <Data for case study 2>`. The second part of the algorithm selects the counts for a single query and combines those with the counts from the reference, to produce a :math:`2 \times 4` contingency table. For example, with ``AP023375.1`` as the query we generate

.. jupyter-execute::
    :hide-code:

    c = ref.appended(None, query[0][:, :-1])
    c.index_name = "ID"
    c.set_repr_policy(show_shape=False)
    c

Performing the |chisq| homogeneity test produces a |chisq| :index:`test statistic`, associated degrees-of-freedom and |pvalue|.

.. jupyter-execute::
    :hide-code:

    t = c.to_categorical().chisq_test()
    csq = t.statistics
    csq.title = None
    csq

This procedure needs to be applied to all the query samples. Again, we will perform the last, interpretation, of out :ref:`essential setsp <essential_steps>` later.
