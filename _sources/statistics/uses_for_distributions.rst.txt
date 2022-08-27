******************************************************************
Beyond hypothesis testing – exploratory data analysis for genomics
******************************************************************

For many problems in genomics, analysing the distributions of measurements from genomic data is an effective strategy. It can even be the case that the measurement distribution to be evaluated is of |pvalues| for tests applied to genomic data. Alternatively, we can consider the distribution of quantiles, a measurement analogous to a |pvalue| which is obtained as simple transformation from a raw statistic.

The uniform distribution
========================

We now turn our attention to a description of the uniform distribution which we will use to introduce a measure related to the |pvalue| as a cumulative measure of probability density.

Consider a random variable that can obtain any value in [0, 1] (including the boundaries, see :ref:`uniform distribution histogram <uniform_dist>`). We call such a random variable uniformly distributed if all possible values of that random variable have an equal probability of occurring. The probability of observing a value of 0.2 is equal that of observing of 0.8, 0.9, or 0.0.

.. sidebar:: Histogram of a uniformly distributed random variable
    :name: uniform_dist

    Generating some random values from the uniform distribution.

    .. jupyter-execute::

        from numpy.random import rand

        x_uniform = rand(50000)

    .. jupyter-execute::
        :hide-code:

        import plotly.express as px

        fig = px.histogram(x=x_uniform, histnorm="probability", height=300, width=400)
        fig.layout.xaxis.title = "A Statistic"
        fig.layout.xaxis.range = (0, 1)
        fig.layout.yaxis.title = "Probability"
        fig.show()

.. index::
    pair: quantile; distribution

Quantiles as distribution descriptors
=====================================

Quantiles are rank order statistics. They are locations in a sorted collection of values. One example of a quantile you are likely familiar with is the median, which cuts a distribution such that 1/2 of all values are less than it. Following this example, a quantile=0.05 is the point that is greater than 1/20th of all values. We can think of a values quantile as its relative rank with a data set which can be computed as :math:`\frac{r}{n}` where :math:`r` is the rank in :math:`n` values.

Let's play with the quantiles from the uniform distribution that :ref:`I generated <uniform_dist>`. We use the ``numpy.quantile`` function for this purpose. Since we're using a uniform distribution, and following from the definition of this distribution, we can expect that 5% of all uniform random values will be :math:`\le 0.05`. Does our data support this?

.. jupyter-execute::

    from numpy import quantile

    quantile(x_uniform, 0.05)

Conversely, we expect that 5% of all uniform random values will be :math:`\ge 0.95`

.. jupyter-execute::

    1 - quantile(x_uniform, 0.95)

We generated these data using a sample size of 50,000. As we increase that sample size, you will find the estimates of the quantiles from the uniform distribution converge on their expected values. We can this statement more general -- as you increase the sample size the quantile becomes an increasingly good approximation of its |pvalue|.

Quantiles have advantages over the |pvalues| in exploratory data analysis. Not least of which they are derived from the actual data, rather than idealised (theoretical) description. Numerous data exploratory techniques are based upon this quantity (for example Quantile-Quantile plots to compare the distributions of two data sets).
