Grammar, spelling, and mechanics
================================

To maintain consistency across all Mattermost technical documentation, adhere to the guidelines here.

Language and spelling
---------------------

Write documents in English. Use American spelling.

Paragraphs and sentences
------------------------

Paragraphs should express one idea or topic. Long paragraphs are sometimes difficult to read on screen, so try to keep them to 5 sentences or less. Short paragraphs are easier for people to scan quickly.

Try to keep sentences to 25 words or less in length. Short, single-clause sentences are often easier to understand and easier to translate.

Commas
------

As a general rule, the serial comma results in greater clarity. However, there are always edge cases where a serial comma adds confusion to a sentence. Therefore, the Mattermost documentation will use the following rule for commas:

Use the serial comma unless doing so decreases clarity and understanding of the sentence.

Preferred
  The cows ran from wolves, coyotes, and mosquitoes.

Avoid
  The cows ran from wolves, coyotes and mosquitoes.

Tone
----

Use a direct, impartial tone. Most readers of the documentation are looking for answers and solutions to their problems; they are not looking for entertainment.

Preferred
  If your password is rejected, check to make sure that Caps Lock is off, and then carefully type it in again. 

Avoid
  Failed sign in? No problem! Simply enter the correct password and we'll let you in right away.

.. _capital:

Capitalization
--------------

Use title case for page titles and sentence case for section titles.

Title case
  Grammar, Spelling, and Mechanics

Sentence case
  Language and spelling

Voice
-----

Use active voice in preference to passive voice. Active voice has the subject of a sentence doing the action. In passive voice, the subject has an action done to it. Use passive voice only when you want to emphasize the action more than the subject.

Preferred
  The system opens the *Status* pane.

Avoid
  The *Status* pane is opened by the system.

Person
------

Use the second person and avoid the first person.

Preferred
  You can view the status in the *Status* pane.

Avoid
  We'll view the status in the *Status* pane.

Numbers
-------

Spell out numbers when they are the first word in a sentence, otherwise use numeric digits.

Use commas to make long numbers easier to read.

Preferred
  Three cows ran for 6 kilometers when they saw 2,300,097 mosquitoes chasing them.

Avoid
  3 cows ran for six kilometers when they saw 2300097 mosquitoes chasing them.

Text highlighting
-----------------

Use highlighting of text to visually set off words and phrases that are important to readers. Content that should be highlighted includes file names, UI controls, and window titles. The following table has a comprehensive list with examples. 

==============  ==================  =======================
Text            Highlight           Example
==============  ==================  =======================
file name       ``monospace``       ``config.py``
directory name  ``monospace``       ``/opt/mattermost``
inline code     ``monospace``       ``fmt.Printf("2 times %d = %d\n", x, y )``
code samples    ``monospace``       See :ref:`syntax-highlight` for an example.
screen output   ``monospace``       See :ref:`literal-blocks` for an example.
menu selection  **bold**            "Click **File > Save**."
UI selection    **bold**            "Click **Next**."
field names     **bold**            "Enter the font in the **Display Font** field."
commands        ``monospace``       "At the command line, type ``sudo apt-get install nginx``."
citations       *italic*            "Read the book *Clean Code* by Robert Martin."
window titles   *italic*            "The *Account Settings* window opens."
==============  ==================  =======================

Verb tense
----------

Use the present tense.

Preferred
  Sharing this link lets other users view the linked message.

Avoid
  Sharing this link will let other users view the linked message.

Bullet lists
------------

The list items in a bullet list can be either all complete sentences or all sentence fragments. Don't mix complete sentences and sentence fragments in a single list. Remember that a complete sentence begins with an upper case letter and ends with a punctuation mark.

Numbered lists and procedures
-----------------------------

Create numbered lists and procedure steps using arabic numerals for the top-level list and lower case alpha characters for the first nested list. For example:


1. This is the first step.
2. This is the second step.
  
  a. This is a substep.
  b. This is another substep.
  
3. This is the third step.

Linking to other documents
--------------------------

When creating a link to another document in the Mattermost documentation, create a link with a relative URL.

A link with an absolute URL is not as flexible as a relative URL. Relative URLs don't break when the documentation is moved to another host, or if the documentation is hosted on a server that's behind a firewall without access to the Internet.

To create relative links in reStructuredText, see :ref:`relative-links-in-rst`.
