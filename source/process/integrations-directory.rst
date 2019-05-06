====================================
How to Update Integrations Directory
====================================

This document outlines the process for updating https://integrations.mattermost.com/.

New integrations get submitted in the `Integrations & Apps channel <https://community-daily.mattermost.com/core/channels/integrations>`_
via `this form <https://spinpunch.wufoo.com/forms/mattermost-integrations-and-installers/>`_.

Initial Steps
--------------

1. Go to https://mmapps.wpengine.com/wp-login.php and log in with your account. 
If you don’t have an account, ask Marketing for access.

2. Navigate to “Posts” on the left hand sidebar. Click “Add New” below “Posts” 
when adding a new integration.

Integration Elements
--------------------

The following include guidelines for specific elements of an integration.

Title
^^^^^^

This is a short title of the integration, effectively its name. Samples:

 - Facebook
 - Twitter
 - BigBlueButton Plugin

Note: If the integration is a plugin, please include “Plugin” in the title. 
   - To figure out if an integration is a plugin, check its install instructions to see what it refers to. E.g. if it says to configure it as a webhook in Mattermost and as a plugin in Jenkins, it's a plugin in Jenkins, not in Mattermost.

Note: Amazon AWS SNS Plugin - this is named "Amazon SNS" officially, but "AWS" is it's short form, so include both official and short form in the title.

Description
^^^^^^^^^^^^

This is a short description of the integration, typically provided by the integration creator. 
You can usually find a description of the integration on the GitHub project. 

Don’t end the description with a period.

Author
^^^^^^^

GitHub author of the integration. Always a full name, or a company name, depending on their GitHub profile.
If neither is public on their GitHub profile, using their GitHub username is also fine.

Language
^^^^^^^^^

Programming language of the integration. Find this by clicking on the coloured bar in the GitHub project, below the header containing “commits, branches, releases, contributors”, and choosing the language(s) higher than 30%.

Don't add ``Makefile`` unless it's the only language on the repo.
Use ``Go`` instead of Golang.
If there is no language, set to ``N/A`` instead of leaving blank.

License
^^^^^^^^

This is typically found in the GitHub project, on the file named “LICENSE”. The license file should specify the license type. Note that:
License must be compatible with Apache 2.0 (https://apache.org/legal/resolved.html#category-a). E.g. not GPLv3, nor APGLv3.

 - Format: Use ``Apache 2.0``, ``BSD 2-Clause`` or ``BSD 3-Clause``.
 - If not compatible with Apache 2.0, do not add the integration to the website.
 - When the integration is not open source, mark the license as N/A - not open source.

Download URL
^^^^^^^^^^^^^

Go to the GitHub project, find the README file that typically includes install instructions, and link to that.

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

 - License of the integration must be compatible with Apache 2.0 (https://apache.org/legal/resolved.html#category-a). E.g. not GPLv3, nor APGLv3. Only exception is if the integration is not open source.
 - Integration must have been updated in the last 12 months.
 - Every integration link must be related to Mattermost.
 - The integration must have all required information in the submission form.

Marketing
---------

1. Add integration/plugin creators to changelog’s list of contributors.
E.g. for March release, add any new ones from February.

2. Create a tweet for all new integrations.
E.g. https://twitter.com/Mattermost/status/1102709312231596032.

Release Date T-0
------------------

 - Add integrations with more than 50 stars to the “New and Noteworthy” category.
 - Add 8 most recent integrations to “New and Noteworthy”.
    - Oldest on this list should be removed when a new integration is added.
 - Update the Date Last Updated for all integrations.
    - (Also remove any integrations that haven’t been updated in the last 12 months. Note: keep this relaxed. Some older ones are still important to keep.)
 - Add any new plugins from https://github.com/mattermost/mattermost-plugins.
 - Ask Integrations PM if any integrations are good to add or remove from the "Staff Picks" section.
 
Note: These integrations should stay in New and Noteworthy category:

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
