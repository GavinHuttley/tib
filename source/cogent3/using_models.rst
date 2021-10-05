.. jupyter-execute::
    :hide-code:

    import set_working_directory

Modelling sequence evolution
============================

``cogent3`` has a lot of substitution models! The following displays just the nucleotide models.

.. jupyter-execute::

    from cogent3 import available_models

    available_models(model_types="nucleotide")

These are :ref:`cogent3 apps <apps>`. There's also an app for performing hypothesis testing using these models.

Using the ``model`` app
-----------------------

Using the ``model`` app involves specifying the substitution model name and a tree. If you are analysing just 3 sequences, the tree is not required. Otherwise, the tree can be a path to a file or a :ref:`newick formatted string <newick>`.

The resulting model instance can then be called as if it was a function, passing it an alignment instance. It will maximise the likelihood of the model for the alignment and return a custom result data type.

I'm creating an app to apply the :ref:`f81` substitution model to an alignment and specifying the a tree as a file path.

.. jupyter-execute::

    from cogent3.app import evo

    f81 = evo.model("F81", tree="data/brca1_primate.tree")

.. warning:: If you are providing a tree, the tip names must exactly match the names in the alignments that will be analysed.

.. note:: If you are analysing 3 sequences, there is only one possible unrooted tree and the model object will automatically construct it for you.

We now load our alignment and fit the model to it.

.. jupyter-execute::

    from cogent3 import load_aligned_seqs

    aln = load_aligned_seqs("data/brca1_primate.fasta", moltype="dna")
    result = f81(aln)

``model_result``
----------------

The app returns a ``model_result`` object whose representation provides an overview of the fitted model.

.. jupyter-execute::

    result

The column titles in that summary display have the following meaning

.. jupyter-execute::
    :hide-code:

    from cogent3 import make_table

    t = make_table(
        data={
            "Column Heading": ["key", "lnL", "nfp", "DLC", "unique_Q"],
            "": [
                "The dictionary key for accessing this model",
                "The log-likelihood value",
                "The number of free parameters in the model",
                "Diagonal largest in column in all P matrices.",
                "Whether the Q uniquely map to P",
            ],
        },
        index_name="Column Heading",
    )
    t.set_repr_policy(show_shape=False)
    t

The last two are concerned with model identifiability (if either is ``False``, the results could be unreliable).

