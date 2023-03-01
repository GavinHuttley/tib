.. sidebar:: Tips for writing functions and staying sane

    This is such an important message, I'm saying it multiple times on this page.
    
    Here are two ways to write functions that are guaranteed to create headaches.
    
        1. Pass in function parameters that are mutable data types AND modify them within the function.
        2. Use variables that are defined outside the function.
    
    What are the alternatives?
    
        1. Either do not modify input parameters or copy them within the function.
        2. Pass all the variables your function needs into the function.

    Of course, if you love errors and hard to debug problems go ahead and ignore this advice.

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
    
    def valid_python_name(arguments, optional_argument=None):  # the function signature line
        # indented lines of code that are only executed
        # when this function is called
        return

And, of course, functions must be defined before they are used!

The following is a valid, but not particularly useful, function. As the function definition does not include any arguments, the function is invoked by simply using its name and the standard call syntax ``"()"``.

.. code::
    
    def echo_hello():
        print("Hello! Hello!")
    
    echo_hello()

.. note:: By convention, functions are put at the top of script files. The convention is motivated by the desire to make the code easy to read.

.. index::
    pair: void; functions

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

.. note:: The function was defined before it was used. There were multiple arguments separated by a ``","``. We used the ``return`` keyword to deliver the result of this calculation to the calling code (line starting with ``result =...``).

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

When calling a function, the order in which you provide arguments defines what variable they're assigned to. One exception to this is if you specify the arguments as ``argument=value`` (key-value arguments).

.. tab-set::
    
    .. tab-item:: Correct Invocation

        Both ``a`` and ``b`` are required. 

        .. jupyter-execute::

            get_diff(6, 4)

        .. jupyter-execute::

            get_diff(b=6, a=4)

    .. tab-item:: Incorrect Invocation

        If you don't provide both arguments you will get an *exception*, in this case a ``TypeError``.

        .. jupyter-execute::
            :raises:

            get_diff(1)

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
    :raises:

    get_diff(absolute=True, 0.1, -0.5)

.. note:: There is an exception for calling a function. A function call where all arguments are expressly named will work even if optional arguments are not last, e.g. ``get_diff(absolute=True, a=-4, b=6)``.

.. _functions: http://greenteapress.com/thinkpython2/html/thinkpython2004.html#sec30

.. index:: docstring, string literal

An advanced design pattern: Putting constraints on how your functions are used
------------------------------------------------------------------------------

You can force your users to employ the key-value invocation, as illustrated by the following.

.. jupyter-execute::
    :raises:

    def get_diff(*, a, b):  # note the * character
        diff = a - b
        return diff

    get_diff(a=4, b=6)  # users now must use argument=value, otherwise there's an error

The reason for this is it forces your users to check the parameters of your function when they call it, increasing the chance they use it correctly! It also makes their code easier to read.

.. note:: This is a "for your information" entry only.

Documenting a function with a doctstring
----------------------------------------

We can document how to use a function we write by writing a docstring. When you use ``help()`` on a built in function, it's the docstring of that function which is being displayed. The syntactic definition of a docstring is:

- They are a string literal. By convention, they are defined using triple quotes surrounding the text. They can span multiple lines.
- They are the first statement after the function signature.

.. index::
    pair: pass; statement

