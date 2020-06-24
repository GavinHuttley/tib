:title: Sequence comparison
:css: lectures.css

Connecting data with biological model – sequence comparison
===========================================================

----

Darwin + Mendel + Francis and Crick
===================================

-  descent from a common ancestor
-  both parents transmit hereditary information to progeny
-  hereditary information is encoded in DNA
-  each position in a DNA sequence derived from a residue in an ancestor
-  the latter property applies to individuals of different species

----

- The above is a gross simplification.
- How we connect biological sequence data to biological process arises from the implications of the crucial discoveries by these individuals.
- This will be expanded on an an extremely important way the the Molecular Evolution module.

----

Consider the history of 2 sequences
-----------------------------------

::

                 |
      +--------ACAGT--------+     Ancestor
      |                     |
      |                   AxxxT   3 bp deletion
      |                     |
    ACAGT                  AT     Sampled sequences
    
    Seq1                  Seq2

----

What we observe is
------------------

::

   seq1  ACAGT
   seq2  AT

----

What are the possible alignments?
---------------------------------

::

   seq1  ACAGT
   seq2  A---T

OR

::

   seq1  ACAGT
   seq2  --A-T

----

So the “history” is hidden
~~~~~~~~~~~~~~~~~~~~~~~~~~

And yet, as you will come to see, making inferences regarding historical
relatedness underpins much of how we utilise biological sequence data.

So how can we decide which positions in two (or more) sequences are
related?

----

The Dotplot – an extremely useful visualisation approach
--------------------------------------------------------

This very neat approach to establishing the relatedness between
biological sequences was invented here at ANU, by Dr. Adrian Gibbs.

.. image:: images/dotplot_pub.png
    :scale: 50%

----

.. image:: images/dotplot_fig1ab.png
    :scale: 50%

----

.. note:: A subset of Figure 1 of Gibbs and McIntyre. Dotplot of cytochrome C amino acid sequences from Human to: Rhesus macaque, Tuna fish. (The N-terminus is at the top left, which corresponds to the “translation start” the protein.) Each dot indicates where the amino acid is identical between the two sequences.

    Long stretches of identity form a diagonal. A break – existence of multiple diagonals – can arise from changes in “state” (the amino acids differ, but the flanking amino acids are the same), or insertions / deletions (new sequence inserted or existing sequence removed) that have occurred. The latter are frequently referred to as “indels”.

*Note:* that when analysing two sequences, it is typically not possible to establish whether it was a deletion or an insertion.

----

Python coordinates differ from Cartesian coordinates
====================================================

In cartesian coordinates, they are ordered :math:`(x, y)` and the origin
is in the bottom left.

.. image:: images/cartesian_coords.png

----

In Python coordinates, they are ordered :math:`(y, x)` and the origin is
the top left.

.. image:: images/array_coords.png

----

The original dotplot algorithm
==============================

Consider two sequences, ``X`` and ``Y`` with lengths ``n`` and ``m``
respectively. We establish the matches between

----

Pseudocode
----------

::

   create a matrix of zeros, M, with dimensions n x m
   for i in 1 ... n:
       for j in 1 ... m:
           if X[i] == Y[j] then
               M[i, j] = 1

   display M as a grid with 1 equaling black, 0 white

.. note::  I am *not* using Python indexing here!

.. note:: This is, in effect, a k-mer matching algorithm where :math:`k=1`.

----

Demo output for the simplest dotplot
------------------------------------

::

   seq1  ACAGT
   seq2  AT

.. code:: ipython3

    from plotly.offline import iplot
    #        A  G  C  G  T
    data = [[1, 0, 0, 0, 0],  #  A
            [0, 0, 0, 0, 1]]  #  T
    
    trace = dict(type="heatmap", z=data,
                 colorscale=[[0.0, "rgb(256,256,256)"],
                             [1.0, "rgb(0,0,0)"]],
                 showscale=False)
    layout = {"width": 500, "height": 250, "legend":None, 
             "xaxis": {"showline": True, "mirror": True},
             "yaxis": {"showline": True, "mirror": True}}
    fig = dict(data=[trace], layout=layout)
    iplot(fig)

.. image:: output_18_0.png
    :scale: 25%

----

.. Let’s implement the dotplot algorithm!
