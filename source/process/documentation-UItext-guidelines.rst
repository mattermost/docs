In-Code Text Guidelines
============================
This is the Mattermost style guide for in-code text. Use it as a reference to ensure that the text on the Mattermost user interface (UI) is consistent and clear.

Note

These guidelines are not intended to slow down or otherwise impede contributions, which are always welcome. No contribution will be rejected due to non-conforming style, although it might be edited.

....

.. contents:: 
   :depth: 2

....

UI elements
-----------------------------
Use this table when writing the text for UI elements such as windows and dialog boxes.

.. list-table::
   :widths: 10 30 10 15 35
   :header-rows: 1

   * - Element
     - Image 
     - Capitalization
     - Phrasing
     - Examples     
   * - Menu
     - |menu.png|
     - Headline
     - - Noun, noun phrase, or verb
       - No punctuation
       - Not more than three words
     - - *Members*
       - *Account Preferences*
       - *Log Out*
   * - Tooltip
     - |tooltip.png|
     - Sentence
     - - Sentence fragment or sentence
       - No punctuation
       - Include articles (*a*, *an*, *the*)
     - - *Start a Zoom meeting*
       - *Flag for following up*
       - *Remove from this list*
   * - In-field text
     - |field.png|  
     - Sentence
     - - Sentence fragment, sentence, or word
       - No punctuation
       - Include articles (*a*, *an*, *the*)
     - - *Add a comment*
       - *Search*
   * - Action button
     - |action.png|
     - Headline
     - - Verb or verb phrase
       - No articles (*a*, *an*, *the*)
       - Exceptions: *OK*, *Yes*, *No*
     - - *Add Comment*
       - *Edit*
   * - Label before a UI element
     - |label_before.png|
     - Sentence
     - - Noun, verb, or sentence fragment
       - End with a colon
       - Include articles (*a*, *an*, *the*)
     - - *Sign in with:*
       - *Other words, separated by commas:*
   * - Label after a UI element
     - |label_after.png|
     - Sentence
     - - Noun, verb, or sentence fragment
       - No punctuation
     - - *Channels grouped by type*
       - *Alphabetically*
   * - Help text
     - |help.png|
     - Sentence
     - Complete sentences, with punctuation
     - - *You can add 20 more people.*
       - *People are invited automatically to join the channel.*
   * - Title
     - |title.png|
     - Headline
     - - Sentence fragment or sentence
       - No punctuation
     - - *Notification Preferences for Channel*
       - *Contributors*

Messages
--------

In general, do not blame the user. Inform, explain, and suggest.

If a message contains variables (tokens): 

- Do not use verbs or adjectives as variables.
- Do not create plurals of variables by adding an *s*.
- If the variable is a noun, use a qualifier after the variable. For example, say *The {channel_name} channel was created* instead of saying *The {channel_name} was created*

Notifications
~~~~~~~~~~~~~~

A notification message is for informing somebody about something that happened. Such messages do not need any user input, and do not prevent a user from continuing to use Mattermost.

- Use either a complete sentence or a sentence phrase. 
- If using a complete sentence, end it with a period.
- Examples:

  - *Member added to channel*
  - *The plug-in was installed.*

Confirmations
~~~~~~~~~~~~~~

A confirmation message is for asking somebody to confirm whether the immediately preceding command should be proceeded with. The user cannot use Mattermost until a confirmation is given or denied.

- Use complete sentences.
- Include a question that has a Yes/No answer.
- Examples:

  - *Are you sure you want to delete this channel?*
  - *A plug-in with this ID already exists. Would you like to overwrite it?*

Warnings
~~~~~~~~~

A warning message is for alerting somebody about something that might go wrong. The user can continue using Mattermost unless the warning message needs an explicit user input.

- Use complete sentences.
- Explain what has happened or can happen, and what can go wrong as a consequence.
- If the message contains a question, phrase it in such a manner so that it has a Yes/No answer (unless you have specific action buttons for the message).

- Examples:

  - *The Enterprise licence will expire in 2 days. If you do not renew it, some features will be disabled on licence expiry.*
  - *If you claim this AD/LDAP account, you will no longer be able to log in with your email. Do you want to continue?*

Errors
~~~~~~~

An error message is for telling somebody that something went wrong. Errors prevent a user from doing a task or accessing a feature till the error is resolved.

- Use complete sentences.
- If what went wrong isn't obvious, explain in one sentence.
- If a solution or workaround isn't obvious, suggest one.
- Examples:

  - *This message is too long. Shorten it to 120 characters.*
  - *The passwords do not match.*
   

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
