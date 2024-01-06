.. margin:: Protein binding to DNA and sequence information
    :name: Binding to DNA

    .. figure:: /_static/images/seqcomp/tata_bp.png
        :scale: 50 %
    
        Crystal structure of TBP bound to a short segment of DNA
    
        Structure `from NCBI <http://bit.ly/2i0s4pk>`_

    .. figure:: /_static/images/seqcomp/tata_logo.png
        :scale: 50 %
    
        An information theoretic representation of sequence preference of TBP
        
        Logo `from Jaspar <http://jaspar.genereg.net/matrix/MA0108.2/>`_.

.. _encoding_info:

The role of sequence in encoding life
=====================================

A grand challenge in biology is to understand how life is encoded. We understand simple encoding cases and how the information is converted into function. In general, "biological information" is abstractly represented by a series of nucleotides in a nucleic acid. To transform that information into a functional molecule requires a process of transcription. For instance, DNA can encode a protein and that protein is produced via a process of transcription of DNA into RNA and subsequent translation of the RNA into a polypeptide (a chain of amino acids). Alternately, if the DNA encodes a functional RNA molecule then only transcription is required.

Our understanding of encoding of functional molecules leads to the view that the genome of an organism contains, at the very least, the instructions required to specify a substantial part of organismal phenotype. But we also know that an organism is not simply represented by the ordering of nucleotides into large DNA molecules.

All :math:`\sim 10^{13}` cells in our body contain the same genome. And yet somehow, these cells manage to attain distinct cellular phenotypes, such as cardiac cells, sperm cells, hair follicle cells, etc. How is a complex multicellular organism, like us, achieved when their cells have the same information content? The answer lies in their selective reading of that information.

It is long been appreciated that regulatory control of genes underpins cell-type-specific differentiation. This is achieved by a layer of regulatory encoding -- referred to as epigenetics -- and associated molecular mechanisms. For instance, in eukaryotes DNA associated with an octamer of histone proteins forms a structure referred to as a nucleosome (see :ref:`DNA organisation <organisation_dna>`). These provide the molecular foundation for changing the level of compaction of DNA. Highly compacted chromatin is inaccessible to the machinery responsible for transcribing DNA into RNA, thus preventing it from contributing to cellular phenotype [1]_. Cell type differences in which genomic regions are accessible thus leads to cell type differences in phenotype.

.. [1] It's worth highlighting that there seems to be a threshold in the number of mRNA transcripts from a gene that are required before the encoded product is produced to a level sufficient to influence phenotype. Examination of the raw experimental data from RNAseq experiments (which quantify transcript abundance) reveals that some level of RNA appears evident for almost all genes. In other words, just because transcripts of a gene exist in a cell does not mean the gene is "functioning" in that cell.

.. figure:: /_static/images/seqcomp/transcription.png
    :scale: 75 %
    :name: organisation_dna
    
    Organisation of eukaryotic DNA
    
    From `Wasserman, & Sandelin <http://doi.org/10.1038/nrg1315>`_

Mechanistically, how do these interactions with DNA work? Some short stretches of DNA sequence (referred to as motifs) are central to regulation of gene expression. One instance of this is illustrated in `Binding to DNA`_. The crystal structure of the transcription factor protein TBP and it's target DNA sequence shows how the former slots into the minor groove of the associated DNA sequence. The lower panel shows a visualisation (referred to as a :index:`sequence logo` :cite:`Schneider:1990aa`) that summarises the affinity of TBP to specific bases in a DNA sequence. I point out here, not all DNA interacting molecules demonstrate such clear target sequence specificity. Of particular note is evidence that histone octamers do not have such specificity.

.. margin:: Encoded in DNA
    :name: Encoded in DNA

    .. figure:: /_static/images/seqcomp/in_dna.png
        :scale: 50 %
    
    Epigenetic factor positioning encoded by DNA.

    From `Science, 322, 434–438 <http://doi.org/10.1126/science.1160930>`_

Understanding epigenetics is clearly crucial to understanding cellular processes. But the question remains, where is the information for epigenetic control encoded? One elegant experiment that endeavoured to tackle this question is highlighted in the sidebar (`Encoded in DNA`_). Wilson et al took advantage of an inbred mouse strain that segregates human chromosome 21. They asked the question, do the mouse epigenetic factors (e.g. transcription factors and other DNA binding molecules) bind to this piece of human DNA where the human epigenetic factors do? This would indicate the information is encoded in the human DNA sequence. Or, do they bind elsewhere? This would indicate they are guided to their position by mouse-specific information.

The results best supported the former interpretation -- epigenetic factor binding and thus regulatory control is specified in the DNA. So perhaps DNA really does encode everything!

