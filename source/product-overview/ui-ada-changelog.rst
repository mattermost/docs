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
   * - v11.6
     - (UI) Added support for Default Agent in suggestions and integrated Agents into the App Bar.
   * - v11.6
     - (UI) Improved the reliability of AI recap summarization by using structured JSON output from the LLM.
   * - v11.6
     - (UI) Added a new feature of creating teams and channels using `anonymous URLs <https://docs.mattermost.com/end-user-guide/collaborate/share-links.html>`__ so the channel and team name are not revealed in the URL. Requires Enterprise Advanced license.
   * - v11.6
     - (UI) Added `popouts <https://docs.mattermost.com/end-user-guide/collaborate/search-for-messages.html#search-for-message>`__ for Recent Mentions, Saved Messages, and Search Results via the right-hand side.
   * - v11.6
     - (UI) The emoji picker on web and Desktop now inserts unicode emoji characters into the message composer instead of shortcode text.
   * - v11.6
     - (UI) Renamed Enterprise Advanced feature Content Flagging to Data Spillage.
   * - v11.6
     - (UI) Added `a contextual note <https://docs.mattermost.com/administration-guide/onboard/sso-google.html#step-3-configure-mattermost-for-google-apps-sso>`__ in Security Settings that explains how Google SSO can synchronize usernames and emails, shown alongside the Sign-in Method details.
   * - v11.6
     - (UI) Renamed ``SlackAttachment`` and ``SlackAttachmentField`` types to ``MessageAttachment`` and ``MessageAttachmentField``. Old names are maintained as deprecated aliases for backward compatibility with plugins.
   * - v11.6
     - (UI) Posts created by integrations using Slack-compatible attachments (webhooks, bots, plugins) are now fully searchable in Elasticsearch. Previously, only the attachment text field was indexed. Now title, pretext, fallback, and field content are also indexed. A bulk re-index is required after upgrade to apply this to existing posts.
   * - v11.6
     - (UI) Added timezone support and manual time entry for Interactive Dialog ``datetime`` fields.
   * - v11.6
     - (UI) Added sub-day relative date patterns (H/M/S) for datetime dialog fields, enabling min/max constraints with hour, minute, and second precision.
   * - v11.5
     - (UI) Added support for `auto-translations <https://docs.mattermost.com/end-user-guide/collaborate/autotranslate-messages.html>`__. Initial Beta release. Requires Enterprise Advanced license.
   * - v11.5
     - (UI) Added the ability for web app plugin code to be loaded asynchronously.
   * - v11.5
     - (UI) `AI Rewrites <https://docs.mattermost.com/end-user-guide/collaborate/send-messages.html#rewrite-messages-with-ai>`__ now includes some context from the most recent messages in the thread to help provide better rewrites.
   * - v11.5
     - (UI) Available AI Agents are now shown in the @-mention autocomplete menu, regardless of channel membership.
   * - v11.5
     - (UI) Added the ability to access channel settings and rename a channel from the channel info right-hand sidebar.
   * - v11.5
     - (UI) Added tooltips to action buttons, and action errors are now displayed.
   * - v11.5
     - (UI) Updated the signup flow to replace the newsletter opt-in with a checkbox to agree to the **Acceptable Use Policy** and **Privacy Policy**.
   * - v11.5
     - (UI) Added back `offline Help documentation <https://docs.mattermost.com/end-user-guide/collaborate/send-messages.html>`__ accessible from the message composer.
   * - v11.5
     - (UI) Added `new icons <https://docs.mattermost.com/end-user-guide/collaborate/channel-types.html#archived-channels>`__ for archived and private channels.
   * - v11.5
     - (Accessibility) Fixed an issue where the profile status menu disappeared at higher zoom levels or at resized window on mobile view.
   * - v11.4
     - (UI) Updated illustrations and visual design for the initial loading screen, preparing workspace flow, IP filtering empty state, and admin console feature discovery panels.
   * - v11.4
     - (UI) Added adjustments to thread and right-hand side plugin pop-out titles.
   * - v11.4
     - (UI) MS Teams and Outlook on mobile no longer display a "Your browser does not support notifications" warning banner when running Mattermost embedded in those apps.
   * - v11.3
     - (UI) Added Korean language support and upgraded Korean translations from Alpha to Official.
   * - v11.3
     - (UI) Added pop-outs for right-hand-side (RHS) plugins.
   * - v11.3
     - (UI) Removed outdated system notices.
   * - v11.3
     - (UI) Removed the Collapsed Reply Threads tutorial.
   * - v11.3
     - (UI) Added support for triggering user mentions using the full-width at-sign (＠) in addition to the standard half-width at-sign (@), improving the experience for users of Japanese input methods.
   * - v11.3
     - (UI) Added the ability to schedule posts in 15-minutes interval.
   * - v11.3
     - (UI) Updated Giphy SDK from 8.1.0 to 10.1.0.
   * - v11.3
     - (UI) Custom Profile Attributes now always return a set of `default attributes <https://docs.mattermost.com/administration-guide/manage/admin/user-attributes.html#add-attributes>`__ if they're not set.
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
