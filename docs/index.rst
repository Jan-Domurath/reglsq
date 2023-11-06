Welcome to reglsq documentation!
================================

.. toctree::
   :maxdepth: 3
   :hidden:
   :caption: Contents

   tutorials/index.rst
   how_to/index.rst
   topic/index.rst
   reference/index.rst
   bibliography.rst

.. only:: html

   *insert fancy picture or animation*


   Parts of the documentation
   ==========================

   .. grid:: 1 2 2 2
      :margin: 4 4 0 0
      :gutter: 1

      .. grid-item-card:: :octicon:`rocket` Getting Started
         :link: tutorials/index
         :link-type: doc

         Start here to learn how to use the tool.

      .. grid-item-card:: :octicon:`light-bulb` How-to(s)
         :link: how_to/index
         :link-type: doc

         Check here if you have specific questions.

      .. grid-item-card:: :octicon:`mortar-board` Topic guides
         :link: topic/index
         :link-type: doc

         How the tool works and how specific cases are handled.

      .. grid-item-card:: :octicon:`repo` Reference
         :link: reference/index
         :link-type: doc

         All the details.

   .. add some links to the sidebar

   .. toctree::
      :maxdepth: 1
      :hidden:
      :caption: About

      Changelog <changelog.rst>
      Contributing <contributing.rst>

   .. toctree::
      :maxdepth: 1
      :hidden:
      :caption: Links

      GitHub Page <https://github.com/goodyear/reglsq>

.. note: if you want to change the indices in the sidebar have a look at ``doc/_templates/layout.html``
