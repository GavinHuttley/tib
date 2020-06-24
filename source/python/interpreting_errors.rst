Interpreting errors
===================

Every programmer makes errors, it's normal. Experienced programmers are most experienced in interpreting the error messages produced by Python. These errors are referred to as "tracebacks" [1]_.

The following code is broken:

.. jupyter-execute::
    :linenos:
    :raises:

    a = "some text"
    k += a

First, in the traceback, the last line indicates the type of the exception (``NameError`` in this simple case) and the statement triggering it (``k +=``). The offending line is indicated by ``---->``.

And a slightly more complicated case

.. jupyter-execute::
    :linenos:
    :raises:

    def echo(name):
        print(name

This is a ``SyntaxError`` -- imbalanced ``()``. Note the `^` in the traceback, which indicates the first place where the syntax is erroneous. It also indicates the line number. In the Jupyter case, these line numbers are within the cell. In a standard Python script, they are within the entire file.

See if you can figure out the one below.

.. jupyter-execute::
    :linenos:
    :raises:

    name = "Tim"
    if name = "Tim":
        greet = "Fist bump!"
    else:
        greet = "Hi"

.. [1] See this article_ for a more complete description.

.. _article: https://realpython.com/python-traceback/
