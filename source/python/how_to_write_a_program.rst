Pulling it together -- writing your own programs
================================================

While it can seem daunting, the key to writing a program is to just start typing.

First, do you need to open a file for reading? Then that's the first piece of code you write.

.. code:: python
    
    datafile = open("some-data.txt")
    print(datafile)
    datafile.close()

Second, what type of data are you going to be handling? If you can, it's a good idea to make a really small sample data file. You can do this by grabbing a larger one and editing it down to be small (say just a few records). Having a small file means you know exactly what's in there, and your program should run really quick.

When you've got the sample data organised, think about what you're supposed to be producing. Do you need to produce a certain type of data structure? For example, a dictionary with "labels" as keys and the biological sequence as the "value". In this example, you know then there are two different types of information you need to extract from your file and that the program must satisfy 3 criteria:

1. extracts sequence labels correctly 
2. extracts sequences correctly 
3. associates labels and sequences correctly, i.e. "label1" is the key for "sequence1".

Broken down like this, it becomes the case that you solve one of these pieces at a time. Solving means write the code and a test that (given known input) checks your code produces the correct output.

This approach then becomes the foundation for an algorithm with modular design. A modular approach to implementing software makes it easier to validate correctness of the code.

One approach to modularising code is to write a number of functions which are then used to build more extensive programs. Some good pointers for whether some code should be written as function are:

- the code is likely to be useful in multiple locations, so making it a function will eliminate redundancy
- the code is relatively short (say under 100 lines) and its correctness is critical to overall correctness of a program

Either of these is sufficient reason to write a function.

Building a program from functions requires only that the function is defined before it is used and that it is in the name space where it is to be used. So for the example I've given above, you have two functions you could write.

That said, don't be too rigid in how you approach a problem. It may be that keeping things as separate functions doesn't "work well". But it never hurts to start writing in that way.

I illustrate the semantics of this process here using a simple numerical example of computing some summary statistics. The ``get_summary_stats`` functions is an example of a *wrapper function*. It's primary purpose is to call two other functions without any additional computations.

.. jupyter-execute::
    :linenos:

    from math import sqrt

    def mean(x):
        """returns the mean of x"""
        total = sum(x)
        num = len(x)
        return total / num

    assert mean([0, 5, 8, 11]) == 6.0, "error in mean calculation"

    def std(x, mu):
        """returns the sample standard deviation of x given mu (the mean of x)."""
        n = len(x)
        variance = 0.0
        for element in x:
            val = (element - mu) ** 2
            variance += val
        variance /= n - 1  # sample std dev
        return sqrt(variance)

    assert round(std([0, 5, 8, 11], 6), 4) == 4.6904, "error in calculating std dev"

We can now use the ``mean`` and ``std`` functions with confidence.

.. jupyter-execute::
    :linenos:

    def get_summary_stats(x):
        """returns the mean and sample standard deviation"""
        assert len(x) > 0, "Cannot compute mean, std on zero-length array"
        mu = mean(x)
        std_dev = std(x, mu)
        return mu, std_dev

    mu, std_dev = get_summary_stats(range(20))
    mu, std_dev
