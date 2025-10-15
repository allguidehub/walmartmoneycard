# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Walmart MoneyCard Activation Guide'
author = 'Walmart Support Team'
copyright = '2025, Walmart'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (add if needed, e.g., 'sphinx_rtd_theme')
extensions = []

# Allow reStructuredText raw HTML support
raw_enabled = True

# Paths that contain templates
templates_path = ['_templates']  # Uncomment if custom templates are used

# Files/folders to exclude from the build
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional: you can enable Read the Docs theme later)
# html_theme = 'sphinx_rtd_theme'

# Basic HTML page titles
html_title = "How to Activate Walmart MoneyCard – Complete Guide"
html_short_title = "Walmart MoneyCard Activation"

# Favicon (place favicon.ico in _static or main folder if used)
html_favicon = 'favicon.ico'  # Update path if needed

# Hide page source link
html_show_sourcelink = False

# Allow raw/unsafe HTML inside .rst files
html_allow_unsafe = True

# Theme custom options
html_theme_options = {
    'show_powered_by': False,
}

# Static assets path (uncomment if using CSS or JS files)
# html_static_path = ['_static']

