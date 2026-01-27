Format messages
===============

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Use the messaging formatting toolbar
------------------------------------

From Mattermost v7.0, you can format your messages in Mattermost using the message formatting toolbar without having to specify any Markdown syntax.

.. image:: ../../images/message-formatting-toolbar.gif
  :scale: 50
  :alt: The message formatting toolbar, available from Mattermost v7.0, doesn't require Markdown syntax, and makes formatting message text fast and easy.

The message formatting toolbar offers the following formatting options:

+----------------------------------------------------------------------------------+-------------------------+
| **Formatting option**                                                            | **Icon**                |
+==================================================================================+=========================+
| `Bold, italicize, or strike out text <#use-markdown>`_                           | |bold-icon|             |
|                                                                                  | |italics-icon|          |
|                                                                                  | |strikeout-icon|        |
+----------------------------------------------------------------------------------+-------------------------+
| Add `headings <#headings>`_, `links <#links>`_,                                  | |headings-icon|         |
| or attachments                                                                   | |copy-link-icon|        |
|                                                                                  | |attachments-icon|      |
+----------------------------------------------------------------------------------+-------------------------+
| Format a numbered list, a bulleted list, quoted text, or                         | |numbered-icon|         |
| text as code                                                                     | |bullets-icon|          |
|                                                                                  | |quotes-icon|           |
|                                                                                  | |code-icon|             |
+----------------------------------------------------------------------------------+-------------------------+
| :doc:`Add emojis or GIFs </end-user-guide/collaborate/react-with-emojis-gifs>`   | |emoji-icon|            |
+----------------------------------------------------------------------------------+-------------------------+
| :doc:`Set message priority </end-user-guide/collaborate/message-priority>`       | |message-priority-icon| |
+----------------------------------------------------------------------------------+-------------------------+

Review how your message formatting will look when the message is sent by selecting the **Show/Hide Preview** |preview-icon| icon. Return to your draft message by selecting the icon again.

.. tip::

  - Hide the formatting options by selecting the **Show/Hide Formatting** |hide-formatting-icon| icon. Select the icon again to show the formatting options. 
  - You can control whether post formatting is rendered within the message formatting editor. When disabled, raw text is shown. See the :doc:`Channels customization </end-user-guide/preferences/manage-advanced-options>` documentation for details. 
 
Use Markdown
-------------

You can also format your messages in Mattermost using Markdown to control `text styling <#text-style>`__, `links <#links>`__, `headings <#headings>`__, `lists <#lists>`__, `code blocks <#code-blocks>`__, `in-line code <#in-line-code>`__, `in-line images <#in-line-images>`__, `horizontal lines <#horizontal-lines>`__, `block quotes <#block-quotes>`__, `tables <#tables>`__, and `math formulas <#math-formulas>`__. Markdown makes it easy to format messages: type a message as you normally would, then use formatting syntax to render the message a specific way. For a guide to using Markdown in Mattermost, `see this blog post <https://mattermost.com/blog/laymans-guide-to-markdown-on-mattermost/>`_.

.. image:: ../../images/messagesTable1.png
   :alt: Formatting markdown controls the look and feel of text messages.

Text style
~~~~~~~~~~

You can use either ``_`` or ``*`` around a word or phrase to make it italic, or ``__`` or ``**`` around a word or phrase to make it bold. 

.. tip::
    
    Common formatting keyboard shortcuts are supported. Bold text by pressing :kbd:`Ctrl` :kbd:`B` on Windows and Linux, or :kbd:`⌘` :kbd:`B` on Mac. Italicize text by pressing :kbd:`Ctrl` :kbd:`I` on Windows or Linux, or :kbd:`⌘` :kbd:`I` on Mac.

* ``*italics*`` (or ``_italics_``) renders as *italics*
* ``**bold**`` renders as **bold**
* ``***bold-italic***`` renders as |bold_italics|
* ``~~strikethrough~~`` renders as |strikethrough|

.. |bold_italics| image:: ../../images/bold_italics.png
  :width: 100px
  :alt: Bold Italics
  
.. |strikethrough| image:: ../../images/strikethrough.png
  :width: 100px
  :alt: Strike Through

Links
~~~~~

.. tip::

  Format selected message text as a link by pressing :kbd:`Ctrl` :kbd:`K` on Windows and Linux, or by pressing :kbd:`⌘` :kbd:`K` on Mac.

Channel links
^^^^^^^^^^^^^

Create a link to a public channel in a message by typing ``~`` followed by the channel name (e.g. ``~roadmap``). Channel members see private channel names returned.

