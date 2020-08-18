Data Visualisation using Plotly
===============================

.. todo:: add links to plotly express and a section describing

.. [1] The foundation data structure of all ``Plotly`` plotting is a dict which has two components, a "trace" and a "layout". We will use the ``express``  module, which simplifies the interface to plotting.

Plotly_ is a javascript based plotting library that has interfaces for Python and multiple other programming languages [1]_. This javascript foundation enables its ability to display interactive plots within web browsers. Below I introduce the `Plotly Express`_ [2]_.

.. [2] I will use the ``as`` keyword in the import statement, allowing me to specify a new name (``px``) by which to refer to express. This is a common practice.

.. _Plotly: https://plotly.com/python
.. _`Plotly Express`: https://plotly.com/python/plotly-express/

.. index::
    pair: scatter; plotly
    pair: coordinates; plotly

Scatter plots
-------------

A quirk of Plotly is that cartesian coordinates (i.e. :math:`x`, :math:`y` coordinates) are represented as separate series for the :math:`x` and :math:`y` components. For instance, let's display a single point at :math:`x=1,y=3` (or :math:`(1,3)`) on a scatter plot using the ``scatter()`` function. This returns a Plotly figure object which can be used for display.

.. jupyter-execute::
    :linenos:

    import plotly.express as px

    fig = px.scatter(x=[1], y=[3])
    fig.show()

To add another point at ``(3, 7)`` we append `3` to the `x` list and `7` to the `y` list.

.. jupyter-execute::
    :linenos:

    import plotly.express as px

    fig = px.scatter(x=[1, 3], y=[3, 7])
    fig.show()

Modifying axis labels
---------------------

We can specify our own labels for the *x* and *y* axes

.. jupyter-execute::
    :linenos:

    import plotly.express as px

    fig = px.scatter(x=[1, 3], y=[3, 7], labels={"x": "species 1", "y": "species 2"})
    fig.show()

Modifying display
-----------------

.. index::
    pair: heigh; plotly
    pair: width; plotly

Modifying figure size
---------------------

The figure dimensions will adjust to your browser width, unless you specify their width and/or height. The units for those settings are pixels. We make a square plot.

.. jupyter-execute::
    :linenos:

    import plotly.express as px

    fig = px.scatter(x=[1, 3], y=[3, 7], width=400, height=400)
    fig.show()


.. index::
    pair: traces; plotly
    pair: layout; plotly
    pair: data; plotly
    pair: dict; plotly
    pair: marker; plotly
    pair: symbol; plotly

Selecting different symbols and/or sizes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Making more refined changes to display properties requires some inspection of the base objects. As mentioned above, dictionaries are the basis for all Plotly objects and the dict has two top-level components: "data" and "layout". The data consists of a series of "traces". Attributes, such as coordinates of scatter points and the type of plot are recorded in individual traces. Inspecting the last figure from above.

.. jupyter-execute::
    :linenos:

    len(fig.data) # there's a single trace

.. jupyter-execute::
    :linenos:

    fig.data[0]

We can access an individual element using standard dictionary operations.

.. jupyter-execute::
    :linenos:

    fig.data[0]["marker"]

We can change these values and the change will affect the figure [3]_.

.. jupyter-execute::
    :linenos:

    fig.data[0]["marker"]["size"] = 18
    fig.data[0]["marker"]["symbol"] = "square"
    fig.show()

.. [3] A demonstration of the fine-grained control of marker sizes, etc.. `can be found here <https://plotly.com/python/marker-style/>`_.

Histograms
----------

.. jupyter-execute::
    :linenos:

    import plotly.express as px
    import numpy as np

    x = np.random.randn(1000)
    
    fig = px.histogram(x=x)
    fig.show()
    x[:10]

Bar charts
----------

When dealing with genomic data, we frequently deal with genomic coordinates. One type of question that is raised in these circumstances is whether observations are random across the genome [4]_. We can use a bar plot to visually examine the density of observations.

.. [4] `Here's an example <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2822288/figure/fig1/>`_ that identified oscillating signals in genetic divergence.

This specific example is contrived as I'm using simulated data points, but the approach here will be useful.

Generate some 100 random integers between 0 and 21.

.. jupyter-execute::
    :linenos:

    from numpy.random import randint

    nums = randint(low=10, high=31, size=100)

Use a builtin Python counter class to count the number of occurrences of the different integers [5]_.

.. [5] You use this class just like a ``dict``.

.. jupyter-execute::
    :linenos:

    from collections import Counter

    counts = Counter(nums)
    print(counts)

Generate the x and y series for plotting.

.. jupyter-execute::
    :linenos:

    x, y = [], []
    for n in sorted(counts):
        x.append(n)
        y.append(counts[n])

Construct the bar chart

.. jupyter-execute::
    :linenos:

    import plotly.express as px
    
    fig = px.bar(x=x, y=y)
    fig.show()

Exercises
=========

**1.** Look at the plotly documentation and convert one of the scatter plots into a line plot.

**2.** In the bar chart example above, the numbers were generated from 10-31. The midpoint of this range is 20 (there are 10 smaller numbers and 10 larger numbers). Modify the x-axis values so that instead of showing the x-axis values rangig from 10 to 30, centred on 20, they range from -10 to 10, centred on 0. The result should look identical to the above but any current x-axis values < 20 will be negative.

