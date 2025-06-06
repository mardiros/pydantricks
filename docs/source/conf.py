# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import tomllib

sys.path.insert(0, os.path.abspath("../../src"))


# -- Project information -----------------------------------------------------
def _get_project_meta():
    with open("../../pyproject.toml", "rb") as pyproject:
        return tomllib.load(pyproject)["project"]


pkg_meta = _get_project_meta()
project = str(pkg_meta["name"])
author = f"{pkg_meta['authors'][0]['name']} <{pkg_meta['authors'][0]['email']}>"
copyright = f"{pkg_meta['authors'][0]['name']} and contributors"

# The short X.Y version
version = str(pkg_meta["version"])
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "autodoc2",
]

autodoc2_packages = [
    {"path": "../../src/pydantricks"},
]

autodoc2_module_all_regexes = [
    "pydantricks",
]

autodoc2_docstring_parser_regexes = [
    # this will render all docstrings as Markdown
    (r".*", "myst"),
]

autodoc2_hidden_objects = ["private", "inherited"]
autodoc2_render_plugin = "myst"

autodoc2_output_dir = "develop"
autodoc2_sort_names = True

# Configure MyST parser
myst_enable_extensions = [
    "colon_fence",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
    "deflist",
    "fieldlist",
    "linkify",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []  # "_static"]
