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

Namespaces
==========

.. todo:: write an explanation

and some text

.. sidebar:: Variable scope

    .. image::  ../images/namespace.png
    
    1. Global Namespace: is at the current module level name space
    2. Local Namespace: is in the `pointless_display` name space level

