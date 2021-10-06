Keyboard Shortcuts
==================

Keyboard shortcuts perform operations in Mattermost to help you navigate through channels and make a more efficient use of your keyboard. See also `slash commands <https://docs.mattermost.com/messaging/executing-slash-commands.html>`__ for alternate ways to help carry out actions with a keyboard instead of a mouse.

To display a list of available keyboard shortcuts, press CTRL+/ (CMD+/ on Mac), or use the ``/shortcuts`` slash command.

.. note::

   Though Mattermost keyboard shortcuts support standard languages and keyboard layouts, they may not work if you use keymapping that overwrites default browser shortcuts.

Navigation 
----------

.. tabs::

  .. tab:: Desktop App v5.0 onwards

    Mattermost Desktop App v5.0 introduces additional ways to navigate your Mattermost interface, including server selections, as well as tabs for Channels, Playbooks, and Boards.

    **Navigate between Mattermost servers**
    
    +-----------------+-----------------+----------------------------------------------------------------------------------------------------------+
    | On Windows      | On Mac          | Description                                                                                              |
    +=================+=================+==========================================================================================================+
    | CTRL+SHIFT+S    | CMD+CTRL+S      | Opens the Server selector. Use UP/DOWN arrows to navigate between servers. Use ENTER to select a server  |
    +-----------------+-----------------+----------------------------------------------------------------------------------------------------------+
    | CTRL+SHIFT+1    | CMD+CTRL+1      | Navigates to the first server in the Servers list                                                        |
    +-----------------+-----------------+----------------------------------------------------------------------------------------------------------+
    | CTRL+SHIFT+2    | CMD+CTRL+2      | Navigates to the second server in the Servers list                                                       |
    +-----------------+-----------------+----------------------------------------------------------------------------------------------------------+

    .. tip::
      If you have more than 3 or more Mattermost servers, you can continue to increment the shortcut key number based on the server's position within the server in the Servers list.

    **Navigate Between Channels, Boards, and Playbooks**

    +-----------------+-----------------+-------------------------------------------------------------------+
    | On Windows      | On Mac          | Description                                                       |
    +=================+=================+===================================================================+
    | CTRL+1          | CMD+1           | Navigates to the Channels tab                                     |
    +-----------------+-----------------+-------------------------------------------------------------------+
    | CTRL+2          | CMD+2           | Navigates to the Boards tab                                       |
    +-----------------+-----------------+-------------------------------------------------------------------+
    | CTRL+3          | CMD+3           | Navigates to the Playbooks tab                                    |
    +-----------------+-----------------+-------------------------------------------------------------------+
    | CTRL+TAB        | CMD+TAB         | Navigates to the next tab based on your current position          |
    +-----------------+-----------------+-------------------------------------------------------------------+
    | CTRL+SHIFT+TAB  | CMD+SHIFT+TAB   | Navigates to the previous tab based on your current position      |
    +-----------------+-----------------+-------------------------------------------------------------------+

    All existing navigation keyboard shortcuts available in Mattermost v4.7 and earlier releases continue to be supported in Desktop App v5.0.

  .. tab:: Desktop App v4.7 and earlier

    Mattermost Desktop App v4.7 and earlier releases support the following navigation keyboard shortcuts:

    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | On Windows                 | On Mac                    | Description                                                                    |
    +============================+===========================+================================================================================+
    | ALT+UP                     | OPTION+UP                 | Previous channel or direct message in the channel sidebar                      |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | ALT+DOWN                   | OPTION+DOWN               | Next channel or direct message in the channel sidebar                          |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | ALT+SHIFT+UP               | OPTION+SHIFT+UP           | Previous channel or direct message in the channel sidebar with unread messages |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | ALT+SHIFT+DOWN             | OPTION+SHIFT+DOWN         | Next channel or direct message in the channel sidebar with unread messages     |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | CTRL+ALT+UP                | CMD+OPTION+UP             | Previous team                                                                  |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | CTRL+ALT+DOWN              | CMD+OPTION+DOWN           | Next team                                                                      |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | CTRL+ALT+[1-9]             | CMD+OPTION+[1-9]          | Switch to a specific team                                                      |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | CTRL+K                     | CMD+K                     | Open a quick channel switcher dialog                                           |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | CTRL+SHIFT+K               | CMD+SHIFT+K               | Open the Direct Messages dialog                                                |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | CTRL+SHIFT+A               | CMD+SHIFT+A               | Open the Account Settings dialog                                               |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | CTRL+SHIFT+M               | CMD+SHIFT+M               | Open recent mentions                                                           |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | CTRL+SHIFT+L               | CMD+SHIFT+L               | Set focus to center channel input field                                        |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    | CTRL+.                     | CMD+.                     | Open and close the right-hand sidebar                                          |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+
    || CTRL+SHIFT+F (Mobile App) || CMD+SHIFT+F (Mobile App) || Move focus to the Search field and search the current channel                 |
    || CTRL+F (Desktop App)      || CMD+F (Desktop App)      ||                                                                               |
    +----------------------------+---------------------------+--------------------------------------------------------------------------------+

