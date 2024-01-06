Pulling it together -- writing your own programs
================================================

Break the problem into pieces
-----------------------------

While it can seem daunting, the key to writing a program is to break the problem into smaller pieces and solve those individually. How do I recognise what to work on first, how can I decide what a piece is? I suggest thinking in terms of order of operations. To illustrate these steps let's look at a simple equation.

.. math::

    x=b+\sqrt{b^2 + 4ac}

Here's a listing of the parts:

1. :math:`b`
2. the :math:`\sqrt{~}`, which contains

    2.1. :math:`b^2`, which is
    
        :math:`b\times b`
    
    2.2. :math:`4ac`, which is
    
        :math:`4\times a \times c`

To actually solve this problem requires we work from the inside (the most indented bullet points) towards the outside (the least indented bullet points). So let's do this thing!

I'm going to rewrite the bullet list, defining the names of python variables I will use for each level.

1. ``b`` (well that was easy!)
2. ``sqrt_term``

    2.1. ``b_sq``

    2.2. ``four_ac``

The first thing we have to do is define the variables we will use before we actually use them. We will just give them some starting numerical values (we know they have to be numbers because maths!) [1]_.

.. margin::
  
    .. [1] Let's also make our life easy by defining only positive numerical values so we don't have to worry about handling the :math:`\sqrt{~}` of a negative number.

.. jupyter-execute::

    b = 5
    a = 1.1
    c = 32

That actually defines ``b`` (1.), so the first of our parts is solved. Now let's solve go to the inner most pieces and define ``b_sq`` (2.1).

.. jupyter-execute::

    b_sq = b * b

Then ``four_ac`` (2.2).

.. jupyter-execute::

    four_ac = 4 * a * c

Now we can compute ``sqrt_term`` (2.).

.. jupyter-execute::
    
    from math import sqrt

    sqrt_term = sqrt(b_sq + four_ac)

and the final solution (``x``)

.. jupyter-execute::

    x = b + sqrt_term
    x

We can, of course, write this as a single statement.

.. jupyter-execute::

    x = b + (b**2 + 4 * a * c) ** 0.5
    x

Now this is a simple problem. For more challenging problems, as discussed below, breaking problems into pieces and making sure each piece works is a more successful strategy.

Look for patterns
-----------------

Part of what we have just done is to look at the "problem" (execute an equation) and recognised patterns in it (based on mathematical order of operations). That approach also applies to more complicated challenges.

Let's say we want to read in a plain text file which contains a header column followed by rows of numbers where fields are delimited by the tab character. Here is the first few lines of just such a file.

::

    length	kappa
    0.017963959082536105	8.567983199899585
    0.036913880515213056	7.658395694530731

Algorithmically, the top level problems are:

1. Open the file (see :ref:`files`)
2. Read the file line by line  (see :ref:`files`)
    
    2.1. Transform each line into usable data


That last point is the inner most, so we focus our attention on the challenge of transforming lines. We look at the sample of the file to we identify any patterns and notice 2 features. The first is that all lines have the same number of fields (separated by ``\t``). The second is that the header row is different in that the values are not numbers. We now modify the enumeration to give some more detail.

1. Open the file (see :ref:`files`)
2. Read the first line in the file

    2.1. Split the line into fields

3. Read the remaining lines in the file (see :ref:`files`)
    
    3.1. Split a line into fields
    
        3.1.1. Convert the line items into ``float``'s
    
4. Close the file (see :ref:`files`)

So I suggest the place to start is 3.1.1. I'm going to write separate functions for each of these steps. The reason being that it allows us to reuse code [2]_, makes checking the code correctness easier and simplifies building more complex algorithms into being just the inclusion of already written functions.

 Important here since 2.1 and 3.1 are the same. Using a function means we only have to write it once and we can use it as many times as seems appropriate.

We start this program with a function that takes a list of strings where every value needs to be converted into a ``float``. I'm going to write it and test it, using an ``assert``, with some sample data.

.. index:: assert, type casting

.. jupyter-execute::

    def cast_to_floats(values):
        """turns a series of strings into floats"""
        result = []
        for value in values:
            value = float(value)
            result.append(value)
        return result
    
    sample = ["0.0", "24.3", "13.5"]
    got = cast_to_floats(sample)
    assert got == [0.0, 24.3, 13.5]

Yay! So that's 3.1.1 out of the way. The next step out is solve 3.1. We also do this by writing a separate function that we check using some synthetic data and make sure it gives us the result we expect.

.. jupyter-execute::

    def line_to_fields(line):
        """splits at \t and cleans up the elements"""
        line = line.split("\t")
        # I think we should remove any leading / trailing white space from elements
        result = []
        for item in line:
            result.append(item.strip())
        return result
    
    # this sample is \t delimited with a \n character at the end
    # just as it would be if read from a file
    sample = "0.0\t24.3\t13.5\n"
    got = line_to_fields(sample)
    assert got == ["0.0", "24.3", "13.5"]

Double Yay! That's 3.1 (and thus 2.1) out of the way [3]_.

.. margin::
  
    .. [3] Also note this code will work if a line has 1 field, or 1 million fields.

Returning to the task list, we remove the steps we've already done, making it simpler to see what remains.

1. Open the file
2. Read the first line in the file
3. Read the remaining lines in the file
4. Close the file

The first and last are easy (see :ref:`files`). The remaining tasks (listed in the Exercise below) need to be solved before these 4 steps can all be combined into a single function. That function should use the ``line_to_fields()`` and ``cast_to_floats()`` functions that we have already written. At which point, job well done!

Exercises
=========

#. Using any text file, identify how to read just the first line.

#. Identify how to loop over all the lines in a file.

#. Identify how you can keep all the results of converting lines into floats.

#. Write a function ``parser()`` that completes the algorithm. You can apply it to the sample data you make up that looks like the above, or use :download:`this file <../data/numbers.tsv>`.
