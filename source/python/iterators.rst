.. index:: iterator, generator

Iterators
=========

An iterator is a special type of object that can be iterated (looped) over. You will encounter cases where a function you would expect to return a series that could be sliced instead returns a generator object that has to be iterated over in order to obtain it's contents.

.. index:: reversed()

For example, the built in function ``reversed()``.

.. jupyter-execute::

    new_order = reversed(["e", "a", "b", "g"])
    new_order

Looping works

.. jupyter-execute::

    for element in new_order:
        print(element)

If you just want such an object to be a list, for example, then a more succinct approach is to cast it using ``list()``.

.. jupyter-execute::

    new_order = reversed(["e", "a", "b", "g"])
    new_order = list(new_order)
    new_order

.. index::
    pair: yield; keyword

The ``yield`` keyword
---------------------

You can write your own generator functions by using the keyword ``yield`` instead of ``return``.

There are several benefits of generator functions. Just one of which is they provide a means for iterating over some data series without having to load everything into memory. For instance, if you have a massive data file of human genetic variants and but you only want 100 records where the alleles are C/T and on chromosome 10.

.. index::
    pair: as; keyword

The ``as`` keyword
------------------

This keyword facilitates a type of assignment. They can be used in a number of different contexts, such as part of a with statement.

.. code-block::
    
    with open("some_path.txt") as infile:
        lines = infile.readlines()

They can also be used in imports and when trapping exceptions.

Exercises
=========

.. todo:: 

    exercise with data like
    
    data = "\n".join("some text").replace (" \n", "\n")
    write code that loops over data and reaassembles the independent words
    this is a good preliminary example of having to store data and acting on it
    after you have collected everything -- entree to processing a fasta file

#. ``data`` is a list of the characters from words put onto separate lines. The space between words being indicated by a blank line. Write an algorithm that reconstructs the original words and spaces as a single string.

    .. tab-set::
    
        .. tab-item:: The data

            .. jupyter-execute::
        
                data = """s
                o
                m
                e

                t
                e
                x
                t""".splitlines()
        
        .. tab-item:: Expected output
    
            .. jupyter-execute::
                :hide-code:
        
                words = []
                word = []
                for c in data:
                    c = c.strip()
                    if c:
                        word.append(c)
                    else:
                        words.append("".join(word))
                        word = []
            
                words.append("".join(word))
                print(repr(" ".join(words)))
    

#. Write a function that takes a file path, opens the file and returns all the lines in that file.

#. Convert the above function to a generator that yields one line at a time.


.. todo:: add a variant of first question where task is to assemble words into a list