Enable Content Flagging
========================

.. include:: ../../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

Content flagging helps prevent accidental data spillage and helps system administrators respond quickly to potential leaks without disrupting collaboration. Enabling this feature empowers Mattermost users to report messages that may contain sensitive, regulated, or inappropriate information, and enables designated content reviewers to assess and take appropriate action by removing or dismissing flagged messages.

By making every team member a first line of defense against sensitive-data exposure, content flagging strengthens mission-critical, secure deployments and supports compliance with organizational and regulatory data-handling standards.

Before you begin
----------------

You must be a System Admin in Mattermost. You need to identify who will be content reviewers for flagged messages, and you need to decide whether flagged messages should be hidden from users in Mattermost while under review.

Enable
-------

Content flagging isn't enabled by default. To enable content flagging:

1. Go to **System Console > Site Configuration > Content Flagging**. 
2. Set **Enable content flagging** to **True**.

Alternatively, you can configure content flagging via the :ref:`config.json file or through environment variables <administration-guide/configure/site-configuration-settings:content flagging>`.

Configure
---------

1. Under **Content Reviewers**, define who should review flagged content:

   - **Same reviewers for all teams**: Set to **True** to apply one global reviewer list across all teams, or **False** to configure reviewers per team.
   - **Reviewers**: Start typing to search for users to assign as content reviewers.

   .. important::

      Choose reviewers carefully. Assigning reviewer roles grants access to potentially sensitive information and may expose data from private channels.

      - A global reviewer can view flagged messages from all teams and channels, including private channels they’re not a member of.
      - Team-specific reviewers can view flagged messages from their assigned teams, including private channels within those teams they're not members of.

   - **Additional reviewers**: Optionally include:

     - **System Administrators**: System admins receive flagged messages for all teams they are part of.
     - **Team Administrators**: Team admins receive flagged messages for their respective teams.

2. Under **Notification Settings**, specify who receives updates at each stage of the flagging workflow when content is flagged or reviewed:

   - **Notify when content is flagged**: Reviewer(s), Author.
   - **Notify when a reviewer is assigned**: Reviewer(s).
   - **Notify when content is removed**: Reviewer(s), Author, Reporter.
   - **Notify on dismissal**: Reviewer(s), Author, Reporter.

   All notifications are sent via the **content-review** bot as direct messages.

3. Under **Additional Settings**, configure how the flagging workflow behaves:

   - **Reasons for flagging**: Define the preset categories that appear in the flagging dialog for users (for example: **Inappropriate content**, **Sensitive data**, **Security concern**, **Harassment or abuse**, **Spam or phishing**).
   - **Require reporters to add comment**: Set to **True** to require users to add a short explanation when flagging a message.
   - **Require reviewers to add comment**: Set to **True** to require reviewers to add a comment when resolving a flag.
   - **Hide message from channel while it is being reviewed**: Set to **True** to automatically hide flagged messages from the channel until reviews are complete. If a root post is flagged, the entire thread is hidden.

.. tip::
   We recommend enabling **Hide message from channel while it is being reviewed** and require comments from both reporters and reviewers to maintain transparency, accountability, and an auditable record of actions.

Monitor flagged messages
------------------------

When :doc:`a user flags a message </end-user-guide/collaborate/flag-messages>`, the **content-review** bot sends a direct message to all content reviewers.

Direct messages from the **content-review** bot is a centralized moderation queue, where reviewers can view, assign, and act on flagged messages without leaving Mattermost. Reviewers can use it to monitor potential data spills, coordinate response, and maintain an auditable record of review activity.

Each flagged message appears as a card-formatted message that includes:

- **Flagged by**: The user who reported the message.
- **Status**: The current state of the review. All flagged content starts in **Pending** status.
- **Reason**: The reason selected by the reporter (for example, **Sensitive data**, **Inappropriate content**).
- **Message preview**: A snippet of the flagged message, including the author, timestamp, and original channel.
- **Reviewer**: The user currently assigned to review the message (initially **Unassigned**).
- **Channel**: The name of the channel where the message was originally posted.
- **Team**: The team context for the flagged message.
- **Comment**: Any reporter-provided context.
- **Post ID**: The system identifier for the original message for auditing purposes.

Reviewers can select **View details** to take action as follows:

- Assign a **Reviewer** responsible for reviewing the flagged message.
- **Remove message**: Permanently delete the flagged message from its original channel for all users. The status of the flagged message changes to **Removed**.
- **Keep message**: Dismiss the flag and restore the message if it was hidden. The status of the flagged message changes to **Retained**.
- **Add a comment**: Record the reason for the decision when required.

Once an action is taken, the **Status** field updates automatically. The **content-review** bot sends follow-up notifications to the reporter, author, and other reviewers based on how content flagging is configured.

Deleted messages
~~~~~~~~~~~~~~~~

When a reviewer permanently removes a flagged message, the message and all associated data are deleted from the database and can't be recovered, including:

- Message content and properties: The text of the message and any associated post properties.
- File metadata: Information about files attached to the message (e.g., file names, IDs, and links to storage).
- File metadata from edit history: Information about files attached to earlier versions of the message.
- Edit history: All previous versions of the message and their timestamps.
- Uploaded files: The actual files stored in Mattermost’s file storage (local, S3, etc.).
- Priority data: Any message priority or importance settings.
- Acknowledgements: Records of users who acknowledged the message.
- Reminders: Any reminders created for the message.

Best practice recommendations
-----------------------------

Before rolling out content flagging organization-wide, we recommend communicating that the feature protects both users and the organization from accidental data spillage. Start with a pilot team to validate reviewer notifications and workflows, integrate the process with existing data-handling or incident-response playbooks, and require reporter and reviewer comments to ensure every decision is transparent and auditable.