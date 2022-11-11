# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LouPlanchamp.github.io'
copyright = '2022, Lou Planchamp'
author = 'Lou Planchamp'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

html_title= 'Lou Planchamp'

html_theme_options = {
  "github_url": "https://github.com/LouPlanchamp",
  "icon_links": [
        {
            "name": "Instagram",
            "url": "https://www.instagram.com/neuroanat_b1_unige/",
            "icon": "fa-brands fa-instagram",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/lou-planchamp-55073b167/",
            "icon": "fa-brands fa-linkedin",
        },        
        ],
  "search_bar_text": "Search this site...",
}

html_favicon = "_static/brain-solid.svg"

html_static_path = ['_static']

# -- Sidebar Options for HTML output -------------------------------------------------
html_sidebars = {'index': ['sidebar.html'],
                 'about': ['sidebar.html'],
                 'blog':['tagcloud.html','archives.html']}

html_css_files=['custom.css']

extensions+=['ablog']
blog_title='mon blog'
blog_path='blog'
blog_post_pattern='posts/*/*'