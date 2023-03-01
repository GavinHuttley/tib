Logical syntax
==============

.. index::
    pair: "\t"; white space
    pair: "\n"; white space
    pair: "\r"; white space
    pair: "\l"; white space
    pair: " "; white space

*White space* characters are critical components of Python syntax. The ``" "``, ``\t`` and ``\n`` characters are employed.

As you will see, indentation of Python lines is used to delineate logical structure to a program. Lines that sequentially follow and are at the same indentation level are executed according to the same conditions.

Indentation can be done using ``\t`` or spaces. In general, it's best to uses spaces and the convention is to use 4 spaces as a unit of indentation. In most text editors, this can be done by setting a preference for soft tabs equal to 4 spaces.

.. index:: indentation

Indentation levels in a file
----------------------------

.. sidebar:: Indentation defines logical structure
    :name: Indentation defines logical structure
    
    .. code:: text
    
        Initial text at the left-most position (level 1)
            Indented text using 4-spaces (level 2)
            Text with the same indentation is (level 2)
            part of the same logical group (level 2)
                Nested logic gets additional (level 3)
                indentation (level 3)
        
        Returning back to the original level (level 1)
    
    Indentation, expressed as a number of spaces (``" "`` from the left-most side of a page) defines logical grouping of commands in Python. (By convention, 4-spaces are used for each level.)

When you are writing scripts, your file **must** have some lines that have no indentation.

.. code-block:: python
    :caption: Like this

    print("Hello World!")

.. code-block:: python
    :caption: Not like this!

        print("# Correct")

.. index::
    pair: if; conditionals
    pair: elif; conditionals
    pair: else; conditionals

Conditionals
------------

.. index::
    pair: Truthy; bool
    pair: Falsy; bool

.. sidebar:: Truthy and Falsy
    :name: Truthy and Falsy
    
    .. jupyter-execute::
    
        bool("")
    
    Data values that evaluate (i.e. ``bool(value)``) to ``False`` are termed *Falsy*.
    
    .. jupyter-execute::
    
        bool([3, 2])
    
    Data values that evaluate to ``True`` are termed *Truthy*.
    
    This property allows simplifying conditional statements.

A "conditional" is a statement whose execution depends on the value of a variable. Python conditionals require using the ``:`` (colon) character to complete a statement.

I want to choose a ``greet`` based on the value of ``name``. This objective is expressed as a Python conditional.

.. code-block:: python

    name = "Timbo"
    if name == "Gavin":
        greet = "Hello Guru"
    else:
        greet = "What Up"

More complicated conditionals
-----------------------------

If you have more than two conditions, you can use ``elif``. The first case is always assessed using ``if``, then ``elif``, and last is ``else``.

.. code:: python

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

    sequence = "ACGTTAGGTATGTAA"
    if "ATG" in sequence:
        start_codon = True

Or

.. jupyter-execute::

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

    print("Before the while loop")
    count = 0
    while count < 3:
        print(count)
        count += 1
    print("After the while loop")

.. jupyter-execute::

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

A ``for`` loop operates until it gets to the end of the series it's given. The components of a for statement are:

.. code-block:: python

    for variable_name in my_series:
        # indented code to be executed at each step
    
    # de-indented code executed after the for loop

So the key parts of a valid for statement line are:

1. Begins with the ``for`` keyword
2. a valid python variable name, ``variable_name`` in the above [1]_
3. the series of objects to be iterated over, ``my_series`` in the above
4. terminated by a ``:``

.. [1] So far, variable :index:`assignment` has been done using :ref:`explicit assignment statements <assignment>`. But in the for loop, ``variable_name`` is defined as part of the ``for`` statement. Python will set update the value of ``variable_name`` at each iteration to be the next object in ``my_series``.

The for loop definition is completed by adding the code you wanted to execute on each iteration through the loop. Here's an example.

.. jupyter-execute::

    word = "cheese"
    for letter in word:
        print(letter)

In this case, our series of objects is ``word`` (a string). The variable ``letter`` is defined in the ``for`` loop statement and it will take on the value of each object (a string of length 1) in ``word``. The code to be executed at each iteration through the loop is just a print statement. All lines of indented code following the ``for`` statement will be executed at each iteration.

.. note:: Strings have the special property of being *iterable*. Many other Python data types also have this property, including lists, tuples, dicts and files.

.. index::
    pair: enumerate; loops

``enumerate`` loops, a special ``for`` loop
"""""""""""""""""""""""""""""""""""""""""""

A ``for`` loop with the convenience of also returning the index of the element in the series.

.. jupyter-execute::

    word = "cheese"
    for value in enumerate(word):
        print(value)

.. index::
    pair: #; comment
    pair: comment lines; comment

functions return multiple objects. If you know a certain number of objects will be returned then knowing how to do a multiple assignment can be useful.

It can also be applied in other contexts. One particularly useful context is in looping. In the following example, I'm looping over pairs of integers and assigning the results to separate variables. Note the use of the ``","`` in the ``for`` statement.

Multiple unpacking in loops
^^^^^^^^^^^^^^^^^^^^^^^^^^^

One particularly useful context to use multiple unpacking is in looping. In the following example, I'm looping over pairs of integers and assigning the results to separate variables. Note the use of the ``","`` in the ``for`` statement.

The tedious way
"""""""""""""""

.. jupyter-execute::

    # here is a tedious way
    coordinates = [(0, 1), (0, 2), (0, 3)]
    for coord in coordinates:
        x = coord[0]  # grabbing each integer by it's index
        y = coord[1]
        print(x, y)

The succinct way
""""""""""""""""

.. jupyter-execute::

    # This is more succinct
    coordinates = [(0, 1), (0, 2), (0, 3)]
    for x, y in coordinates:
        print(x, y)

Comments in code
----------------

In Python, a comment is all text occurring after the  ``#`` symbol line. All characters occurring after it are ignored by the interpreter. Comment lines are used to explain in normal language what a block of code is doing, or to record other information such as the license.

.. jupyter-execute::

    # this is a comment

    a = 2 ** 16 # and this is another comment

Exercises
=========

#. Show whether the number ``11`` is Truthy or Falsy?

#. Show whether ``{}`` is Truthy or Falsy?

#. Iterate over ``text`` and, if a character is a vowel ("aeiou"), print the character and its index in ``text``.

.. tab-set:: 
    
    .. tab-item:: Data

        .. jupyter-execute::

            text = "Some random text"
    
    .. tab-item:: Expected Output
    
        Fancy formatting not required.
    
        .. jupyter-execute::
            :hide-code:
        
            print("Index :  Vowel")
            for i, c in enumerate(text):
                if c in "aeiou":
                    print(f"{i:5} : {c!r}")

#. Write a ``for`` loop that prints whether the elements of ``values`` are Truthy, Falsey or actually the booleans True/False.

.. tab-set::
    
    .. tab-item:: Data

        .. jupyter-execute::

            values = [0, 11, {}, False, True]

    .. tab-item:: Expected Output

        .. jupyter-execute::
            :hide-code:
    
            for e in values:
                if type(e) == bool:
                    val = "is a bool"
                elif e:
                    val = "is Truthy"
                else:
                    val = "is Falsy"

                print(f"{e!r} {val}")
