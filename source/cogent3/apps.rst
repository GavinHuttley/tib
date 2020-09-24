.. _apps:

Overview of ``cogent3`` apps
============================

``cogent3.apps`` can be though of as customised functions that have some special capabilities. The approach to using an existing app is to construct a configured instance, typically by calling the app with some argument values tuned for your particular case. You then apply it to input data by simply calling, without specifying any arguments.

There are quite a few apps and you can see an overview of what's available as follows

.. jupyter-execute::

    from cogent3 import available_apps
    
    apps = available_apps()
    
    apps.head()

That function returns a cogent3 table, so I'm just displaying the first few rows.

See the `cogent3 apps documentation <https://cogent3.org/doc/app/index.html>`_ for more details.
