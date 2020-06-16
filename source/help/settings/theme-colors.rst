.. _theme-colors:

Theme Colors
============

The colors of the Mattermost user interface are customizable in **Account Settings > Display > Theme**. You can import your theme colors from Slack, customize the colors yourself, or choose from four standard themes designed by the Mattermost team.

Any changes you make are applied to all teams that you belong to. In Enterprise Edition, you can choose to apply the theme to the current team only, allowing you to have a different theme for each team.

Standard Themes
---------------

Select **Theme Colors** to choose from four standard themes designed by the Mattermost team. To make custom adjustments on the four standard theme colors, click a standard theme and then select **Custom Theme** to load the standard theme into the custom theme color selectors.

Import Theme from Slack
-----------------------

To import a theme, go to **Preferences > Sidebar Theme** from within Slack, open the custom theme option, copy the theme color vector and then paste it into the *Input Slack Theme* input box in Mattermost. Any theme settings that are not customizable in Slack will default to the “Mattermost” standard theme settings.

Custom Themes
-------------

Observe a live preview as you customize theme colors and then click **Save** to confirm your changes. Discard your changes by exiting the settings window and clicking **Yes, Discard**.

Sidebar Styles
~~~~~~~~~~~~~~

Sidebar BG
  Background color of the Channels pane, and Account and Team settings navigation sidebars.
Sidebar Text
  Text color of read channels in the Channels pane, and tabs in the Account and Team settings navigation sidebar.
Sidebar Header BG
  Background color of the header above the Channels pane and all dialog window headers.
Sidebar Header Text
  Text color of the header above the Channels pane and all dialog window headers.
Sidebar Unread Text
  Text color of unread channels in the Channels pane.
Sidebar Text Hover BG
  Background color behind channel names and settings tabs as you hover over them.
Sidebar Text Active Border
	Color of the rectangular marker on the left side of the Channels pane or Settings sidebar indicating the active channel or tab.
Sidebar Text Active Color
	Text color of the active channel or tab in the Channels pane or Settings sidebar.
Online Indicator
	Color of the online indicator appearing next to team members names in the Direct Messages list.
Away Indicator
	Color of the away indicator appearing next to team members names in the Direct Messages list when they have had no browser activity for 5 minutes.
Do Not Disturb Indicator
	Color of the do not disturb indicator appearing next to team members names in the Direct Messages list.
Mention Jewel BG
	Background color of the jewel indicating unread mentions that appears to the right of the channel name. This is also the background color of the “Unread Posts Below/Above” indicator appearing at the top or bottom of the Channels pane on shorter browser windows.
Mention Jewel Text
	Text color on the mention jewel indicating the number of unread mentions. This is also the text color on the “Unread Posts Below/Above” indicator.

Center Channel Styles
~~~~~~~~~~~~~~~~~~~~~

Center Channel BG
	Color of the center pane, right-hand sidebar and all dialog window backgrounds.
Center Channel Text
	Color of all the text - with the exception of mentions, links, hashtags and code blocks - in the center pane, right-hand sidebar, and dialogs.
New Message Separator
	The new massage separator appears below the last read message when you click into a channel with unread messages.
Mention Highlight BG
	Highlight color behind your words that trigger mentions in the center pane and right-hand sidebar.
Mention Highlight Link
	Text color of your words that trigger mentions in the center pane and right-hand sidebar.
Code Theme
	Background and syntax colors for all code blocks.

Link and Button Styles
~~~~~~~~~~~~~~~~~~~~~~

Link Color
	Text color of all links, hashtags, teammate mentions, and low priority UI buttons.
Button BG
	Color of the rectangular background behind all high priority UI buttons.
Button Text
	Text color appearing on the rectangular background for all high priority UI buttons.

Exporting a Custom Theme
~~~~~~~~~~~~~~~~~~~~~~~~

You can export a theme by copying the "Theme Code" from the Custom Theme menu.

Go to **Account Settings > Display > Custom Theme > Copy and paste to share theme colors** and copy the theme code to export it.

Importing a Custom Theme
~~~~~~~~~~~~~~~~~~~~~~~~

You can import a theme by pasting a "Theme Code" into the Custom Theme menu.

Go to **Account Settings > Display > Custom Theme > Copy and paste to share theme colors** and paste a theme code to import it, then click **Save**.

Custom Theme Examples
~~~~~~~~~~~~~~~~~~~~~

Customize your theme colors and share them with others by copying and pasting theme vectors into the input box. Below are some example themes with their corresponding theme vectors.

GitHub theme
^^^^^^^^^^^^

.. image:: ../../images/theme2.PNG
  :alt: theme2

.. code-block:: none

  {"awayIndicator":"#D4B579","buttonBg":"#66CCCC","buttonColor":"#FFFFFF","centerChannelBg":"#FFFFFF","centerChannelColor":"#444444","codeTheme":"github","linkColor":"#3DADAD","mentionBg":"#66CCCC","mentionColor":"#FFFFFF","mentionHighlightBg":"#3DADAD","mentionHighlightLink":"#FFFFFF","newMessageSeparator":"#F2777A","onlineIndicator":"#52ADAD","sidebarBg":"#F2F0EC","sidebarHeaderBg":"#E8E6DF","sidebarHeaderTextColor":"#424242","sidebarText":"#2E2E2E","sidebarTextActiveBorder":"#66CCCC","sidebarTextActiveColor":"#594545","sidebarTextHoverBg":"#E0E0E0","sidebarUnreadText":"#515151"}

