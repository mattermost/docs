==========================
Organizing Mattermost
==========================

As Mattermost spreads to dozens, hundreds and thousands of users the importance of organizing channels and teams increases.

This document shares some best practices from various Mattermost deployments. We cover a number of topics:

1. `The importance of channel names`_
2. `How to organize channels`_
3. `Channel naming examples`_

---------------------------------------------------
The importance of channel names
---------------------------------------------------

Channels organize communication in Mattermost.

When naming or renaming channels consider:

- Channel names appear in menus where users select which conversations to join.
- Channel names are unique, and limited to 22 characters to ensure readability on both desktop and mobile devices.
- An additional 128 characters are available to add a "Channel Purpose" visible when users are selecting channels.
- An additional 1024 characters are available for describing the channel in detail in the "Channel Header".

When naming channels, consider the following:

Scoping Names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's natural to start with broadly defined channels and let them divide into more narrow topics as discussions progress.

For example, you might begin with a "Marketing" channel for all things related to marketing. As conversations progress, you might naturally divide that channel into: "Marketing: Website", "Marketing: Social Media", "Marketing: General".

.. tip :: Use colons to separate sections of channel names, rather than `` - `` or `` > `` which require more spaces to display nicely.

As the organization grows, disciplines might also split across business units, products and geographies, with channel names like "US: Marketing" and "UK: Marketing"

.. tip :: If you need to shorten country names, use standard `2-letter country codes <http://www.nationsonline.org/oneworld/country_code_list.htm>`_

As you grow further, you can combine the hierarchies, with formats like ``[SUB-TEAM]: [TOPIC]: [SUB-TOPIC]``. For example: ``US: Mrkt: Website`` and ``UK: Mrkt: Social Media``

.. tip :: Shorten words, particularly categories, by removing vowels, endings and redundant letter sounds. Example: Turn "Marketing" into "Mrkt", and "Project" into "Prjt".

Good naming can take a team up to several thousand channels without causing significant confusion. Eventually every organization hits a limit and an additional team might need to be created on the server to accommodate a very large number of channels.

Navigating to channels using the keyboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another reason why channel names in Mattermost are limited to 22 characters is the common use of keyboard shortcuts to jump quickly to channels.

Users can use CTRL+K to bring up a dialog where they can quickly type in the first few letters of a channel, which triggers auto-complete. Pressing ENTER jumps to the channel directly.

Keeping names clear and short lets users navigate large collections of channels quickly.

.. tip :: Use ALT+SHIFT+UP and ALT+SHIFT+DOWN to move up and down to the next channel with an unread message.

---------------------------------------------------
How to organize channels
---------------------------------------------------

With guidance on how to set channel names, here are different types of channels to consider:

Topic Channels
~~~~~~~~~~~~~~~~~~

Topics are a broad category for organizing discussions. Topics are similar to how a user might create a folder for organizing emails or documents::

    Examples: Recruiting, Interviews, Legal Reviews, Documentation

Users can join and leave topic-based channels, as well as add colleagues to have topic-based discussions.

As teams get larger and the number of channels increase, you may start naming topics in a hierarchy to make them easier to find::

	Example: Legal: Trademarks, Legal: Contracts, Legal: Licensing


Meeting Channels
~~~~~~~~~~~~~~~~~~

Channels are often used to organize regular meetings. Members can add topics as messages, which would be discussed during the regular meeting time::

	Examples: Monday Sales Update, All Hands Meeting

There are a number of built-in features to make meetings in Mattermost easier to manage:

1) Numbered agenda items in title text

You can number and format messages as agenda items to discuss for the next meeting.

Try pasting the following as an example in a channel designated for meetings::

	#### 1) Agenda item example

	Commentary about agenda item to be discussed.

2) Threaded messaging

On an agenda item message, you can select ``[...] > Reply`` to leave comments about an agenda item before or after a meeting to extended discussion.

3) Header links

If you're meeting remotely, add persistent links to your video or audio conferencing solution, like Zoom, Google Hangouts, or BlueJeans in the `channel header <https://docs.mattermost.com/help/settings/channel-settings.html#channel-header>`_.

When it's time to meet, your team can click the conference link to connect.

Sub-Teams
~~~~~~~~~~~~~~~~~~

Sub-teams can include people from the same discipline, project teams, people with the same manager or other groups brought together for a shared purpose::

	Examples: Developers, Marketers, Offsite Organizing Committee, SusanK's Directs

As sub-teams grow beyond a manageable size for one channel, they can sub-divide::

	Examples: US: Developers, UK: Developers, SusanK's Directs, SusanK's Extended Directs

Projects
~~~~~~~~~~~~~~~~~~

Project channels discuss how groups of people can come together to achieve specific outcomes::

	Examples: Logo Design, Localization, Product Launch

Projects are often private channels rather than public channels and are often used to organize a small team around a project brought up in a larger channel. The Project Channel is used to do detailed work, and updates are communicated back to larger channels in many instances.

Location Channels
~~~~~~~~~~~~~~~~~~

If your teams are in different buildings, cities or regions, you can create channels to help people coordinate meetings and get-togethers::

	Examples: Building 10, Palo Alto, Toronto, Delaware

This helps share announcements and discussions relevant to only those locations.

Data Channels
~~~~~~~~~~~~~~~~~~

Sometimes you want to set up integrations to automatically bring data into certain channels. Information like Twitter updates, new or updated support tickets or bug reports, or mentions of your company name in the news can all be made available in channels your team chooses to monitor. Some people might use these channels like a daily newspaper, reading about everything that's happened in the last day.

Others may configure their notifications to only get their attention when their username, or certain key words are mentioned. There's a wide array of options::

	Examples: Bugs, Support Tickets, Twitter, News Mentions

---------------------------------------------------
Channel naming examples
---------------------------------------------------

Here is an example of what a marketer's channels might look like in a small team::

    CHANNELS
    * Recruiting
    * Interviews
    * Marketing
    * Sales
    * All Hands Meeting
    * Town Square
    * Off-Topic

    PRIVATE CHANNELS
    * Website
    * Twitter Marketing
    * Logo Design

    DIRECT MESSAGES
    * [Sales People]
    * [Marketers]
    * [Recruiter]
    * [Manager]

Here is an example of what a marketer's channels might look like if she was working in the Palo Alto, California, office of a large enterprise, working on a product called "Pontoon"::

    CHANNELS
    * Geo: PA: Recruiting
    * Geo: PA: Interviews
    * US: Mrkt: General
    * US: Sales: West Coast
    * US: All Hands
    * Town Square
    * Off-Topic

    PRIVATE CHANNELS
    * Pontoon: Mkrt: Website
    * Pontoon: Mkrt: Twitter
    * Pontoon: Mkrt: Logo Design

    DIRECT MESSAGES
    * [West Coast Sales People]
    * [Marketing Peers]
    * [Recruiter for PA office]
    * [Manager]
