.. _types:

The basic data types
====================

Think of how you interpret the following:

    "According to Pythagoras, with sides of a right angle triangle equal to 3 and 4, the hypotenuse is 5."

Based on the context, you infer the numerical meaning of the characters ``3``, ``4`` and ``5``. But to a computer, everything within the quotes is just a series of characters. We need to define our data explicitly in order for the computer to be able to operate on it effectively.

This leads directly to the notion of *data types*. Python comes with a number of core data types that I define below.

.. index:: string, str

**string**
    specified either using ``''`` or ``""`` around the content of interest. This is just a series of characters. It can be empty (has length 0) or much greater than that [1]_.

.. [1] Immutable means once the variable has been defined, it's value cannot be modified.

.. jupyter-execute::

    a = "a string"
    a

.. jupyter-execute::

    e = ""
    e

note that ``e`` is an empty string.

.. index::
    pair: int; types

**int**
    an integer. Specified by using a number without a ``.``. This is a numeric data type.

.. jupyter-execute::

    i = 4

.. index::
    pair: float; types

**float**
    a floating point number. Specified by using a ``.``. This is a numeric data type.

.. jupyter-execute::

    pi = 2.14
    f = 1.0
    f

.. note:: A floating point number is NOT the same as a decimal! They are an approximation.

.. index::
    pair: bool; types
    pair: True / False; types

**bool**
    A boolean, which can be either ``True`` or ``False``. These are special values that are produced by the relational operators.

.. jupyter-execute::

    a = 2
    a > 3
    b = True


.. index::
    pair: None; types

**None**
    A special type of the same name which is often a default value.

.. jupyter-execute::

    a = None
    a is None

Now we get to "collection" data types [2]_. Collections contain a number of elements and those elements can be of different types. Collection types are extremely powerful and wind up being a foundation for sophisticated algorithms.

In defining instances of collection types, different elements are delimited using a ``,`` separator.

.. [2] Sometime, strings, lists and tuples are referred to as "sequence" types. In this grouping, strings are distinguished from tuples and lists since every element of a string is of the same type by definition. This constraint does not apply to lists, tuples, etc...

.. index::
    triple: list; types; collection objects

**list**
    As the name implies, it is a series with (≥ 0) elements. These elements do not have to be the same type (as I illustrate) [3]_.

.. [3] Mutable data types can be modified after creation.

.. jupyter-execute::

    l = [0, "text"]
    l

.. index::
    triple: tuple; types; collection objects

**tuple**
    Almost the same as a list, but defined using different parentheses and [1]_.

.. jupyter-execute::

    t = (0, "text")
    t

.. index::
    triple: dict; types; collection objects

**dict**
    A dictionary. Like a conventional one, we look up entries in it using some "key" and get a "value" in return. Note the special parentheses used in the definition and also usage of ``:`` to separate the key and value. As with tuples and lists, they can contain different data types. The keys for a dictionary must always be of an immutable data type (so ``str``, ``tuple``, ``int``, ``float``) but the values can be of any data type. ``dict``'s are mutable, you can add keys or remove keys. You can modify the values for a key as you want.

.. jupyter-execute::

    d = {"a": "first character", "b": 2}
    d

Add another key

.. jupyter-execute::
    :linenos:

    d["new key"] = "some text"
    d


.. index::
    pair: type(); types

.. todo:: keys must be immutable, define a hash

How to tell the type of a variable
----------------------------------

Well that's easy!

.. jupyter-execute::

    a = 4
    type(a)

.. index::
    pair: type casting; types

Type casting
------------

In programming, this has the explicit meaning of converting one data type into another. Of course, this is not always possible. For instance, it makes no sense to try and convert a ``dict`` into a ``float``.

Casting is done using functions with names matching the data type.

int to float
^^^^^^^^^^^^

.. jupyter-execute::

    i = 4
    f = float(i)
    f

float to int
^^^^^^^^^^^^

.. jupyter-execute::

    f = 4.8
    i = int(f)
    i

string to float
^^^^^^^^^^^^^^^

.. jupyter-execute::

    s = "  4.45"
    f = float(s)
    f

But if casting from a string may require multiple steps. For instance, you cannot directly cast ``s`` to an int.

.. jupyter-execute::
    :raises:

    i = int(s)

string to list, tuple
^^^^^^^^^^^^^^^^^^^^^

Casting between the collection types is similar.

.. jupyter-execute::

    l = list(s)
    l
    t = tuple(s)
    t

Casting to a dict requires more work, as the original data type must have a shape that matches the required ``key, value`` pair pattern.

Objects to strings
^^^^^^^^^^^^^^^^^^

This is an extremely common task, not least because of the need to convert data to strings for writing to file. I will show two basic approaches.

.. index::
    pair: string formatting; str
    pair: C-style; str

"C-style" format strings
""""""""""""""""""""""""

So-called because this is the approach used in the C programming language. In this instance, we use the ``%`` sign in a couple of different ways. Firstly, we essentially define a template string with placeholders for whichever data we need to convert. These place-holders are also indicated by a ``%<c>`` where a following character (which I've indicated by ``<c>``) indicates the type of data that will be put there. After the closing quote, we then have another ``%`` which precedes the actual variables to be cast.

In the following I convert to a string: an int (using ``%d``); a float to two places (using ``%f``); a dict (using the generic ``%s``, which can be applied to any object).

.. jupyter-execute::

    i = 24
    s = "%d" % i
    s

.. jupyter-execute::

    f = 3.14678
    s = "%.2f" % f
    s

.. jupyter-execute::

    d = {1: ["some text", 4, "in a list!"]}
    s = "%s" % d
    s

You can of course have multiple elements in a single statement.

.. jupyter-execute::

    s = "%d\t%.2f\n" % (i, f)
    s

.. note:: For multiple data to be converted, they must be enclosed within ``()`` after the ``%``.

.. index::
    pair: format; str
    pair: f-strings; str

Using "format" strings
""""""""""""""""""""""

These are new to Python, since version 3.6. I'll bundle the int and float into a single statement.

.. jupyter-execute::

    i = 20
    x = 420000.134
    s = f"{i}\t{x:,.2f}\n"
    s

.. note:: The ``f`` preceding the quotes is what indicates this is a format string. You indicate where a variable should go using the ``{variable name}`` syntax. The formatting of numbers happens after the ``:``. The ``:,`` indicates separate thousands by ",", the ``.2f`` means float to 2 places.

Exercises
=========

**1.** What happens when you cast the following to a dict using the ``dict()`` command.

.. jupyter-execute::
    :linenos:

    data = [0, "a", 1, "b"]

**2.** What happens when you cast the following to a dict using the ``dict()`` command.

.. jupyter-execute::
    :linenos:

    data = [[0, "a"], [1, "b"]]

**3.** Try creating a dict using different data types as keys. Do they all work?

**4.** Make a really large int. Format it as a string with a thousands separator.

**5.** Create a float and convert it to a string. Repeat this, but change the displayed precision (how many decimal places are shown).
