.. index::
    download data

.. margin:: Downloading data files to your computer
    :name: download_data
    
    .. code-block:: python
        
        import cogent3

        url = "https://replace with the full url to the file"
        aln = cogent3.load_aligned_seqs(url)
        aln.write("som/local/path.fa")
        
    Several sections have sample data files for you to work on. The ``cogent3.loading...`` `functions  <https://cogent3.org/doc/api/index.html#loading-data-from-file>`_ can read content from urls. They will return a ``cogent3`` object which has a ``write()`` method that can be used to save the data locally. The above example is for downloading an alignment. To get the url, you need to right+click (or control+click) on the web page link and select "copy link". Paste that into your notebook as per above.
    
    .. note:: Since the filename suffix is used to identify the file format, make sure the local filename has the same suffix as the original.

.. _cogent3_topic:

#################################################
Molecular Evolutionary Analyses Using ``cogent3``
#################################################

We have focussed, thus far, on developing an understanding of programming logic and then applied that to tackling basic algorithmic tasks in sequence comparison. While this skill is invaluable, there is an advantage to using existing tools designed for manipulating the data types that define the fundamental structures in the analysis of biological data. Combining your developing skills in programming with familiarity of important domain specific tools, you greatly expand the range of problems you can address. You will find cases where are able adapt existing tools to solving problems for which there is no current solution.

``cogent3`` is just such a library for analysis of genomic sequences. Just as ``numpy`` provides critical capabilities for solving numerical computational problems, ``cogent3`` provides the analogous tools for handling biological data and certain categories of analysis. 

``cogent3`` is a Python library for handling genomic data with particular strengths in statistical analysis of genomic divergence. It provides tools for loading standard data formats, manipulation of biological data, statistical modelling (including standard statistical tests). These will be introduced via introduction to the major data types and concepts.

.. note:: See cogent3_ for the full project documentation. We will link to specific sections as appropriate.

.. toctree::
    :hidden:

    data_formats
    sequences
    explore_variation
    genetic_codes
    moltype
    apps
    using_models
    tables
    statistical_tests

.. todo:: json
    serialisation

.. todo:: advanced sequence and alignment

    annotations, sequence features
    entropy
    provenance and the info attribute
    output formats
    strand symmetry

.. todo:: intro phylogenies
.. todo:: phylogenetic trees

    loading, making, newick format, handling spaces
    drawing

.. todo:: intro models and hypotheses
    rate matrices
    motif probs

.. todo:: statistical tests

.. todo:: data formats
    json