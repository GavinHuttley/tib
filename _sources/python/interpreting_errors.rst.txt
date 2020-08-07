.. sidebar:: Debugging a simple Python script using an IDE

    .. raw:: html
    
        <video width="50%" height="50%" controls>
          <source src="https://cloudstor.aarnet.edu.au/plus/s/ClULdjdqQm9EosK/download" type="video/mp4">
          Your browser does not support the video tag.
        </video>

.. _debugging:

Fixing errors
=============

.. todo:: define an error as an exception

Every programmer makes errors, it's normal. The most important step towards fixing errors is interpreting the error messages produced by Python. Error messages produced by Python are referred to as "tracebacks" [1]_.

.. [1] See this article_ for a more complete description.

Here's some broken code:

.. jupyter-execute::
    :linenos:
    :raises:

    a = 42
    k += a

First, in the traceback, the last line indicates the type of the exception (``NameError`` in this simple case) and the statement triggering it (``k +=``). The offending line is indicated by ``---->``.

.. panels::
    :column: col-lg-12 p-2

    .. dropdown:: :fa:`eye,mr-1` Click to see the fixed code
            
        Variables must be defined before they're used

        .. jupyter-execute::
        
            a = 42
            k = 0
            k += a

And a slightly more complicated case

.. jupyter-execute::
    :linenos:
    :raises:

    def echo(name):
        print(name

This is a ``SyntaxError`` -- imbalanced ``()``. Note the ``^`` in the traceback, which indicates the first place where the syntax is erroneous. It also indicates the line number. In the Jupyter case, these line numbers are within the cell. In a standard Python script, they are within the entire file.

.. panels::
    :column: col-lg-12 p-2

    .. dropdown:: :fa:`eye,mr-1` Click to see the fixed code
            
        Balance the parentheses.

        .. jupyter-execute::
        
            def echo(name):
                print(name)

Exercises
=========

Fix the errors in the following.

**1.**

.. jupyter-execute::
    :linenos:
    :raises:

    name = "Tim"
    if name = "Tim":
        greet = "Fist bump!"
    else:
        greet = "Hi"

**2.** Consider the following function, which is meant to compute the square of a number, i.e. :math:`x^2`

.. jupyter-execute::
    :linenos:
    :raises:

    def squared(num):
        return num * 2


.. _article: https://realpython.com/python-traceback/
