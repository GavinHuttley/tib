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

    nums = [3, 0, 6, 1]
    sorted(nums)

The original object is left unmodified.

.. jupyter-execute::

    nums

Python is an object oriented language
-------------------------------------

A precursor to understanding methods is to understand what is meant by an "object".

As the title states, Python belongs to a class of programming languages called "object oriented". The success of "object oriented" programming languages (there are many) arise (at least in part) from the fact they encourage modularisation of code. This modularisation reduces the number of lines of code and makes the resulting programs easier to write, to check for bugs, and thus to maintain.

So what is an "object"? It's an abstract concept, but in essence an object represents something. It can be a number, a string, a file, etc.. Thus "objects" are instances of a type of data.

.. index:: instance

So what's an instance? An instance is an occurrence of a type of data, which will have a location in memory that is different to other occurrences of the same type of data. I'll use the built-in function ``id()`` (which returns a unique identifier, related to the address in memory):

.. jupyter-execute::

    a = [3, 0, 6, 1]
    id(a)

.. jupyter-execute::

    b = [3, 0, 6, 1]
    id(b)

Although ``a`` and ``b`` are equivalently defined -- both lists of exactly the same integers -- they are not the same instance.

.. index:: methods

.. _methods:

Methods
-------

Which leads us to methods. A method is a function bound to a specific object that applies to the data encapsulated in that instance.

This means that when you call a method on one object, it only operates on that object. I'll demonstrate that by using a method on lists to sort the elements.

.. jupyter-execute::

    a.sort()
    a

.. jupyter-execute::

    b

You can see that ``a`` was affected, while ``b`` was not.

So with a method, it operates on the specific instance of data to which it's bound. For a function, you need to explicitly provide the data to the function as an argument as we did in our above usage of the builtin function ``sorted()``. To use a method, you don't need to provide the data it will operate on, but for a function you do.

Here are the key patterns for using a method:

1. You access them (which is also known as referencing them) using the ``"."`` notation, e.g. ``some_variable.a_bound_method`` where the instance is ``some_variable`` and the method is ``a_bound_method``.
2. You use them like all functions (see the above), except you do not provide the data, e.g. ``some_variable.a_bound_method()``.

Simple!

.. index::
    pair: concatenating; string

So how do I use methods and functions?
--------------------------------------

There are some general principles in how to use functions and methods. First, using ``help()`` will show you what arguments a function or method can take

.. sidebar:: Interpreting help() for a function
    :name: Interpreting help() for a function

    .. image::  /_static/images/func_help.png
        :scale: 50
    
    The function signature lists the required and optional arguments.
    
    1. Required arguments are listed first. In this case, the name of that argument tells you it must be an "iterable" object.
    2. Optional arguments are listed as `<argumemt name>=<default value>`. In this case, there are two optional arguments. One called ``key``, another called ``reverse``.
    3. Return value. The help text tells us this function will return a new list with members sorted in ascending order.

Functions
^^^^^^^^^

Focussing on functions first. If a function is what we call a void function then it operates only on the arguments you give it and returns nothing [2]_. The obvious example of this is ``print()``. Fruitful functions actually return a value. You can establish what type that value will be by either reading help (see `Interpreting help() for a function`_) or running an experiment (calling the function with some data).

.. [2] Actually, in Python every function and method returns something. Void functions and methods return `None` (try it on `print()`.

Methods
^^^^^^^

It becomes a little bit trickier when we talk about methods. That said, the strategy suggested above of using ``help()`` or simple experiments applies here too.

Recalling that methods are bound to the data they operate on, we can divide methods into those which:

- describe the data
- transform the data

Consider the string ``"GGTCATGAAGGTC"``. Example string methods that describe the data are ``find()``, ``startswith()``. In these cases, the method will return a value.

.. jupyter-execute::

    seq = "GGTCATGAAGGTC"
    seq.find("ATG")

In an interactive interpreter (like Jupyter which we've used here), the returned value is displayed. In order to use the information, we have to assign it to a variable which we now do.

.. jupyter-execute::

    orf_start = seq.find("ATG")

These descriptive methods are pretty simple to comprehend. The challenge comes when you start using methods that transform the data. Again, using ``help()`` on the object is the most reliable approach.

.. sidebar:: Interpreting help() for a method
    :name: Interpreting help() for a method

    .. image::  /_static/images/method_help.png
        :scale: 50
    
    The help indicates the return value will be a string transformed such that the all characters are lower case except the first character.

In this example given in `Interpreting help() for a method`_, a new string will be returned. This means the original instance will be unchanged.

.. jupyter-execute::

    text = "HELLO WORLD"
    capitalized = text.capitalize()
    text

.. jupyter-execute::

    capitalized

.. index:: immutable, mutable

If we were working on a ``list`` type, however, transforming methods **do not** return a value and in fact are void methods. Instead the data in the instance is modified itself.

.. jupyter-execute::

    words = ["HELLO", "WORLD"]
    words.reverse() # reverse the item order
    words

This leads us to a general principle

.. note:: If a data type is immutable (e.g. strings, tuples), then any transformation methods will return a new instance of the same type. Thus you must assign the returned value of a method call on an immutable type in order to use it! If instead the type is mutable (e.g. lists, dicts) then the data of the existing instance is modified in-place.

A useful trick for concatenating strings
----------------------------------------

Getting help on a string method that can be used to concatenate.

.. jupyter-execute::

    help("".join)

.. note:: All elements of the series must be of type ``str``.

.. jupyter-execute::

    data = ["AAA", "CCC"]
    "".join(data)

.. jupyter-execute::

    "-".join(data)

.. jupyter-execute::

    "\t".join(data)


.. todo:: define difference between function and method, former nearly always MUST be given an argument, e.g. reversed(), reverse()

Exercises
=========

#. What comparison operators can you use to confirm my statements regarding same value and different instance?

#. For the built-in ``len``, is it a function or a method? Demonstrate its usage.

#. Join the ``data`` variable from above with the new line character.
