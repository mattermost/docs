====================================
How to Update Integrations Directory
====================================

This document outlines the internal process for updating https://integrations.mattermost.com/.

New integrations get submitted in the `Integrations and Apps channel <https://community-daily.mattermost.com/core/channels/integrations>`_
via `this form <https://spinpunch.wufoo.com/forms/mattermost-integrations-and-installers/>`_.

Initial Steps
--------------

1. Go to https://mmapps.wpengine.com/wp-login.php and log in with your account. 
If you don’t have an account, ask Marketing for access.

2. Navigate to “Posts” on the left hand sidebar. Click “Add New” below “Posts” 
when adding a new integration.

Integration Elements
--------------------

The following includes guidelines for specific elements of an integration.

Title
^^^^^^

Short title of the integration, effectively its name. Examples:

 - Facebook
 - Twitter
 - BigBlueButton Plugin

Note: If the integration is a plugin, please include “Plugin” in the title.

   - To figure out if an integration is a plugin, check its install instructions to see what it refers to. E.g. if it says to configure it as a webhook in Mattermost and as a plugin in Jenkins, it's a plugin in Jenkins, not in Mattermost.

Note: If it's an Amazon related integration, include both the official and short form in the title ("Amazon" and "AWS"). E.g. "Amazon AWS SNS Plugin".

Description
^^^^^^^^^^^^

Short description of the integration, typically provided by the integration creator. 

You can also usually find a description of the integration on the GitHub project. 

Don’t end the description with a period.

Author
^^^^^^^

GitHub author of the integration. 

Always a full name, or a company name, depending on their GitHub profile.

If neither a full name or a company name is public on their GitHub profile, using their GitHub username is also fine.

Language
^^^^^^^^^

Programming language of the integration. 

Find this by clicking on the coloured bar in the GitHub project, below the header containing “commits, branches, releases, contributors”, and choose the language(s) higher than 30%.

Tips:

 - Don't add "Makefile" unless it's the only language on the repo.
 - Use "Go" instead of "Golang".
 - If there is no language, set to "N/A" instead of leaving it blank.

License
^^^^^^^^

This is typically found in the GitHub project, on the file named “LICENSE”. The license file should specify the license type.

Note: License must be compatible with Apache 2.0 (https://apache.org/legal/resolved.html#category-a). E.g. not GPLv3, nor APGLv3. If not compatible with Apache 2.0, do not add the integration to the website.

For formatting, write "Apache 2.0", "BSD 2-Clause" or "BSD 3-Clause".

When the integration is not open source, mark the license as "N/A - not open source".

Download URL
^^^^^^^^^^^^^

Link to the README file on the GitHub project which typically includes install instructions.

Source Code URL
^^^^^^^^^^^^^^^^

Link to their GitHub repo.

Date Published
^^^^^^^^^^^^^^^

Typically found in the GitHub project by selecting the “Releases” tab in the header. Navigate to the oldest release, and use its date as the “Date Published” field.

If there are no releases, go to the “Contributors” tab in the header, and select the start date as the “Date Published” field.

Categories
^^^^^^^^^^^

Choose the categories you feel best fit the integration. If you’re uncertain, compare what categories are used by Slack, Atlassian and/or Salesforce (see list below). If still uncertain, ask Integrations PM.

 - https://marketplace.atlassian.com/  
 - https://slack.com/apps 
 - https://appexchange.salesforce.com/ 

Featured Image
^^^^^^^^^^^^^^

This is a logo of the integration, e.g. Facebook logo for Facebook integration. 

Use Twitter to find official logos if none are provided by the integration creator. If there is no good icon/logo to use, go to https://mattermost.wayfx.com/0ddc9bpne/p/45193 and choose an icon that best fits the integration type.

Use an icon that's at least 80x80px in size.

Date Last Updated
^^^^^^^^^^^^^^^^^

Check the date of "Last Commit" on the repository.

Guidelines
-----------

1. License of the integration must be compatible with Apache 2.0 (https://apache.org/legal/resolved.html#category-a). E.g. not GPLv3, nor APGLv3. Only exception is if the integration is not open source.
2. Integration must have been updated in the last 12 months.
3. Every integration link must be related to Mattermost. Especially if the integration is not open source, it should be obvious to users that it's related to Mattermost.

Marketing
---------

1. Add integration/plugin creators to changelog’s list of contributors.

 - E.g. for March release, add any new ones from February.

2. Post a tweet for all new integrations.

 - E.g. https://twitter.com/Mattermost/status/1102709312231596032.
 
Announcement
------------

a) Once the integration entry has been added to the directory, please reply back in the Integrations channel with a screenshot of the entry that was added, a link to its install guide, and an at-mention for Integrations PM. Example:

  .. code-block:: none
  
    [@-username] Standup Raven Plugin added to https://integrations.mattermost.com

    https://github.com/standup-raven/standup-raven/blob/master/README.md

    [Attached image]

b) Once Integrations PM has acknowledged, please re-post to `Announcements channel <https://community.mattermost.com/private-core/channels/announcements>`_.

Release Date T-0
------------------

1. Add integrations with more than 50 stars to the “New and Noteworthy” category.
2. Add 8 most recent integrations to the “New and Noteworthy” category.
  - Oldest on this list should be removed when a new integration is added.
3. Update the Date Last Updated for all integrations.
4. Remove any integrations that haven’t been updated in the last 12 months. (Note: keep this relaxed. Some older ones are still important to keep.)
5. Add any new plugins from https://github.com/mattermost/mattermost-plugins.
6. Ask Integrations PM if any integrations are good to add or remove from the "Staff Picks" section.
 
Note: These integrations should be kept in the "New and Noteworthy" category:

 - https://www.pagerduty.com/docs/guides/mattermost-integration-guide/
 - https://marketplace.atlassian.com/apps/1215055/slack-for-confluence?hosting=cloud&tab=overview
 - https://github.com/cpanato/mattermost-plugin-statuspage
 - https://github.com/Lujeni/matterllo
 - https://docs.opsgenie.com/docs/mattermost-integration
 - https://github.com/blindsidenetworks/mattermost-plugin-bigbluebutton
 - https://github.com/cvitter/mattermost-bitbucket-bridge
 - https://github.com/42wim/matterbridge
 - https://github.com/loafoe/hubot-matteruser
 - https://github.com/mattermost/mattermost-plugin-github
 - https://github.com/mattermost/mattermost-bot-sample-golang
 - https://github.com/mattermost/mattermost-plugin-jira
 - https://github.com/mattermost/mattermost-plugin-zoom 
