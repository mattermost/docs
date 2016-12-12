Using reStructuredText Markup
=============================

The reStructuredText specification allows for a certain degree of flexibility in markup to achieve your goals. For example, you can use any one of more than a dozen characters for section title underlines, and you have the option of using an overline in addition to an underline.

However, for consistency and ease of use, the Mattermost documentation should use a single convention, despite the existence of allowable alternatives.

For more information about reStructuredText markup, see the `reStructuredText Markup Specification <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_. Additional markup constructs are implemented by Sphinx, the documentation generator used by Mattermost. For information about the additional constructs, see `Sphinx Markup Constructs <http://www.sphinx-doc.org/en/stable/markup/index.html>`_.

Use the following markup conventions in Mattermost documentation:

Page titles
-----------

For page titles, use the = character for the title underline, with no overline. For example:

.. code-block:: none
  
  Using reStructuredText Markup
  =============================

Unlike Markdown, underlines in reStructuredText must be at least as long as the title text.

Section titles
--------------

If your document has more than one section, use the - character for the section title underline. For example:

.. code-block:: none
  
  Section titles
  --------------

If you do need subsections, use the the ~ character for the first subsection level, and the ^ character for the second subsection level. For example:

.. code-block:: none
  
  Subsection One
  ~~~~~~~~~~~~~~
  
  Subsection Two
  ^^^^^^^^^^^^^^
  
Inline markup
-------------

Bold
  Use double asterisks. For example: ``**bold text**``.

Italic
  Use single asterisk. For example: ``*italic text*``.

Monospace
  Use double backquotes. For example: ````monospace text````

.. _arbitrary-text-label:

Bullet lists
------------

For bullet lists and sublists, use only the - character. For example:

.. code-block:: none
  
  - list item one
  - list item two
    - sublist item one
    - sublist item two
  - list item three

Numbered lists and procedure steps
----------------------------------

Create numbered lists and procedure steps using arabic numerals for the top-level list and lower case alpha characters for the first nested list. For example:

.. code-block:: none
  
  1. This is item one.
  2. This is item two.
    
    a. This is nested item one.
    b. This is nested item two.
    
  3. This is item three.
  
Links to external web pages
---------------------------

The quickest and easiest way to create a link in reStructuredText is to use the URL without any extra markup. For example:

.. code-block:: none
  
  https://www.mattermost.org/manifesto/

On output to HTML, the link looks like this: https://www.mattermost.org/manifesto/.

You can also create a link that has link text. For example:

.. code-block:: none
  
  `Mattermost Manifesto <https://www.mattermost.org/manifesto/>`_

On output to HTML, the link looks like this: `Mattermost Manifesto <https://www.mattermost.org/manifesto/>`_

Pay close attention to the syntax. The link starts with a backquote character, followed by the text that you want to see in the document, a final space, the < character, the URL, the > character, a closing backquote, and finally an underscore.

.. _relative-links-in-rst:

Links to targets within the Mattermost docs
-------------------------------------------

The Sphinx processor extends reStructuredText to implement references to locations within a documentation set. The extensions are called `roles`, and the two roles that are relevant in Mattermost documentation are the ``:doc:`` role and the ``:ref:`` role.

The ``:doc:`` role is used for creating relative links to other documents. The ``:ref:`` role is used for creating relative links to arbitrary locations within the documentation set, including within the same document. In both cases, the HTML output is a relative URL for the target location.

The following example uses the ``:doc:`` role to link to the `Integrations Overview` page. The source file is called ``integrations.rst`` and is in the ``overview`` directory.

.. code-block:: none

  For more information about integrating with Mattermost, see :doc:`../overview/integrations`.

Note that the filename extension is not part of the construct. On output, the link looks like this: "For more information about integrating with Mattermost, see :doc:`../overview/integrations`." The Sphinx processor pulls in the title of the document to use as the link text. 

The ``:ref:`` role is a two-part construct. One part is the link itself, and the other part is the target. The target has the following form, and should preceed a section title:

.. code-block:: none

  .. _arbitrary-text-label:
  
  Bullet lists
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

You can also add the following image options: `alt`, `height`, `width`, `scale`, `align`, and `target`. For example:

.. code-block:: none

  .. image:: ../images/choices.png
    :alt: The choices that you can make.
    :height: 100px
    :width: 200px
    :align: left

Inserting an inline image is a bit more complicated. It's a two-part construct that consists of a label and the image directive. Surround the label text with vertical bars, the `|` character. For example:

.. code-block:: none

  Some of the emoji that you can use are |emoji|.

Later on in the document, perhaps at the end of the paragraph that contains the label, insert the following image directive:

.. code-block:: none

  .. |emoji| image:: ../images/emoji.png
    :alt: Some of the emoji that you can use.
    :align: middle

.. _literal-blocks:

Literal blocks
--------------

In reStructuredText markup, the double colon marks the start of a section of literal text that corresponds to the HTML <pre> tag. However, the Sphinx processor applies syntax highlighting for Python to literal blocks, which is not always desired in Mattermost documentation.

To use a literal block as originally intended in the reStructuredText specification, you must cheat a little, and use the Sphinx code-block directive with the language set to `none`. For example:

.. code-block:: none

  .. code-block:: none

.. _syntax-highlight:

Code blocks with syntax highlighting
------------------------------------

To create a code block with syntax highlighting, use the Sphinx code-block directive with the language set to the language that you want highlighted. Many languages are available, but in Mattermost documentation the most likely ones are as follows:

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

The highlighting is provided by Pygments Python syntax highlighter, which supports a large number of programming and markup languages. For a complete list, see `Available lexers <http://pygments.org/docs/lexers/>`_
