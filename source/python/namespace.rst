.. sidebar:: Variable scope
    :name: Variable scope

    .. image::  /_static/images/namespace.png
        :scale: 40
    
    1. Global Namespace: is at the current module level name space
    2. Local Namespace: is in the ``display`` name space level

.. index:: namespace, scope

Namespaces
==========

.. todo:: write an explanation

A fundamental concept in programming, most easily explained with reference to the `Variable scope`_.

In brief, variables defined within the local scope are only "available" within that scope. Variables defined within the global scope can be accessed within a local scope.

.. jupyter-execute::
    :linenos:

    a = 2
    def foo():
        b = 3
        print(a + b)
    
    foo()

.. sidebar:: Namespace relationships

    .. digraph:: namespace

        graph [splines=ortho]
        a [shape="rectangle" label="Namespaces" width=5]
        l [shape="square" label="Local\nnamespace" width=1 height=1]
        ln [shape="rectangle" label="Specific to\ncurrent function\nor class method" width=1 height=1.2]
        g [shape="square" label="Global\nnamespace" width=1 height=1]
        gn [shape="rectangle" label="Specific to\ncurrent module" width=1 height=1.2]
        b [shape="square" label="Built-in\nnamespace" width=1 height=1]
        bn [shape="rectangle" label="Global to\nall modules" width=1 height=1.2]
        a -> l;
        l -> ln
        a -> g;
        g -> gn;
        a -> b;
        b -> bn;

    `After Skillbrew <https://pt.slideshare.net/p3infotech_solutions/python-programming-essentials-m19-namespaces-global-variables-and-docstrings/3>`_.


But they cannot be modified within the local scope (unless you use the ``global`` keyword [1]_).

.. [1] Using ``global`` is typically a bad idea in terms of algorithmic robustness.

.. jupyter-execute::
    :linenos:
    :raises:

    def foo2():
        a = a + b
        print(a)
    
    foo2()

.. sidebar:: Exploring namespaces using the debugger

    .. raw:: html
    
        <video width="50%" height="50%" controls>
          <source src="https://cloudstor.aarnet.edu.au/plus/s/DfRA9NA9hAI5qHq/download" type="video/mp4">
          Your browser does not support the video tag.
        </video>

Exercises
=========

Consider this broken code

.. jupyter-execute::
    :linenos:
    :raises:

    CONSTANT = 2
    
    def add_squared_constant(data_series):
        """adds squared constant to elements of data_series"""
        CONSTANT = CONSTANT**2
        result = [v + CONSTANT for v in data_series]
        return result
    
    data = [4, 12, 42]
    sqd = add_squared_constant(data)


**1.** Fix ``add_squared_constant()`` so it works to return ``[8, 16, 46]`` given ``data``.

**2.** Fix, without using the ``global`` keyword, so it works to return ``[8, 16, 46]`` given ``data``.

**3.** Fix, using the ``global`` keyword, so it works to return ``[8, 16, 46]`` given ``data``. What happens to the global variable ``CONSTANT`` [2]_?

.. [2] A part of the coding style guidelines I use is to use ALL CAPS for variables that are meant to be treated as constants.