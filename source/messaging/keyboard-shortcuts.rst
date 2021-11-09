Keyboard Shortcuts
==================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Keyboard shortcuts perform operations in Mattermost to help you navigate through channels and make a more efficient use of your keyboard. See the `Executing Slash Commands <https://docs.mattermost.com/messaging/executing-slash-commands.html>`__ documentation for alternate ways to help carry out actions with a keyboard instead of a mouse.

To display a list of available keyboard shortcuts, press CTRL+/ (CMD+/ on Mac), or use the ``/shortcuts`` slash command.

.. note::

   Though Mattermost keyboard shortcuts support standard languages and keyboard layouts, they may not work if you use keymapping that overwrites default browser shortcuts.

Mattermost server and product navigation
----------------------------------------

.. tabs::

  .. tab:: Desktop App v5.0 onwards

    Mattermost Desktop App v5.0 introduces additional ways to navigate your Mattermost interface, including server selections, as well as tabs for Channels, Playbooks, and Boards. The following keyboard shortcuts are supported in Mattermost Desktop App only.
    
    +-----------------+-----------------+------------------------------------------------------------------------------------+
    | On Windows      | On Mac          | Description                                                                        |
    +=================+=================+====================================================================================+
    | CTRL+F          | CMD+F           | Move focus to the Search field and search the current channel.                     |
    +-----------------+-----------------+------------------------------------------------------------------------------------+  
    | CTRL+SHIFT+S    | CMD+CTRL+S      | Open the Servers selector, then use UP/DOWN arrows to navigate between servers.    |
    |                 |                 | Use ENTER to select a server.                                                      |
    +-----------------+-----------------+------------------------------------------------------------------------------------+
    || CTRL+SHIFT+1,  || CMD+CTRL+1,    || Navigate to the first server in the Servers list. Replace the number with the     |
    || CTRL+SHIFT+2   || CMD+CTRL+2     || server's position within the server in the Servers list.                          |
    +-----------------+-----------------+------------------------------------------------------------------------------------+
    | CTRL+TAB        | CMD+TAB         | Navigate to the next product tab based on the current product selected.            |
    +-----------------+-----------------+------------------------------------------------------------------------------------+  
    | CTRL+SHIFT+TAB  | CMD+SHIFT+TAB   | Navigate to the previous product tab based on the current product selected.        | 
    +-----------------+-----------------+------------------------------------------------------------------------------------+
    | CTRL+1          | CMD+1           | Navigate to the Channels tab.                                                      |
    +-----------------+-----------------+------------------------------------------------------------------------------------+
    | CTRL+2          | CMD+2           | Navigate to the Boards tab.                                                        |
    +-----------------+-----------------+------------------------------------------------------------------------------------+
    | CTRL+3          | CMD+3           | Navigate to the Playbooks tab.                                                     |
    +-----------------+-----------------+------------------------------------------------------------------------------------+
    | CTRL+TAB        | CMD+TAB         | Navigate to the next product tab based on your current position.                   |
    +-----------------+-----------------+------------------------------------------------------------------------------------+
    | CTRL+SHIFT+TAB  | CMD+SHIFT+TAB   | Navigate to the previous product tab based on your current position.               |
    +-----------------+-----------------+------------------------------------------------------------------------------------+

  .. tab:: Desktop App v4.7 and earlier

    Mattermost Desktop App v4.7 and earlier releases support the following navigation keyboard shortcuts:

    +----------------------------+---------------------------+-------------------------------------------------------------------------------------------------------+
    | On Windows                 | On Mac                    | Description                                                                                           |
    +============================+===========================+=======================================================================================================+
    | CTRL+F                     | CMD+F                     | Move focus to the Search field and search the current channel.                                        |
    +----------------------------+---------------------------+-------------------------------------------------------------------------------------------------------+  
    | CTRL+1, CTRL+2, CTRL+3     | CMD+1                     | Navigate to the first server in the Servers list. Replace the number with the server's tab position.  |
    +----------------------------+---------------------------+-------------------------------------------------------------------------------------------------------+
    | CTRL+TAB                   | CMD+TAB                   | Navigate to the next server tab based on the current server selected.                                 |
    +----------------------------+---------------------------+-------------------------------------------------------------------------------------------------------+
    | CTRL+SHIFT+TAB             | CMD+SHIFT+TAB             | Navigate to the previous server tab based on the current server selected.                             |
    +----------------------------+---------------------------+-------------------------------------------------------------------------------------------------------+  
    | ALT+DOWN                   | OPTION+DOWN               | Next channel or direct message in the channel sidebar.                                                |
    +----------------------------+---------------------------+-------------------------------------------------------------------------------------------------------+

General Mattermost navigation 
-----------------------------

The following keyboard shortcuts are supported in all supported browsers and in the Mattermost Desktop App.

.. note::
  See our `Keyboard Accessibility <https://docs.mattermost.com/messaging/keyboard-accessibility.html>`__ documentation for additional navigation keyboard shortcuts for screen reader users.