.. note::

  Additional navigation keyboard shortcuts for screen reader users can be found `here <https://docs.mattermost.com/messaging/keyboard-accessibility.html>`_.


Files
-----

+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| On Windows                             | On Mac                                 | Description                                                    |
+========================================+========================================+================================================================+
| CTRL+U                                 | CMD+U                                  | Upload a file                                                  |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+

Messages
--------

+----------------------------------------+----------------------------------------+----------------------------------------------------------------------------+
| On Windows                             | On Mac                                 | Description                                                                |
+========================================+========================================+============================================================================+
| CTRL+UP (in empty input field)         | CMD+UP (in empty input field)          | Reprint previous message or slash command you entered                      |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------------------+
| CTRL+DOWN (in empty input field)       | CMD+DOWN (in empty input field)        | Reprint next message or slash command you entered                          |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------------------+
| SHIFT+UP (in empty input field)        | SHIFT+UP (in empty input field)        | Reply to the most recent message in the current channel                    |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------------------+
| UP (in empty input field)              | UP (in empty input field)              | Edit your last message in the current channel                              |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------------------+
| @[character]+TAB                       | @[character]+TAB                       | Autocomplete @username beginning with [character]                          |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------------------+
| ~[character]+TAB                       | ~[character]+TAB                       | Autocomplete channel beginning with [character]                            |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------------------+
| :[character]+TAB                       | :[character]+TAB                       | Autocomplete emoji beginning with [character]                              |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------------------+
| CTRL+SHIFT+\\                          |  CMD+SHIFT+\\                          | React to last message in channel or thread                                 |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------------------+

Formatting
----------

+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| On Windows                             | On Mac                                 | Description                                                    |
+========================================+========================================+================================================================+
| CTRL+B                                 | CMD+B                                  | Bold text                                                      |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| CTRL+I                                 | CMD+I                                  | Italicize text                                                 |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| CTRL+ALT+K                             | CMD+ALT+K                              | Format text as a link                                          |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+

Browser Built-in
----------------

+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| On Windows                             | On Mac                                 | Description                                                    |
+========================================+========================================+================================================================+
| ALT+LEFT                               | CMD+[                                  | Previous channel in your history                               |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| ALT+RIGHT                              | CMD+]                                  | Next channel in your history                                   |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| CTRL+PLUS                              | CMD+PLUS                               | Increase font size (zoom in)                                   |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| CTRL+MINUS                             | CMD+MINUS                              | Decrease font size (zoom out)                                  |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| SHIFT+UP (in input field)              | SHIFT+UP (in input field)              | Highlight text to the previous line                            |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| SHIFT+DOWN (in input field)            | SHIFT+DOWN (in input field)            | Highlight text to the next line                                |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
| SHIFT+ENTER (in input field)           | SHIFT+ENTER (in input field)           | Create a new line                                              |
+----------------------------------------+----------------------------------------+----------------------------------------------------------------+
