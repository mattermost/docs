Team settings
=============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Team settings enable system and team administrators to adjust settings applied to a specific team. Using Mattermost in a web browser or the desktop app, select the team name to access **Team Settings**.

.. image:: ../images/team-settings.png
  :alt: Access team settings from the team name. 

Info settings
-------------

Info settings provide configuration options for how teams are displayed to users.

Team name
~~~~~~~~~

Your **Team Name** is displayed on the login screen, and in the top of the channel sidebar for your team. 

Team names can contain any letters, numbers, or symbols, must be 2 - 64 characters in length, and are case-sensitive. 

.. note::
  
  Team names don't support `some unicode characters <https://www.w3.org/TR/unicode-xml/#Charlist>`__. 

Team description
~~~~~~~~~~~~~~~~

Your **Team Description** is displayed when viewing the list of teams available to join and in the tooltip when hovering over the team name in the team sidebar.

You can enter a description up to 50 characters in length. 

.. note::
  
  Team descriptions don't support `some unicode characters <https://www.w3.org/TR/unicode-xml/#Charlist>`__. 

Team icon
~~~~~~~~~

A **Team Icon** displays in the team sidebar. By default, the team icon contains the first two letters of the team name. 

To customize the team icon:

1. Select **Team Settings**.

2. Select the Team Icon **Edit** option.

.. image:: ../images/edit-team-icon.png
  :alt: Manage the team icon from Team Settings.

3. Select an icon image in BMP, JPG, or PNG format. We recommend using square images with a solid background color since transparency in PNG icons fills with a white background in the team sidebar.

4. Select **Save**.

.. tip::
  When a team icon is configured, select **Remove image** to reset the team icon to the default icon containing the first two letters of the team name.

Access settings
---------------

Access settings enable the ability to control who can join the team.


Users with a specific email domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System and team administrators can limit who can join the team based on their email domain. Enable this option to specify approved email domains. Separate multiple email domains using spaces, commas, pressing :kbd:`Tab`, or pressing :kbd:`Enter`. 

When enabled, only users that have an email domain from the approved domain list is able to join the team. Team members who joined prior to approved domains being specified won't be removed from the team once approved email domains are configured and enforced.

.. important::

  Mattermost deployments using :ref:`email authentication <configure/authentication-configuration-settings:enable sign-in with email>` must also enable the :ref:`require email verification configuration setting <configure/authentication-configuration-settings:require email verification>` for domain restrictions to be effective.

Users on this server
~~~~~~~~~~~~~~~~~~~~~

System and team administrators can include the team in a list of teams to join for new Mattermost users who aren't yet members of a team. Enable this option to allow any user with a Mattermost account on this instance to join this team from the **Teams you can join** page.

.. tip::
  
  When you enable this option, users looking for more teams to join will also see this team in the list when they select the |plus| icon in the team sidebar.

Invite code
~~~~~~~~~~~

The **Invite Code** is used as part of the URL in team invitation links. Select **Regenerate** to create a new invitation link and invalidate any previous link.
