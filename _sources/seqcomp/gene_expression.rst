.. _gene_expression:

Gene expression in a nutshell
=============================

.. todo:: add screencast on gene expression. It should emphasise role of TFs, interacting with DNA.

The purpose of this section is not to present an authoritative synopsis of gene expression. Instead, the objective is to present a simplified overview of what we understand about the nature of information encoding in DNA which influences gene expression and how that information is organised.

.. figure:: /_static/images/seqcomp/Gene_structure_eukaryote_2_annotated.svg
    :name: gene regulation
    
    The structural elements of eukaryotic genes
    
    Image by `Thomas Shafee <https://en.wikipedia.org/wiki/File:Gene_structure_eukaryote_2_annotated.svg>`_

.. index::
    pair: transcription start site; TSS

The :ref:`structural elements of eukaryotic genes <gene regulation>` figure illustrates both the generalised information content associated with genes, and the stepwise processes via which a gene is transcribed and ultimately translated into a protein. I want to draw your attention to the annotated segments that are listed as regulatory sequence. Such segments exist at the 5'- and 3'- boundaries of a gene. Between these lies the gene body, consisting of exons and introns. Immediately flanking the gene are the UTR (untranslated region). Preceding the 5'-UTR is the promoter region which is further broken into "core" and "proximal". The promoter region is the target for binding of molecules that facilitate and/or initiate transcription the downstream gene into RNA. The transcript includes the UTRs as well as the gene body. One important feature not explicitly represented in this figure is the actual site at which transcription starts. This is commonly referred to as the TSS (transcription start site). The TSS is largely defined by the core promoter :cite:`Juven-Gershon:2008aa`. As that citation argues, there can be variability in the TSS for an individual gene. We are primarily interested in how information is encoded in promoter regions.

.. index::
    pair: transcription factor binding site; TFBS
    pair: transcription factor; TF
    pair: cis-regulatory module; CRM

.. margin:: Cartoon of regulatory element organisation
    :name: regulatory element organisation

    .. figure:: /_static/images/seqcomp/transcription.png
        :scale: 75 %
    
        Regulatory element organisation in eukaryotic DNA
    
        From `Wasserman, & Sandelin <http://doi.org/10.1038/nrg1315>`_

.. margin:: Binding to DNA
    :name: Binding to DNA

    .. figure:: /_static/images/seqcomp/tata_bp.png
        :scale: 50 %
    
        Crystal structure of TBP bound to a short segment of DNA
    
        Structure `from NCBI <http://bit.ly/2i0s4pk>`_

A somewhat more detailed cartoon presenting concepts of regulatory encoding is shown in the :ref:`Figure on regulatory element organisation <regulatory element organisation>`. One elementary encoding unit of regulatory information is the TFBS (transcription factor binding site). These are the target binding sequence of transcription factors (or TFs, see `Binding to DNA`_). As illustrated, some TFBS are localised proximal to the TSS while others are more distant. The exact distance (measured in terms of length of DNA sequence between the TFBS and the gene TSS) can be quite extensive [1]_. Also of interest here is the occurrence of cis-regulatory modules (CRMs) where multiple TFBS occur in a cluster, indicating binding by multiple TFs is involved in regulating a genes expression. This figure incorrectly implies that gene regulatory signals only exist outside the gene. Enhancer elements located within introns have been reported.

.. margin::
  
    .. [1] Application of chromatin conformation capture experimental procedures have demonstrated  that, within the nucleus, primary sequence span is not always a reliable measure of physical proximity between regulatory elements and the genes regulate :cite:`Fullwood:2009aa,Lieberman-Aiden:2009aa`.

This is a grossly simplified representation of how gene regulation happens. Regulatory control is a complicated process mediated by multiple elements.

How can we, as data analysts, inform the understanding of this complex problem? All statistical, and / or computational, analyses should start simple. Start with simple hypotheses and evaluate it and define a new hypotheses. By iterating this process we can gradually build well founded, more complicated models. In this process there should also be, ideally, empirical experiments.

Exercises
=========

#. Make a visual **model** of how information is transformed from its genomic encoding into molecular action. From the above, draw a "simple" schematic [2]_ that shows the essential components of a gene. Add to that drawing elements that illustrate the presumed causal relationship of TFs and TFBs to the transcription of the gene into RNA. A drawing on paper is fine! You want this model to be reflect the essential patterns of this process. Imagine trying to explain this process to a first year student using your schematic. (Your schematic should be :ref:`simpler than the one above <regulatory element organisation>`.)

#. Use your model to explain the case of no gene expression.

.. margin::
  
    .. [2] By simple I mean do not add every possible configuration for how things might be organised. For instance, just focus on the gene and its immediately flanking sequence. Decide what the *essential* features are and just draw those.  Your model is wrong, but it is your starting point for beginning to reason about this essential biological process.

------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha
