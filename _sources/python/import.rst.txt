.. index:: import, modules

Extending capabilities using ``import``
=======================================

In Python, the capabilities of the core name space is relatively stripped down. Much of the power of the language comes from the availability of modules. For instance, many basic mathematical operations must be imported, e.g. ``log`` or ``sqrt`` are functions that exist within the ``math`` module. This module is part of what is referred to as the Python *standard library*, i.e. it comes standard with all Python installations. How we gain access to these is through the ``import`` statement.

.. jupyter-execute::
    :linenos:

    import math

    math.sqrt(4)

.. jupyter-execute::
    :linenos:

    math.log10(10)

.. jupyter-execute::
    :linenos:

    math.log(10)

Modules also serve to allow simplification of code. This enable putting logically related functions into a single file. They facilitate reuse of those functions in different programs, thus reducing redundancy and increasing the robustness of software.

"third party" libraries
-----------------------

.. index:: 3rd party libraries, third party libraries

An even greater appeal of Python is the availability of highly sophisticated modules written by others.

Of particular note is numpy_ (numerical Python). This library is arguably the main reason Python is so popular in science. Numpy provides critical routines in numerical mathematics, particularly linear algebra. But it's very broadly useful, being ~10x faster than straight Python implementations. It also allows succinct expressions for arrays and provides very useful methods on arrays.

Other invaluable libraries for science are Scipy, Pandas, Matplotlib, IPython and biology specific libraries (such as Cogent3_).

We will cover ``numpy`` in a separate section.

Why use libraries written by others?
------------------------------------

- Widely scrutinised, so less chance of code errors
- Typically better performance
- May provide algorithms that are simply too difficult to write yourself!

There are an increasing number of Biology specific libraries. My own lab produces a number of open sourced library for genomic biology (e.g. Cogent3_, which we will use later in the course).

Writing your own modules
------------------------

You can easily write you own modules so that your own code can be readily reused by yourself, or shared with others. You will do this!

.. _numpy: https://www.numpy.org
.. _Cogent3: https://cogent3.org
