############
Contributing
############

*******************************
Setup a development environment
*******************************

Create a virtual environment

.. code-block:: shell-session

    $ git clone git@github.com:goodyear/reglsq.git
    $ cd reglsq
    $ /apps/share/Python/3.10/bin/python3 -m venv .venv --prompt reglsq
    $ source .venv/bin/activate
    $ python -m pip install -U pip wheel
    $ python -m pip install -e .
    $ python -m pip install -r requirements_dev.txt
    $ pre-commit install


.. caution::

    You will have to reload the virtual environment every time you start a new shell.


Use pre-commit
==============

`Pre-commit <https://pre-commit.com/>`_ will be automatically executed to check/cleanup your code before any commit.

You can also run pre-commit directly to check your files at any time


.. code-block:: shell-session

    $ pre-commit run --all-files


*************
Documentation
*************

The documentation is set up to loosely follow `"Diátaxis" <https://diataxis.fr/>`_.

Install dependencies
====================

To build the the documentation you need to install some additional packages, they are listed in ``requirements.txt``.

You can install all of them with

.. code-block:: shell-session

    $ source .venv/bin/activate
    $ python -m pip install -r requirements.txt


Build the documentation
=======================

To build the docs, go into the ``docs`` folder and run ``make html``.

.. code-block:: shell-session

    $ source .venv/bin/activate
    $ cd docs
    $ make html


The documentation will be build in ``docs/_build/html``. You can open the ``index.html`` file.

Note sometimes it makes sense to clean the docs with ``make clean``.

reStructuredText
================

The documentation is written in `reStructuredText <https://docutils.sourceforge.io/rst.html>`_.

Here are some useful pages to help get started:

- `Sphinx's reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
- `TYPO3's reStructuredText & Sphinx <https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/WritingReST/Index.html>`_
- `Some simple examples <https://effective-happiness-af55b240.pages.github.io/latest/example/example.html>`_

Documentation style
===================

You can write docstrings in `google <https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`_ or `numpy <https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard>`_ style, thanks to the `napoleon extension <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_.

You can mix the style by function, method, but not within the same docstring.

In order to write a latex formula use (note ``r`` in front of top quotes)

.. code-block:: rst

    r"""
    for single line equation:
    ..math::

        \rho = x\cos\theta + y\sin\theta

    or inline
    :math:`\rho = x\cos\theta + y\sin\theta`

    """
