.. _genetic_codes:

Genetic Codes
=============

Fundmental information encoding system and a fascinating subject of study. ``cogent3`` provides a dedicated object for handling genetic code information. The genetic codes included with ``cogent3`` are indicated in the following table indicates.

.. jupyter-execute::
    :hide-code:

    from cogent3 import available_codes

    available_codes()

Use the top level ``get_code()`` function to get a specific genetic code. Use a code ID from the above table.

.. jupyter-execute::

    from cogent3 import get_code

    gc = get_code(1)
    gc

Useful ``GeneticCode`` attributes
---------------------------------

``sense_codons``
    The codons that encode an amino acid. The trinucleotide string is the key, the single character IUPAC code for the amino acid is the value.

``codons``
    Maps all codon strings to corresponding amino acid IUPAC code.

``synonyms``
    Maps all amino acid IUPAC codes to their codons. (The reverse of ``codons``.)

Using ``GeneticCode`` instances
-------------------------------

Genetic code objects act like dictionaries for trinucleotide strings or single letter strings. The former are interpreted as RNA or DNA, the latter as the single code amino acid.

You can get the encoded amino acid from a RNA triplet

.. jupyter-execute::

    aa = gc["UAC"]
    aa

or DNA triplet.

.. jupyter-execute::

    aa = gc["TAC"]
    aa

The mapping from codon to amino acid is provided by a ``sense_codons`` attribute of the genetic code instance. So calling ``list()`` on that dict returns just the sense codons [#]_.

.. margin::

    .. [#] I'm truncating that list to just 4 elements to simplify the display.

.. jupyter-execute::

    list(gc.sense_codons)[:4]

You can get all the codons that encode an amino acid.

.. jupyter-execute::

    codons = gc["Y"]
    codons

You can check whether a codon is a start

.. jupyter-execute::

    gc.is_start("ATG")

or stop codon

.. jupyter-execute::

    gc.is_start("TAA")

Stop codons are represented by ``"*"`` character.

.. jupyter-execute::

    gc["TGA"]

.. jupyter-execute::

    gc["*"]

You can translate a string.

.. jupyter-execute::

    gc.translate("TCGACCGTTTAAGCC")

You can get the code as a Table,

.. jupyter-execute::

    table = gc.to_table()
    table

See the cogent3_ cookbook documentation for more on using genetic codes.

Exercises
---------

Identify all sense codons that differ from each other at only one of the codon positions. Group these pairs by codon position [#]_. The following questions refer to these groupings.

.. margin::

    .. [#] 1st, 2nd and 3rd codon position.

#. Pick a genetic code and, for each such codon position group, count the number of changes that are synonymous. Is there a difference between the codon position and the proportion of synonymous changes?

#. Does the property measured in the previous question differ between the genetic codes?

#. Categorise the codon differences by whether they are a transition or transversion change (see :ref:`point_mutations`). Assess whether the fraction of synonymous changes differs between transition and transversion changes.

#. Is there variation (between the genetic codes) in the number of stop codons? Assess this programmatically.

    *Hint: look at the attributes on the genetic code instance.*

