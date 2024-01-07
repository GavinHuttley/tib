Getting help
============

Two builtin functions that are incredibly useful for figuring out what attributes an object [1]_ has and what those attributes can do.

.. margin::
  
    .. [1] All variables in Python are referred to as objects.

- ``dir(some_variable)`` lists the attributes of ``some_variable``, including methods.
- ``help(some_function)`` displays helpful information about what ``some_function`` does and how you use it

Examples of using ``dir()`` and ``help()``
------------------------------------------

.. index:: dir()

Let's create a list and see what it's attributes are using ``dir()``.

.. jupyter-execute::

    data = []
    dir(data)

.. note:: All attributes whose name begins with an underscore (``"_"``) character are referred to as *private* attributes. At this point in your education you should ignore them.

So what are these things?

.. jupyter-execute::

    print(type(data.append))

.. index:: help()

Use ``help()`` to figure out what can they do.

.. jupyter-execute::

    help(data.append)

.. index::
    pair: hints; type

Type hints are useful!
----------------------

Python is known as a "duck-typing" language [#]_. That said, many python functions and methods have definitions that are annotated with :index:`type hints`. Think of these as the assumptions the function is making and an assumption that you can make regarding its output.

To illustrate this, I define a function below that has two arguments (``a``, ``b``) that are both "expected" to be type ``int``. This is communicated by the ``: int`` that follows the argument name. You can expect the function to return an ``int``, which is indicated by the ``-> int`` following the closing parenthesis.

.. code-block:: python
    
    def add_ints(a: int, b: int) -> int:
        return a + b

.. [#] This phrase stems from the adage that "if it walks like a duck and talks like a duck, it is a duck." In essence, Python programs work so long as the variable has the necessary attributes. This differs from typed languages, such as ``C``, where you must define in advance exactly what type every variable will be.

Those types are only considered hints because there is not actual type checking [#]_! That function would work just fine if either of the input arguments was a ``float`` too, so what good are type hints? Many modern programming editors also help guide your coding by alerting you when your program starts calling functions with types that don't match function (or method) signatures. So, if you only call a function with the indicated types, your program is less likely to have bugs.

.. [#] Tools such as `mypy <http://mypy-lang.org>`_ can do static type checking.
