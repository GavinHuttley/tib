Introduction to Comparison of Biological Sequences
==================================================

The comparison of biological sequences is arguably the core task of bioinformatics. In this course, we split this into two domains: comparison of sequences that are related solely by function; comparison of sequences that share a common ancestor.

We start the topic by framing the problem of sequence analysis from the perspective of what we understand about the origins of biological sequences and the role they play in living systems. Our purpose with these descriptions is not to provide an exhaustive background but, hopefully, just a refresher of things you already know.

Descended from a common ancestor
--------------------------------

In 1859, Charles Darwin (aka the Dude!) published his seminal work on the origin of species. In it, he proposed that descent occurred with modification and that this "modification" was heritable variation which affected an individuals ability to survive and reproduce. Evolution thus occurring as a consequence of natural selection eliminating individuals that contained variants not well suited to their environment and / or had a lower ability to reproduce when compared to their contemporaries.

Darwin clearly understood that organismal phenotype was heritable and thus required an information system with associated mechanisms for its transmission. He further understood that differences existed between individuals in the copy of the information system they possessed which must be responsible for those differences in phenotype. But he did not understand the mechanism of how inheritance occurred [1]_.

.. margin::
  
    .. [1] Well he did have a model, but it was disproved by his cousin, Francis Galton, a major figure in the history of statistics.

Darwin's work was highly controversial at the time, including his conclusion that all living things on Earth had descended from a common ancestor.

Just 6 years later, in 1865, Gregor Mendel published his work on the laws of inheritance. These constitute the foundation principles of what we now refer to as genetics [2]_. Unfortunately, Mendel's work was largely ignored for 35 years until after it was replicated by 3 botanists (de Vries, Correns, and von Tschermak-Seysenegg). It took another 53 years before Watson and Crick presented evidence for the physical structure of the hereditary molecule -- DNA. This laid the foundation for examination of how information for life is encoded.

.. margin::
  
    .. [2] Mendel did not use that term.

In the 1920-40's, seminal work done by |Sewall_Wright|_, `J. B. S. Haldane <https://en.wikipedia.org/wiki/J._B._S._Haldane>`_,  `Ronald Fisher <https://en.wikipedia.org/wiki/Ronald_Fisher>`_, `Theodosius Dobzhansky <https://en.wikipedia.org/wiki/Theodosius_Dobzhansky>`_ and others established what is referred to as the "Neo-Darwinian Synthesis". This work re-expressed Darwin's theory in terms of genetical mechanisms of inheritance -- unifying the two fields. The work is dominantly mathematical, it constitutes the foundations of population genetics, and it provides the basis from which we now view the distribution of genetic variation. Another major extension to those foundations from which we interpret genetic variation was the work of Motoo Kimura in 1968 on the Neutral Theory of Molecular Evolution. (As in all the above, there were numerous other contributors to development of these ideas and theory.)

These large frameworks provide a perspective from within which we can view biological systems, irrespective of the scale we are interested in. Ranging from biochemical reactions, to cellular biology to organisms to ecosystems. All levels of biological organisation have been shaped by the processes that govern the inheritance of the molecular information system and by the relationship between the information encoded in DNA and its manifestation in phenotype.

In this topic we will begin thinking about how we can interrogate DNA sequences to discover how information is encoded and how we can quantify relationships among DNA sequences. The latter is a precursor to a mechanistic understanding of how evolution has, and is, operating.

The major take-home messages relevant to this topic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- All living things on the planet ultimately descended from a common ancestor
- Both parents transmit hereditary information to progeny [3]_
- Hereditary information is encoded in a nucleic acid, typically DNA
- Each position in a DNA sequence derived from a residue in an ancestor

.. margin::
  
    .. [3] For diploid, sexually reproducing organisms.
