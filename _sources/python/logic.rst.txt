Logical syntax
==============

.. index::
    pair: "\t"; white space
    pair: "\n"; white space
    pair: "\r"; white space
    pair: "\l"; white space
    pair: " "; white space

White space characters are critical components of Python syntax. The ``" "``, ``\t`` and ``\n`` characters are employed.

As you will see, indentation of Python lines is used to delineate logical structure to a program. Lines that sequentially follow and are at the same indentation level are executed according to the same conditions.

Indentation can be done using ``\t`` or spaces. In general, it's best to uses spaces and the convention is to use 4 spaces as a unit of indentation. In most text editors, this can be done by setting a preference for soft tabs equal to 4 spaces.

.. index:: indentation

Indentation levels in a file
----------------------------

.. todo:: define what you mean by indentation

When you are writing scripts, your file **must** have some lines that have no indentation.

.. code-block:: python
    :linenos:
    :caption: Like this

    print("Hello World!")

.. code-block:: python
    :linenos:
    :caption: Not like this!

        print("# Correct")

.. index::
    pair: if; conditionals
    pair: elif; conditionals
    pair: else; conditionals

Conditionals
------------

.. todo:: define what you mean by conditional

Python conditionals require using the ``:`` (colon) character to complete a statement.

.. code-block:: python
    :linenos:

    name = "Timbo"
    if name == "Gavin":
         greet = "Hello Guru"
    else:
        greet = "What Up"

More complicated conditionals
-----------------------------

If you have more than two conditions, you can use ``elif``. The first case is always assessed using ``if``, then ``elif``, and last is ``else``.

.. code:: python
    :linenos:

    name = "Timbo"
    if name == "Gavin":
        greet = "Hello guru"
    elif name == "Timbo":
        greet = "What Up"
    else:
        greet = "Sorry, but I do not know your name."
        
Conditional statement with multiple clauses
-------------------------------------------

There are binary operations that can be combined to increase the complexity of conditional clauses. Specifically, ``and``, ``or`` ``not``.

.. jupyter-execute::
    :linenos:

    k = 24
    j = 3
    if k > 0 and j > 0:
        print("Both positive")

check we don't try taking the log of negative numbers

.. code::

    from math import log
    
    if k < 0 or j < 0:
        print("Cannot take log of a negative")
    else:
        print(log(k) - log(j))

We can use ``not`` to negate a statement.

.. code::

    if k and not j:
        print("k is different from zero, but j must be zero")

As an alternate, there may be causes where you wish to check for existence of a value in a series.

.. jupyter-execute::
    :linenos:

    sequence = "ACGTTAGGTATGTAA"
    if "ATG" in sequence:
        start_codon = True

Or

.. jupyter-execute::
    :linenos:

    numbers = [0, 23, 47, 61]
    if 2 not in numbers:
        absent = True

.. index:: looping

Repetition / Looping / Iteration
--------------------------------

These are mechanisms for doing exactly the same thing over and over. The primary approaches to doing this are the ``while`` and ``for`` statements. (In general, the ``for`` statement is preferred.)

.. index::
    pair: while; loops

``while`` loops
^^^^^^^^^^^^^^^

.. jupyter-execute::
    :linenos:

    print("Before the while loop")
    count = 0
    while count < 3:
        print(count)
        count += 1
    print("After the while loop")

.. jupyter-execute::
    :linenos:

    count = 0
    while count < 1000:
        print(count)
        count += 1
        if count == 3:
            break  # a special key word for exiting loops

.. note:: The indentation specifies the logical grouping of statements. Only the indented lines after the ``while`` statement are executed when the condition (``count < 3``) is ``True``.

.. index::
    pair: for; loops

``for`` loops
^^^^^^^^^^^^^

.. jupyter-execute::
    :linenos:

    word = "cheese"
    for letter in word:
        print(letter)

.. note:: Strings have the special property of being *iterable*. Many other Python data types also have this property, including lists, tuples, dicts and files.

.. index::
    pair: enumerate; loops

``enumerate`` loops, a special ``for`` loop
"""""""""""""""""""""""""""""""""""""""""""

A ``for`` loop with the convenience of also returning the index of the element in the series.

.. jupyter-execute::
    :linenos:

    word = "cheese"
    for value in enumerate(word):
        print(value)

.. index::
    pair: #; comment
    pair: comment lines; comment

Comments in code
----------------

In Python, a comment is all text occuring after the  ``#`` symbol line. All characters occurring after it are ignored by the interpreter. Comment lines are used to explain in normal language what a block of code is doing, or to record other information such as the license.

.. jupyter-execute::
    :linenos:

    # this is a comment

    a = 2 ** 16 # and this is another comment

.. todo:: add some exercises regarding conditionals and iteration
