.. jupyter-execute::
    :hide-code:

    import set_working_directory

****************************
What is molecular evolution?
****************************

.. index:: pretty print

.. sidebar:: Variation between species
    :name: Variation between species

    .. jupyter-execute::

        from cogent3 import load_aligned_seqs

        aln = load_aligned_seqs("data/brca1_primate.fasta", moltype="dna")

    .. jupyter-execute::
        :hide-code:

        aln = aln[36:]
        aln.set_repr_policy(num_pos=36, ref_name="Human")

    .. jupyter-execute::

        aln
    
    This is a "pretty print" display style in which only the first sequence is shown in full. All other sequences display a base only when it doesn't match that reference sequence, otherwise a ``.`` is displayed.

Molecular Evolution is a domain of research that is concerned with why biological sequences look the way they do. Can we explain the distribution of genetic variation between biological sequences (RNA, DNA, and proteins) in terms of their evolutionary origins? Can we establish whether severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) is showing signs of adaptive evolution to its new host - us? These questions are within the domain of molecular evolution.

Since the nucleic acids are the information system of living things and can also be, along with proteins, functional, molecular evolution draws on genetics, molecular and cell biology, biochemistry, and chemistry. At a conceptual level, molecular evolution is closely related to population genetics and, as such, is very much focussed on the process of evolution as it manifests in biological sequences.

At a practical level, using genetic variation as an indicator of biological importance is central to much of modern biology. Researchers who are engaged in molecular studies of specific proteins or genes rely on resources provided by a genome portal (like ucsc_ or ensembl_) to get insights into what a molecule of interest might actually be doing. One of the types of information that these portals present to facilitate understanding is a comparison of the biological sequences from different species. Why? We will answer that question in this topic.

#. define biological problem and make testable predictions
#. sample appropriate homologous sequences
#. align the sequences
#. select a single phylogenetic tree
#. pick evolutionary model(s)
#. fit model(s) and evaluate hypotheses

**********************
What is phylogenetics?
**********************

Phylogenetics is concerned with the problem of inferring the relationships between members of a collection of biological sequences. This relationship is displayed as a tree. As the methods employed to estimate relationships in phylogenetics are the same methods used to understand process in molecular evolution, phylogenetics is a sub-discipline (albeit highly specialised) of molecular evolution.

.. jupyter-execute::
    :hide-code:
    
    from cogent3 import make_tree
    
    tree = make_tree("(Galago,Howler Monkey,(Rhesus,(Orangutan,(Gorilla,(Human,Chimpanzee)))));")
    fig = tree.get_figure()
    fig.tip_font = {"size": 18, "color": "blue"}
    fig_dim = 500
    fig.show(width=fig_dim, height=fig_dim)

.. sidebar:: The phylogenetic workflow
    :name: phylo_workflow

    .. digraph:: phylo_workflow
    
        graph [fontsize=12 fontname="Verdana" compound=true];
        node [shape="square"  color="white" style=filled];

        subgraph cluster_preprocess {
            style=filled;
            color=lightgreen;
            A;
            B;
            }

        subgraph cluster_decide_model {
            style=filled;
            color=lemonchiffon3;
            C;
            D;
            }

        subgraph cluster_fit_model {
            style=filled;
            color=lightblue;
            E;
            F;
            }

        A [label="Sample\nHomologous\nSequences"];
        B [label="Multiple\nSequence\nAlignment"];
        C [label="Choose\nPhylogenetic\nMethod"];
        D [label="Choose\nSubstitution\nModel"];
        E [label="Estimate\nModel &\nTree"];
        F [label="Display\nResults"];

        A -> B;
        C -> D;
        E -> F;

        A -> C [ltail=cluster_preprocess lhead=cluster_decide_model];
        C -> E [ltail=cluster_decide_model lhead=cluster_fit_model];

        Db [label="Database" shape=none];
        Sft [label="Software" shape=none];
        Db -> A [head=cluster_preprocess];
        Db -> D [style=invis];
        Db -> Sft [style=invis];
        Sft ->C;
        Sft ->E [style=invis];

In the :ref:`Phylogenetic Workflow <phylo_workflow>` figure I display the basic workflow for phylogenetic reconstruction. There is substantial overlap with molecular evolutionary analysis in general, but the emphasis here is on the problem of estimating a tree. The steps are:

#. sample homologous sequences from tax of interest
#. align the sequences
#. choose method to build the phylogenetic tree.
    
    - pick a substitution model
    
#. Estimate the phylogenetic tree

    - we may include a technique for estimating the level of uncertainty in that tree
