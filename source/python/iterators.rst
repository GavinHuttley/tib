Iterators
=========

An iterator is a special type of object that can be iterated (looped) over. You will encounter cases where a function you would expect to return a series that could be sliced instead returns an object that has to be iterated over in order to obtain it's contents.

For example, the built in function ``reversed()``.

.. jupyter-execute::
    :linenos:

    new_order = reversed(["e", "a", "b", "g"])
    new_order

Looping works

.. jupyter-execute::
    :linenos:

    for element in new_order:
        print(element)

If you just want such an object to be a list, for example, then a more succinct approach is to cast it using ``list()``.

.. jupyter-execute::
    :linenos:

    new_order = reversed(["e", "a", "b", "g"])
    new_order = list(new_order)
    new_order
