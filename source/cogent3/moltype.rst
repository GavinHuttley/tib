.. _moltypes:

``MolType`` – specifying biological sequence type
=================================================

True biological sequences are polymers of monomeric units with distinct chemical properties. These are represented by specific alphabets of allowed characters, a collection of ambiguous characters [1]_, and various operations that can be performed on them. In ``cogent3``, we represent some of these using concepts with the an object type called a ``MolType``. The available moltypes are displayed by calling a convenience function, ``available_moltypes()``.

.. [1] The nomenclature (character alphabets) for representing biological sequences are defined by the International Union of Pure and Applied Chemistry (IUPAC).

.. index::
    pair: moltype; cogent3

.. jupyter-execute::

    from cogent3 import available_moltypes

    available_moltypes()

.. note:: Typically you specify what moltype your data is simply using the string abbreviation of the appropriate molecular type.

To illustrate the object capabilities, we load the DNA moltype and use some of the methods.

.. jupyter-execute::

    from cogent3 import get_moltype

    dna = get_moltype("dna")
    dna

For this moltype, there's a notion of the complement of a sequence

.. jupyter-execute::

    dna.complement("TTGG")

and of the reverse complement.

.. jupyter-execute::

    dna.rc("TTGG")

The IUPAC ambiguities for DNA are accessed as an attribute (which is just a ``dict``).

.. jupyter-execute::

    dna.ambiguities

The alphabet attribute stores defines the alphabet states and provides, among other things, mapping's between characters "A", "C" etc.. to integers (which is how some data structures represent sequences).

.. jupyter-execute::

    dna.alphabet
