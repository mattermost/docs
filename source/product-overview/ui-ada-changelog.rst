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
   * - v11.10
     - (UI) Added a WYSIWYG editor option for message composition, allowing users to compose messages with rich-text formatting while preserving full Markdown round-trip.
   * - v11.10
     - (UI) Added a media gallery layout for posts with multiple images or videos, plus inline frame previews for single videos.
   * - v11.10
     - (UI) Added support for a file upload element type in interactive dialogs.
   * - v11.10
     - (UI) Added support for MM Blocks as a new way to create Interactive Messages.
   * - v11.10
     - (UI) Plugins and integrations can now open stacked child dialogs from within an interactive dialog using the new ``action_button`` element type.
   * - v11.10
     - (UI) Bot accounts, OAuth apps, incoming webhooks, and plugins can now deliver posts silently — visible in the channel without producing notifications, unread badges, or the "New Messages" separator.
   * - v11.10
     - (UI) Bot accounts managed by a plugin now display the managing plugin's ID in the Bot Accounts list instead of a generic "Managed by plugin" label.
   * - v11.10
     - (UI) Added inline plugin metadata to the Plugin Management page and plugin settings page showing the plugin ID, version, and links to the website and release notes when available.
   * - v11.10
     - (UI) The agent selector now respects the configured default agent and remembers your last-selected agent.
   * - v11.10
     - (UI) Mattermost now proactively warns the owner of a personal access token with a direct message from the system bot as the token approaches expiry (7, 3, and 1 days before), so token-backed integrations no longer break without warning.
   * - v11.10
     - (UI) Token owners are now notified by a direct message from the system bot when one of their personal access tokens is removed after expiring.
   * - v11.10
     - (UI) Added a **Regenerate** option to Personal Access Tokens in **Account Settings > Security**.
   * - v11.10
     - (UI) Changed Left-Hand-Side/Right-Hand-Side to only be resizable with the left mouse button.
   * - v11.9
     - (UI) Added zoom and pan support to the image file preview: use the scroll wheel to zoom at the cursor, click-and-drag to pan, and +/-/0 keyboard shortcuts (reported on webapp).
   * - v11.9
     - (UI) Added a toast notification for plugin-rejected file uploads, consistent with the existing notification for rejected downloads.
   * - v11.9
     - (UI) Added a Data Spillage Handling feature discovery page in the System Console for lower-tier licenses.
   * - v11.9
     - (UI) Added clearer validation messaging for invalid user attribute names in the System Console.
   * - v11.9
     - (UI) Incoming webhooks now show information about the last time they were triggered.
   * - v11.9
     - (UI) Threads started by a webhook are no longer highlighted for the user who owns the webhook.
   * - v11.9
     - (UI) Added user setting "Auto-follow threads on channel-wide mentions" (Settings → Notifications). When disabled, @channel/@all/@here mentions no longer force thread membership; users still receive mention notifications but must manually follow the thread.
   * - v11.9
     - (UI) Hardened the web app against crashes caused by components rendered by a plugin.
   * - v11.8
     - (UI) Added a new keyboard shortcut, ``Shift`` + ``ESC``, that marks all channels, threads, and direct messages as read for a team on webapp / desktop app.
   * - v11.8
     - (UI) Added an overflow menu for channel bookmarks when the bookmark bar runs out of space. Bookmarks can be reordered via drag-and-drop between the bar and the overflow menu, or via keyboard (Space to select, arrow keys to move) on webapp. Replaced ``react-beautiful-dnd`` with ``@atlaskit/pragmatic-drag-and-drop``.
   * - v11.8
     - (UI) Added an unread badge to Recaps.
   * - v11.8
     - (UI) Added `managed channel categories <https://docs.mattermost.com/end-user-guide/preferences/customize-your-channel-sidebar.html>`__ for **Channel Admins** to enforce sidebar organization across teams.
   * - v11.8
     - (UI) Added per-channel classification assignment and banner integration for webapp/desktop app.
   * - v11.8
     - (UI) Added `support <https://docs.mattermost.com/administration-guide/manage/admin/user-attributes.html>`__ for **CPA Display Name** for user-facing labels of user attributes.
   * - v11.8
     - (UI) Changed the **Invite People** modal to allow pasting any text, not only valid email formats.
   * - v11.8
     - (UI) Standardized many buttons throughout the app, which may result in minor UX changes.
   * - v11.8
     - (UI) Updated the **Enable Testing Commands** user interface to explicitly warn that ``EnableTesting`` must never be used in production.
   * - v11.8
     - (UI) Changed the mobile view search box to only autofocus when the search button is pressed (reported on mobile browser).
   * - v11.8
     - (UI) Improved the **Default "Report a Problem"** `behavior <https://docs.mattermost.com/administration-guide/configure/site-configuration-settings.html>`__ to open a support ticket via email with metadata for licensed servers, and redirect to the Mattermost forums for free edition in webapp / desktop apps.
   * - v11.8
     - (UI) Added support for system-scoped properties — property fields and values that attach to the Mattermost instance itself.
   * - v11.8
     - (UI) Added the ability to define a property attribute once and reuse it across different object types (e.g., users, channels).
   * - v11.8
     - (UI) Exposed the ``DefaultCategoryName`` to the `user interface <https://docs.mattermost.com/administration-guide/configure/site-configuration-settings.html>`__ so admins can add, edit, and remove it easily.
   * - v11.8
     - (UI) Moved interactive dialog date/datetime properties into ``datetime_config``.
   * - v11.8
     - (UI) When a channel is shared or unshared with a remote, a system message will now be shown.
   * - v11.8
     - (UI) On new installations using Elasticsearch or OpenSearch, search now includes public channels the user is not a member of by default.
   * - v11.8
     - (UI) Added support for incoming webhooks to define a ``root_id`` to create posts in a thread.
   * - v11.8
     - (UI) Updated membership policy user interface copy in the System Console and public channel settings to clarify qualifying-user requirements and auto-add behavior.
   * - v11.8
     - (UI) Hid redundant "Download Apps" links and onboarding download reminders when Mattermost runs inside the Desktop app.
   * - v11.7
     - (UI) Message attachment footers now support full Markdown rendering, including bold, italic, links, and emoji.
   * - v11.7
     - (UI) Changed the **Browse Channels** modal and ``~channel`` autocomplete to prioritize channels with a matching display name.
   * - v11.7
     - (UI) Added an "Open in new tab" button to the **Product Switcher** menu.
   * - v11.7
     - (UI) Substring matching is now allowed when searching channel members in the member sub-panel in a channel.
   * - v11.7
     - (Accessibility) Improved accessibility of thread list menus.
   * - v11.7
     - (UI) Improved autocomplete while typing in Korean and using Firefox.
   * - v11.7
     - (UI) Updated license renewal and expiry notification emails with refreshed branding, copy, and layout.
   * - v11.7
     - (UI) Added the ability to open channels in a separate popout window, with full channel and right-hand side functionality.
   * - v11.7
     - (UI) Dropped support for JS features required by browsers over three years old.
   * - v11.7
     - (UI) Renamed user-visible references from "Custom Profile Attributes" to "User Attributes" across the admin console, error messages, and server translations.
   * - v11.7
     - (UI) Added the `ability to handle <https://docs.mattermost.com/administration-guide/onboard/connected-workspaces.html>`__ from which remotes a channel is shared from the channel settings user interface.
   * - v11.7
     - (UI) Channel banners are now shown in thread views.
   * - v11.6
     - (UI) Added support for Default Agent in suggestions and integrated Agents into the App Bar.
   * - v11.6
     - (UI) Improved the reliability of AI recap summarization by using structured JSON output from the LLM.
   * - v11.6
     - (UI) Added a new feature of creating teams and channels using `anonymous URLs <https://docs.mattermost.com/end-user-guide/collaborate/rename-channels.html>`__ so the channel and team name are not revealed in the URL. Requires Enterprise Advanced license.
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
