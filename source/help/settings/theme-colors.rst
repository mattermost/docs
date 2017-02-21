.. _theme-colors:

Theme Colors
============

The colors of the Mattermost user interface are customizable in **Account Settings > Display > Theme**. You can import your theme colors from Slack, customize the colors yourself, or choose from four standard themes designed by the Mattermost team.

In Enterprise Edition, if you belong to multiple teams, you can choose to apply any changes across teams by selecting "Apply New Theme to All Teams" before saving. If this is not selected, any changes are only applied to the current team.

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

You can find sample themes below. You can also find `theme codes shared by the community from the Mattermost community forum. <https://forum.mattermost.org/t/share-your-favorite-mattermost-theme-colors/1330>`_

Custom Theme Examples
~~~~~~~~~~~~~~~~~~~~~

Customize your theme colors and share them with others by copying and pasting theme vectors into the input box. Below are some example themes with their corresponding theme vectors.

GitHub theme
^^^^^^^^^^^^

.. image:: ../../images/theme2.PNG
  :alt: theme2

.. code-block:: none

  Sidebar BG: #2071A7, Sidebar Text: #FFFFFF, Sidebar Header BG: #2F81B7, Sidebar Header Text: #FFFFFF, Sidebar Unread Text: #FFFFFF, Sidebar Text Hover BG: #136197, Sidebar Text Active Border: #7AB0D6, Sidebar Text Active Color: #FFFFFF, Online Indicator: #7DBE00, Away Indicator: #DCBD4E, Mention Jewel BG: #FBFBFB, Mention Jewel Text: #2071A7, Center Channel BG: #F2F4F8, Center Channel Text: #333333, New Message Separator: #FF8800, Mention Highlight BG: #FFF2BB, Link Color: #2F81B7, Mention Highlight Link: #2F81B7, Button BG: #1DACFC, Button Text: #FFFFFF, Code Theme: github

Monokai theme
^^^^^^^^^^^^^

.. image:: ../../images/theme3.PNG
  :alt: theme3

.. code-block:: none

  Sidebar BG: #262626, Sidebar Text: #FFFFFF, Sidebar Header BG: #363636, Sidebar Header Text: #FFFFFF, Sidebar Unread Text: #CCCCCC, Sidebar Text Hover BG: #525252, Sidebar Text Active Border: #7E9949, Sidebar Text Active Color: #FFFFFF, Online Indicator: #99CB3F, Away Indicator: #B8B884, Mention Jewel BG: #7E9949, Mention Jewel Text: #FFFFFF, Center Channel BG: #FFFFFF, Center Channel Text: #444444, New Message Separator: #90AD58, Mention Highlight BG: #54850C, Link Color: #90AD58, Mention Highlight Link: #FFFFFF, Button BG: #90AD58, Button Text: #FFFFFF, Code Theme: monokai

Solarized Dark theme
^^^^^^^^^^^^^^^^^^^^

.. image:: ../../images/theme1.PNG
  :alt: theme1

.. code-block:: none

  Sidebar BG: #4F2F4C, Sidebar Text: #FFFFFF, Sidebar Header BG: #452842, Sidebar Header Text: #FFFFFF, Sidebar Unread Text: #E5E5E5, Sidebar Text Hover BG: #452842, Sidebar Text Active Border: #A65EA0, Sidebar Text Active Color: #FFFFFF, Online Indicator: #52ADAD, Away Indicator: #D4B579, Mention Jewel BG: #F2777A, Mention Jewel Text: #FFFFFF, Center Channel BG: #FFFFFF, Center Channel Text: #444444, New Message Separator: #F2777A, Mention Highlight BG: #F2777A, Link Color: #F2777A, Mention Highlight Link: #FFFFFF, Button BG: #E08D8F, Button Text: #FFFFFF, Code Theme: solarized_dark

Solarized Light theme
^^^^^^^^^^^^^^^^^^^^^

.. image:: ../../images/theme4.PNG
  :alt: theme4

.. code-block:: none

  Sidebar BG: #DE718E, Sidebar Text: #FFFFFF, Sidebar Header BG: #DE6785, Sidebar Header Text: #FFFFFF, Sidebar Unread Text: #FFFFFF, Sidebar Text Hover BG: #CC6983, Sidebar Text Active Border: #43E8D4, Sidebar Text Active Color: #FFFFFF, Online Indicator: #88E0E5, Away Indicator: #CCDB91, Mention Jewel BG: #55A3A8, Mention Jewel Text: #FFFFFF, Center Channel BG: #FFFFFF, Center Channel Text: #444444, New Message Separator: #55A3A8, Mention Highlight BG: #55A3A8, Link Color: #55A3A8, Mention Highlight Link: #FFFFFF, Button BG: #55A3A8, Button Text: #FFFFFF, Code Theme: solarized_light
