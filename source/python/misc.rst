.. jupyter-execute::
    :hide-code:

    import set_working_directory

Miscellaneous Python features
=============================

.. index::
    pair: escaping characters; str
    pair: raw; str
    pair: r""; str

.. _escaping_chars:

Raw strings and escaping characters
-----------------------------------

Some characters have special meaning and including them in a string requires "escaping" them. This can be done using a ``\`` character. For instance, normally including the character ``\n`` in a string introduces a new line character.

.. jupyter-execute::

    text = "hello\nworld"
    print(text)

If we don't want that to happen, we can either "escape" the ``\`` character

.. jupyter-execute::

    text = "hello\\nworld"
    print(text)

or define it as a raw string by prefacing the string definition with the ``r`` character. The main advantage of this approach is it's easier to write.

.. jupyter-execute::

    text = r"hello\nworld"
    print(text)


.. index::
    triple: bytes; str; string
    triple: encode; decode; str
    triple: encode; decode; string

.. index::
    pair: b""; str

``bytes`` strings
-----------------

A type of string. The available methods are substantially the same as for ``str`` objects. There are important exceptions. You can create a ``bytes`` instance using a special string prefix.

.. jupyter-execute::

    btext = b"some text"
    btext

.. jupyter-execute::

    type(btext)

We can convert a ``bytes`` instance to a standard string using the ``decode()`` method [1]_.

.. [1] utf_ stands for the unicode translation format, of which there are multiple.

.. _utf: https://en.wikipedia.org/wiki/Unicode#UTF

.. jupyter-execute::

    text = btext.decode(encoding="utf8")
    type(text)

.. jupyter-execute::

    text

We can convert a standard string into a ``bytes`` instance using the ``encode()`` method.

.. jupyter-execute::

    back = text.encode(encoding="utf8")
    back


``open()`` files in binary mode
-------------------------------

Using ``mode="rb"`` opens a file in binary mode. The file contents are returned as ``bytes`` without any decoding.

.. jupyter-execute::

    with open("python/misc.rst", mode="rb") as infile:
        line = infile.readline()

    line

Empty series evaluate to ``False``
----------------------------------

One property of Python builtin series is that if they are empty, then they evaluate to ``False``. This is referred to as :index:`Falsy` and the converse is :index:`Truthy`.

.. jupyter-execute::

    sample_data = ["some text", ""]
    for text in sample_data:  # yes, lists are iterable too!
        if text:
            print("YES", text)
        else:
            print("NO Empty string")

.. note:: I iterated over elements of the list ``sample_data``. I also used conditionals within the ``for`` loop.

The values ``0```, ``0.0`` and ``None`` also evaluate to ``False``.

.. index:: assert, testing, correctness

Checking correctness using ``assert``
-------------------------------------

**It's essential to check the correctness of your code.** Knowing where and when you do this is a skill that you will develop by programming. For now I just demonstrate the syntax for using the ``assert`` statement.

.. jupyter-execute::

    name = "Gav"
    assert type(name) == str, "name [%s] is not a string" % name
    print("Sanity check passed!")

This is what it looks like when it fails.

.. jupyter-execute::
    :raises:

    name = 0
    assert type(name) == str, "name [%s] is not a string" % name

.. index::
    pair: list; comprehension
    pair: dict; comprehension

"Comprehensions"
----------------

A comprehension is a very succinct, and simple, ``for`` loop. They are quite fast and are useful.

List comprehensions
^^^^^^^^^^^^^^^^^^^

Here's an example for converting floats into strings.

.. jupyter-execute::

    nums = [
        0.37756786229607986,
        0.7110011013846619,
        0.349506300557232,
        0.8966182758861486,
    ]
    s = [str(v) for v in nums]
    s

Dictionary comprehensions
^^^^^^^^^^^^^^^^^^^^^^^^^

So many uses for a dict! A simple demonstration, using the ``nums`` variable from above. Notice in this case I'm using multiple unpacking.

.. jupyter-execute::

    k_v = [["A", 0.1], ["C", 0.2], ["G", 0.3], ["T", 0.4]]
    d = {k: v for k, v in k_v}
    d

.. index:: zip, unzip

Zipping / Unzipping series
--------------------------

Say you have two data series, of equal length, and you want them combined into a single object. This can be done using the built-in `zip()`. For example, here's a ``zip`` operation performed on two strings:

.. jupyter-execute::

    seq1 = "AGTAATATTGAAGACAAAATATTTGGGAAAACCTATCGGAAGAAGGCAAGCCTCCCCAAC"
    seq2 = "AGTAATACTGAAGACAAAATATTTGGGAAAACCTATCGGAGGAAGGCAAGCCTCCCCAAC"
    columns = list(zip(seq1, seq2))
    columns[:5]

You can also unzip series. For example, consider the following list of lists. We can decompose that into 2 separate series using `zip` with the argument prefaced by ``*``.

.. jupyter-execute::

    coords = [[0, 23], [42, 42], [13, 27]]
    x, y = zip(*coords)
    x
    y

.. index:: method chaining

.. _method_chaining:

Method chaining
---------------
    
When you make multiple method calls on the "same" object, this is called "chaining" or "method chaining". It can be done when the method call returns an object that contains the next method. These statements are read left to right. For example, in the following, I chain the string methods ``strip()`` and ``split()``.

.. jupyter-execute::

    text = "A\tB\t\n"
    data = text.strip().split()
    data

These types of expressions are used to save creating intermediate variables and, some argue, for clarity.
