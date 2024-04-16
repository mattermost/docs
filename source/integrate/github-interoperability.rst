Integrate GitHub into Mattermost
================================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Minimize distractions and reduce context switching between your GitHub code repositories and your communication platform by integrating GitHub with Mattermost. Help your teams stay focused and productive with real-time updates on commits, pull requests, issues, and more directly from Mattermost channels.

Setup
------

The following integration configuration steps are required.

Register an OAuth app in GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every Mattermost user who wants GitHub interoperabilty must perform the following steps while logged in to GitHub.

1. Go to https://github.com/settings/applications/new to register an OAuth app.
2. Set the following values:

    - Application name: ``Mattermost GitHub Plugin - <your company name>``
    - Homepage URL: ``https://github.com/mattermost/mattermost-plugin-github``
    - Authorization callback URL: ``https://your-mattermost-url.com/plugins/github/oauth/complete``, replacing ``https://your-mattermost-url.com`` with your Mattermost URL. This value must match the Mattermost server URL you use to log in.

3. Submit.
4. Select **Generate a new client secret**, and enter your GitHub password to continue.
5. Copy the **Client ID** and **Client Secret** in the resulting screen. Provide these values to your Mattermost system admin.
6. Select both **Generate** buttons in **Webhook Secret** and **At Rest Encryption Key**.

Create a webhook in GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in Mattermost. Create a Mattermost webhook for each GitHub organization you want to set up.

.. tab:: Cloud

    Skip registation steps and use the preregistered GitHub OAuth application by going to **System Console > Plugins > GitHub**. 
    
    .. note::
        
        Requires `Chimera Proxy URL <https://github.com/mattermost/chimera>`__ to be configured for the server. Can't be used with GitHub Enterprise.

.. tab:: Self-Hosted

    1. In Mattermost, go to **System Console > Plugins > GitHub**, and generate a new value for **Webhook Secret**, and copy this value. It will be used in a later step. 
    2. Save the secret.
    3. In GitHub, go to the **Settings** page where you want to send notifications from, then select **Webhooks** in the sidebar.
    4. Select **Add Webhook**.
    5. Set the following values:

        - **Payload URL**: ``https://your-mattermost-url.com/plugins/github/webhook``. Replace ``https://your-mattermost-url.com`` with your Mattermost URL.
        - **Content Type**: application/json
        - **Secret**: The **Webhook Secret** value you copied earlier.

    6. Under **Which events would you like to trigger this webhook?**, select **Let me select individual events**.
    7. Select the following events: 

        - **Branch or Tag creation**
        - **Branch or Tag deletion**
        - **Issue comments**
        - **Issues**
        - **Pull requests**
        - **Pull request review**
        - **Pull request review comments**
        - **Pushes**
        - **Stars**

    8. Select **Add Webhook** to save your changes.

Configure the GitHub account in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in Mattermost.

1. Confirm whether your Mattermost deployment has a ``github`` user account. If it exists, that account posts GitHub messages in channels by default, and the messages won't include a BOT tag. You can change this account behavior to include a BOT tag by using one of the following methods:

- Convert the user account to a bot using :ref:`mmctl user convert <manage/mmctl-command-line-tool:mmctl-user-convert>`.
- Change the existing ``github`` username to something else. A new bot account called ``github`` is created the Mattermost server is restarted when the :ref:`enable bot account creation <configure/integrations-configuration-settings:enable bot account creation>` configuration setting is enabled.

.. note::

    - Older versions of the GitHub interation, including v0.9.0 and earlier, require you to set the username the plugin is attached to by going to **System Console > Plugins > GitHub**.

2. Go to **System Console > Plugins > GitHub** to finish configuration, then selct **Save**.

    - Enter the **GitHub OAuth Client ID** and **GitHub OAuth Client Secret** obtained during registration
    - Regenerate the **At Rest Encryption Key** by selecting **Regenerate**.
    - (Optional) Lock the plugin to a single GitHub organization by setting **GitHub Organization** to the name of your GitHub organization.
    - (GitHub Enterprise Only): Set **Enterprise Base URL** and **Enterprise Upload URL** values to your GitHub Enterprise URLs, e.g. ``https://github.example.com``. These values are often the same.
    - (Mattermost desktop app only) Display or hide GitHub notification counters in the Mattermost sidebar.
    - (Optional) Work with private repositories by enabling **Enable Private Repositories**. Affected users are notified once private repositories are enabled, and must reconnect their GitHub accounts to gain access to private repositories.
    - (Optional) Connect to private GitHub repositories by default, when private repositories are enabled.
    - (Optional) Expand permalinks to GitHub files with previews. Can enable for public repositories or public and private repositories, or disable.
    - (Optional) Log webhook events when log level set to DEBUG.
    - (Optional) Show commit author instead of committer in GitHub push event notifications.

