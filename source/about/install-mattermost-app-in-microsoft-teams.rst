Install the Mattermost App in Microsoft Teams
=============================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. note::

    You must `install the Microsoft Teams plugin in Mattermost </plugins/install-mattermost-for-microsoft-teams-plugin>`__ before you can install the Mattermost app in Microsoft Teams. 

To install the Mattermost app in Microsoft Teams:

1. In Mattermost, as an administrator, go to System Console > Plugins > Mattermost for Microsoft Teams. At the bottom of the settings page, select **Download Manifest** to download a ZIP file containing the Microsoft Teams application manifest pre-configured for your Mattermost workspace.
2. In Microsoft Teams, as an administrator, go to the Microsoft Teams admin center under **Teams Apps > Manage Apps**, or use the following URL: ``https://admin.teams.microsoft.com/policies/manage-apps``.
3. Select **Upload new app**, then upload the app manifest you downloaded in the previous step.

You’re all set! The Mattermost app is now available to everyone in your Microsoft Teams workspace.

Pin the Mattermost app in Microsoft Teams
------------------------------------------

1. Add the Mattermost app by selecting **Apps** within the left-hand sidebar, select **Add** located next to the Mattermost for Microsoft Teams app, then select **Add** again. Once added, your Mattermost workspace is now embedded in your Microsoft Teams instance. 
2. Pin the Mattermost app in your left-hand sidebar to access it easily in the future, by right-clicking the Mattermost tab and selecting **Pin**.
3. Sign in with your email/password credentials, and use the Mattermost app to collaborate with technical and operations teams.

Limitations
------------

The Mattermost app currently only supports email/password log in to the Mattermost workspace. SSO authentication with SAML 2.0 providers (Okta, OneLogin, Microsoft ADFS) and with your Microsoft365 account are under consideration.

Troubleshooting
----------------

If you face any issues while installing or using the app in Microsoft Teams, you can either:

- Open a new issue in the `Mattermost for Microsoft Teams GitHub repository <https://github.com/mattermost/mattermost-plugin-msteams-sync/issues/new>`__. 
- Or, create a new topic in our `peer-to-peer troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`__.

Demonstration
--------------

Check out this `YouTube demo <https://youtu.be/Mg-stF7_Bjk>`__, from Doug Lauder, Senior Software Design Engineer at Mattermost, to get started with Mattermost for Microsoft Teams:

.. raw:: html
  
   <iframe width="560" height="315" src="https://www.youtube.com/embed/Mg-stF7_Bjk" alt="Video on self hosted subscription" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>