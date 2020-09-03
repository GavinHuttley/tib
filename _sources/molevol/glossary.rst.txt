Glossary of terms
=================

data
    An alignment of sequences descended from a common ancestor.

fit a model
    Numerical optimisation of parameters in a model. In the case of maximum likelihood, the model parameters are selected that produce the maximum likelihood of observing the data under the model.

maximum likelihood
    A method of parameter estimation

maximum likelihood estimators (MLEs)
    the estimated values of model parameters after fitting

rate matrix (Q)
    A square matrix with off-diagonal elements ≥ 0 and row sums of 0. Represents the instantaneous rate of change from the row label state (e.g. a nucleotide) to a column label state (e.g. another nucleotide)

substitution matrix (P)
    A square matrix of probabilities, with row sums of 1. Represents the probability of substituting  the row label state with the column label state for a given time interval. Typically derived from Q by maxtrix exponentiation.

rate parameter
     A component of Q, specifying the instantaneous rate of change between row and column states

tree, phylogenetic tree
    A graph displaying the relationship amongs sequences

branch length
    On a phylogenetic tree, the expected number of substitutions per site for a specific branch. This is a parameter estimated by maximum likelihood

site
     A column in a multiple sequence alignment

Likelihood ratio (LR)
     A test statistic that is distributed $\chi^2$ with degrees of freedom equal to the difference in the number of free parameters between alternate and null models.

number of free parameters
    Parameters in the likelihood function that are "free" -- can be modified by the numerical optimiser -- to modify the fit to data.
