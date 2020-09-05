Getting help
============

Two builtin functions that are incredibly useful for figuring out what attributes an object [1]_ has and what those attributes can do.

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
