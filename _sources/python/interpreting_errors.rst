.. margin:: Debugging a simple Python script using an IDE

    .. index::
        pair: Debugging a simple Python script using an IDE; screencasts

    .. raw:: html
    
        <video width="50%" height="50%" controls>
          <source src="https://github.com/GavinHuttley/tib/assets/3102996/b77758b4-60c3-4302-b7a6-59c703b6d77d" type="video/mp4">
          Your browser does not support the video tag.
        </video>

.. index::
    pair: errors; Exceptions

.. _debugging:

Fixing errors
=============

Every programmer makes errors, it's normal. The most important step towards fixing errors is interpreting the error messages produced by Python. In Python, error messages come in the form of "exceptions" which produce a "traceback" [1]_ that declares the type of exception and which piece of code triggered it.

.. margin::
  
    .. [1] See this article_ for a more complete description.

Here's some broken code:

.. tab-set::
    
    .. tab-item:: Invalid Code

        .. jupyter-execute::
            :raises:

            a = 42
            k += a

        First, in the traceback, the last line indicates the type of the exception (``NameError`` in this simple case) and the statement triggering it (``k +=``). The offending line is indicated by ``---->``.

    .. tab-item:: Fixed Code

        Variables must be defined before they're used

        .. jupyter-execute::
    
            a = 42
            k = 0
            k += a

And a slightly more complicated case

.. tab-set:: 

    .. tab-item:: Invalid Code
        .. jupyter-execute::
            :raises:

            def echo(name):
                print(name

        This is a ``SyntaxError`` -- imbalanced ``()``. Note the ``^`` in the traceback, which indicates the first place where the syntax is erroneous. It also indicates the line number. In the Jupyter case, these line numbers are within the cell. In a standard Python script, they are within the entire file.

    .. tab-item:: Fixed Code

        Balance the parentheses.

        .. jupyter-execute::
    
            def echo(name):
                print(name)


Exercises
=========

#. Fix the errors in the following.

    .. jupyter-execute::
        :raises:

        name = "Tim"
        if name = "Tim":
            greet = "Fist bump!"
        else:
            greet = "Hi"

#. Consider the following function, which is meant to compute the square of a number, i.e. :math:`x^2`. Define the type of error and then fix it.

    .. jupyter-execute::
        :raises:

        def squared(num):
            return num * 2


.. _article: https://realpython.com/python-traceback/
