.. _intro_to_testing:

#################################
Introduction to Testing in Python
#################################

.. sectionauthor:: Gavin Huttley

.. todo:: add a continuous integration topic

********************************
Why do we need to test software?
********************************

When a scientist conducts an experiment in a lab, they generate results under some experimental condition which they then seek to interpret. Let us consider `PCR <https://en.wikipedia.org/wiki/Polymerase_chain_reaction>`_ as an example. A PCR experiment has 4 components (ignoring the hardware required to conduct the experiment):

1. A thermostable DNA polymerase enzyme
2. A reaction mix (the reagent) [#]_
3. DNA Primers [#]_
4. The **template** [#]_

.. [#] This provides a suitable environment for the DNA polymerase enzyme, includes essential ions and the chemical building blocks (dNTPs) to make DNA
.. [#] Short DNA fragments that complement the boundaries of the fragment to be amplified.
.. [#] In one sense, this corresponds to the "unknown query".

Let us consider a PCR experiment that has been applied to a query sample only and which did not result in any detectable amplified DNA. How does the experimentalist know how to interpret the result? The only conclusion that can be drawn is the result is ambiguous because there are multiple possible explanations [#]_ due to too many potential sources of error in the experiment.

.. [#] The query truly does not contain the target sequence. Alternately, the enzyme may have been defective, or the dNTPs were missing, etc...

Now consider if we added a **positive control** to this experiment. This corresponds to including a replicate such that components 1-3 were identical but the template (component 4) is now DNA that is *known* to contain the target. For this replicate, we have eliminated one source of uncertainty (the template contains the target) on the basis of previous work. Accordingly, we reasonably expect a positive outcome (amplified DNA is certain). If, in this replicate, DNA *was* amplified we could eliminate defects in components 1-3 as a basis for the absence of amplified DNA from our query template.

Now imagine we run another experiment with two replicates, one of which is a positive control, the other is a different query template. In this experiment, amplified DNA was found for both the positive control and the query. We have another ambiguous conclusion [#]_.

.. [#] The query truly does contain the target sequence. Alternately, the enzyme mix (or reagent mix, or primers) was contaminated with a sequence containing a match etc...

If we add a **negative** control to this experiment, we have much clearer capacity to interpret the outcome. A negative control would be another replicate with the same components 1-3, but no template. Again, there is a known outcome for this replicate (no amplified DNA). If, in our rerunning of the experiment, there was no amplified DNA in the negative control, then the interpretation is much clearer.

Quite clearly, the inclusion of experimental controls affects the interpretability of the results.

To extend this analogy further, this level of controls really reflects a common view of how "science" is undertaken. Any experimental test of an unknown is accompanied by testing replicates where the outcome is known *a priori*. It is the results of an assay on those knowns that guides our conclusion with regard the sample that had material whose properties were unknown.

The success of experiments such as what I have described above relies on another level of checking. These are quality control checks of the integrity of the ingredients that go to make up each of the different components. Checks that the DNA polymerase enzyme is, in fact, a DNA polymerase and that its concentration is correct. Checks that all of the prescribed components of the reagent mix are present and in the correct concentration. Checks that these components do not contain any DNA contamination, etc... When these building blocks are rigorously verified we have confidence that we will not waste our time in conducting an experiment.

I would hope, at this point, that you can start to see the parallels with writing software. The functions we write in a program become components of larger algorithms, just like the components in the PCR experiment. And just as quality control checks are required for producing the components of any empirical experimental system, so too are quality control checks required for our functions. These checks are tests of correctness of those functions.

.. note:: The interpretability of output from algorithms remains uncertain unless suitable controls are run.

**********************************
The structure of tests of software
**********************************

.. epigraph::

    “The more I learn about proprietary software, the more I worry that objective truth might perish from the earth.”
    
    --- Professor Paul Romer, Awarded the 2018 Nobel Prize in Economics, and Python Programmer.

To test software function we must write additional code. This additional code uses our functions, providing an assortment of inputs and ensuring the resulting outputs match our prior expectation. In the same way that you should not trust results from an experiment that was performed without suitable controls, you should not trust the output of software that has not been adequately tested. Before I proceed to examples, I emphasise here that what we will begin to undertake corresponds to the quality checks described for the integrity of the ingredients used for the experimental system. Correctly designing experiments with controls must also be done when those experiments are computational and this is the much harder problem!

Let us begin by defining a problem that we wish to solve. Say I need a function to process gene coordinates. The function will receive the start and end positions of a gene and return the DNA strand on which it is encoded [#]_.

.. [#] For the non-biologist, DNA is a double helix whose individual strands are antiparallel. A gene is a directionally encoded block of information that is absolute and all genes are chemically oriented in the same way. With respect to a genes encoding, its start position is always less than its end position. The frame of reference by which we refer to DNA is arbitrary. The chosen reference DNA strand is referred to as the plus ("+") strand and its complimentary partner as the minus strand. Accordingly, from a "+" strand frame of reference the coordinate for the end of a "-" strand gene occurs before its start.

.. jupyter-execute::

    def get_strand(start: int, end: int) -> str:
        if not type(start) == type(end) == int:
            raise TypeError("must be integers")
        
        if start == end:
            raise ValueError("gene start cannot equal end")
        
        if min(start, end) < 0:
            raise ValueError("gene cannot have a negative coordinate")
        
        return "+" if start < end else "-"

This function returns the ``"-"`` character if the start position is greater than the end, indicating the gene is on the minus strand, ``"+"`` otherwise. Note I'm also checking that the inputs are positive integers and that they are not equal to each other.

How we test this is by writing functions that check different aspects of its execution. The most crucial component of a test function is use of an ``assert`` statement. We assert will assert that ``get_strand()`` returns an expected value given specific inputs. While the order in which you write tests does not matter, I'm going to start by checking it produces the output I expect for data for which an output is define.

.. index::
    pair: fail; test
    pair: pass; test

.. note:: A test is considered to have **failed** if an ``AssertionError`` was raised. A test **passed** if there was no ``AssertionError``.

.. jupyter-execute::

    def test_get_strand_output():
        """given well formed input it should produce expected output"""
        assert get_strand(0, 2) == "+"
        assert get_strand(20, 20000) == "+"
        assert get_strand(20000, 20) == "-"
        assert get_strand(2, 0) == "-"
    
    test_get_strand_output()

I also want to be sure that if I give it invalid data, that each of the cases I have attempted to catch are in fact caught. This is a good point at which to introduce you to the fact that software libraries exist that are designed to facilitate software testing. One of their features is they make it easier to check that specific types of assertions are raised. I will use the pytest_ library.

.. jupyter-execute::

    import pytest
    
    def test_just_ints():
        """only integers are allowed"""
        for a, b in [(0, 23.0), ("ab", 2), (1.0, 40.0)]:
            with pytest.raises(TypeError):
                get_strand(a, b)
    
    test_just_ints()

I also need to check if I give it either equal start, end or a negative value. In this case, we have a different error type.

.. jupyter-execute::

    def test_no_negatives():
        """only positive integers"""
        for a, b in [(0, -23), (-1, 40), (-1, -20)]:
            with pytest.raises(ValueError):
                get_strand(a, b)
    
    def test_no_equal():
        """no equal values"""
        for a, b in [(0, 0), (1000, 1000)]:
            with pytest.raises(ValueError):
                get_strand(a, b)
    
    test_no_negatives()
    test_no_equal()

.. note:: All the test functions are named such that the function name begins with the word ``test``. This is by design since testing tools use that information to find tests in a project.

*****************
How tests are run
*****************

From the terminal
=================

While the functions written in this document illustrate the nature of testing some code, they do not reflect how tests are organised and run in practice.

If you adhere to conventions used by testing libraries like pytest_, these tools are able to automatically detect test functions. As noted above, beginning the test functions with ``test`` makes the tests discoverable [#]_. Testing software also calls these functions. This means it is not necessary to make the calls yourself. Just define the function and run the test tool against your code.

As an example, I have a project called cogent3_ and in the main directory of the repository I have a directory called ``tests``. I invoke all my tests by doing the following

.. code-block::

    $ cd path/to/cogent3/tests
    $ pytest

.. [#] When ``pytest`` is run within a directory, it searches all files for class / function names that match this (or a related) pattern. These tests are thus *discovered* by pytest.

In a jupyter notebook
=====================

Testing code within a notebook is more restricted than for standard python scripts. There is a third-party library, ``ipytest`` which provides mechanisms for using ``pytest`` to run tests in notebooks. See `the documentation <ipytest>`_ for how to use it.

*************
Test coverage
*************

Defining the quality of software is a difficult problem. From an individuals perspective, a useful benchmark for your own code is how many lines of your code are actually exercised by your tests? This is referred to as "code coverage". Some IDEs, like PyCharm, build in tools to obtain such measures. There is also an extension to pytest, `pytest-cov <https://github.com/pytest-dev/pytest-cov>`_, which can be easily invoked using command line flags when you run your tests. I can run this and have it generate a html file, which allows exploring the sections that are not covered by tests. For ``cogent3``, I run the following.

.. code-block::

    $ pytest --cov-report html --cov=cogent3 ./ --ignore=test_app_mpi.py

******************************************
Adding testing to your ongoing development
******************************************

As projects become larger, adding tests along with new features becomes crucial. Automating the execution of tests is an important step that simplifies the process of developing your code. Tools for continuous integration (often referred to as CI) are now builtin to many of the standard code hosting platforms. On GitHub, they are termed `GitHub Actions <https://github.com/features/actions>`_, on `Bitbucket they are termed pipelines <https://bitbucket.org/product/features/pipelines>`_.

