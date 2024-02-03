.. _odds-ratios:

Odds-ratio's
============

There are a multitude of statistical measures that are presented as odds-ratios (hereafter OR). They are often seen in terms of evaluating clinical studies. For instance, the odds-ratio of statin medication increasing life-span. We will be concerned with using the odds-ratio to distinguish between competing hypotheses.

Consider an odds ratio that contrast the probability of a sequence under an alternate hypothesis (:math:`p_{alt}`) against the probability of the sequence under a null hypothesis (:math:`p_{null}`). In this instance, an OR equal to 1 if :math:`p_{alt} = p_{null}`, i.e. the sequence is equally likely under both models. OR > 1 indicates the sequence is more likely under the alternate, while a value less than 1 implies the converse.

.. margin::
  
    .. [1] Recalling that :math:`\log(a/b)=\log(a) - \log(b)`, and :math:`\log(a \times b) = \log(a) + \log(b)`.

Log-odds -- the logarithm variant
---------------------------------

A log-odds ratio is simply the log-transformation of the odds ratio [1]_. For example, for OR=1, the log-odds :math:`\log_{10}(OR)=0` [2]_.

.. margin::
  
    .. [2] If you find a log-odds value hard to interpret, convert it back into a natural number by raising the logarithm base to the power of the log-odds. For example, if the log-odds value you have is :math:`LOR`, and it was obtained as :math:`LOR = \log_2(OR)`, then the reverse operation is :math:`OR = 2^{LOR}`.
