Connect GitLab to Mattermost
================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Minimize distractions and reduce context switching between your GitLab code repositories and your communication platform by integrating GitLab with Mattermost. Help your teams stay focused and productive with daily task summaries, real-time updates and notifications on new and closed merge requests, new and closed issues, and tag creation events, directly from Mattermost channel subscriptions.

.. image:: ../images/gitlab_mattermost.png
  :alt: An example of the GitLab integration for Mattermost.

.. note::
  - You can also control which events trigger notifications beyond default events, including merges, issue comments, merge request comments, pipelines, and pull reviews.
  - Mattermost supports both Software-as-a-Service (SaaS) and on-premises versions of GitLab.

Setup
------

Setup starts in GitLab and configuration ends in Mattermost.

Register an OAuth app in GitLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in GitLab.

1. Go to https://gitlab.com/-/profile/applications or https://gitlab.YOURDOMAIN.com/-/profile/applications, replacing ``YOURDOMAIN.COM`` with your GitHub URL, to register an OAuth app with GitLab.
2. Set the following values:

  - **Name**: ``Mattermost GitLab Plugin - <YOUR COMPANY NAME>``
  - **Redirect URI**: ``https://YOUR-MATTERMOST-URL.COM/plugins/com.github.manland.mattermost-plugin-gitlab/oauth/complete``, replacing ``YOUR-MATTERMOST-URL.COM`` with your Mattermost URL. This value must match the Mattermost server URL you use to log in.

3. Select ``api`` and ``read_user`` in **Scopes**.
4. Save your changes. Copy the **Application ID** and **Secret** fields in the resulting screen.
  - Authorization callback URL: ``https://YOUR-MATTERMOST-URL.COM/plugins/github/oauth/complete``, replacing ``https://YOUR-MATTERMOST-URL.COM`` with your Mattermost URL. 

3. Submit these changes.
4. Select **Generate a new client secret**, and enter your GitHub password to continue. 
5. Copy the **Client ID** and **Client Secret** in the resulting screen. 
6. Generate a **Webhook Secret** and **At Rest Encryption Key** by selecting **Generate**.

Create a webhook in GitLab
~~~~~~~~~~~~~~~~~~~~~~~~~~

Don't forget to add a webhook in GitLab!

.. this process is missing from the README

Mattermost configuration
~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in Mattermost.

Go to **System Console > Plugins > GitHub** to finish configuration, then select **Save**.

- Enter the **GitLab URL**, **GitLab OAuth Client ID**, and **GitLab OAuth Client Secret** you obtained when `registering the OAuth app in GitLab <#register-an-oauth-app-in-GitLab>`__.
- Generate a **Webhook Secret** and **At Rest Encryption Key** by selecting **Generate**.
- (Optional) Lock the plugin to a single GitLab group by setting **GitLab Group** to the name of your GitLab group.
- (Optional) Work with private repositories by enabling **Enable Private Repositories**. Affected users are notified once private repositories are enabled, and must reconnect their GitLab accounts to gain access to private repositories.

Enable
------

Once all setup and configuration is complete, a Mattermost system admin can go to **System Console > Plugins > GitLab** to enable GitLab interoperability. Notify your teams that they can connect their GitLab accounts to Mattermost.

Upgrade
~~~~~~~

We recommend updating this integration as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost.
Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-gitlab/releases>`__ for the latest release, available releases, and compatibiilty considerations.

Usage
-----

You must register an OAuth app in GitLab for Mattermost, and then connect your GitLab account to Mattermost to use GitLab interoperabilty. Once connected, you'll receive direct messages from the GitLab bot in Mattermost when someone mentions you, requests a review, comments on, or modifies one of your merge requests/issues, or assigns you to an issue on GitLab.

Connect your GitLab account to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect your GitLab account to Mattermost by running the ``/gitlab connect`` slash account. Disconnect your account by running the ``/gitlab disconnect`` slash comamnd. Run the ``/gitlab me`` slash command to review the connected GitLab account.

Get started
~~~~~~~~~~~

Run the  ``/gitlab todo`` slash command to get a list of todos, assigned issues, assigned merge requests and merge requests awaiting your review. Alternatively, use the options located in the left sidebar.

Run the ``/gitlab webhook`` slash command to have GitLab send events to Mattermost. For example: ``/gitlab webhook add group[/project]``

Channel subscriptions
~~~~~~~~~~~~~~~~~~~~~

Run the ``/gitlab subscriptions list`` to review all of your subscriptions.

Run the ``/gitlab subscriptions add owner[/repo] [features]`` slash command to subscribe a Mattermost channel and receive posts for new merge requests, issues, or other features, from a GitLab repository. To unsubscribe and stop receiving posts, run the ``/gitlab subscriptions delete owner/repo`` slash command.

For each project you want to receive notifications for or subscribe to, create a webhook in a channel where you want to watch events sent from GitLab by running the ``/gitlab subscribe`` slash command. For example: ``/gitlab subscriptions add group[/project]``

.. note::

  For GitLab versions prior to 1.2:

  1. In GitLab, go to the project you want to subscribe to, and select **Settings > Integrations** in the sidebar.
  2. Set the following values:

    - **URL**: ``https://YOUR-MATTERMOST-URL.COM/plugins/com.github.manland.mattermost-plugin-gitlab/webhook``, replacing ``https://YOUR-MATTERMOST-URL.COM`` with your Mattermost URL. Ensure that you add ``/plugins/com.github.manland.mattermost-plugin-gitlab/webhook`` to the URL, or the webhook won't work.
    - **Secret Token**: Copy the webhook secret you generated earlier.
    - Select all the events in **Triggers**.
    - Add the webhook.


Run the  ``/gitlab settings [setting] [value]`` slash command to update your preferences for the plugin:

- Turn personal notifications on or off.
- Turn reminders on or off when you connect initially each day.

Get help
--------

Mattermost customers can open a `Mattermost support case <https://mattermost.zendesk.com/hc/en-us/requests/new>`_. To report a bug, please open a GitHub issue against the `Mattermost GitLab plugin repository <https://github.com/mattermost/mattermost-plugin-gitlab>`_.

For questions, feedback, and assistance, join our pubic `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`_ on the `Mattermost Community Server <https://community.mattermost.com/>`_ for assistance, or join us on the  `Mattermost Discussion Forum <https://forum.mattermost.org/c/plugins>`_.

Customize
---------

This integration contains both a server and web app portion. Visit the `Mattermost Developer Workflow <https://developers.mattermost.com/extend/plugins/developer-workflow/>`__ and `Mattermost Developer environment setup <https://developers.mattermost.com/extend/plugins/developer-setup/>`_ for information about developing, customizing, and extending Mattermost functionality.
