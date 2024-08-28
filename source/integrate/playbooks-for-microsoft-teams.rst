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

Update and configure the Playbooks integration for Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This step must be completed once by an Administator of the Mattermost instance.

1. As a System Administrator, open the **System Console > Plugin Management** page to upload the `latest preview build of Mattermost Playbooks <https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v2.0.1%2Btabapp>`_ with support for the Teams app integration.

2. Once uploaded, click **Settings** under the Playbooks plugin to **Enable Teams Tab App** and enter your Microsoft Teams tenant ID in the **Authorised Tenant IDs for Teams Tab App** field. 

.. note::

  Mattermost Playbooks for Teams is currently available as a technical preview, requiring System Admins to manually upload the latest experimental version of Playbooks to support this new functionality. This will be fully supported and pre-packaged with the Mattermost server in v10.1 (October).

Choose which Playbook runs are accessible to Microsoft Teams users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This step can be completed by any user with the permissions to add participants to Playbooks or Runs.

Now that the Playbooks plugin is updated and configured, you'll have to choose which Playbook runs are accessible by users in Microsoft Teams. Playbooks Runs where the **@msteams** bot is a partcipant are visible to users in Microsoft Teams who've installed the Mattermost Playbooks for Teams application and configured it with the appropriate Mattermost server URL. To add the **@msteams** bot as a participant to a Playbook Run, find the active Run in the Mattermost Playbooks product (or go to the associated run channel), click on the **Participants** in the right-hand sidebar, and then add the **@msteams** bot as a new participant. 

.. tip::

You must ensure the **@msteams** bot is member of the associated team before it can be added to a Playbook or Run. 


Install the Mattermost Playbooks for Teams application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This step can be completed by any Microsoft Teams user in the associated tenant that was configured for the Playbooks plugin in the steps above. 

1. Sign into your Microsoft Teams account from a `browser <https://teams.microsoft.com/>`_ or the desktop application.

2. Click the **[+] Apps** button in the Microsoft Teams sidebar.

3. Search for "Mattermost Playbooks for Teams" and then click **Add** to install the application.

4. (Optional) Pin the application to your Teams sidebar by right clicking on it and selecting *Pin*

5. Once the app is installed, enter the URL for your Mattermost Enterprise self-managed or cloud server.

Setup is now complete. You should now see a list of all active runs where the **@msteams** is a participant. You can click on any active run to see recent status updates in chronological order.

 
FAQ
-----


Do I need a Mattermost instance to use this application?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, you must have an active Mattermost Enterprise self-managed or cloud deployment to use this app.

Why don't I see any runs after entering my Mattermost server URL?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please ensure you've added the **@msteams** bot to any runs you want to be accessible from Microsoft Teams. You can automate this step for future runs of a Playbook by inviting the **@msteams** bot as a participant in the **Actions** section of any Playbook configuration.

