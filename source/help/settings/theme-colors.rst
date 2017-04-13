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

.. image:: ../../images/theme1.PNG
  :alt: theme1

.. code-block:: none

  {"awayIndicator":"#D4B579","buttonBg":"#E08D8F","buttonColor":"#FFFFFF","centerChannelBg":"#FFFFFF","centerChannelColor":"#444444","codeTheme":"solarized_dark","linkColor":"#F2777A","mentionBg":"#F2777A","mentionColor":"#FFFFFF","mentionHighlightBg":"#F2777A","mentionHighlightLink":"#FFFFFF","newMessageSeparator":"#F2777A","onlineIndicator":"#52ADAD","sidebarBg":"#4F2F4C","sidebarHeaderBg":"#452842","sidebarHeaderTextColor":"#FFFFFF","sidebarText":"#FFFFFF","sidebarTextActiveBorder":"#A65EA0","sidebarTextActiveColor":"#FFFFFF","sidebarTextHoverBg":"#452842","sidebarUnreadText":"#E5E5E5"}

Solarized Light theme
^^^^^^^^^^^^^^^^^^^^^

.. image:: ../../images/theme4.PNG
  :alt: theme4

.. code-block:: none

  {"awayIndicator":"#CCDB91","buttonBg":"#55A3A8","buttonColor":"#FFFFFF","centerChannelBg":"#FFFFFF","centerChannelColor":"#444444","codeTheme":"solarized_light","linkColor":"#55A3A8","mentionBg":"#55A3A8","mentionColor":"#FFFFFF","mentionHighlightBg":"#55A3A8","mentionHighlightLink":"#FFFFFF","newMessageSeparator":"#55A3A8","onlineIndicator":"#88E0E5","sidebarBg":"#DE718E","sidebarHeaderBg":"#DE6785","sidebarHeaderTextColor":"#FFFFFF","sidebarText":"#FFFFFF","sidebarTextActiveBorder":"#43E8D4","sidebarTextActiveColor":"#FFFFFF","sidebarTextHoverBg":"#CC6983","sidebarUnreadText":"#FFFFFF"}