Labeled links
^^^^^^^^^^^^^

Create labeled links by putting the desired text in square brackets ``[ ]`` and the associated link in round brackets ``( )``.

``[Check out Mattermost!](https://.mattermost.com/)``

Renders as: `Check out Mattermost! <https://mattermost.com/>`_

Headings
~~~~~~~~

Make a heading by typing ``#`` and a space before your title. For smaller headings, use more ``#``'s.

.. code-block:: text

  ## Large Heading
  ### Smaller Heading
  #### Even Smaller Heading

Renders as:

.. image:: ../../images/Headings1.png
   :alt: Large Heading

Alternatively, you can underline the text using equal signs ``===`` or hyphens ``---`` to create headings.

.. code-block:: text

  Large Heading
  -------------

Renders as:

.. image:: ../../images/Headings2.png
   :alt: Smaller Heading

Lists
~~~~~

Create a list by using asterisks ``*``, hyphens ``-``, and/or plus signs ``+`` interchangeably as bullets. Indent bullet points by adding two spaces in front each one.

.. code-block:: text

  * item one
  - item two
    + item two sub-point

Renders as:

* item one
* item two

  * item two sub-point

Make an ordered list by using numbers instead:

.. code-block:: text

  1. Item one
  1. Item two
  1. item three

Renders as:

#. Item one
#. Item two
#. Item three

You can also start a list at any number:

.. code-block:: text

  4. The first list number is 4.
  1. The second list number is 5.
  1. The third list number is 6.

Renders as:

4. The first list number is 4.
5. The second list number is 5.
6. The third list number is 6.

Make a task list by including square brackets ``[ ]``. Mark a task as complete by adding an ``x``.

.. code-block:: text

  - [ ] Item one
  - [ ] Item two
  - [x] Completed item

Renders as:

.. image:: ../../images/checklist.png
   :alt: List

Code blocks
~~~~~~~~~~~

Creating a fixed-width code block is recommended for pasting multi-line blocks of code or other text output because it's easier to read with fixed-width font alignment. Examples include block text snippets, ASCII tables, and log files. Rendered code blocks include a **Copy** option to copy the contents of the code block.

This can be accomplished by placing three backticks ``````` on the line directly above and directly below your code:

.. code-block:: text

  ```
  this is my
  code block
  ```

.. tip::

  Type three backticks ```````, press :kbd:`Shift` :kbd:`Enter` on Windows or Linux, or :kbd:`⇧` :kbd:`↵` on Mac, ``<type_your_code>``, press  :kbd:`Shift` :kbd:`Enter` on Windows or Linux, or :kbd:`⇧` :kbd:`↵` on Mac again, then type three more backticks ```````.


Or by indenting each line by four spaces:

.. code-block:: text

      this is my
      code block

  ^^^^ 4x spaces

Syntax highlighting
^^^^^^^^^^^^^^^^^^^^

To add syntax highlighting, type the language to be highlighted after the ``````` at the beginning of the code block. Mattermost also offers four different code themes (GitHub, Solarized Dark, Solarized Light, and Monokai) that can be changed in **Settings > Display > Theme > Custom Theme > Center Channel Styles**.

Supported languages and their aliases include:

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Language</th>
      <th class="head">Aliases</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">ActionScript</td>
      <td valign="middle">actionscript, as, as3</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">AppleScript</td>
      <td valign="middle">applescript</td>
    </tr>  
    <tr class="row-odd">
      <td valign="middle">Bash</td>
      <td valign="middle">bash, sh</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Clojure</td>
      <td valign="middle">clojure</td>
    </tr>  
    <tr class="row-odd">
      <td valign="middle">CoffeeScript</td>
      <td valign="middle">coffescript, coffee, coffee-script</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">C/C++</td>
      <td valign="middle">cpp, c++, c</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">C#</td>
      <td valign="middle">cs, c#, csharp</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">CSS</td>
      <td valign="middle">css</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">D</td>
      <td valign="middle">d, dlang</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Dart</td>
      <td valign="middle">dart</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Delphi</td>
      <td valign="middle">delphi</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Diff</td>
      <td valign="middle">diff, patch, udiff</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Django</td>
      <td valign="middle">django</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Dockerfile</td>
      <td valign="middle">dockerfile, docker</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Elixir</td>
      <td valign="middle">elixir, ex, exs</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Erlang</td>
      <td valign="middle">erlang, erl</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Fortran</td>
      <td valign="middle">fortran</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">F#</td>
      <td valign="middle">fsharp</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">G-Code</td>
      <td valign="middle">gcode</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Go</td>
      <td valign="middle">go, golang</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Groovy</td>
      <td valign="middle">groovy</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Handlebars</td>
      <td valign="middle">handlebars, hbs, mustache</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Haskell</td>
      <td valign="middle">haskell, hs</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Haxe</td>
      <td valign="middle">haxe</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Java</td>
      <td valign="middle">java</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">JavaScript</td>
      <td valign="middle">javascript, js</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">JSON</td>
      <td valign="middle">json</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Julia</td>
      <td valign="middle">julia, jl</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Kotlin</td>
      <td valign="middle">kotlin</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">LaTeX</td>
      <td valign="middle">latex, tex</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Less</td>
      <td valign="middle">less</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Lisp</td>
      <td valign="middle">lisp</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Lua</td>
      <td valign="middle">lua</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Makefile</td>
      <td valign="middle">makefile, make, mf, gnumake, bsdmake</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Markdown</td>
      <td valign="middle">markdown, md, mkd</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Matlab</td>
      <td valign="middle">matlab, m</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Objective C</td>
      <td valign="middle">objectivec, objective_c, objc</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">OCaml</td>
      <td valign="middle">ocaml</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Perl</td>
      <td valign="middle">perl, pl</td>
    </tr>
        <tr class="row-odd">
      <td valign="middle">Pascal</td>
      <td valign="middle">pascal, pas</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">PostgreSQL</td>
      <td valign="middle">pgsql, postgres, postgresql</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">PHP</td>
      <td valign="middle">php, php3, php4, php5</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">PowerShell</td>
      <td valign="middle">powershell, posh</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Puppet</td>
      <td valign="middle">puppet, pp</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Python</td>
      <td valign="middle">python, py</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">R</td>
      <td valign="middle">r, s</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Ruby</td>
      <td valign="middle">ruby, rb</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Rust</td>
      <td valign="middle">rust, rs</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Scala</td>
      <td valign="middle">scala</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Scheme</td>
      <td valign="middle">scheme</td>
    <tr class="row-odd">
      <td valign="middle">SCSS</td>
      <td valign="middle">scss</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Smalltalk</td>
      <td valign="middle">smalltalk, st, squeak</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">SQL</td>
      <td valign="middle">sql</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Stylus</td>
      <td valign="middle">stylus, styl</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Swift</td>
      <td valign="middle">swift</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Text</td>
      <td valign="middle">text</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">TypeScript</td>
      <td valign="middle">typescript, ts, tsx</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">VB.Net</td>
      <td valign="middle">vbnet, vb, visualbasic</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">VBScript</td>
      <td valign="middle">vbscript</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">Verilog</td>
      <td valign="middle">verilog</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">VHDL</td>
      <td valign="middle">vhdl</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">HTML, XML</td>
      <td valign="middle">html, xml</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">YAML</td>
      <td valign="middle">yaml, yml</td>
    </tr>
  </table>

Example:

.. code-block:: text

  ``` go
  package main
  import "fmt"
  func main() {
      fmt.Println("Hello, 世界")
  }
  ```

Renders as:

**GitHub Theme**

.. image:: ../../images/syntax-highlighting-github.png
   :alt: Syntax Highlighting in GitHub

**Solarized Dark Theme**

.. image:: ../../images/syntax-highlighting-sol-dark.png
   :alt: Syntax Highlighting Dark

**Solarized Light Theme**

.. image:: ../../images/syntax-highlighting-sol-light.png
   :alt: Syntax Highlighting Light

**Monokai Theme**

.. image:: ../../images/syntax-highlighting-monokai.png
   :alt: Syntax Highlighting Monokai

In-line code
~~~~~~~~~~~~

Create in-line monospaced code text by surrounding it with backticks `````. Don't use single quotes ``'``.

.. code-block:: text

  `monospace`

Renders as: ``monospace``.

In-line images
~~~~~~~~~~~~~~

In-line images are images added within lines of text. You can control whether all in-line images over 100px in height are automatically collapsed or expanded in messages by setting a :doc:`user preference </end-user-guide/preferences/manage-your-display-options>`, or by using the ``/collapse`` and ``/expand`` slash commands.

To add in-line images to text, use an exclamation mark ``!`` followed by the ``alt text`` in square brackets ``[ ]``, then the ``image URL`` in round brackets ``( )``. You can add hover text after the link by placing the text in quotes ``" "``.

Example:

.. code-block:: text

  ![alt text](URL of image "Hover text")

If the height of the original image is more than 500 pixels, Mattermost sets the image height at 500 pixels and adjusts the width to maintain the original aspect ratio.

You can set the width and height of the displayed image after the URL of the image by using an equals sign ``=`` followed by values for both width and height ``##x##``. If you set only the width, Mattermost adjusts the height to maintain the original aspect ratio.

.. warning::
  The native apps do not support fixed width and height and will display the full-size image.

Examples:

.. code-block:: text

  .. |mattermost-icon-76x76| image:: ../images/icon-76x76.png
  .. |mattermost-icon-50x76| image:: ../images/icon-50x76.png

In-line image with hover text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

  ![Mattermost](../images/icon-76x76.png "Mattermost Icon")

Renders as:

  .. image:: ../../images/icon-76x76.png
    :alt: Mattermost

In-line image with link
^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  An extra set of square brackets ``[ ]`` is required around the alt text, and round brackets ``( )`` are required around the image link.

.. code-block:: text

  [![Mattermost](../images/icon-76x76.png)](https://github.com/mattermost/mattermost)

Renders as:

  .. image:: ../../images/icon-76x76.png
    :target: https://github.com/mattermost/mattermost
   
In-line image displayed with fixed width and height
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: An in-line image that's 50 pixels wide and 76 pixels high.

.. code-block:: text

  ![Mattermost](../images/icon-76x76.png =50x76 "Mattermost Icon")

Renders as:

  .. image:: ../../images/icon-50x76.png
    :alt: Mattermost
    :name: Mattermost Icon 

In-line image displayed with fixed width
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example: An in-line image that's 50 pixels wide where the system adjusts the height to maintain the original aspect ratio.

.. code-block:: text

  ![Mattermost](../images/icon-76x76.png =50 "Mattermost Icon")

Renders as:

  .. image:: ../../images/icon-76x76.png
    :alt: Mattermost
    :width: 50
 
Horizontal lines
~~~~~~~~~~~~~~~~

Create a line by using three ``*``, ``_``, or ``-``.

``***``

Renders as:

---------------------------------------------------------------------------

Block quotes
~~~~~~~~~~~~

Create block quotes using ``>``.

``> block quotes`` renders as:

.. image:: ../../images/blockQuotes.png

Tables
~~~~~~

Create a table by placing a dashed line ``---`` under the header row, then separating each column with using pipes ``|``. The columns don’t need to line up exactly. Choose how to align table columns by including colons ``:`` within the header row.

.. code-block:: text

  | Left-Aligned  | Center Aligned  | Right Aligned |
  | :------------ |:---------------:| -----:|
  | Left column 1 | this text       |  $100 |
  | Left column 2 | is              |   $10 |
  | Left column 3 | centered        |    $1 |

Renders as:

.. image:: ../../images/markdownTable1.png
   :alt: Markdown Table Sample

.. note::

  Multi-line text in a table cell isn't supported using HTML tags such as ``<br>`` or ``<br/>``.

Math Formulas
~~~~~~~~~~~~~

.. tab:: Using Inline LaTeX

  You can create formulas that display inline using LaTeX. Use the dollar sign ($) symbol at the beginning and end of each formula.

  .. note::

    This feature is :ref:`disabled by default <administration-guide/configure/site-configuration-settings:enable inline latex rendering>`. Contact your system admin to enable this setting in **System Console > Site Configuration > Posts** to use this feature.

  .. code-block:: text

    $X_k = \sum_{n=0}^{2N-1} x_n \cos \left[\frac{\pi}{N} \left(n+\frac{1}{2}+\frac{N}{2}\right) \left(k+\frac{1}{2}\right) \right]$

  Renders as:

  .. image:: ../../images/latex-inline.png
    :alt: An inline LaTeX math equation sample.
    
.. tab:: Using LaTeX in Code Blocks

  Create formulas as code blocks by using LaTeX in a ``latex`` `code blocks <#code-blocks>`__. 

  .. note::

    This feature is :ref:`disabled by default <administration-guide/configure/site-configuration-settings:enable latex code block rendering>`. Contact your system admin to enable this setting in **System Console > Site Configuration > Posts** to use this feature.

  .. code-block:: text

    ```latex
    X_k = \sum_{n=0}^{2N-1} x_n \cos \left[\frac{\pi}{N} \left(n+\frac{1}{2}+\frac{N}{2}\right) \left(k+\frac{1}{2}\right) \right]
    ```

  Renders as:

  .. image:: ../../images/latex-codeblock.png
    :alt: A LaTeX code block math equation sample.

.. include:: ../../_static/badges/academy-message-formatting.rst
  :start-after: :nosearch:
