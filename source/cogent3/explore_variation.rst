Exploring genetic variation using Alignments
============================================

Alignments and sequence collections contain methods to facilitate exploring genetic variation.

Find the variable positions
---------------------------

.. jupyter-execute::

    from cogent3 import load_aligned_seqs
    
    aln = load_aligned_seqs("source/data/brca1-bats.fasta", moltype="dna")
    aln = aln[:30]
    var_pos = aln.variable_positions(include_gap_motif=False)
    var_pos


Entropy per aligned position
----------------------------

We start by looking at entropy measures (see :ref:`shannon_entropy` for background). We will focus on alignments and column wise measurement.

.. jupyter-execute::

    aln = load_aligned_seqs("source/data/brca1.fasta", moltype="dna")
    aln = aln[9:120]

    aln.entropy_per_pos()

.. index::
    triple: k-mer; motif_len; cogent3

There are a number of options here, including the fact that we can specifically ask for entropy measurement for |kmers| > 1. In ``cogent3``, we use the argument ``motif_length`` to specify the value of :math:`k`.

Visual display of information per aligned position
--------------------------------------------------

Sequence logo's to represent information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You've seen how sequence logos are used to visualise PSSMs. They can also be used to visualise the amount of information at specific positions. The alignment objects have a ``seqlogo()`` method that computes the information (see :ref:`information`) at a position. The resulting display has the letter stack height equalling the information.

.. jupyter-execute::

    logo = aln.seqlogo(width=700, height=300, wrap=60, vspace=0.07)
    logo.show()

.. note:: ``cogent3`` uses plotly for visualisation. Methods that return a drawable return a custom ``cogent3`` object that behaves "like" a plotly object, but is not one.

The ``wrap`` argument indicates how many alignment columns to include on a row. The ``vspace`` argument how much vertical space between rows. Typically, it takes a bit of tweaking to get the plot width / height right to make the display sensible.

.. warning:: This is a compute intensive type of display! Start with a short stretch of alignment first and gradually increase the length.

Information plots
^^^^^^^^^^^^^^^^^

This is a line plot that smoothes the information scores and also displays them with information about gaps.

.. jupyter-execute::

    aln = load_aligned_seqs("source/data/brca1.fasta", moltype="dna")
    aln = aln[:1500]

    info_plot = aln.information_plot()
    info_plot.show(width=600, height=250, window=30)

You can remove one of the traces by clicking on it's member in the figures legend. You can also zoom in on parts of the plot by click and drag to include the portion you want. Double click the plot to revert back.

.. sidebar:: Saving a png of your plot

    .. image:: /_static/images/cogent3/plotly-save-png.png
    
    Hover your mouse over the image and a control panel is displayed. Click on the camera icon to download an image to your computer.

Comparing sequences using dotplots
----------------------------------

``cogent3`` implements an advanced dotplot algorithm with some very useful features for exploring the relationship between sequences, and the quality of your alignment. Note that this method also exists on the ``SequenceCollection`` class.

.. warning:: The dotplot algorithm is slow! Start on a smaller slice of the alignment to begin with.

Dotplot between random sequences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::
    
    subaln = aln[:750]
    dp = subaln.dotplot()
    dp.show(width=500, height=500)

.. note:: The ``alignment`` item in the legend shows the path the alignment algorithm found. Hopefully, that sits precisely on top of a diagonal!

Include the reverse complement in the dotplot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    dp = subaln.dotplot(rc=True)
    dp.show(width=500, height=500)

Change the match criteria
^^^^^^^^^^^^^^^^^^^^^^^^^

Two key arguments to the ``dotplot()`` method that affect the definition match are ``window`` and ``threshold``. The former is the same as specifying the size of the |kmer| being compared. The latter controls how many characters within the |kmer| must be identical for it to be a match.

.. jupyter-execute::

    dp = subaln.dotplot(rc=True, window=6, threshold=6)
    dp.show(width=500, height=500)

Set a plot title
^^^^^^^^^^^^^^^^

.. jupyter-execute::

    dp = subaln.dotplot(rc=True, window=6, threshold=6, title="Demo dotplot")
    dp.show(width=500, height=500)

Specify the sequences to be compared
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    dp = subaln.dotplot(name1="Human", name2="Wombat")
    dp.show(width=500, height=500)

If you just specify ``name1``, then the second sequence will be chosen at random.

Dotplot a sequence to itself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can be useful for examining the existence of inversions, repeated sequence features, etc...

.. jupyter-execute::

    dp = subaln.dotplot(name1="Wombat", name2="Wombat", title="Wombats are awesome!")
    dp.show(width=500, height=500)

Exercises
=========

Download the :download:`large alignment of BRCA1 sequences </data/brca1.fasta>`.

#. Look at the ArrayAlignment_ documentation and identify methods that can be used to select the positions that are variable.

#. Google the definition of a moving average. Then experiment with changeing the ``window`` argument to ``information_plot()``. How do you interpret the impact of increasing the value of ``window``?
    
#. Select a smallish segment from the one of the sequences within the downloaded data set (say < 50 bases). Manually edit that so that contains an inversion. Use ``make_unaligned_seqs()`` to create a sequence collection and dotplot this synthetic sequence to itself using ``rc=True``.

#. Modify your synthetic sequence to have some repeats and see what the effect of changing ``window`` and ``threshold`` are on the detection of those.
