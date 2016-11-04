=============================
Using reStructuredText Markup
=============================

The reStructuredText specification allows for a certain degree of flexibility in markup to achieve your goals. For example, you can use any one of more than a dozen characters for section title underlines, and you have the option of using overline in addition to an underline.

However, for consistency and ease of use, the Mattermost documentation should use a single convention, despite the existence of allowable alternatives.

For more information about reStructuredText markup, see the `reStructuredText Markup Specification`_. Additional markup constructs are implemented by Sphinx, the documentation generator used by Mattermost. For information about the additional constructs, see `Sphinx Markup Constructs`_.

Use the following markup conventions in Mattermost documentation:

Page titles
===========

For page titles, use an overline and an underline. Use the = character. For example:

::
  
  =============================
  Using reStructuredText Markup
  =============================

Unlike Markdown, overlines and underlines in reStructuredText must be at least as long as the title text.

Section titles
==============

If your document has more than one section, use the = character for the section title underline. For example:

::
  
  Section titles
  ==============

If you do need subsections, use the the - character for the first subsection level, and the \` character for the second subsection level. For example:

::
  
  Subsection One
  --------------
  
  Subsection Two
  ``````````````

Bullet lists
============

For bullet lists and sublists, use only the - character. For example:

.. code-block:: none
  
  - list item one
  - list item two
    - sublist item one
    - sublist item two
  - list item three

Numbered lists and procedure steps
==================================

Create numbered lists and procedure steps using arabic numerals for the top-level list and lower case alpha characters for the first nested list. For example:

.. code-block:: none
  
  1. This is item one.
  2. This is item two.
    
    a. This is nested item one.
    b. This is nested item two.
    
  3. This is item three.
  
Linking to other documents
==========================

Use relative links to reference other documents in the Mattermost doc set. Also, use either the :doc: or :ref: linking mechanisms that are provided by Sphinx.

Preferred
  .. code-block:: none
  
    :doc:`sg_mattermost-doc-style`
    :ref:`target-label`

Avoid
  .. code-block:: none
  
    `Mattermost Documentation Style Guide`_
    
    _Mattermost Documentation Style Guide: sg_mattermost-doc-style.html

For more information about how to use :doc: and :ref:, see `Inline markup`_ on the Sphinx documentation page.


.. _reStructuredText Markup Specification: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
.. _Sphinx Markup Constructs: http://www.sphinx-doc.org/en/stable/markup/index.html
.. _Inline markup: http://www.sphinx-doc.org/en/stable/markup/inline.html

Literal blocks
==============

In reStructuredText markup, the double colon marks the start of a section of literal text that corresponds to the HTML <pre> tag. However, the Sphinx processor applies syntax highlighting for Python to literal blocks.

To use a literal block as originally intended in the reStructuredText specification, you must cheat a little, and use explicit code block markup with the language set to `none`. For example:

.. code-block:: none

  .. code-block:: none


Menu selections
===============

To indicate a series of menu selections, avoud the menuselection role that the Sphinx processor provides.

Preferred
  .. code-block:: none
  
    Click **File > Open**.

  This produces Click **File > Open**.

Avoid
  .. code-block:: none
  
    Click :menuselection:`File --> Open`.

  This produces :menuselection:`File --> Open`
