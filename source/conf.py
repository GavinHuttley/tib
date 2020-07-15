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
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "nbsphinx",
    "jupyter_sphinx",
    "sphinx_panels",
    "sphinxcontrib.bibtex",
    "sphinx_rtd_theme",
]

todo_include_todos = False
show_authors = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["*/sample_homologs.ipynb", "*molevol*"]

html_theme = "sphinx_rtd_theme"
# -- Options for HTML output -------------------------------------------------

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "GavinHuttley", # Username
    "github_repo": "tib", # Repo name
    "github_version": "develop", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}

html_static_path = ["_static"]

html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': False,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}

html_css_files = [
    'css/custom.css',
]

