.. sidebar:: Paths to files and folders

    .. raw:: html
    
        <video width="50%" height="50%" controls>
          <source src="https://cloudstor.aarnet.edu.au/plus/s/eNFvT0aJuBjbxw4/download" type="video/mp4">
          Your browser does not support the video tag.
        </video>


.. sidebar:: Reading a text file using an IDE

    .. raw:: html
    
        <video width="50%" height="50%" controls>
          <source src="https://cloudstor.aarnet.edu.au/plus/s/xmNqykwFd73UnTg/download" type="video/mp4">
          Your browser does not support the video tag.
        </video>

.. role:: python(code)
   :language: python

Working with files
==================

.. index::
   pair: file path; files
   pair: open(); files
   pair: open mode; files

The location of a file (its file path) is specified as a string (see the screencast on Unix Paths). We use the ``open()`` function to open files. Whether a file is opened for reading or writing is defined by the *mode* argument. For example ``mode="w"`` means write. Any pre-existing contents in the file would be lost. Opening a file to read does not return the files contents.

.. sidebar:: File properties

    File objects behave like a standard Python series, you can *iterate* over their lines. See the "Reading a text file..." screencast.

.. note:: File objects have a ``close()`` method, which you should use when finished.

.. jupyter-execute::
    :raises:

    seqfile = open("data/sample.fasta", mode="r")
    print(type(seqfile))

.. jupyter-execute::
    :linenos:

    print(seqfile)

.. index::
   pair: close; files

Then closing it using the ``close()`` method.

.. jupyter-execute::
    :raises:

    seqfile.close()

.. jupyter-execute::

    print(seqfile)

There is another approach to ensuring the file is always closed. This involves using the ``with`` statement. This statement invokes what's referred to as a "context manager". The advantage to using this approach is it ensures the file is closed.

.. jupyter-execute::

    with open("data/sample.fasta", mode="r") as seqfile:
        print(seqfile)

.. jupyter-execute::

    seqfile.closed  # closed for us

Reading contents of a file
--------------------------

File objects are iterable and the "unit" of iteration is a line, i.e. the file object returns all data up until the next line-feed character.

.. index::
   pair: iterate contents; files

.. jupyter-execute::
    :linenos:

    # the default mode argument value is "r"
    with open("data/sample.fasta") as seqfile:
        for line in seqfile:
            print(repr(line))

.. note:: I've used a built-in function ``repr()``. This shows the *representation* of the object. I've done that here because it shows the new-line characters at the end of each line.

Writing data to a file
----------------------

In order to write data to a file, we must specify the ``mode="w"``.

The data also needs to be converted to strings. One way to do this is to use a string format conversion. For instance, consider the example of having a list of float's. If we try to write this to a file, it will raise an exception.

.. index::
   pair: writing; files

.. jupyter-execute::
    :linenos:
    :raises:

    nums = [0.378, 0.711, 0.349, 0.897]

    with open("some-data.txt", mode="w") as outfile:
        outfile.writelines(nums)

.. note:: I've used the ``writelines()`` method, which attempts to write every element of the series.

So we need to convert to strings AND we need to put a new-line character at the end of each one.

.. jupyter-execute::
    :linenos:
    :raises:

    text = ["%f\n" % v for v in nums]
    with open("some-data.txt", mode="w") as outfile:
        outfile.writelines(text)

Writing delimited output
------------------------

One of the most common data file formats are ones where multiple fields on line correspond to one record. The different fields are separated from each other by a common *delimiter*, a specific character. Such a format is very easy to parse.

For instance, the *GFF* format (Generic File Format) is a file format commonly employed in genomics for storing genome annotation data, e.g. locations of genes or exons. GFF is a plain text file format with the following fields::

    <seqname> <source> <feature> <start> <end> <score> <strand> <frame> [attributes] [comments]

According to the format specification, these fields are tab (``'\t'``) delimited. To generate such output we need to store the field values in a series object (such as a list). This allows us to then use the string ``join()`` method to produce a single string with all field elements.

.. note:: Writing comma delimited files is done in the same way. Just replace ``'\t'.join`` with ``','.join``.

Exercises
=========

**1.** Below I have two GFF records stored as a list of records, each record being a list. Write these data to a tab-delimited file.

.. jupyter-execute::
    :linenos:

    annotations = [
        [
            "scaffold-650",
            "projected",
            "gene",
            "71406",
            "72760",
            ".",
            "+",
            ".",
            "ID=TRIVIDRAFT_53420;Name=TRIVIDRAFT_53420",
        ],
        [
            "scaffold-650",
            "projected",
            "exon",
            "71406",
            "71690",
            ".",
            "+",
            "0",
            "Name=exon-1;Parent=TRIVIDRAFT_53420",
        ],
    ]

**2.** On linux and MacOS, the ``\n`` character is used to denote line endings. Windows uses ``\r\n``. Using ``help(open)``. Figure out how you would specify a file is written using line endings that differ to your operating system. Then do that for the data above.

**3.** How you can check the line-endings of a file using Python. Is their another tool for your operating system?

----

This :download:`tab delimited text file <../data/donor_by_cancer_type.tsv>` is derived from the `Pan-Cancer Analysis of Whole Genomes project <https://dcc.icgc.org/pcawg>`_. Using this file, answer the following using plain python only (no 3rd party libraries).

**4.**  The file contains two columns: ``Donor_ID``, ``Project_Code``. Parse this file to produce a list of ``Donor_ID`` whose ``Project_Code`` equals ``"Skin-Melanoma"``.

**5.** Read the lines from this file and create a ``dict`` with keys corresponding to ``Project_Code`` and values being the list of all corresponding ``Donor_ID``, e.g. :python:`{'CNS-PiloAstro': ['DO36068', 'DO35934', ...`.

