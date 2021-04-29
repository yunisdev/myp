.. python-script-manager documentation master file, created by
   sphinx-quickstart on Thu Apr 29 13:01:25 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-script-manager's documentation!
=================================================
`Github repository <https://github.com/kritibytes/flaskmng>`_

What is PSM?
#################

**PSM** is a tool that helps you to manage and develop your Python apps easily.

Usage
#####

First of all, you must create virtual environment.

.. code:: bash

   > python -m venv env

To activate,

.. code:: bash

   > . env/Scripts/activate # for Windows
   > source env/bin/activate # for Linux

Then, for installing python-script-manager to the virtual environment you must use
pip. After installing pip enter the command given below:

.. code:: bash

   > pip install python-script-manager

API Reference
#############

.. click:: python_script_manager.__main__:main
   :prog: psm
   :nested: full

**Thanks for using!**
---------------------
<!-- 


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search` 
-->
