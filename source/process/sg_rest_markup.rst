ReStructuredText Markup
=======================

The reStructuredText specification allows for a certain degree of flexibility in markup to achieve your goals. For example, you can use any one of more than a dozen characters for section title underlines, and you have the option of using an overline in addition to an underline.

However, for consistency and ease of use, the Mattermost documentation should use a single convention, despite the existence of allowable alternatives.

For more information about reStructuredText markup, see the `reStructuredText Markup Specification <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`__. Additional markup constructs are implemented by Sphinx, the documentation generator used by Mattermost. For information about the additional constructs, see `Sphinx Markup Constructs <https://www.sphinx-doc.org/en/1.7/markup/index.html>`__.

Use the following markup conventions in Mattermost documentation:

Page Titles
-----------

Underline page titles using `=`, with no overline. Underlines should be as long as the title text. For example:

.. code-block:: none

  Document Title
  ==============

Section Titles
--------------

Underline using `-` for section titles. For example:

.. code-block:: none

  Section Title
  -------------

Underline subsections using `~` for the first subsection level, and `^` for the second subsection level. For example:

.. code-block:: none

  Subsection One
  ~~~~~~~~~~~~~~

  Subsection Two
  ^^^^^^^^^^^^^^

.. _table-of-contents:

Table of Contents
-----------------

Insert a table of contents into a document using the following format:

.. code-block:: none

  .. contents::
      :backlinks: top

Inline Markup
-------------

Bold
  Use double asterisks. For example: ``**bold text**``.

Italic
  Use single asterisk. For example: ``*italic text*``.

Monospace
  Use double backquotes. For example: ````monospace text````

.. _arbitrary-text-label:

Bullet Lists
------------

For bullet lists and sublists, use ``-`` before the list item. For example:

.. code-block:: none

  - list item one
  - list item two
    - sublist item one
    - sublist item two
  - list item three

Numbered Lists and Procedure Steps
----------------------------------

Create numbered lists and procedure steps using numbers for the top-level list and lower case alpha characters for the first nested list. For example:

.. code-block:: none

  1. This is item one.
  2. This is item two.

    a. This is nested item one.
    b. This is nested item two.

  3. This is item three.

Name-value Groups
-----------------

To create a name-value group such as a definition list, type the term on a line by itself. On the next line, indent the definition. For example:

.. code-block:: none

  Total Users
    The total number of active accounts created on your system. Excludes inactive accounts.
  Total Teams
    The total number of teams created on your system.

External Links
---------------

URLs are automatically rendered as links in Sphinx; however, where possible, it is preferred that hyperlinks are created within the text of a sentence. Hyperlinks within a sentence can be created using the following formatting:

``Link display text <URL-of-website>`__``, for example:

.. code-block:: none

  `Mattermost Manifesto <https://www.mattermost.org/manifesto/>`__

The link renders as: `Mattermost Manifesto <https://www.mattermost.org/manifesto/>`__

.. _relative-links-in-rst:

Internal Links to Mattermost Docs
----------------------------------

The Sphinx processor extends reStructuredText to implement references, called roles, to locations within a documentation set. The two roles that are relevant in Mattermost documentation are the ``:doc:`` role and the ``:ref:`` role.

The ``:doc:`` role is used for creating relative links to other documents. The ``:ref:`` role is used for creating relative links to arbitrary locations within the documentation set, including within the same document. In both cases, the HTML output is a relative URL for the target location.

The following example uses the ``:doc:`` role to link to the `Integrations Overview` page. The source file is called ``integrations.rst`` and is in the ``overview`` directory.

.. code-block:: none

  For more information about integrating with Mattermost, see :doc:`../overview/integrations`.

Note that the filename extension is not part of the construct. On output, the link looks like this: "For more information about integrating with Mattermost, see :doc:`../overview/integrations`." The Sphinx processor pulls in the title of the document to use as the link text.

The ``:ref:`` role is a two-part construct. One part is the link itself, and the other part is the target. The target has the following form, and should preceed a section title:

.. code-block:: none

  .. _arbitrary-text-label:

  Bullet Lists
  ------------

To generate a link to the section, use the ``:ref:`` role as follows:

.. code-block:: none

  For more information about bullet lists, see :ref:`arbitrary-text-label`.

The Sphinx processor creates a relative link to the section, and uses the section title as the link text. On output, the link looks like this: "For more information about bullet lists, see :ref:`arbitrary-text-label`."

Images
------

Use the following construct to insert an image:

.. code-block:: none

  .. image:: ../images/choices.png

You should use `alt` tag for all images.

You can also add the following image options: `height`, `width`, `scale`, `align`, and `target`. For example:

.. code-block:: none

  .. image:: ../images/choices.png
    :alt: The choices that you can make.
    :height: 100px //number refers to pixels
    :width: 200px //number refers to pixels
    :align: left //left, right or middle
    :scale: 50 //number is a percentage

Inserting an inline image is a bit more complicated. It's a two-part construct that consists of a label and the image directive. Surround the label text with vertical bars, the ``|`` character. For example:

.. code-block:: none

  Some of the emoji that you can use are |emoji|.

Then insert the following image directive at the bottom of the document:

.. code-block:: none

  .. |emoji| image:: ../images/emoji.png
    :alt: Some of the emoji that you can use.
    :align: middle

.. _literal-blocks:

Literal Blocks
--------------

To use a literal block with no syntax highlighting, use the Sphinx code-block directive with the language set to ``none``. For example:

.. code-block:: none

  .. code-block:: none

.. _syntax-highlight:

Code Blocks with Syntax Highlighting
------------------------------------

To create a code block with syntax highlighting, use the Sphinx code-block directive with the language set to the language that you want highlighted. `Many languages are available <http://pygments.org/docs/lexers/>`__, but in Mattermost documentation the most likely ones are as follows:

- go
- rest
- html
- javascript
- coffee
- bash

The following example is a block of Go code using the :linenos: option, which causes line numbers to be displayed.

.. code-block:: none

  .. code-block:: go
    :linenos:

    newPassword := props["new_password"]
  	if err := utils.IsPasswordValid(newPassword); err != nil {
  		c.Err = err
  		return
  	}

The example produces the following output:

.. code-block:: go
  :linenos:

  newPassword := props["new_password"]
	if err := utils.IsPasswordValid(newPassword); err != nil {
		c.Err = err
		return
	}
