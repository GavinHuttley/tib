.. _genetic_codes:

Genetic Codes
=============

Fundmental information encoding system and a fascinating subject of study. ``cogent3`` provides a dedicated object for handling genetic code information. There are quite a few different genetic codes, as the following table indicates.

.. jupyter-execute::
    :hide-code:

    from cogent3 import available_codes

    available_codes()

Use the top level function to get a specific genetic code.

.. jupyter-execute::

    from cogent3 import get_code

    gc = get_code(1)
    gc

Genetic code objects act like dictionaries for trinucleotide strings or single letter strings. The former are interpreted as RNA or DNA, the latter as the single code amino acid.

You can get the encoded amino acid from a RNA triplet

.. jupyter-execute::

    aa = gc["UAC"]
    aa

or DNA triplet.

.. jupyter-execute::

    aa = gc["TAC"]
    aa

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

    gc.translate("TCGACCGTTTAAGCC")

You can get the code as a Table,

.. jupyter-execute::

    table = gc.to_table()
    table

See the cogent3_ cookbook documentation for more on using genetic codes.

Exercises
---------

Identify all sense codons that differ from each other at only one of the codon positions. Group these pairs by codon position.

The following questions refer to these groupings.

    #. Pick a genetic code and, for each such codon position group, count the number of changes that are synonymous. Is there a difference between the positions in the proportion of synonymous changes?

    #. Does the property measured in 2.) vary between the genetic codes?

    #. Now categorise the codon differences by whether they are a transition or transversion change. Assess whether the fraction of synonymous changes differs between transition and transversion changes.

#. Is there variation (between the genetic codes) in the number of stop codons?

    *Hint: look at the attributes on the genetic code instance.*

