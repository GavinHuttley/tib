Writing functions
=================

Now we cover writing your own functions_.

A function represents a named grouping of statements. They form a critical aspect of modular design to algorithms. By allowing referencing of a related block of code, one can substantially reduce redundancy in your code. This confers a number of major advantages:

1. It makes the code easier to read
2. Checking the correctness of a smaller block of code is easier
3. Errors only need to be fixed in one place
4. It allows building large, complicated programs from a small collection of tested sections.

So using functions will improve the reliability of your programs.

.. index::
    pair: syntax; function
    pair: return; function
    pair: return; statement

The critical syntax elements
----------------------------

- ``def``, the critical keyword telling Python you are defining a function
- a valid Python name, which is used to reference the function
- ``()``, which flank any arguments that might be a part of the function signature 
- ``:``, to indicate completion of the signature
- arguments, required or optional (have a default value)
- body of function must be indented
- ``return``, optional, which is used to specify what the function returns

The general form of a Python function.

.. code:: python
    
    def valid_python_name(arguments, optional_argument=None):
        # indented lines of code
        return

And, of course, they must be defined before they are used!

The following is a valid, but not particularly useful, function. As the function definition does not include any arguments, the function is invoked by simply using it's name and the standard call syntax ``"()"``.

.. code::
    
    def echo_hello():
        print("Hello! Hello!")
    
    echo_hello()

.. note::  By convention, functions are put at the top of script files. The convention is motivated by the desire to make the code easy to read.

Void functions
--------------

The ``echo_hello`` function is called a ``void`` function -- functions whose purpose does not require returning a value. That said, even if they don't use a ``return`` statement, they return the value ``None``.

Fruitful functions
------------------

These are functions that return something from their execution. We have encountered several examples of fruitful builtin functions like ``dir()``, ``int()``. These functions took an argument, operated on it, and returned something. The following is a simple fruitful function.

.. jupyter-execute::

    def get_diff(a, b):
        diff = a - b
        return diff

    result = get_diff(4, 6)
    result

.. note::  The function was defined before it was used. There were multiple arguments separated by a ``","``. We used the ``return`` keyword to deliver the result of this calculation to the calling code (line starting with ``result =...``).

.. index::
    pair: arguments; function
    pair: required arguments; function

Required arguments
------------------

.. jupyter-execute::

    def get_diff(a, b):
        diff = a - b
        return diff

    get_diff(4, 6)

.. jupyter-execute::

    get_diff(6, 4)

.. jupyter-execute::

    get_diff(b=6, a=4)

.. jupyter-execute::
    :linenos:
    :raises:

    get_diff(1)

- When calling a function, the order in which you provide arguments defines what variable they're assigned to
    - UNLESS you specify them as argument=value
- In the above, `a` and `b` are required. If you don't provide both of them, you will get an *exception*

.. index::
    pair: optional arguments; function
    pair: keyword arguments; function

Optional arguments
------------------

These are function arguments that have default values. You've seen this with the ``open()`` function. The ``mode`` argument defaults to read (``"r"``). In fact, the ``open()`` function has both required and optional arguments.

Writing and using functions that have optional arguments
--------------------------------------------------------

.. jupyter-execute::

    def get_diff(a, b, absolute=False):
        diff = a - b
        if absolute and diff < 0:  # both absolute AND (diff < 0) must be True
            diff = abs(diff)
        return diff

    # using default value for absolute
    get_diff(-4, 6)

.. jupyter-execute::

    # setting value for absolute
    get_diff(-4, 6, absolute=True)

Ordering arguments
------------------

Required arguments MUST occur before optional arguments. This constraint holds for both writing your own functions and for using functions.

.. jupyter-execute::
    :linenos:
    :raises:

    get_diff(absolute=True, 0.1, -0.5)

.. note:: There is an exception for calling a function. A function call where all arguments are expressly named will work even if optional arguments are not last, e.g. ``get_diff(absolute=True, a=-4, b=6)``.

.. _functions: http://greenteapress.com/thinkpython2/html/thinkpython2004.html#sec30

.. index:: docstring, string literal

Documenting a function with a doctstring
----------------------------------------

We can document how to use a function we write by writing a docstring. When you use ``help()`` on a built in function, it's the docstring of that function which is being displayed. The syntactic definition of a docstring is:

- They are a string literal. By convention, they are defined using triple quotes surrounding the text. They can span multiple lines.
- They are the first statement after the function signature.

.. index::
    pair: pass; statement

The following illustrates the form of a docstring with a simple function with no contents other than the docstring [1]_.

.. [1] The Python ``pass`` statement is a null ("do-nothing") operation. It's used as a placeholder when the language requires a syntactic element.

.. jupyter-execute::
    :linenos:

    def myfunc():
        """a do nothing demo
        
        multi-line docs
        """
        pass

.. jupyter-execute::
    :linenos:

    help(myfunc)

Exercises
=========

Using the following data

.. jupyter-execute::
    :linenos:

    data = " [ 0.2 0.1 0.3 0.4 0.0 ] "

**1.** Write a function called ``cast_to_floats()`` that takes a single string (as per ``data``) and converts it into a list of floats. Apply this function to ``data``.

**2.** Write another function called ``normalised_freqs()`` that takes a series of floats (like the result of 1.) and has an optional argument ``pseudocount`` (with a default value of 0). The function adds ``pseudocount`` [2]_ to every frequency.

Then add some assert statements to your function to check the user input for both the frequencies and the constant are valid (e.g. all values are ``0<=freq<1``).

Use an assert to check the result satisfies the following, all numbers sum to 1.0 (within numerical precision) and all values satisfy ``0 < v < 1``.

**3.** Write another function, ``str_to_normalised()`` that takes the same input of ``cast_to_floats()`` and also has an optional argument for ``pseudocount``. This function should first call ``cast_to_floats()`` to get the floats. Then call ``normalised_freqs()`` with that result to get the final normalised series.  ``str_to_normalised()`` then returns this value.

.. [2] A pseudocount is a number, typically a frequency (e.g. 0.5), used to avoid zeros. They're used in statistical models where the empirical data have zero observations but the prior belief holds those states are possible and thus should have a frequency > 0.
