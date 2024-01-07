import datetime
import os

today = datetime.date.today()

os.environ["COGENT3_WARNINGS"] = "ignore"
os.environ["COGENT3_ALIGNMENT_REPR_POLICY"] = "wrap=30,num_pos=30"

project = "Topics in Bioinformatics"
copyright = f"2020-{today:%Y}, Gavin Huttley"
release = f"{today:%Y.%m.%d}"
author = "Gavin Huttley"


# -- General configuration ---------------------------------------------------

rst_prolog = """
.. include:: <s5defs.txt>
.. include:: /_globals.rst
"""

extensions = [
    "sphinx.ext.graphviz",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "nbsphinx",
    "jupyter_sphinx",
    "sphinx_design",
    "sphinxcontrib.bibtex",
    "sphinx_book_theme",
]

# todo_include_todos = True
show_authors = True
graphviz_output_format = "svg"

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["*/sample_homologs.ipynb", "*/orig_nbks/*"]

html_theme = "sphinx_book_theme"
# -- Options for HTML output -------------------------------------------------

html_static_path = ["_static"]

html_title = project

html_theme_options = {
    "collapse_navbar": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "show_navbar_depth": 1,
    "repository_url": "https://github.com/GavinHuttley/tib",
    "use_repository_button": True,
}

html_css_files = [
    "css/custom.css",
]

bibtex_bibfiles = ["references.bib"]
