UI & ADA Changelog
==================

This changelog tracks User Interface (UI) and Accessibility (ADA) changes across Mattermost releases. Administrators can use this page to easily see what changed in the UI from their current version to the one they're upgrading to, and track ADA improvements release to release.

Changelog
--------------

.. list-table::
   :header-rows: 1
   :widths: 10 70

   * - Version
     - Change Description
   * - v11.5
     - (UI) Added support for auto-translations. Initial Beta release. Requires Enterprise Advanced license `MM-64493 <https://mattermost.atlassian.net/browse/MM-64493>`__.
   * - v11.5
     - (UI) Added the ability for web app plugin code to be loaded asynchronously `MM-67538 <https://mattermost.atlassian.net/browse/MM-67538>`__.
   * - v11.5
     - (UI) AI Rewrites now includes some context from the most recent messages in the thread to help provide better rewrites.
   * - v11.5
     - (UI) Available AI Agents are now shown in the @-mention autocomplete menu, regardless of channel membership `MM-67118 <https://mattermost.atlassian.net/browse/MM-67118>`__.
   * - v11.5
     - (UI) Added the ability to access channel settings and rename a channel from the channel info right-hand sidebar `MM-66862 <https://mattermost.atlassian.net/browse/MM-66862>`__.
   * - v11.5
     - (UI) Added tooltips to action buttons, and action errors are now displayed `MM-65023 <https://mattermost.atlassian.net/browse/MM-65023>`__.
   * - v11.5
     - (UI) Updated the signup flow to replace the newsletter opt-in with a checkbox to agree to the **Acceptable Use Policy** and **Privacy Policy** `MM-67030 <https://mattermost.atlassian.net/browse/MM-67030>`__.
   * - v11.5
     - (UI) Added back offline **Help** documentation accessible from the message composer `MM-61383 <https://mattermost.atlassian.net/browse/MM-61383>`__.
   * - v11.5
     - (UI) Added new icons for archived and private channels `MM-66561 <https://mattermost.atlassian.net/browse/MM-66561>`__.
   * - v11.5
     - (Accessibility) Fixed an issue where the profile status menu disappeared at higher zoom levels or at resized window on mobile view `MM-64655 <https://mattermost.atlassian.net/browse/MM-64655>`__.
   * - v11.4
     - (UI) Updated illustrations and visual design for the initial loading screen, preparing workspace flow, IP filtering empty state, and admin console feature discovery panels `MM-67081 <https://mattermost.atlassian.net/browse/MM-67081>`__.
   * - v11.4
     - (UI) Added adjustments to thread and right-hand side plugin pop-out titles `MM-66898 <https://mattermost.atlassian.net/browse/MM-66898>`__.
   * - v11.4
     - (UI) MS Teams and Outlook on mobile no longer display a "Your browser does not support notifications" warning banner when running Mattermost embedded in those apps `MM-66769 <https://mattermost.atlassian.net/browse/MM-66769>`__.
   * - v11.3
     - (UI) Added Korean language support and upgraded Korean translations from Alpha to Official.
   * - v11.3
     - (UI) Added pop-outs for right-hand-side (RHS) plugins `MM-66875 <https://mattermost.atlassian.net/browse/MM-66875>`__.
   * - v11.3
     - (UI) Removed outdated system notices `MM-65785 <https://mattermost.atlassian.net/browse/MM-65785>`__.
   * - v11.3
     - (UI) Removed the Collapsed Reply Threads tutorial `MM-66470 <https://mattermost.atlassian.net/browse/MM-66470>`__.
   * - v11.3
     - (UI) Added support for triggering user mentions using the full-width at-sign (＠) in addition to the standard half-width at-sign (@), improving the experience for users of Japanese input methods.
   * - v11.3
     - (UI) Added the ability to schedule posts in 15-minutes interval `MM-66859 <https://mattermost.atlassian.net/browse/MM-66859>`__.
   * - v11.3
     - (UI) Updated Giphy SDK from 8.1.0 to 10.1.0 `MM-66374 <https://mattermost.atlassian.net/browse/MM-66374>`__.
   * - v11.3
     - (UI) Custom Profile Attributes now always return a set of `default attributes <https://docs.mattermost.com/administration-guide/manage/admin/user-attributes.html#add-attributes>`__ if they're not set `MM-66460 <https://mattermost.atlassian.net/browse/MM-66460>`__.
   * - v11.3
     - (UI) Added a new webapp plugin component ``registerSidebarBrowseOrAddChannelMenuComponent``, which allows users to add options to the ``BrowseOrCreateChannel`` menu. 
   * - v11.2
     - (UI) Enabled `thread popouts <https://docs.mattermost.com/end-user-guide/collaborate/organize-conversations.html#start-or-reply-to-threads>`__ in the browser.
   * - v11.2
     - (UI) Reduced the channel banner height.
   * - v11.2
     - (UI) Improved license and plan name clarity throughout the user interface. License settings and the **About** modal now display specific plan names (Professional, Enterprise, Entry) instead of the generic "Enterprise Edition" label, reducing confusion between edition and plan terminology.
   * - v11.1
     - (UI) Added support for standalone windows pop-out. Threads can now be popped out to its own window in Desktop.
   * - v11.1
     - (UI) The desktop app version is now shown on the **About** modal, allowing clicking to copy both the server and desktop app versions.
   * - v11.1
     - (UI) Removed Mattermost MS Teams Sync plugin from pre-packaged plugins.
   * - v11.1
     - (UI) Downgraded French language support from Beta to Alpha.
   * - v11.0
     - (UI) Removed Playbooks v1 from pre-packaged plugins.
   * - v11.0
     - (UI) Updated the library used for customizing scrollbars.
   * - v11.0
     - (UI) Increased page size when retrieving posts in channels with high number of hidden messages.
