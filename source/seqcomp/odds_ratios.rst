.. _odds-ratios:

Odds-ratio's
============

There are a multitude of statistical measures that are presented as odds-ratios (hereafter OR). They are often seen in terms of evaluating clinical studies. For instance, the odds-ratio of statin medication increasing life-span. We will be concerned with using the odds-ratio to distinguish between competing hypotheses.

Consider an odds ratio that contrast the probability of a sequence under an alternate hypothesis (:math:`p_{alt}`) against the probability of the sequence under a null hypothesis (:math:`p_{null}`). In this instance, an OR equal to 1 if :math:`p_{alt} = p_{null}`, i.e. the sequence is equally likely under both models. OR > 1 indicates the sequence is more likely under the alternate, while a value less than 1 implies the converse.

Log-odds -- the logarithm variant
---------------------------------

A log-odds ratio is simply the log-transformation of the odds ratio [1]_. For example, for OR=1, the log-odds :math:`log_{10}(OR)=0` [2]_.

----

.. [1] Recall that log(a) - log(b) = log(a/b), and log(a) + log(b) = log(a * b)
.. [2] If you find the log-odds hard to interpret, convert them back into a natural number by raising the logarithm base to the log-odds. For example, if ``log_odds = log2(OR)``, then the reverse operation is ``OR = 2**log_odds``
