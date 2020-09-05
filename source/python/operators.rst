.. index::
    pair: <; operators
    pair: <=; operators
    pair: >; operators
    pair: >=; operators
    pair: ==; operators
    pair: !=; operators
    pair: is; operators

Operators
=========

In addition to the mathematical operators we have covered, there are *relational operators*.

- ``<`` less than
- ``<=`` less than or equal to
- ``>`` greater than 
- ``>=`` greater than or equal to
- ``==`` equal to
- ``!=`` not equal to
- ``is`` the same instance, has the same location in memory [1]_.

.. [1] This is more stringent than ``==``.

.. index::
    pair: &; bitwise operators
    pair: |; bitwise operators
    pair: ^; bitwise operators

.. _bitwise_operators:

Bitwise operators
=================

These are typically employed for operations involving integers. However, they also apply to the Python ``set`` type.

- ``&`` is bitwise AND of the arguments
- ``|`` is bitwise *inclusive* OR of the arguments
- ``^`` is bitwise *exclusive* OR of the arguments

Exercises
=========

#. Try these operators on different data types, e.g.

    .. jupyter-execute::

        "abcd" < "ABCD"

#. What happens if you try them on different data types?
 