Enable
------

Once all setup and configuration is complete, go to **System Console > Plugins > GitHub** to enable GitHub interoperability.

Notify your team so they can connect their GitHub account to Mattermost and get started.

Upgrade
--------

We recommend updating this functionality when new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost.

Usage
-----

In Mattermost, run the ``/github connect`` slash command in any Mattermost channel to link your Mattermost account with your GitHub account. 

Run the ``/github subscriptions add`` slash command to subscribe a Mattermost channel to receive notifications for new pull requests, issues, branch creation, and more in a GitHub repository.

For example, to post notifications for issues, issue comments, and pull requests matching the label **Help Wanted** from the ``mattermost/mattermost-server`` GitHub repository, use: ``/github subscriptions add mattermost/mattermost-server --features issues,pulls,issue_comments,label:"Help Wanted"``

The following flags are supported:
- ``--features``: A comma-delimited list of one or more of: issues, pulls, pulls_merged, pulls_created, pushes, creates, deletes, issue_creations, issue_comments, pull_reviews, label:"labelname". Defaults to ``pulls,issues,creates,deletes``.
- ``--exclude-org-member``: The events triggered by organization members that won't be delivered. It will be locked to the organization configured and only works for users whose membership is public. Organization members and collaborators are not the same.
- ``--render-style``: Notifications are delivered in the specified style (for example, the body of a pull request will not be displayed). Supported values are ``collapsed``, ``skip-body``, or ``default`` (which is the same as omitting the flag).
- ``--exclude``: A comma-separated list of the repositories to exclude from getting the subscription notifications like ``mattermost/mattermost-server``. Only supported for subscriptions to an organization.

Run the ``/github todo`` slash command to get a message with items to do in GitHub, including a list of unread messages and pull requests awaiting your review.

Run the ``/github settings`` slash command to update your settings for notifications and daily reminders.

Run the ``/github setup`` slash command to configure the integration between GitHub and Mattermost. This command has the following subcommands:

    ``/github setup oauth``: Sets up the OAuth2 application in GitHub, establishing the necessary authorization connection between GitHub and Mattermost.
    ``/github setup webhook``: Creates a webhook from GitHub to Mattermost, allowing real-time notifications and updates from GitHub to be sent to Mattermost channels.
    ``/github setup announce``: Sends a message to designated channels in Mattermost, announcing the availability of the GitHub integration for team members to use.

And more! - Run the ``/github help`` slash command to see what else you can do.

Frequently asked questions
---------------------------

How do I connect a repository instead of an organization?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set up your GitHub webhook from the repository instead of the organization. Notifications and subscriptions will then be sent only for repositories you create webhooks for. The reminder and ``/github todo`` searches the whole organization, but only show items assigned to you.

How do I send notifications when a certain label is applied?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to send notifications to a Mattermost channel when **Severity/Critical** label is applied to any issue in the ``mattermost/mattermost-plugin-github`` repository, run the following slash command to subscribe to these notifications: ``/github subscriptions add mattermost/mattermost-plugin-github issues,label:"Severity/Critical"``

How does the plugin save user data for each connected GitHub user?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub user tokens are AES-encrypted with an **At Rest Encryption Key** configured in Mattermost. Once encrypted, the tokens are saved in the ``PluginKeyValueStore`` table in your Mattermost database.

Get help
--------

Mattermost customers can open a `Mattermost support case <https://mattermost.zendesk.com/hc/en-us/requests/new>`_. To report a bug, please open a GitHub issue against the `Mattermost GitHub repository <https://github.com/mattermost/mattermost-plugin-github>`_.

For questions, feedback, and assistance, join our pubic `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`_ on the `Mattermost Community Server <https://community.mattermost.com/>`_ for assistance, or join us on the  `Mattermost Discussion Forum <https://forum.mattermost.org/c/plugins>`_.

Customize
---------

This integration contains both a server and web app portion. Visit the `Mattermost Developer Workflow <https://developers.mattermost.com/extend/plugins/developer-workflow/>`__ and `Mattermost Developer environment setup <https://developers.mattermost.com/extend/plugins/developer-setup/>`_ for information about developing, customizing, and extending Mattermost functionality.

In order to get your environment set up to run Playwright tests, please see the setup guide at `e2e/playwright <https://github.com/mattermost/mattermost-plugin-github/blob/master/e2e/playwright#readme>`_.