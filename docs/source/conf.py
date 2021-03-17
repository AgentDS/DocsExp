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

# sys.path.insert(0, os.path.abspath('.'))
current_dir = os.path.dirname(__file__)
target_dir = os.path.abspath(os.path.join(current_dir, "../.."))
sys.path.insert(0, target_dir)
print(target_dir)

# -- Project information -----------------------------------------------------

project = 'Docs Experiment'
copyright = '2021, AgentDS'
author = 'AgentDS'

# The full version, including alpha/beta/rc tags
release = '0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
              # 'sphinx.ext.autodoc',
              'autoapi.extension',  # this one is really important
              # 'sphinx.ext.autosummary',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.mathjax',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              # 'sphinx.ext.doctest',  # it seems dangerous to use this???
              'sphinxcontrib.napoleon',
              'sphinx.ext.autosectionlabel',
              # allows you to refer sections its title. This affects to the reference role (ref)
              ]

# configuration for 'sphinx.ext.autodoc'
# autoclass_content = "both"  # keep both __init__ and class name for each class
autodoc_mock_imports = ["numpy", "torch", "torchvision"]
# autodoc_typehints = 'signature'
# autodoc_default_options = {
#     'members': True,
#     'undoc-members': True,
# }
autoclass_content = 'both'  # it seems not work for class init params
# autodoc_default_options = {
#     # 'ignore-module-all': True
#     'show-inheritance': None
# }    # do not use this, unwanted inheritance for class

# configuration for 'autoapi.extension'
autoapi_type = 'python'
autoapi_dirs = ['../../docsexp']
autoapi_template_dir = '_autoapi_templates'

# Napoleon settings, not useful???
# napoleon_google_docstring = True
# napoleon_include_init_with_doc = True


# Add more mapping for 'sphinx.ext.intersphinx'
intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'PyTorch': ('http://pytorch.org/docs/master/', None),
                       'numpy': ('https://numpy.org/doc/stable/', None)}

# build the templated autosummary files
# autosummary_generate = True
# numpydoc_show_class_members = False

# autosectionlabel throws warnings if section names are duplicated.
# The following tells autosectionlabel to not throw a warning for
# duplicated section names that are in different documents.
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, 'todo' and 'todoList' produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
# html_theme = "sphinx_typo3_theme"  # white font in API docstrings... DO NOT use it

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# # ClassDocumenter.add_directive_header uses ClassDocumenter.add_line to
# #   write the class documentation.
# # We'll monkeypatch the add_line method and intercept lines that begin
# #   with "Bases:".
# # In order to minimize the risk of accidentally intercepting a wrong line,
# #   we'll apply this patch inside of the add_directive_header method.
#
# from sphinx.ext.autodoc import ClassDocumenter, _
#
# add_line = ClassDocumenter.add_line
# line_to_delete = _(u'Bases: %s') % u':class:`object`'
#
#
# def add_line_no_object_base(self, text, *args, **kwargs):
#     if text.strip() == line_to_delete:
#         return
#
#     add_line(self, text, *args, **kwargs)
#
#
# add_directive_header = ClassDocumenter.add_directive_header
#
#
# def add_directive_header_no_object_base(self, *args, **kwargs):
#     self.add_line = add_line_no_object_base.__get__(self)
#
#     result = add_directive_header(self, *args, **kwargs)
#
#     del self.add_line
#
#     return result
#
#
# ClassDocumenter.add_directive_header = add_directive_header_no_object_base
