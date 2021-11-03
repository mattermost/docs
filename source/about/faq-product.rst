Product Questions
=================

What features are available on different Mattermost clients?
------------------------------------------------------------

The following chart highlights the end user features of Mattermost and their support across Web, Desktop, and Mobile applications (iOS and Android).

**Legend:**

* X - Full Support
* O - Partial support

.. csv-table::
    :header: "Feature", "Web", "Desktop", "Mobile"

    **MESSAGES**
    "Threaded messages", "X", "X", "X"
    "Markdown", "X", "X", "O"
    "Emojis", "X", "X", "X"
    "Emoji reactions", "X", "X", "X"
    "Viewing emoji reactions", "X", "X", "X"
    "File sharing", "X", "X", "X"
    "@ mentions", "X", "X", "X"
    "Hashtags", "X", "X", "X"
    "Search (with in:, from:, before:, on: and after:)", "X", "X", "X"
    "Search highlighting", "X", "X"
    "View/marking pinned or saved posts", "X", "X", "X"
    "Image link previews", "X", "X", "X"
    "Website previews", "X", "X", "X"
    "Notifications", "X", "X", "X"
    "**CHANNELS**"
    "Create a new channel", "X", "X", "X"
    "Join a channel", "X", "X", "X"
    "Leave a channel", "X", "X", "X"
    "Favorite a channel", "X", "X", "X"
    "Mute a channel", "X", "X", "X"
    "Manage members", "X", "X", "X"
    "Add members", "X", "X", "X"
    "Edit channel", "X", "X", "X"
    "Archive members", "X", "X", "X"
    **TEAMS**
    "Multi-team support for notifications", "X", "X", "X"
    "Team switching", "X", "X", "X"
    "Team-based theming", "X", "X", "X"
    "Team settings", "X", "X"
    "Join existing team", "X", "X", "X"
    "Create a new team", "X", "X"
    "Get team invite link", "X", "X",
    "Add members to team", "X", "X",
    "Manage team members", "X", "X",
    "Leave team", "X", "X"
    **FOCALBOARD**
    "Boards, cards, and views", "X", "O"
    **INTEGRATIONS**
    "Slash commands", "X", "X", "O"
    "Server-side plugins", "X", "X", "X"
    "User interface plugins", "X", "X",
    "Oauth applications", "X", "X", "X"
    "Incoming webhooks", "X", "X", "X"
    "Outgoing webhooks", "X", "X", "X"
    "Message attachments", "X", "X", "X"
    "Message buttons", "X", "X", "X"
    "Message menus", "X", "X", "X"
    **AUTHENTICATION**
    "Email-password login", "X", "X", "X"
    "AD/LDAP", "X", "X", "X"
    "SAML SSO", "X", "X", "X"
    "GitLab SSO", "X", "X", "X"
    "Office 365 SSO", "X", "X", "X"
    "Google SSO", "X", "X",
    **OTHER**
    "Localization for 16 languages", "X", "X", "X"
    "Custom user interface themes", "X", "X", "X"
    "Account settings", "X", "X", "O"

..  _feature-quality-levels:

What feature quality levels does Mattermost have?
--------------------------------------------------

We strive to release viable features. This means that we put in a significant amount of effort to ensure we solve a use case with a high bar for quality. A feature that's viable and meets our criteria for our production quality levels will be released to production.

However, when working on large and complex features or new products, we may need to test them with a high volume of customers and users. For these scenarios, we'll release them as experimental or beta and implement feature flags and/or A/B testing to validate the effectiveness of features prior to production-level release.

We dogfood our features on our community server and provide many configuration options that ensure customers can opt-in when trying experimental or beta features.

This list describes the quality levels of Mattermost features, and what can be expected at each level.

Production Level Quality
- Recommended for use in production environments
- Eligible for commercial support by `Mattermost, Inc. <https://mattermost.com/support/>`__
- Detailed documentation is available
- Tested on several platforms

Beta Level Quality
- Support best-effort only. `Premier Support <https://mattermost.com/support/>`__ is recommended for use in production environments
- Core functionality is stable, but iteration based on feedback is ongoing
- Detailed documentation may not be available yet
- Data schema may not be complete, and may require manual migrations to future versions

Experimental Level Quality
- Not recommended for use in production
- Unknown level of stability
- Feature set covers a small or specific set of use cases. Additional use and edge cases will be added over time
- Data loss can occur as data schemas and configurations may change
- Minimal documentation is available