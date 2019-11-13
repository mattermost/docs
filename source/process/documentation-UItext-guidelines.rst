User Interface Text Guidelines
===============================
This is the Mattermost style guide for text used in the Mattermost product. Use these guidelines to ensure text on the Mattermost user interface (UI) is consistent and clear.  These guidelines cover two types of UI text:

- Messages triggered because something happened
- Static text on the user interface

.. note::

Contributions that do not adhere to this style guide will receive edit requests; we'll merge your contribution once you edit the text to conform to these guidelines. You might want to look at the `UX design guidelines`_ as well.

....

.. contents:: 
   :depth: 2

....

General principles for in-product text
---------------------------------------

- Keep in mind that your users are from all over the world. Use words that are clear and easy to understand.
- Be concise.
- Use the active voice, except for these cases:

   - If you'll end up blaming the user. For example, don't say *You entered an incorrect password*. Instead, say *The password is incorrect*.
   - If you're describing what just happened. For example, it's okay to say *Your incoming webhook is set up*.
   - If the subject (the doer of an action) is the Mattermost application itself. For example, it's okay to say *The image is deleted* instead of *The server deleted the image*.
   
- Use the present tense to describe a current state or condition, and the future tense to state something that is very definitely going to happen.
- If you're asking the user to do or not do something, use imperatives (command phrases). For example, say *Do not change the Hostname* instead of saying *It is not recommended to change the Hostname*. Better still, explain what could go wrong if they do or don't do something. For example, say *Do not change the Hostname because if you do so <this bad thing will happen>.*

Guidelines for messages
------------------------

Don't blame the user. Inform them about what happened, explain why it happened, and suggest a way forward.

Try to use complete sentences in your messages. A sentence phrase (an incomplete sentence) might sound okay in English but could present internationalization challenges.

If a message contains variables (tokens):

- Do not use verbs or adjectives as variables.
- Do not create plurals of variables by adding an *s*.
- If the variable is a noun, use a qualifier after the variable. For example, say *The {channel_name} channel was created* instead of saying *The {channel_name} was created*.

Messages can be of the following types: notification, confirmation, warning, and error. The following sections contain guidelines that are specific to each of these types.

Notification messages
~~~~~~~~~~~~~~~~~~~~~~

A notification message is for informing somebody about something that happened. Such messages do not need any user input, and do not prevent a user from continuing to use Mattermost.

- Use either a complete sentence or a sentence phrase. 
- If using a complete sentence, end it with a period.
- Examples:

  - *Member added to channel*
  - *The plug-in was installed.*

Confirmation messages
~~~~~~~~~~~~~~~~~~~~~~

A confirmation message is for asking somebody to confirm whether the immediately preceding command should be proceeded with. The user cannot use Mattermost until a confirmation is given or denied.

- Use complete sentences.
- Include a question that has a Yes/No answer.
- Examples:

  - *Are you sure you want to delete this channel?*
  - *A plug-in with this ID already exists. Would you like to overwrite it?*

Warning messages
~~~~~~~~~~~~~~~~

A warning message is for alerting somebody about something that might go wrong. The user can continue using Mattermost unless the warning message needs an explicit user input.

- Use complete sentences.
- Explain what has happened or can happen, and what can go wrong as a consequence.

- Examples:

  - *The Enterprise license expires in 2 days. If you do not renew it, some features will be disabled on licence expiry.*
  - *If you claim this AD/LDAP account, you will no longer be able to log in with your email.*

Error messages
~~~~~~~~~~~~~~~

An error message is for telling somebody that something went wrong. Errors prevent a user from doing a task or accessing a feature till the error is resolved.

- Use complete sentences.
- If what went wrong isn't obvious, explain in one sentence.
- If a solution or workaround isn't obvious, suggest one.
- Examples:

  - *Messages must have fewer than 120 characters.*
  - *A connection to the marketplace server could not be established. Check your settings on the [System Console](<hyperlink>).*


Guidelines for UI elements
---------------------------
Use this table when writing the text for UI elements such as windows, dialog boxes, labels, and prompts.

.. list-table::
   :widths: 10 30 10 25 25
   :header-rows: 1

   * - Element
     - Image 
     - Capitalization [*]_
     - Phrasing
     - Examples     
   * - Menu
     - |menu.png|
     - Headline style
     - - Noun, noun phrase, or verb
       - No punctuation
       - Not more than three words
       - Action after clicking is obvious, without needing someone to click to discover
     - - *Members*
       - *Account Preferences*
       - *Log Out*
   * - Tooltip
     - |tooltip.png|
     - Sentence style
     - - Sentence fragment or sentence
       - No punctuation
       - Include articles (*a*, *an*, *the*)
       - Keep it short
     - - *Start a Zoom meeting*
       - *Flag for following up*
       - *Remove from this list*
   * - In-field text
     - |field.png|  
     - Sentence style
     - - Sentence fragment, sentence, or word that's an example of a valid entry
       - No punctuation
       - Include articles (*a*, *an*, *the*)
     - - *Add a comment*
       - *Search*
   * - Action button
     - |action.png|
     - Headline style
     - - Verb or verb phrase
       - No longer than 3 words
       - No articles (*a*, *an*, *the*)
       - Exceptions: *OK*, *Yes*, *No*
     - - *Add Comment*
       - *Edit*
   * - Label before a UI element
     - |label_before.png|
     - Sentence style
     - - Noun, verb, or sentence fragment that's the title of the UI element
       - End with a colon where it precedes another UI element such as a radio button or check box
       - Include articles (*a*, *an*, *the*)
     - - *Sign in with:*
       - *Other words, separated by commas:*
   * - Label after a UI element
     - |label_after.png|
     - Sentence style
     - - Noun, verb, or sentence fragment
       - No punctuation
       - Brief (lengthier explanations belong to help text)
     - - *Channels grouped by type*
       - *Alphabetically*
   * - Help text
     - |help.png|
     - Sentence style
     - Complete sentences, with punctuation
     - - *You can add 20 more people.*
       - *People are invited automatically to join the channel.*
   * - Title
     - |title.png|
     - Headline style
     - - Sentence fragment or sentence
       - No punctuation
     - - *Notification Preferences for Channel*
       - *Contributors*

.. [*] For headline style, capitalize all words except those with 3 letters or fewer, articles (*a*, *an*, *the*), prepositions (*on*, *to*, *in*, *from*, *of*), and coordinating conjunctions (*and*, *but*, *or*, *for*). Despite these exceptions, always capitalize the first and last word. For sentence style, capitalize only the first word.

Cheatsheet: UI text
-----------------------
|cheatsheet.png|

.. |menu.png| image:: ./images/menu.png
  :alt: menu
.. |tooltip.png| image:: ./images/tooltip.png
  :alt: tooltip
.. |field.png| image:: ./images/field.png
  :alt: in-field text
.. |action.png| image:: ./images/action.png
  :alt: action button
.. |label_before.png| image:: ./images/label_before.png
  :alt: labels before a UI element
.. |label_after.png| image:: ./images/label_after.png
  :alt: labels after a UI element
.. |help.png| image:: ./images/help.png
  :alt: help text
.. |title.png| image:: ./images/title.png
  :alt: title
.. |cheatsheet.png| image:: ./images/cheatsheet.png
  :alt: cheatsheet for punctuation and capitalization
.. _UX design guidelines: https://docs.mattermost.com/developer/fx-guidelines.html#design-guidelines
