Team Settings
=============

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The Team Settings menu offers Team Admins and System Admins the ability to adjust settings applied to a specific team. To access the settings, open the channel menu at the top of the channel sidebar and select **Team Settings**. 

General
-------

General settings provide options around how teams are displayed to users. 

Team name
~~~~~~~~~

Your **Team Name** is displayed on the sign-in screen, and in the top of the channel sidebar for your team. 

You can enter a name up to 15 characters in length. Please note that `some unicode characters <https://www.w3.org/TR/unicode-xml/#Charlist>`_ are not supported. The length of team names is limited to ensure readability.

Team description
~~~~~~~~~~~~~~~~

Your **Team Description** is displayed when viewing the list of teams available to join and in the tooltip when hovering over the team name in the team sidebar.

You can enter a description up to 50 characters in length. Please note that `some unicode characters <https://www.w3.org/TR/unicode-xml/#Charlist>`_ are not supported. 

Team icon
~~~~~~~~~

Your **Team Icon** appears in the team sidebar, visible if users are members of more than one team.

You can upload a team icon in BMP, JPG or PNG format. Square images with a solid background color are recommended, since transparency in PNG icons fills with a white background in the team sidebar. Removing the team icon resets it to the default icon that contains the first two letters of the team name.

Allow only users with a specific email domain to join this team
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specifying domains in this setting prevents users from joining the team when their email domain is not on the list. Only users that have an email domain matching the defined domains may join the team. 

Users without a matching domain on the team prior to the domain being specified will not be removed after the domain is added. For servers with email authentication **System Console > Authentication > Email > Require Email Verification** must be set to ``true`` for domain restrictions to be effective.

Allow anyone to join this team
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After a user logs in to the site, they are shown a Team Selection page if they don't belong to a team. Any team with **Allow anyone to join this team** option set to **Yes** will show up on this page under "Teams you can join". 

A user can access the Team Selection page by also clicking the "+" icon at the bottom of their team sidebar or from the **Main Menu > Join Another Team**.

Invite code
~~~~~~~~~~~

The **Invite Code** is used as part of the URL in the team invitation link retrieved when you select your team name and then choose **Invite people**.

Import
------

Import from Slack
~~~~~~~~~~~~~~~~~

You can import channels and users from Slack into Mattermost. Please review our documentation on `Slack Import <https://docs.mattermost.com/onboard/migrating-to-mattermost.html#migrating-from-slack>`__ for more details.
