Glossary of terms
=================

data
    An alignment of sequences descended from a common ancestor.

:index:`estimate`
    The value of a parameter obtained from a population sample. Statisticians employ "hat" notation to identify a quantity as being an estimate of a parameter, e.g. :math:`\hat \pi_A` is an estimate of the parameter :math:`\pi_A`

:index:`fit a model`
    Numerical optimisation of parameters in a model. In the case of maximum likelihood, the model parameters are selected that produce the maximum likelihood of observing the data under the model

:index:`free parameter`
    A model parameter whose value is not fixed during numerical optimisation, hence the parameter is free to vary

:index:`maximum likelihood`
    A method of parameter estimation

:index:`maximum likelihood estimators (MLEs)`
    The estimated values of model parameters after fitting

:index:`parameter`
    A parameter is a term in a model. More generally, it refers to the true value of a quantity from a population.

:index:`rate matrix` (Q)
    A square matrix with off-diagonal elements ≥ 0 and row sums of 0. Represents the instantaneous rate of change from the row label state (e.g. a nucleotide) to a column label state (e.g. another nucleotide)

:index:`substitution matrix` (P)
    A square matrix of probabilities, with row sums of 1. Represents the probability of substituting  the row label state with the column label state for a given time interval. Typically derived from Q by matrix exponentiation.

:index:`rate parameter`
    A component of Q, specifying the instantaneous rate of change between row and column states

:index:`tree`, phylogenetic tree
    A graph displaying the relationship among sequences

:index:`branch length`
    On a phylogenetic tree, the expected number of substitutions per site for a specific branch. This is a parameter estimated by maximum likelihood

:index:`site`
    A column in a multiple sequence alignment

:index:`Likelihood ratio` (\ :index:`LR`\ )
    A test statistic that is distributed |chisq| with degrees of freedom equal to the difference in the number of free parameters between alternate and null models.

:index:`number of free parameters` (\ :index:`nfp`\ )
    Parameters in the likelihood function that are "free" -- can be modified by the numerical optimiser -- to modify the fit to data.

:index:`degrees of freedom` (\ :index:`df`\ )
    A quantity defining the difference in the number of parameters between two models.

