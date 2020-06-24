project = "Topics in Bioinformatics"
copyright = "2020, Gavin Huttley"
author = "Gavin Huttley"

release = "2020"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.graphviz",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "nbsphinx",
    "jupyter_sphinx",
    "sphinx_panels",
    "sphinxcontrib.bibtex",
]

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["*/sample_homologs.ipynb", "*molevol*"]

html_theme = "alabaster"
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


def setup(app):
    import pathlib, sys

    css = pathlib.Path(html_static_path[0]) / "css"
    for fn in css.glob("*.css"):
        app.add_css_file(f"{fn}")
        sys.stderr.write("{fn}\n")
