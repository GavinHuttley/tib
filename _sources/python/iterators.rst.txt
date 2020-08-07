.. index:: iterator, generator

Iterators
=========

An iterator is a special type of object that can be iterated (looped) over. You will encounter cases where a function you would expect to return a series that could be sliced instead returns a generator object that has to be iterated over in order to obtain it's contents.

.. index:: reversed()

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

.. index::
    pair: yield; keyword

The ``yield`` keyword
---------------------

You can write your own generator functions by using the keyword ``yield`` instead of ``return``.

There are several benefits of generator functions. Just one of which is they provide a means for iterating over some data series without having to load everything into memory. For instance, if you have a massive data file of human genetic variants and but you only want 100 records where the alleles are C/T and on chromosome 10.

Exercises
=========

**1.** Write a function that takes a file path, opens the file and returns all the lines in that file.

**2.** Convert the above function to a generator that yields one line at a time.
