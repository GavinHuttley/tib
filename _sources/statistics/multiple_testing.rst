.. individual result view versus a distributional analysis view, how those are related
.. multiple test correction
.. false discovery rate

**********************************
Hypothesis testing on genomic data
**********************************

For scientists dealing with genomic data, studies were only a single hypothesis test is performed are rare. Rather, the same hypothesis test may be employed thousands, or hundreds of thousands of times. For instance, Genome Wide Association Studies (or GWAS) evaluate for each Single Nucleotide Polymorphism (or SNP) whether allele counts differ between disease and non-disease samples. With each such test returning a |pvalue|, the risk of incorrectly rejecting a null hypothesis is greatly amplified.

Let's define our significance threshold as per the convention, a |pvalue|\ :math:`\le 0.05`. Drawing on the definition of the |pvalue|, we expected to obtain a significant result 5% of the time. This means that if we looked at GWAS results from 100 SNPs when there is no genetic basis for a phenotype (i.e. the null hypothesis is true), we expect 5 SNPs to be "significant". If we looked at 100,000 SNPs, we expect 5000 to be significant.

This is the critical issue confronting genomics studies with very significant practical implications. It not cost-effective to follow up on each such significant result as if it were an equally likely candidate. Instead, we need to employ statistical procedures that adjust for the number of tests that have been performed and increase our confidence that what we select are true positives.

The Bonferroni correction
=========================

This approach to correcting for multiple tests attempts to control the "number" of errors (false discoveries), specifically the probability of seeing 1 or more such errors. This is a strict, very conservative, approach. In applying this, one is prone to accepting the null hypothesis when it's actually False.

If one conducts :math:`k` statistical tests and the desired significance level is |alpha|, then we compute a corrected significance threshold of :math:`\frac{\alpha}{k}`. If we set |alpha|\ =0.05 and :math:`k`\ =100, then the corrected single test threshold is :math:`\alpha^\prime`\ =0.0005.

