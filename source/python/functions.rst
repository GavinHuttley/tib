.. index:: functions

Functions and methods
=====================

.. todo:: make sure you emphasise that all variables operate on by a function should either be passed in as arguments OR created internally -- need to avoid people defining a module level variable that's a mutable data structure

This is a central concept in programming. It provides a means of encapsulating several lines of code (that do something useful) and providing a reference such that this block can be called in multiple places in a larger program.

.. index::
   pair: builtin; functions

Builtin functions
-----------------

We have already been using some built-in functions. These are ``print()``, ``type()``, ``int()``, etc.

Here are the key patterns to using functions that you need to remember.

1. They have a name by which you refer to them, e.g. ``print`` or ``type``
2. You "invoke" or "call" a function using ``()`` after the name. Hence ``print()``.
3. Typically, functions take "arguments". An argument, is a variable that will be operated on by the function. For example:

.. jupyter-execute::

    text = "Hello World"
    print(text)

In the above, the argument is ``text``.

The built in functions ``range()`` and ``sum()`` are widely used. The former for generating the range of indices required to loop over elements in a series. The latter is as the name implies. For more detailed information about their capabilities, use the builtin ``help()`` function!

Another useful builtin function is ``sorted()``. As the name implies, this takes a series and returns a copy with the elements ordered [1]_.

.. [1] The elements don't have to be numbers.

.. jupyter-execute::
    :linenos:

    nums = [3, 0, 6, 1]
    sorted(nums)

The original object is left unmodified.

.. jupyter-execute::
    :linenos:

    nums

Python is an object oriented language
-------------------------------------

A precursor to understanding methods is to understand what is meant by an "object".

As the title states, Python belongs to a class of programming languages called "object oriented". The success of "object oriented" programming languages (there are many) arise (at least in part) from the fact they encourage modularisation of code. This modularisation reduces the number of lines of code and makes the resulting programs easier to write, to check for bugs, and thus to maintain.

So what is an "object"? It's an abstract concept, but in essence an object represents something. It can be a number, a string, a file, etc.. Thus "objects" are instances of a type of data.

.. index:: instance

So what's an instance? An instance is an occurrence of a type of data, which will have a location in memory that is different to other occurrences of the same type of data. I'll use the built-in function ``id()`` (which returns a unique identifier, related to the address in memory):

.. jupyter-execute::
    :linenos:

    a = [3, 0, 6, 1]
    id(a)

.. jupyter-execute::
    :linenos:

    b = [3, 0, 6, 1]
    id(b)

Although ``a`` and ``b`` are equivalently defined -- both lists of exactly the same integers -- they are not the same instance.

.. index:: methods

Methods
-------

Which leads us to methods. A method is a function bound to a specific object that applies to the data encapsulated in that instance.

This means that when you call a method on one object, it only operates on that object. I'll demonstrate that by using a method on lists to sort the elements.

.. jupyter-execute::
    :linenos:

    a.sort()
    a

.. jupyter-execute::
    :linenos:

    b

You can see that ``a`` was affected, while ``b`` was not.

So with a method, it operates on the specific instance of data to which it's bound. For a function, you need to explicitly provide the data to the function as an argument as we did in our above usage of the builtin function ``sorted()``. To use a method, you don't need to provide the data it will operate on, but for a function you do.

Here are the key patterns for using a method:

1. You access them (which is also known as referencing them) using the ``"."`` notation, e.g. ``some_variable.a_bound_method`` where the instance is ``some_variable`` and the method is ``a_bound_method``.
2. You use them like all functions (see the above), except you do not provide the data, e.g. ``some_variable.a_bound_method()``.

Simple!

.. index::
    pair: concatenating; string

A useful trick for concatenating strings
----------------------------------------

Getting help on a string method that can be used to concatenate.

.. jupyter-execute::
    :linenos:

    help("".join)

.. note:: All elements of the series must be of type ``str``.

.. jupyter-execute::
    :linenos:

    data = ["AAA", "CCC"]
    "".join(data)

.. jupyter-execute::
    :linenos:

    "-".join(data)

.. jupyter-execute::
    :linenos:

    "\t".join(data)


.. todo:: define difference between function and method, former nearly always MUST be given an argument, e.g. reversed(), reverse()

Exercises
=========

**1.** What comparison operators can you use to confirm my statements regarding same value and different instance?

**2.** For the built-in ``len``, is it a function or a method? Demonstrate its usage.

**3.** Join the ``data`` variable from above with the new line character.