The following illustrates the form of a docstring with a simple function with no contents other than the docstring [#]_.

.. [#] The Python ``pass`` statement is a null ("do-nothing") operation. It's used as a placeholder when the language requires a syntactic element.

.. jupyter-execute::

    def myfunc():
        """a do nothing demo

        multi-line docs
        """
        pass

.. jupyter-execute::

    help(myfunc)

Functions that call other functions
-----------------------------------

There is no magic here. If you can use a Python built-in function, you can use a function you wrote. In the following, the function ``squared_diffs()`` takes two number series and returns the square of the element-wise difference while the function  ``diff_two()`` takes two number series and returns their element-wise difference.

.. jupyter-execute::

    def diff_two(a, b):
        result = []
        for i in range(len(a)):
            result.append(a[i] - b[i])
        return result

    def squared_diffs(a, b):
        diffs = diff_two(a, b)  # calling diff_two which is defined above
        return [v ** 2 for v in diffs]


    squared_diffs([93, 14, 47, 82], [59, 0, 66, 82])


Things not to do!
-----------------

**DO NOT** use global variables (see :ref:`namespaces`). Either pass the variable in as an argument or create it within the function. Adhere to the principle of making code "Easy To Change". In the case of functions, this means making them depend only on the arguments you give them. The following is bad.

.. jupyter-execute::

    result = []

    def myfunc1(arg):
        result.append(arg)
        return result

    myfunc1(4)
    myfunc1(4)
    result

As I show in that code snippet, each call to ``myfunc1()`` modifies the module level variable ``result`` because it is a mutable type. So ``result`` records all such calls! If you really need a list inside that function, define it within the function or pass it in as an argument. But see the next point.

**DO NOT** define the default value of an optional variable to be a mutable data type. Here's an example

.. jupyter-execute::

    def myfunc2(arg, result=[]):
        result.append(arg)
        return result

    r = myfunc2(20)
    r = myfunc2(90)
    r

Same behaviour as the previous example because that definition of ``result`` is actually happening at the module level, even if it's in a function signature! However many times you call ``myfunc2()`` is how many elements will be in the returned list. This effect holds for any mutable data type. Here's a better approach.

.. code-block:: python

    def myfunc3(arg, result=None):
        result = result or []
        result.append(arg)
        return result

**DO NOT** modify an input data structure unless your docstring (or the name of your function) states clearly that's what it will do. Copying can be expensive in terms of speed and memory, but unexpected changes in state of some data can cause hard to debug problems and so be more expensive in terms of programmer time. This is why it's a good idea to put important data into data types that are immutable (e.g. pick a ``tuple`` over a ``list`` for instance) or at least harder to change.

.. epigraph::

    A Foolish Consistency is the Hobgoblin of Little Minds
    
    --- Ralph Waldo Emerson, Self-reliance, 1841

That quote applies to the above remarks, make exceptions to those thoughtfully. Except for mutable data types as default values -- never do that unless you love hard to debug problems and misery.

Exercises
=========

Using the following data

.. jupyter-execute::

    data = " [ 0.2 0.1 0.3 0.4 0.0 ] "

#. Write a function called ``cast_to_floats()`` that takes a single string (as per ``data``) and converts it into a list of floats. Apply this function to ``data``.

#. Write a function called ``normalised_freqs()`` that takes a series of frequencies (each value is 0 < val < 1 and the series sums to 1) and has an optional argument ``add_to_all`` (with a default value of 0). The function adds ``add_to_all`` [#]_ to every frequency.

    Add some assert statements to your function to check input values are valid (e.g. all values are ``0<=freq<1``).

    Use an assert to check the result satisfies the following, all numbers sum to 1.0 (within numerical precision) and all values satisfy ``0 < v < 1``.

    For example, with the following input values

    .. jupyter-execute::

        freqs = [0.1, 0, 0.3, 0.6]
        add_to_all=0.0001

    Your function should return

    .. jupyter-execute::
        :hide-code:

        import numpy
        d = numpy.array(freqs) + add_to_all
        (d / d.sum()).tolist()

    But if, for example, ``add_to_all < 0`` your function generates an exception.

#. Write another function, ``str_to_normalised()`` that takes the same input of ``cast_to_floats()`` and also has an optional argument for ``add_to_all``. This function should first call ``cast_to_floats()`` to get the floats. Then call ``normalised_freqs()`` with that result to get the final normalised series. ``str_to_normalised()`` then returns this value.

#. Implement the ``myfunc2()`` variant from above. Then try using differemt mutable data type as the default value. Demonstrate the bad side effect of persistent state with subsequent calls to ``myfunc2()``. Make those calls without providing a value to ``result``. Show that the ``myfunc3()`` does not have this problem.

#. For function ``count_CGs()`` defined below. Prove it is incorrect using an ``assert`` statement [#]_. Rewrite the function so it is correct.

    .. jupyter-execute::
    
        def count_CGs(seq):
            """return the total number of C and G in a Seq"""
            return Seq.count("C") + Seq.count("G")
        
        Seq = "ACGCCAGTGCATTACG"
        count_CGs(Seq)
    
    .. jupyter-execute::
    
        count_CGs("ACGTTAATATTATTTTA")
    
.. [#] This type of adjustment to avoid zeros is used to avoid numerical errors.

.. todo:: add a question getting them to expose fragility of uising a mutable data structure as input; create a case where there's a module level list with a member whose value is used by a function such that the second call raises an error, ask them to write the function so it's more robust

.. [#] What this means is that you state an expected value for the function given your input. If the code is incorrect, the function returned value will not equal your expected value thus triggering your assertion statement, resulting in an error. In other words, if the code is wrong you WANT there to be an error.
