Introduction to Comparison of Biological Sequences
==================================================

The comparison of biological sequences is arguably the core task of bioinformatics. In this course, we split this into two segments: whether the sequences are related solely by function, or whether they share a common ancestor.

For this topic, we frame problems in terms of biological questions and, where relevant, specific biological theory. Computational development is focussed on representing research questions as algorithms and interpreting their application on biological data.

The role of sequence in encoding life
-------------------------------------

.. figure:: /images/transcription.png
    :scale: 50 %

    The organisation of eukaryotic DNA [1]_.

.. [1] From `Wasserman, & Sandelin <http://doi.org/10.1038/nrg1315>`_

.. figure:: /images/in_dna.png
    :scale: 50 %
    
    Epigenetic factor positioning encoded by DNA [2]_. 

.. [2] From `Science, 322, 434–438 <http://doi.org/10.1126/science.1160930>`_

Some short stretches of DNA sequence (referred to as motifs) are central to regulation of gene expression. This property can arise from direct binding of protein to DNA.

.. list-table:: Crystal structure of TBP bound to a short segment of DNA [3]_

    * - .. figure:: /images/tata_bp.png
            :scale: 48 %
            :align: left
            
            [3]_
      - .. figure:: /images/tata_logo.png
            :scale: 48 %
            :align: right

.. [3] Structure `from NCBI <http://bit.ly/2i0s4pk>`_

The figure shows the  on the left, while the right panel is a representation of the DNA sequences to which TBP binds.
