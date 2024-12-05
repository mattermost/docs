Product limits
===============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This page describes some of the product limits that apply to Mattermost, including hard and recommended limits.

.. csv-table::
    :header: "Feature", "Hard Limit", "Recommended Limit"

    ":doc:`Group messages </collaborate/create-channels>`", "8 participants", "If 8 isn't enough, create a private channel"
    ":doc:`Call participants </collaborate/make-calls>`", "Unlimited", "50"
    ":ref:`Custom brand text <configure/custom-branding-tools:custom brand text>`", "500", ""
    ":ref:`Custom site description <configure/custom-branding-tools:site description>`", "1024", ""
    ":ref:`Advanced log output <manage/logging:advanced logging>`", "500 MB file size, 1000 audit records", ""
    ":ref:`Custom status <preferences/set-your-status-availability:set a custom status>`", "100 characters", ""
    ":ref:`Channel name <collaborate/channel-header-purpose:channel name>`", "64 characters", ""
    ":ref:`Channel purpose <collaborate/channel-header-purpose:channel purpose>`", "250 characters", ""
    ":ref:`Channel header <collaborate/channel-header-purpose:channel header>` ", "1024 characters", ""
    ":doc:`Bookmarked links & files </collaborate/manage-channel-bookmarks>`", "50", ""
    ":ref:`Message acknowledgement <collaborate/message-priority:request acknowledgements>` response time", "5 minutes", ""
    ":doc:`Custom user group </collaborate/organize-using-custom-user-groups>` notifications", "256 users per group", ""
    ":ref:`Emoji reactions <collaborate/react-with-emojis-gifs:quick emoji reactions>` per message", "50", ""
    ":ref:`Custom emoji uploads <collaborate/react-with-emojis-gifs:upload custom emojis>`", "6000", ""
    ":ref:`Team description <collaborate/team-settings:team description>`", "50 characters", ""
    ":ref:`SSO user session duration <configure/environment-configuration-settings:session length for sso>`", "30 days", ""
    ":ref:`Mobile user session duration <configure/environment-configuration-settings:session length for mobile>`", "30 days", ""
    ":doc:`Attachments per message </collaborate/share-files-in-messages>` (files or images)", "10", ""
    ":ref:`Attachment file size <collaborate/share-files-in-messages:attachment limits and sizes>`", "100 MB", "Configurable"
    ":ref:`Attachment image file size <collaborate/share-files-in-messages:attachment limits and sizes>`", "253 MB", "Configurable"
    ":ref:`Attachment dimensions <collaborate/share-files-in-messages:attachment limits and sizes>`", "7680 pixels x 4320 pixels", "Configurable"
    ":ref:`Attachment image resolution size <collaborate/share-files-in-messages:attachment limits and sizes>`", "33 MP (mega pixels) or 8K resolution", "Configurable"
    ":doc:`User nickname </preferences/manage-your-profile>` ", "64 characters", ""
    ":doc:`Message length </collaborate/send-messages>`", "16,383 characters", ""
    ":ref:`Teams per deployment <collaborate/organize-using-teams:create a team>`", "10,000", ""
    ":doc:`Users per team </collaborate/invite-people>`", "No enforced limit", "Dependent on infrastructure"