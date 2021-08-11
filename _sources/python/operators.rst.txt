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

Relational (comparison) operators
---------------------------------

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
-----------------

These are typically employed for operations involving integers. However, they also apply to the Python ``set`` type.

- ``&`` is bitwise AND of the arguments
- ``|`` is bitwise *inclusive* OR of the arguments
- ``^`` is bitwise *exclusive* OR of the arguments

.. index::
    pair: and; logical operator
    pair: or; logical operator
    pair: in; logical operator



.. _logical_operators:

Logical operators
-----------------

These are used to extend logical statements, joining clauses.

- ``and`` if both clauses evaluate as True

.. jupyter-execute::

    a, b = 20, 5
    
    a > 0 and b > 0

- ``or``, if either clause evaluate as True

.. jupyter-execute::

    a > 0 or b > 0

- ``in``, an element is a member of a series

.. jupyter-execute::

    series = [0, "a", 23]

    "a" in series

Exercises
=========

#. Try these operators on different data types, e.g.

    .. jupyter-execute::

        "abcd" < "ABCD"

#. What happens if you try them on different data types?
 