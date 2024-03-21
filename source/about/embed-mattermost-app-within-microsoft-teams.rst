:orphan:

Embed the Mattermost App within Microsoft Teams (Experimental)
==============================================================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

With the :doc:`Microsoft Teams plugin </about/mattermost-for-microsoft-teams>`, you can embed your Mattermost workspace within your Microsoft Teams instance and take advantage of `embedded app features <#benefits-of-the-embedded-app>`_.

.. important::

    You must :doc:`install the Microsoft Teams plugin in Mattermost </about/install-mattermost-for-microsoft-teams-plugin>` before you can embed the Mattermost app within Microsoft Teams.

To install the Mattermost app in Microsoft Teams:

1. In Mattermost, as an administrator, go to **System Console > Plugins > MS Teams**. At the bottom of the settings page, select **Download Manifest** to download a ZIP file containing the Microsoft Teams application manifest pre-configured for your Mattermost workspace.
2. In Microsoft Teams, as an administrator, go to the Microsoft Teams admin center under **Teams Apps > Manage Apps**, or use the following URL: ``https://admin.teams.microsoft.com/policies/manage-apps``.
3. Select **Upload new app**, then upload the app manifest you downloaded in the previous step.

You’re all set! The Mattermost app is now available to everyone in your Microsoft Teams workspace.

Pin the Mattermost app in Microsoft Teams
------------------------------------------

1. Add the Mattermost app by selecting **Apps** within the left-hand sidebar, select **Add** located next to the Mattermost for Microsoft Teams app, then select **Add** again. Once added, your Mattermost workspace is now embedded in your Microsoft Teams instance. 
2. Pin the Mattermost app in your left-hand sidebar, to access it easily in the future, by right-clicking the Mattermost tab and selecting **Pin**.
3. Sign in with your credentials, and use the Mattermost app to collaborate with technical and operations teams.

Demonstration: Embed Mattermost within Microsoft Teams
-------------------------------------------------------

Check out this `YouTube demo <https://youtu.be/MxegqqfErEg>`__, from Doug Lauder, Senior Software Design Engineer at Mattermost, to learn how to embed Mattermost within Microsoft Teams:

.. raw:: html
  
   <iframe width="560" height="315" src="https://www.youtube.com/embed/MxegqqfErEg" alt="Install the Mattermost app in Microsoft Teams" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


Get users started with the embedded app
----------------------------------------

See our end user documentation for a :ref:`video walkthrough of using Mattermost embedded within Microsoft Teams <collaborate/collaborate-within-embedded-microsoft-teams:demonstration: mattermost embedded in microsoft teams>`.

Benefits of the embedded app
----------------------------

- **Improved reaction time in the event of an incident** by accessing alerting features in Mattermost directly from within Microsoft Teams.

  Mattermost is open-source and can be extensively customized to integrate with various system monitoring and alerting tools. If your tech team has set up unique alerting features in Mattermost, use the app to access these directly from within Teams, including system status updates, improving reaction time in the event of an incident.

- **Simplified workflows through a single interface** for communication and DevOps management.

  If your technical team uses specific DevOps tools (such as Jenkins, Jira, GitHub, etc.) that are tightly integrated with Mattermost, embedding Mattermost in Teams can give direct access to these integrated services. This simplifies workflows by providing a single interface for DevOps use cases.

- **Quickly run scripts within Microsoft Teams**.

  Mattermost supports the use of a CLI, which can be a major advantage for tech teams. If you need to run scripts or execute commands via Mattermost, embedding it within Teams allows you to use this functionality from either platform.

- **Embed custom functionality to accelerate technical workflows**.

  If your tech team has created custom bots and plugins that function with Mattermost, embedding it within Microsoft Teams will allow everyone to access these utilities. These may include custom bots for streamlining incident management, security operations and red/blue team workflows.

Limitations
------------

The embedded Mattermost app currently only supports email/password log in to the Mattermost workspace. SSO authentication with SAML 2.0 providers (Okta, OneLogin, Microsoft ADFS) and with your Microsoft365 account are under consideration.

Get help
---------

If you face any issues while installing or using the app in Microsoft Teams, you can either:

- Open a new issue in the `Mattermost for Microsoft Teams GitHub repository <https://github.com/mattermost/mattermost-plugin-msteams/issues/new>`__. 
- Or, create a new topic in our `peer-to-peer troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`__.