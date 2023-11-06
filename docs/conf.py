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
sys.path.insert(0, os.path.abspath('..'))

import reglsq

# -- Project information -----------------------------------------------------

project = 'reglsq'
copyright = '2022, Goodyear'
author = 'Jan Domurath'

version = reglsq.__version__
# The full version, including alpha/beta/rc tags
release = reglsq.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    'sphinx.ext.mathjax',
    "sphinx_copybutton",
    "sphinx_design",
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "autoclasstoc",
    "sphinxcontrib.bibtex",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates/sphinx']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'   # don't forget to install 'sphinx-rtd-theme'
html_theme = 'furo'


if html_theme == 'sphinx_rtd_theme':
    html_theme_options = {
        'display_version': True,
    }
    templates_path.append("_templates/rtd")
elif html_theme == 'furo':
    templates_path.append("_templates/furo")
    html_theme_options = {
        #  "announcement": "🚧 Work in Progress 🚧",
        "source_repository": "https://github.com/goodyear/reglsq",
        "source_branch": "main",
        "source_directory": "docs/",
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

if html_theme == 'sphinx_rtd_theme':
    html_css_files = [
        'css/custom_rtd.css',
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    ]
elif html_theme == 'furo':
    html_css_files = [
        'css/custom_furo.css',
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    ]

numfig = True

math_number_all = False  # if True, can cause issues
math_eqref_format = "Eq.{number}"

# -- Options for LaTeX output ------------------------------------------------

latex_domain_indices = False

latex_elements = {
    'papersize': "a4paper",
    'extrapackages': r'\usepackage{microtype}'
}

# -- Options for autosummary -------------------------------------------------

autosummary_generate = True

# -- Options for autodoc -----------------------------------------------------

autodoc_default_flags = ['members']
autodoc_typehints = 'both'

# -- Options for napoleon ----------------------------------------------------

napoleon_preprocess_types = True

# -- Options for sphinx copy-button ------------------------------------------

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: |PS> "
copybutton_prompt_is_regexp = True

# -- Options for intersphinx -------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
# -- Options for sphinxcontrib-bibtex ----------------------------------------

bibtex_bibfiles = ['bibfile.bib']


# -- Options for autoclasstoc ------------------------------------------------

from autoclasstoc.sections import PublicDataAttrs, PublicMethods


class PublicMethodsWithoutDunders(PublicMethods):
    key = 'public-methods-without-dunders'
    exclude_pattern = '__'
    include_inherited = False

class PublicAttrWithoutDunders(PublicDataAttrs):
    key = 'public-attr-without-dunders'
    exclude_pattern = '__'
    include_inherited = False


autoclasstoc_sections = [
        'public-methods-without-dunders',
        'public-attr-without-dunders',
]