Monokai theme
^^^^^^^^^^^^^

.. image:: ../../images/theme3.PNG
  :alt: theme3

.. code-block:: none

  {"awayIndicator":"#B8B884","buttonBg":"#90AD58","buttonColor":"#FFFFFF","centerChannelBg":"#FFFFFF","centerChannelColor":"#444444","codeTheme":"monokai","linkColor":"#90AD58","mentionBg":"#7E9949","mentionColor":"#FFFFFF","mentionHighlightBg":"#54850C","mentionHighlightLink":"#FFFFFF","newMessageSeparator":"#90AD58","onlineIndicator":"#99CB3F","sidebarBg":"#262626","sidebarHeaderBg":"#363636","sidebarHeaderTextColor":"#FFFFFF","sidebarText":"#FFFFFF","sidebarTextActiveBorder":"#7E9949","sidebarTextActiveColor":"#FFFFFF","sidebarTextHoverBg":"#525252","sidebarUnreadText":"#CCCCCC"}

Solarized Dark theme
^^^^^^^^^^^^^^^^^^^^

.. image:: ../../images/themeSolarizedDark.PNG
  :alt: themeSolarizedDark

.. code-block:: none

  {"awayIndicator":"#E0B333","buttonBg":"#859900","buttonColor":"#fdf6e3","centerChannelBg":"#073642","centerChannelColor":"#93a1a1","codeTheme":"solarized-dark","linkColor":"#268bd2","mentionBj":"#dc322f","mentionColor":"#ffffff","mentionHighlightBg":"#d33682","mentionHighlightLink":"#268bd2","newMessageSeparator":"#cb4b16","onlineIndicator":"#2AA198","sidebarBg":"#073642","sidebarHeaderBg":"#002B36","sidebarHeaderTextColor":"#FDF6E3","sidebarText":"#FDF6E3","sidebarTextActiveBorder":"#d33682","sidebarTextActiveColor":"#FDF6E3","sidebarTextHoverBg":"#CB4B16","sidebarUnreadText":"#FDF6E3","errorTextColor":"#dc322f"}

Gruvbox Dark theme
^^^^^^^^^^^^^^^^^^

.. image:: ../../images/themeGruvboxDark.PNG
  :alt: themeGruvboxDark

.. code-block:: none

  {"awayIndicator":"#fabd2f","buttonBg":"#689d6a","buttonColor":"#ebdbb2","centerChannelBg":"#3c3836","centerChannelColor":"#ebdbb2","codeTheme":"monokai","errorTextColor":"#fb4934","linkColor":"#83a598","mentionBj":"#b16286","mentionColor":"#fbf1c7","mentionHighlightBg":"#d65d0e","mentionHighlightLink":"#fbf1c7","newMessageSeparator":"#d65d0e","onlineIndicator":"#b8bb26","sidebarBg":"#282828","sidebarHeaderBg":"#1d2021","sidebarHeaderTextColor":"#ebdbb2","sidebarText":"#ebdbb2","sidebarTextActiveBorder":"#d65d0e","sidebarTextActiveColor":"#fbf1c7","sidebarTextHoverBg":"#d65d0e","sidebarUnreadText":"#fe8019"}

One Dark
^^^^^^^^

.. image:: ../../images/themeOneDark.png
  :alt: themeOneDark

`GitHub <https://github.com/georgewitteman/one-dark-mattermost>`_

.. code-block:: none

  {"sidebarBg":"#21252b","sidebarText":"#abb2bf","sidebarUnreadText":"#abb2bf","sidebarTextHoverBg":"#3a3f4b","sidebarTextActiveBorder":"#4d78cc","sidebarTextActiveColor":"#d7dae0","sidebarHeaderBg":"#282c34","sidebarHeaderTextColor":"#abb2bf","onlineIndicator":"#98c379","awayIndicator":"#d19a66","dndIndicator":"#be5046","mentionBj":"#98c379","mentionColor":"#ffffff","centerChannelBg":"#282c34","centerChannelColor":"#abb2bf","newMessageSeparator":"#c67add","linkColor":"#61afef","buttonBg":"#4d78cc","buttonColor":"#ffffff","errorTextColor":"#f44747","mentionHighlightBg":"#525a69","mentionHighlightLink":"#61afef","codeTheme":"monokai","mentionBg":"#98c379"}

Discord Dark Theme
^^^^^^^^^^^^^^^^^^

.. image:: ../../images/discordDarkTheme.png
  :alt: Discord Dark Theme

`GitHub <https://github.com/danger89/mattermost-discord-dark>`_

.. code-block:: none

  {"sidebarBg":"#2f3136","sidebarText":"#ffffff","sidebarUnreadText":"#ffffff","sidebarTextHoverBg":"#33363c","sidebarTextActiveBorder":"#66cfa0","sidebarTextActiveColor":"#ffffff","sidebarHeaderBg":"#27292c","sidebarHeaderTextColor":"#ffffff","onlineIndicator":"#43b581","awayIndicator":"#faa61a","dndIndicator":"#f04747","mentionBg":"#6e84d2","mentionBj":"#6e84d2","mentionColor":"#ffffff","centerChannelBg":"#36393f","centerChannelColor":"#dddddd","newMessageSeparator":"#6e84d2","linkColor":"#2095e8","buttonBg":"#43b581","buttonColor":"#ffffff","errorTextColor":"#ff6461","mentionHighlightBg":"#3d414f","mentionHighlightLink":"#6e84d2","codeTheme":"monokai"}