To see the parameter MLEs, we access the ``lf`` attribute [#]_

.. [#] This attribute is a special cogent3 type which has capabilities for deeper interrogation of model parameters.

.. jupyter-execute::

    result.lf 

There are 2 tables always present in this display – "edge params" and "motif params". The former will always show the branch lengths. The following displays the tree, with the branch length defined by the values in the "edge params" table. The columns "edge" and "parent" denote which branch the "length" column value corresponds to [#]_. That value is the MLE for the expected number of substitutions (our measure of evolutionary time).

.. [#] If you hover your mouse over the internal nodes on the tree, the name of the node will appear.

.. jupyter-execute::

    dnd = result.tree.get_figure()
    dnd.scale_bar = "top left"
    dnd.show()

We can get all those statistics out as ``cogent3`` tables using the ``tabulate_stats`` app

.. jupyter-execute::

    tabulate = evo.tabulate_stats()
    tables = tabulate(result)
    tables

which allows us to get at the parts from the ``lf`` display

.. jupyter-execute::

    tables["edge params"]

Motif params are the state probabilities
----------------------------------------

The "motif params" table corresponds to |pi|, the frequencies of nucleotides in the unobserved ancestor [#]_ of the alignment. More generally, ``cogent3`` uses the variable ``motif_probs`` to denote this. For instance, the alignment has a method for getting the motif probabilities as the average across all sequences.

.. [#] At the node labelled "root".

.. jupyter-execute::

    aln.get_motif_probs()

With default model settings, the values returned by the model will be the same as this.

.. jupyter-execute::

    tables["motif params"]

Refining the model app settings
-------------------------------

Optimising the motif probabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For continuous-time substitution models, the default ``model`` settings are that the process is time-homogeneous (one rate matrix for the entire tree) and |pi|, the state (or motif) probabilities at the root is just that returned by the alignment method. The latter can be changed so that the motif probabilities are treated as free parameters and optimised.

.. jupyter-execute::

    f81_mprobs = evo.model(
        "F81",
        name="F81-mprobs free",
        sm_args=dict(optimise_motif_probs=True),
        tree="data/brca1_primate.tree",
    )

    result = f81_mprobs(aln)

Note that the number of free parameters has now increased by 3.

.. jupyter-execute::

    result

and that the motif probs are different to those above.

.. jupyter-execute::

    result.lf

Constraining a substitution model parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we wish to modify the definition of a likelihood function we need to set rules for the parameter of interest. We do this using the ``param_rules`` argument to ``model()``.

Let's create a new instance of the HKY85 and constrain the likelihood function so that it is F81. To do that, we need to set the |kappa| parameter to be equal to 1, and constant (so the numerical optimiser does not modify it during it's work).

.. jupyter-execute::

    hky_as_f81 = evo.model(
        "HKY85",
        name="HKY85 with κ=1",
        tree="data/brca1_primate.tree",
        param_rules=[dict(par_name="kappa", is_constant=True, value=1)],
    )

    result = hky_as_f81(aln)
    result

As there can be more than one parameter rule applied to a function, we provide them as a list. Each element of the list must be a dictionary with at least one key ``"par_name"``. This is the name of the parameter we wish to modify and the value must be a string. The ``is_constant=True`` sets that parameter as a constant with ``value=1``.

.. jupyter-execute::

    result.lf

From that you can see the lnL and nfp are identical to our first fitting of the F81 model. While the display includes "kappa" (in the "global params" table), it has the value 1 and was not changed by the optimiser.

More generally, the "global params" table shows MLEs for the exchangeability terms in |Q|.

Testing hypotheses using the ``hypothesis`` app
-----------------------------------------------

To perform a hypothesis test, we need two models. I will create a :ref:`hky85` model which will serve as our alternate to the null of F81.

.. jupyter-execute::

    hky85 = evo.model("HKY85", tree="data/brca1_primate.tree")

We construct the hypothesis app by providing the null and alternate models.

.. jupyter-execute::

    hyp = evo.hypothesis(f81, hky85)

We apply it to our alignment.

.. jupyter-execute::

    result = hyp(aln)

The ``hypothesis`` app fits both models to the alignment. One important point to make is, in the case of nested models, it will use the MLEs from the null as "seed" values to alternate as a pre-step to numerical optimisation. This is done for 2 reasons. First, it typically speeds up fitting. Second, it guarantees the likelihood from the alternate will be ≥ that of the null.

``hypothesis_result``
---------------------

The ``hypothesis`` app returns a ``hypothesis_result`` object, which also provides an overview of the hypothesis test outcome.

.. jupyter-execute::

    result

The column titles in that summary display have the following meaning

.. jupyter-execute::
    :hide-code:

    from cogent3 import make_table

    t = make_table(
        data={
            "Column Heading": ["LR", "df", "pvalue", "hypothesis"],
            "": [
                "Likelihood ratio statistic",
                "degrees of freedom",
                "p-value",
                "null or alternate",
            ],
        },
        index_name="Column Heading",
    )
    t.set_repr_policy(show_shape=False)
    t

The LR statistic (computed :ref:`using this equation <likelihood_ratio>`) and df are computed from the ``lnL`` and ``nfp`` values, respectively, of the different models under "hypothesis". The p-value is the probability of a LR ≥ the observed statistic from the theoretical |chisq| distribution with df degrees of freedom.

The ``model_result`` for each of the models is available as ``.null`` and ``.alt`` attributes.

.. jupyter-execute::

    result.alt

``hypothesis_result`` also behaves like a dictionary, with the keys being the model name. So this display is identical to the previous one.

.. jupyter-execute::

    result["HKY85"]

The ``NotCompleted`` object
---------------------------

If your analysis returns one of these, it means there was an error or the algorithm could not complete. That object contains information about where the error occurred and what type it was. See the `cogent3 documentation <https://cogent3.org/doc/app/not-completed.html>`_ for more details.

Exercises
=========

The following require you to repeat the above hypothesis test. Download the :download:`alignment of primate BRCA1 sequences </data/brca1_primate.fasta>` and :download:`the tree </data/brca1_primate.tree>`, or :ref:`using Python <download_data>`.

#. From the test result, which model do you choose and why?

#. Displaying the MLE's for the null hypothesis and the alternate hypothesis in separate cells. Which specific parameter values is responsible for the difference in likelihoods?

#. Give a biological interpretation of the result.

#. What are the assumptions of these models?

.. todo:: add an exercise demonstrating why the average motif probs should not be used
