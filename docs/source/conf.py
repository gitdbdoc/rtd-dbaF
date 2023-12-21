# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'argoPlot-script UserGuide'
copyright = 'since 2022 by dberlianty'
author = 'dberlianty'

release = '0.1'
version = '0.1.0'

# -- General configuration

exclude_patterns = [
    '**.ipynb_checkpoints',
]

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_theme = 'bizstyle'

#html_static_path = ['_static']
#html_show_sourcelink = False
#html_use_index = False
#html_show_sphinx = False


# -- Options for EPUB output
epub_show_urls = 'footnote'