+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| On Windows                 | On Mac                    | Description                                                                      |
+============================+===========================+==================================================================================+
| ALT+UP                     | OPTION+UP                 | Previous channel or direct message in the channel sidebar.                       |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| ALT+DOWN                   | OPTION+DOWN               | Next channel or direct message in the channel sidebar.                           |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| ALT+SHIFT+UP               | OPTION+SHIFT+UP           | Previous channel or direct message in the channel sidebar with unread messages.  |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| ALT+SHIFT+DOWN             | OPTION+SHIFT+DOWN         | Next channel or direct message in the channel sidebar with unread messages.      |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+ALT+UP                | CMD+OPTION+UP             | Navigate to the previous team.                                                   |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+ALT+DOWN              | CMD+OPTION+DOWN           | Navigate to the next team.                                                       |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+ALT+[1-9]             | CMD+OPTION+[1-9]          | Navigate to a specific team.                                                     |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+K                     | CMD+K                     | Open a quick channel selector dialog.                                            |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+SHIFT+K               | CMD+SHIFT+K               | Open the Direct Messages dialog.                                                 |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+SHIFT+A               | CMD+SHIFT+A               | Open the Account Settings dialog.                                                |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+SHIFT+M               | CMD+SHIFT+M               | Open recent mentions.                                                            |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+SHIFT+L               | CMD+SHIFT+L               | Set focus to center channel input field.                                         |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+.                     | CMD+.                     | Open and close the right-hand sidebar.                                           |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+
| CTRL+SHIFT+F               | CMD+SHIFT+F               | Move focus to the Search field and search the current channel.                   |
+----------------------------+---------------------------+----------------------------------------------------------------------------------+

Files
-----

The following keyboard shortcuts are supported in all supported browsers and in the Mattermost Desktop App.

+------------+--------+-----------------+
| On Windows | On Mac | Description     |
+============+========+=================+
| CTRL+U     | CMD+U  | Upload a file.  |
+------------+--------+-----------------+

Messages
--------

The following keyboard shortcuts are supported in all supported browsers and in the Mattermost Desktop App.

+----------------------------------+---------------------------------+-----------------------------------------------------------+
| On Windows                       | On Mac                          | Description                                               |
+==================================+=================================+===========================================================+
| CTRL+UP (in empty input field)   | CMD+UP (in empty input field)   | Reprint previous message or slash command you entered.    |
+----------------------------------+---------------------------------+-----------------------------------------------------------+
| CTRL+DOWN (in empty input field) | CMD+DOWN (in empty input field) | Reprint next message or slash command you entered.        |
+----------------------------------+---------------------------------+-----------------------------------------------------------+
| SHIFT+UP (in empty input field)  | SHIFT+UP (in empty input field) | Reply to the most recent message in the current channel.  |
+----------------------------------+---------------------------------+-----------------------------------------------------------+
| UP (in empty input field)        | UP (in empty input field)       | Edit your last message in the current channel.            |
+----------------------------------+---------------------------------+-----------------------------------------------------------+
| @[character]+TAB                 | @[character]+TAB                | Autocomplete @username beginning with [character].        |
+----------------------------------+---------------------------------+-----------------------------------------------------------+
| ~[character]+TAB                 | ~[character]+TAB                | Autocomplete channel beginning with [character].          |
+----------------------------------+---------------------------------+-----------------------------------------------------------+
| :[character]+TAB                 | :[character]+TAB                | Autocomplete emoji beginning with [character].            |
+----------------------------------+---------------------------------+-----------------------------------------------------------+
| CTRL+SHIFT+\\                    | CMD+SHIFT+\\                    | React to last message in channel or thread.               |
+----------------------------------+---------------------------------+-----------------------------------------------------------+

Formatting
----------

The following keyboard shortcuts are supported in all supported browsers and in the Mattermost Desktop App.

+------------+-----------+-------------------------+
| On Windows | On Mac    | Description             |
+============+===========+=========================+
| CTRL+B     | CMD+B     | Bold text.              |
+------------+-----------+-------------------------+
| CTRL+I     | CMD+I     | Italicize text.         |
+------------+-----------+-------------------------+
| CTRL+ALT+K | CMD+ALT+K | Format text as a link.  |
+------------+-----------+-------------------------+

Browser built-in
----------------

The following keyboard shortcuts are supported in all supported browsers and in the Mattermost Desktop App.

+------------------------------+------------------------------+----------------------------------------+
| On Windows                   | On Mac                       | Description                            |
+==============================+==============================+========================================+
| ALT+LEFT                     | CMD+[                        | Previous channel in your history.      |
+------------------------------+------------------------------+----------------------------------------+
| ALT+RIGHT                    | CMD+]                        | Next channel in your history.          |
+------------------------------+------------------------------+----------------------------------------+
| CTRL+PLUS                    | CMD+PLUS                     | Increase font size (zoom in).          |
+------------------------------+------------------------------+----------------------------------------+
| CTRL+MINUS                   | CMD+MINUS                    | Decrease font size (zoom out).         |
+------------------------------+------------------------------+----------------------------------------+
| SHIFT+UP (in input field)    | SHIFT+UP (in input field)    | Highlight text to the previous line.   |
+------------------------------+------------------------------+----------------------------------------+
| SHIFT+DOWN (in input field)  | SHIFT+DOWN (in input field)  | Highlight text to the next line.       |
+------------------------------+------------------------------+----------------------------------------+
| SHIFT+ENTER (in input field) | SHIFT+ENTER (in input field) | Create a new line.                     |
+------------------------------+------------------------------+----------------------------------------+
