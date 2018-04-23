Grammar, Spelling, and Mechanics
================================

To maintain consistency across all Mattermost technical documentation, adhere to the guidelines here.

Language and Spelling
---------------------

Write documents in English. Use American spelling.

Paragraphs and Sentences
------------------------

Paragraphs should express one idea or topic. Long paragraphs are sometimes difficult to read on screen, so try to keep them to five sentences or less. Short paragraphs are easier for people to scan quickly.

Try to keep sentences to 25 words or less in length. Short, single-clause sentences are often easier to understand and easier to translate. Tools such as the `Hemingway writing app <http://www.hemingwayapp.com/>`_ can be helpful in evaluating readability. Target a readability level of Grade 6.

Tone
~~~~~

Use a direct, impartial tone. Mattermost documentation is written to answer questions and solve problems, not to entertain.

Preferred
  If login fails due to an invalid password, turn Caps Lock off and then re-enter your password.

Avoid
  Failed sign in? No problem! Simply enter the correct password and we'll let you in right away.

Voice
~~~~~~

Use active voice in preference to passive voice. Active voice has the subject of a sentence doing the action. In passive voice, the subject has an action done to it.

Preferred
  The system opens the *Status* pane.

Avoid
  The *Status* pane will be opened by the system.

Person
~~~~~~

Use the second person and avoid the first person.

Preferred
  View the status in the *Status* pane.

Avoid
  We'll view the status in the *Status* pane.

Tense
~~~~~~

Use the present tense.

Preferred
  Sharing this link lets other users view the linked message.

Avoid
  Sharing this link will let other users view the linked message.

Commas
------

Use the serial comma unless doing so decreases clarity and understanding of the sentence.

Preferred
  The cows ran from wolves, coyotes, and mosquitoes.

Avoid
  The cows ran from wolves, coyotes and mosquitoes.

.. _capital:

Capitalization
--------------

Use title case for page titles and section titles.

Title case
  Grammar, Spelling, and Mechanics

Sentence case
  Language and spelling

Numbers
-------

Spell out numbers when the number is the first word in a sentence or is less than or equal to ten, otherwise use numeric digits.

Use commas to make long numbers easier to read.

Preferred
  Three cows ran for six kilometers when they saw 2,300,097 mosquitoes chasing them.

Avoid
  3 cows ran for 6 kilometers when they saw 2300097 mosquitoes chasing them.

Text Formatting
-----------------

Use highlighting of text to visually set off words and phrases that are important to readers. Content that should be highlighted includes file names, UI controls, and window titles. The following table has a comprehensive list with examples.

==================  ==================  ===============================================================
Text                Format              Example
==================  ==================  ===============================================================
Code samples        ``monospace``       See :ref:`syntax-highlight` for an example.
Commands            ``monospace``       "At the command line, type ``sudo apt-get install nginx``."
Directory name      ``monospace``       ``/opt/mattermost``
File name           ``monospace``       ``config.py``
Inline code         ``monospace``       ``fmt.Printf("2 times %d = %d\n", x, y )``
Keystrokes          ``monospace``       "Type ``https://`` in the string field."
Screen output       ``monospace``       See :ref:`literal-blocks` for an example.
Parameter values    ``monospace``       "Set the *auto-config* parameter to ``false``"
Field names         **bold**            "Enter the font in the **Display Font** field."
Clickable control   **bold**            "Click **File > Save**."
Citations           *italic*            "Read the book *Clean Code* by Robert Martin."
Window titles       *italic*            "The *Account Settings* window opens."
User account names  *italic*            "Log in to the *mysql* account."
Parameter names     *italic*            "Set the *auto-config* parameter to ``false``"
Keyboard buttons    Key1+Key2           "Press CTRL+U to upload a file."
Placeholder field   {placeholder}       "Use the URL in the form of {hostname}.mattermost.com/{team}."
==================  ==================  ===============================================================

Bullet Lists
-------------

The list items in a bullet list can be either all complete sentences or all sentence fragments. Don't mix complete sentences and sentence fragments in a single list. Remember that a complete sentence begins with an upper case letter and ends with a punctuation mark.

Numbered Lists and Procedures
-----------------------------

Create numbered lists and procedure steps using arabic numerals for the top-level list and lower case alpha characters for the first nested list. For example:


1. This is the first step.
2. This is the second step.

  a. This is a substep.
  b. This is another substep.

3. This is the third step.

Name-value Groups
-----------------

Use a name-value group instead of a hand-created list.

A name-value group is typically a group of terms and their corresponding definitions, but can also be questions and answers, topics and values, or other name-value groups. In HTML output, a name-value group is represented as a definition list.

Preferred
  Total Users
    The total number of active accounts created on your system. Excludes inactive accounts.
  Total Teams
    The total number of teams created on your system.

Avoid
  **Total Users:** The total number of active accounts created on your system. Excludes inactive accounts.

  **Total Teams:**  The total number of teams created on your system.

Document Linking
------------------

When creating a link to another document in the Mattermost documentation, create a link with a relative URL. To create relative links in reStructuredText, see :ref:`relative-links-in-rst`.

A link with an absolute URL is not as flexible as a relative URL. Relative URLs don't break when the documentation is moved to another host, or if the documentation is hosted on a server that's behind a firewall without access to the Internet.
