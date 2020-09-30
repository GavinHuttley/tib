Statistical tests using ``cogent3``
===================================

The following are a subset statistical tests available within ``cogent3`` organised by analysis problem.

Analyses of categorical data
----------------------------

This involves contrasting counts data against the expectation defined either by another data set or by a prior null hypothesis. The analysis of categorical data is provided by the ``CategoryCounts`` object.

.. note:: The methods on ``CategoryCounts`` also support estimating the |pvalue| using a resampling statistic.

Goodness-of-fit tests
^^^^^^^^^^^^^^^^^^^^^

This type of test compares counts against expected values specified via a prior hypothesis. Here I'll analyse nucleotide counts data, testing the null hypothesis that all bases occur with equal frequency.

.. jupyter-execute::

    from cogent3.maths.stats.contingency import CategoryCounts

    counts = CategoryCounts({"A": 887, "C": 547, "G": 623, "T": 535})
    counts

You can see that the object displays the observed (what we provided), expected values computed as equally frequency values, and the standardised residuals [1]_. Residuals help you interpret where the observed data depart most strongly from the expected values. In this case, the largest absolute value is for the base ``A``. That the residual is positive indicates the observed data has an excess of this base compared to expected (a negative residual indicates a deficit).

.. [1] These are calculated as :math:`\frac{(o-e)}{\sqrt e}` where :math:`o, e` are the corresponding observed and expected values.

``CategoryCounts`` provides several different methods for analysis of categorical data. In this case, we could use either the ``G_fit()`` [2]_ or ``chisq_test()``.

.. [2] G-tests are a likelihood ratio tests and the G statistic is sometimes referred to as G\ :math:`^2`.

.. jupyter-execute::

    result = counts.G_fit()
    result

The statistic, degrees of freedom and associated |pvalue| are all accessible as attributes on the ``result`` object.

.. jupyter-execute::

    result.pvalue

Tests of independence
^^^^^^^^^^^^^^^^^^^^^

.. sidebar:: Constructing ``CategoryCounts`` from a ``Table``

    We can also get to this result via specifying the rows as a list of lists. In doing this, we must add the row label to each row.
    
    .. jupyter-execute::
    
        rows = [["A", 887, 535],
                ["G", 623, 547]]

    We can then create a table from this, by specifying the column header and (importantly) indicating which column corresponds to the row index.
    
    .. jupyter-execute::
    
        from cogent3 import make_table
        
        table = make_table(["", "+", "-"], data=rows, index="")
        table

    The ``Table.to_categorical()`` method returns a ``CategoryCounts`` instance.
    
    .. jupyter-execute::
    
        ssymm = table.to_categorical()
        ssymm

In this type of test, our null hypothesis is that our counts occur independently of specific combinations of categories. Let's assess whether the DNA sequence from which those counts were derived was strand symmetric. The null hypothesis (|Ho|) is that base counts satisfy the following: A=T, G=C. The alternate hypothesis (|Ha|) is they don't, i.e. A≠T, G≠C.

In this case, we need a 2D structure with strand on one axis and base on the other. I pick the purines as my bases on the plus strand, these will be the top-level keys in my 2D dict. The value for each base is a dict with the counts of that base on the plus and minus strands. To reiterate, the keys in the top level dict will become the row labels. The nested dict's must all have the same keys and those keys become the column labels.

.. jupyter-execute::

    data = {"A": {"+": 887, "-": 535}, "G": {"+": 623, "-": 547}}

This can now be used to construct a ``CategoryCounts`` object.

.. jupyter-execute::

    ssymm = CategoryCounts(data)
    ssymm

We use the ``G_independence()`` test to assess the null that the cell counts occur as simply the product of the probabilities of their corresponding categories.

.. jupyter-execute::

    result = ssymm.G_independence()
    result

We reject |Ho| in this case and conclude the sequence is strand-asymmetric with respect to nucleotides.

Analyses of correlations
------------------------

In cases where we have bivariate data we may be interested in whether the two values are correlated. Of course, it would be remiss of me not to remind you of the limits to drawing inferences from correlations.

.. sidebar:: Correlation does not imply causation

    .. figure:: https://imgs.xkcd.com/comics/correlation.png

    See `XKCD <https://xkcd.com/552/>`_ for the original.

    And to drive this point home, see `examples of spurious correlations <http://www.tylervigen.com/spurious-correlations>`_.

We will evaluate these data.

.. jupyter-execute::

    x = (44.4, 45.9, 41.9, 53.3, 44.4, 44.1, 50.7, 45.2, 60.1)
    y = (2.6, 3.1, 2.5, 5.0, 3.6, 4.0, 5.2, 2.8, 3.8)

Compute the Pearson product-moment correlation coefficient and it's |pvalue| (taken from the :math:`t`-distribution assuming the degrees of freedom equals n-2).

.. jupyter-execute::

    from cogent3.maths.stats.test import pearson_correlation

    rho, pval = pearson_correlation(x, y)
    rho, pval

If the data of interest are not normally distributed, one approach to assessing the existence of an association is to use a non-parametric test. In this case we use Kendall's :math:`\tau` (the coefficient of rank correlation), which transforms the data into ranks and compares those.

.. jupyter-execute::

    from cogent3.maths.stats.test import kendall_correlation

    tau, pval = kendall_correlation(x, y, alt="two sided")
    tau, pval

Analyses of distributions
-------------------------

Paired distributions
^^^^^^^^^^^^^^^^^^^^

Say you have paired data -- observations that are coupled in some way, such as from the same individual at different time-points. Specific statistical procedures for this case include the paired :math:`t`-test and the sign test. The former is a parametric statistical procedure, the latter non-parametric.

The paired :math:`t`-test is used to test the null hypothesis that mean (:math:`\bar\mu_d`) of the differences (:math:`d`) between two samples equals 0. There can be different alternate hypotheses (which you pre-specify), e.g. :math:`\bar\mu_d>0` (a one-tailed test). The test has numerous assumptions, including that :math:`d` is normally distributed.

.. jupyter-execute::

    from cogent3.maths.stats.test import t_paired

    x = [7.33, 7.49, 7.27, 7.93, 7.56, 7.81, 7.46, 6.94,
         7.49, 7.44, 7.95, 7.47, 7.04, 7.1, 7.64]
    y = [7.53, 7.70, 7.46, 8.21, 7.81, 8.01, 7.72, 7.13,
         7.68, 7.66, 8.11, 7.66, 7.20, 7.25, 7.79]

    t, pval = t_paired(x, y)
    t, pval

The sign test is basically a binomial test where the frequency is 0.5. In this case, we have the same expectation -- no difference between our two groups. In this case, we turn our paired observations into successes / failures (``x > y``) and sum the number of successes. We need this integer, and the number of "trials" (i.e. how many paired records there are). (Note the use of numpy to simplify the element-wise comparison of ``x`` and ``y`` and to sum the number of ``True``.)

.. jupyter-execute::

    import numpy

    from cogent3.maths.stats.test import sign_test

    x = numpy.array(x)
    y = numpy.array(y)

    num_x_gt_y = (x > y).sum()
    pval = sign_test(num_x_gt_y, len(x))
    pval

Distribution properties
^^^^^^^^^^^^^^^^^^^^^^^

We can compare continuously distributed variables using standard statistical procedures, such as the two sample t-test. We can also employ non-parametric approaches to these.

Two sample t-test
"""""""""""""""""

.. jupyter-execute::

    x = [134, 146, 104, 119, 124, 161, 107, 83, 113, 129, 97, 123]
    y = [70, 118, 101, 85, 107, 132, 94]

.. jupyter-execute::

    from cogent3.maths.stats.test import t_two_sample

    t_two_sample(x, y)

.. index::
    triple: Mann-Whitney; statistical test; cogent3
    triple: MW; statistical test; cogent3
    triple: MW bootstrap; statistical test; cogent3

Mann-Whitney U-test
"""""""""""""""""""

Like the t-test, the Mann-Whitney (MW) test compares distributions by comparing their locations. However, this is a non-parametric test. It converts the original observations into ranks and compares the means of those ranks. 

.. jupyter-execute::

    from cogent3.maths.stats.test import mw_test

    mw_test(x, y)

.. note:: There is also a bootstrap version of the MW test available ``cogent3.maths.stats.test.mw_boot``.

.. index::
    triple: Kolmogorov-Smirnov; statistical test; cogent3
    triple: KS; statistical test; cogent3
    triple: KS bootstrap; statistical test; cogent3

Kolmogorov-Smirnov test
"""""""""""""""""""""""

The Kolmogorov-Smirnov (or KS) test is extremely useful. It is also a non-parametric statistical procedure but, unlike the Mann-Whitney test, it compares the cumulative distributions (both location and shape).

.. jupyter-execute::

    from cogent3.maths.stats.test import ks_test

    k_stat, pval = ks_test(x, y)

.. note:: There is also a bootstrap version of the KS test available ``cogent3.maths.stats.test.ks_boot``.

Using the Kolmogorov-Smirnov test to assess the distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
    triple: quantiles; statistical test; cogent3

We evaluate whether the data from ``x`` are distributed normally. To do this, we obtain the theoretical quantiles from the normal distribution. (These are from the standard normal distribution, with mean of 0 and standard deviation of 1.)

.. jupyter-execute::

    import numpy

    from cogent3.maths.stats.distribution import theoretical_quantiles

    norm_quants = theoretical_quantiles(len(x), "normal")
    norm_quants

So we need to transform ``x`` into standard z-scores before we perform the KS test.

.. jupyter-execute::

    n_x = numpy.array(x, dtype=float)
    mean = n_x.mean()
    # we specify ddof=1 to ensure the standard deviation is mathematically unbiased
    std = n_x.std(ddof=1)
    
    zscores = (n_x - mean) / std

    ks_stat, pval = ks_test(zscores, norm_quants)
    
    print(f"D={ks_stat:.4f}  p-value={pval:.4f}")

Quantile-quantile plots
-----------------------

A graphical way for comparing whether two data sets come from the same statistical distribution. In this case, we compare ``x`` with the theoretical quantiles from the normal distribution. If the data do come from the same distribution, then their points will form a line on the diagonal [3]_. In this case, the data seem very close to that -- consistent with the KS test results.

In order to do the plot, the sample data must be sorted. I also add a diagonal line between the minimum and maximum points. If the data are truly on a diagonal, the data points will be scattered very close to this line.

.. [3] You do not need the quantiles from a theoretical distribution. You can just compare the quantiles from two empirical data sets.

.. jupyter-execute::

    import plotly.express as px
    
    n_x.sort()
        
    fig = px.scatter(
        x=norm_quants,
        y=n_x,
        width=400,
        height=400,
        labels={
            "x": "Theoretical Quantiles",
            "y": "Sample Quantiles",
        },
    )

    fig.add_scatter(x=[norm_quants.min(), norm_quants.max()],
                    y=[n_x.min(), n_x.max()],
                    mode="lines",
                    showlegend=False)
    fig.show()
