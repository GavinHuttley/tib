.. jupyter-execute::
    :hide-code:

    import set_working_directory

Alignments, Sequence Collections and Sequences
==============================================

Biological sequences are represented by several objects in ``cogent3``. Typically, these are created by loading from file or by making them directly from standard python types. There is no more fundamental type than that of sequences. So let's just get cracking and actually load some data from a file. Along the way, I'll point out different aspects of the process of creating objects that you need to pay attention to.

Alignments
----------

Loading aligned sequences from a file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    from cogent3 import load_aligned_seqs

    aln = load_aligned_seqs("data/brca1-bats.fasta", moltype="dna")
    aln

The ``moltype`` argument specifies the molecular type of the sequence. See :ref:`moltypes` for more information.

.. jupyter-execute::

    type(aln)

The ``ArrayAlignment`` is one of the two different ``cogent3`` types for handling sequence alignments and is built using ``numpy.arrays`` [#]_. So, under the hood, sequences are represented as arrays of integers with the integer values corresponding to the index of the character in the alphabet. The class handles conversions to / from the standard text representation.

For all the methods, see ArrayAlignment_.

.. [#] Unless you want to be manipulating sequences via their sequence annotations, this is what you want. See the cogent3_ documentation for the other class.

When we talk about an alignment with ``cogent3``, this is what we mean.

Getting the length of an alignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    len(aln)

Getting the lengths of individual sequences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wait! Aren't all sequences in a alignment exactly the same length? Yes, but only because the include gaps. It's often the case that you want to know how much actual sequence data there is for each sequence. In this case, we use the ``get_lengths()`` method.

.. jupyter-execute::

    aln.get_lengths()

Getting the number of sequences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    aln.num_seqs

Getting the sequence names
^^^^^^^^^^^^^^^^^^^^^^^^^^

These are available as the ``names`` attribute.

.. jupyter-execute::

    aln.names

Getting the individual sequences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alignments have many useful attributes, including the individual sequences. These can be accessed either by the ``seqs`` attribute of the instance (this is just a list of sequence objects).

.. jupyter-execute::

    aln.seqs[0]

by the ``named_seqs`` attribute, which is a dictionary.

.. jupyter-execute::

    aln.named_seqs["TombBat"]

or by the method ``get_seq()``.

.. jupyter-execute::

    aln.get_seq(aln.names[0])

.. index::
    pair: slice; cogent3 Alignment
    pair: stride; slice

Alignments are aligned column based
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This means when you slice them, you are slicing alignment columns.

.. jupyter-execute::

    aln[10:20]

You can also use a "stride".

.. jupyter-execute::

    aln[10:20:3]

.. warning:: Slicing with a stride only works for the ``ArrayAlignment`` class.

``cogent3`` ``Alignment`` types are immutable!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

So any method that modifies their data returns a new instance.

Getting a subset of sequences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is done via a method.

.. jupyter-execute::

    subset = aln.take_seqs(["TombBat", "FlyingFox"])
    subset

Converting sequences into a standard Python ``dict``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is useful if you want to directly manipulate the strings, for instance [#]_

.. [#] I'm slicing the alignment only because I want the dict to be sensibly displayed in this documentation.

.. jupyter-execute::

    data = subset[:21].to_dict()
    data

Creating an alignment from a Python ``dict``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use a different function for building an alignment from standard Python types. The function has a very similar interface to ``load_unaligned_seqs()``.

.. jupyter-execute::

    from cogent3 import make_aligned_seqs

    subset2 = make_aligned_seqs(data=data, moltype="dna")
    subset2

.. index::
    triple: pretty print; cogent3; alignment
    triple: display variation; cogent3; alignment

Writing sequences to file
^^^^^^^^^^^^^^^^^^^^^^^^^

The various alignment and sequence collection objects have a ``write()`` method. Providing a file path with a known suffix generates a text file with that format. For example

.. code-block:: python
    
    subset2.write("some_dir/subset2.fasta")

will produce a fasta formatted sequence file.

Interpreting the display of alignments in Jupyter notebooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The visualisation you see is a style known as a pretty print. The ``"."`` character indicates a match to the character in the first sequence in that column. We refer to this first sequence as the reference.

Colouring is provided for alignments with RNA, DNA or PROTEIN moltypes. If you do not specify a moltype on loading / creating an alignment, the display will not be coloured.

Controlling the display in Jupyter notebooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::
    :hide-code:

    # need to remove the environment variable otherwise the following has no effect
    import os
    
    env_setting = os.environ.pop("COGENT3_ALIGNMENT_REPR_POLICY", None)

This is done via modifying the representation policy. You can change the number of sequences (``num_seqs``), the number of aligned positions that will be shown (``num_pos``), how many columns to display per line (``wrap``).

.. jupyter-execute::

    aln.set_repr_policy(num_pos=15, wrap=10)
    aln

.. warning:: Rendering the html can take a long time if the number of positions (and/or sequences) is large.

You can also specify the sequence to be used as a reference (the default is to use the longest sequence without gaps).

.. jupyter-execute::

    aln.set_repr_policy(ref_name="FreeTaile")
    aln

.. jupyter-execute::
    :hide-code:

    # restore the environment variable
    if env_setting:
        os.environ["COGENT3_ALIGNMENT_REPR_POLICY"] = env_setting

Translating nucleic acids to protein
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are a few factors to consider here. First, some sequences may be incomplete -- meaning the actual sequence does not cover the entire gene and may end with an incomplete codon. Second, the sequence may be complete but terminate with a stop codon. Both of those will cause the translation method to fail. In this case, the data has an incomplete codon (it contains a gap character), which we address as follows

.. jupyter-execute::

    aa_aln = aln.get_translation(incomplete_ok=True)
    aa_aln

If the failure is due to having a stop codon, using the ``trim_stop_codons()`` method first will do the trick, so long as the stop is at the end.

Another key consideration for translation is to specify the genetic code. The default is to use the standard vertebrate code. (See :ref:`genetic_codes` for more details on what ``cogent3`` provides.) We will demonstrate specifying the standard code explicitly (using ``gc=1``).

.. jupyter-execute::

    aa_aln = aln.get_translation(incomplete_ok=True, gc=1)

Getting the reverse complement of nucleic acid sequences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the ``rc()`` method!

.. jupyter-execute::

    subset_rc = subset.rc()
    subset_rc

``SequenceCollection`` -- for unaligned collections of sequences
----------------------------------------------------------------

If your sequences are not aligned, they may not be of the same length. To load such sequence data from file, or create from Python objects, you use the functions ``load_unaligned_seqs()`` and ``make_unaligned_seqs()``. The signatures of these functions match those of their counterparts for aligned sequences. Likewise, many of the methods on ``SequenceCollection`` are the same as for the alignment data types (see SequenceCollection_ for documentation). But note that a ``SequenceCollection`` cannot be sliced.

Making from a collection of unaligned sequences from dict
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    from cogent3 import make_unaligned_seqs

    data = {"seq-0": "ACGGT", "seq-1": "AGGGACGTA"}
    coll = make_unaligned_seqs(data=data, moltype="dna")
    coll

.. jupyter-execute::

    seq_0 = coll.named_seqs["seq-0"]
    seq_0

Making from a collection of unaligned sequences an Alignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just use the ``degap()`` method. This strips all gap characters (`"-"`) from the sequences.

.. jupyter-execute::

    seq_coll = aln.degap()
    seq_coll

Reverse complement and many other methods are available as for alignment data types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    rc_ed = coll.rc()
    rc_ed.named_seqs["seq-0"]

Sequences
---------

Collections and alignments give you an organised interface to manipulate groups of sequences. There is also a specific set of sequence data types. These consist of classes that are specific to the different :ref:`molecular types <moltypes>`. (See DnaSequence_ and ProteinSequence_ for the documentation.)

We can make a sequence from Python data types.

.. jupyter-execute::

    from cogent3 import make_seq
    
    seq = make_seq("ACGTTTAAA", name="seq-0", moltype="dna")
    seq

Sequences are loaded from file using the |load_data|_ functions for collections (``load_unaligned_seqs``), or alignments (``load_aligned_seqs``).

Exercises
=========

Download the :download:`alignment of bat BRCA1 sequences </data/brca1-bats.fasta>`, or :ref:`using Python <download_data>`.

#. Set the ``incomplete_ok`` argument in the ``get_translation()`` method to ``False``. What happens and why?

#. Create an alignment from a dict with sequences that you make up [#]_. Slice the alignment to remove the last 3 aligned columns.

#. Create an alignment from a dict with sequences that you make up. Slice the alignment to get every second codon position.

#. Using the downloaded alignment, count the number of second codon positions that have variation.

#. Load the downloaded alignment without specifying the ``moltype``. Use a method on the object to convert it to the DNA moltype.

.. [#] Sequences in alignments must be exactly the same length.
