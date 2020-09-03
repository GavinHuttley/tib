Data
====

Classes of related sequences
----------------------------

Homolog
    Sequences descended from a common ancestor.

Ortholog
    Sequences that have evolved from a common ancestor by speciation. Typically, orthologous genes in different species retain the same function. For example, the TP53 gene in human and mouse.

Paralog
    Paralogs are sequences that arose from duplication within the same genome. For example, multi-gene families such as the haemoglobins.

.. figure:: /_static/images/molevol/homologs.png
    :scale: 100%

    Homologous gene types.

    Homologs are formed from duplication events. Gene duplication events within a species result in paralogs (or paralogous genes). These can evolve distinct new functions (e.g. the globins). Speciation events lead leads to orthologs (or orthologous genes) whose function is putatively unchanged in the different species. The phylogeny between orthologs that remain unique in their respective genomes should reflect the species tree.

    Figure from :cite:`Searls:2003aa`.

Exercises
---------

I have queried the Ensembl database for some haemoglobins from Human and Macaque. For each database record, I've used Ensembl's definition of the "canonical transcript" (or "major" transcript). I've then obtained the CDS (coding sequence) for each record. I named the sequences {Species Common Name}-{a letter}. I then aligned the sequences.

.. jupyter-execute::
    :hide-code:

    from cogent3 import load_aligned_seqs

    aln = load_aligned_seqs("data/hba1_hbb-aligned.fasta", moltype="dna")
    name_map = {"Human-HBA1": "Human-z", "Rhesus-HBA1": "Rhesus-e", "Human-HBB": "Human-j", 'Rhesus-HBB': "Rhesus-x"}
    aln.rename_seqs(lambda x: name_map[x])

#. Which of the above are orthologs?
#. Which are paralogs?
#. For these sequences, how would you describe the divergence between orthologs compared to that between paralogs?


------

.. rubric:: Citations

.. bibliography:: /references.bib
    :filter: docname in docnames
    :style: alpha
