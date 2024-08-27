Mattermost Playbooks for Teams
==============================

Mattermost Playbooks for Teams improves cross-organizational alignment and awareness by enabling access to your active Mattermost Playbook incidents and status updates directly in Microsoft Teams.

Stakeholders working in Microsoft Teams now gain enhanced visibility into ongoing incidents, while incident responders working in Mattermost can stay focused and eliminate context switching. 

Key Features:

- View active incidents, responders and last updated time
- Read real-time incident status updates in chronological order

.. image:: ../images/mattermost_playbooks_for_teams.png
  :alt: Mattermost Playbooks for Teams, available in the Microsoft Teams App Store

Setup
-----

Install the Mattermost Playbooks for Teams application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Sign into your Microsoft Teams account from a `browser <https://teams.microsoft.com/>`_ or the desktop application.

2. Click the **[+] Apps** button in the Microsoft Teams sidebar.

3. Search for "Mattermost Playbooks for Teams" and then click **Add** to install the application.

4. (Optional) Pin the application to your Teams sidebar by right clicking on it and selecting *Pin*

5. Once the app is installed, enter the URL for your Mattermost Enterprise self-managed or cloud server.

Now that the application is installed in your Microsoft Teams environment, you'll have to choose which Playbook runs are accessible by users in Microsoft Teams.  


Choose which Playbook runs are accessible to Microsoft Teams users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Mattermost, Playbooks runs where the **@msteams** bot is a partcipant are visible to users in Microsoft Teams who've installed the Mattermost Playbooks for Teams application and configured it with the appropriate Mattermost server URL. To add the **@msteams** bot as a participant to a Playbook run, find the active run in the Playbooks product (or go to the associated run channel), click on the **Participants** in the right-hand sidebar, and then add the **@msteams** bot as a new participant.


FAQ
-----


Do I need a Mattermost instance to use this application?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, you must have an active Mattermost Enterprise self-managed or cloud deployment to use this app.

Why don't I see any runs after entering my Mattermost server URL?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please ensure you've added the **@msteams** bot to any runs you want to be accessible from Microsoft Teams. You can automate this step for future runs of a Playbook by inviting the **@msteams** bot as a participant in the **Actions** section of any Playbook configuration.

