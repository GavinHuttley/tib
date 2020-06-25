Data Visualisation using Plotly
===============================

.. todo:: add links to plotly express and a section describing

With ``Plotly``, the basic data structure for defining a plot is a dict. This dict has two components, a "trace" and a "layout".

Plot trace
----------

The trace is a dict and, at a minimum, it requires 3 keys:

- ``"type"``: ``"scatter"`` for a scatter plot
- ``"x"``: the values for the x-axis
- ``"y"``: the values for the y-axis

Note that ``x`` and ``y`` are paired, meaning that ``(x[0], y[0])`` correspond to the cartesian coordinates for the first point.

There are other optional components. To make this just a scatter plot, you should include the following additional keys:

- ``"mode"``: "markers", displays only points on the plot
- ``"marker"``: attributes such as shape, size, color

So here's a sample definition of a trace:

.. jupyter-execute::

    trace = {
        "type": "scatter",
        "x": [0, 1],
        "y": [0, 1],
        "mode": "markers",
        "marker": {"size": 12},
    }

Simple layout
-------------

We want some axis titles, a plot title and define the figure height and width (in pixels).

We define those in the ``layout``. For this very simple demo, we do this as follows

.. jupyter-execute::

    layout = {
        "title": "Sample Title",
        "xaxis": {"title": "value along x-axis"},
        "yaxis": {"title": "value along y-axis"},
        "width": 600,
        "height": 600,
    }

and a Plotly figure, amazingly, is as simple as

.. jupyter-execute::

    fig = {"data": [trace], "layout": layout}

Which we display using the ``show()`` function.

.. jupyter-execute::

    import plotly.io

    plotly.io.show(fig)
