Biological Data Formats
=======================

.. raw:: html

    <figure style="padding: 4px;">
    <img src="https://imgs.xkcd.com/comics/standards.png" style="height: auto; max-width=75%" alt="Editor Wars">
    <figcaption>Read the original at <a href="https://xkcd.com/927/">XKCD</a></figcaption>
    </figure>

Oh dear, this is a mess. Not this document, but the "multitude" of data format standards in Bioinformatics. Bioinformatics is replete with different variants on basic formats. Not all standards are well documented and support for them is ... well, I hope your experience is better than mine. The fact that data formats can be such a problem is a great argument for :ref:`knowing how to code <intro_to_python>`, since that skill gives you the ability to handle the different format variants that no existing tool handles.

The above aside, I will briefly describe and link [1]_ to the canonical description of a data format for the main types of data. I've grouped these into formats related to the major biological data types of sequences, genomic features, and phylogenetic trees.

.. margin::
  
  .. [1] If I can find one.

Sequences and alignments
------------------------

``fasta``
^^^^^^^^^
The most commonly, and probably the easiest to parse, format is that of ``fasta``. There are too many variants of this basic format, so I just `link to the Wikipedia entry <https://en.wikipedia.org/wiki/FASTA_format>`_ and then present an example below.::

    >seqlabel 1 line
    ACCGGTGA
    AAG
    >seqlabel2
    AGGCG

While this is listed as a sequence format it's often used to include multiple sequences, which may be aligned.

``genbank``
^^^^^^^^^^^

GenBank_ is a web portal to a multitude of valuable databases and bioinformatic tools. They also define a number of data file formats and, in particular, the ``genbank`` format for sequence data. This is format includes at a minimum extensive meta-data about a database entry. They do not always contain sequence, but will at least reference identifiers of related sequence records in their database. Below is a `sample record <https://www.ncbi.nlm.nih.gov/nucleotide/AF165912>`_ from GenBank (which  I've edited for brevity)

.. code-block:: text

    LOCUS       AF165912                5485 bp    DNA     linear   PLN 29-JUL-1999
    DEFINITION  Arabidopsis thaliana CTP:phosphocholine cytidylyltransferase (CCT)
                gene, complete cds.
    ACCESSION   AF165912
    VERSION     AF165912.1
    KEYWORDS    .
    SOURCE      Arabidopsis thaliana (thale cress)
      ORGANISM  Arabidopsis thaliana
                Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
                Spermatophyta; Magnoliophyta; eudicotyledons; Gunneridae;
                Pentapetalae; rosids; malvids; Brassicales; Brassicaceae;
                Camelineae; Arabidopsis.
    REFERENCE   1  (bases 1 to 5485)
      AUTHORS   Choi,Y.H., Choi,S.B. and Cho,S.H.
      TITLE     Structure of a CTP:Phosphocholine Cytidylyltransferase Gene from
                Arabidopsis thaliana
      JOURNAL   Unpublished
    REFERENCE   2  (bases 1 to 5485)
      AUTHORS   Choi,Y.H., Choi,S.B. and Cho,S.H.
      TITLE     Direct Submission
      JOURNAL   Submitted (06-JUL-1999) Biology, Inha University, Yonghyon-Dong
                253, Inchon 402-751, Korea
    FEATURES             Location/Qualifiers
         source          1..5485
                         /organism="Arabidopsis thaliana"
                         /mol_type="genomic DNA"
                         /db_xref="taxon:3702"
                         /ecotype="Col-0"
         gene            1..4637
                         /gene="CCT"
         regulatory      1..1602
                         /regulatory_class="promoter"
                         /gene="CCT"
    <features removed for brevity>
    ORIGIN
            1 ccagaatggt tactatggac atccgccaac catacaagct atggtgaaat gctttatcta
           61 tctcattttt agtttcaaag cttttgttat aacacatgca aatccatatc cgtaaccaat
          121 atccaatcgc ttgacatagt ctgatgaagt ttttggtagt taagataaag ctcgagactg

``gff`` – general feature format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

     The GFF format, although widely used, has fragmented into multiple incompatible dialects.

     --- Lincoln Stein, in the prologue to defining ``gff3``.

Sounds like the cartoon at the top doesn't it! Anyway, it is widespread and an important format for storing information about sequence annotations [2]_, so here's the canonical gff3_ definition. This is a tab delimited format with 9 distinct fields. It's the last field, ``attributes``, that proves to be the most difficult to parse. Below is a small sample of a file posted on the definition page.

.. margin::
  
  .. [2] Annotations associate a reported feature of the sequence and the specific sequence coordinates to which it maps, e.g. the promoter for the gene CCT in the sample GenBank record.

.. code-block:: text

     0  ##gff-version 3.1.25
     1  ##sequence-region ctg123 1 1497228
     2  ctg123 . gene            1000  9000  .  +  .  ID=gene00001;Name=EDEN
     3  ctg123 . TF_binding_site 1000  1012  .  +  .  ID=tfbs00001;Parent=gene00001

.. _newick:

newick format for phylogenetic trees
------------------------------------

This is the most widespread text format for dsitributing phylogenetic trees. Clades of lineages are denoted by ``()`` and separate by ``,`` and can be grouped into subclades. Branch lengths are indicated by numbers after a colon character. There is some funky behaviour around dealing with spaces in tip names, they are often represented in the name as an underscore character (``"_"``). If you can, avoid any issues by not having spaces or underscores in names. Here's a sample. 

.. code-block:: text
    
((Human:0.006062440217780064,Chimpanzee:0.003020541234140796):0.09488527928524751,((Mouse:0.06659142318491332,Rat:0.05783486638653178):0.17244926332734278,Wombat:0.4522900123679113):0.0424545337445269,Horse:0.05802695948476483);