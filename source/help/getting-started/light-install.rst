Light Install Guide
===================

Mattermost is a messaging and collaboration platform. With Mattermost, you can integrate the tools you use every day into one place and never miss a notification or task. 

Before you get started you'll need:

* A clean Ubuntu server (18.04 or 20.04) with root level access
* (Recommended) A domain name pointing to your server (e.g. ``mymattermostserver.com``)
* (Recommended) Email addresses of your team members so you can invite them to the server

Installation
-------------

Install Mattermost using `Mattermost Omnibus <https://docs.mattermost.com/install/mattermost-omnibus.html>`_.

Open a terminal window and enter:

.. code-block:: sh

  curl -o- https://deb.packages.mattermost.com/repo-setup.sh | sudo bash

Then, to install the Omnibus package, run:

.. code-block:: sh

  sudo apt install mattermost-omnibus

.. note::
  
  Although the recommended way to install and configure Omnibus is with SSL enabled, if you want to use or test without it (or without a domain name), you can run: 

  .. code-block:: sh
  
    sudo MMO_HTTPS=false apt install mattermost-omnibus

When your server is up and running, navigate to it via the domain name (e.g. ``mymattermostserver.com``) that points to your server (or the server’s IP address if you’re not using a domain name). Next, create a team and invite people to join your Mattermost server.

If you have any problems installing Mattermost Omnibus, see the `troubleshooting guide <https://docs.mattermost.com/install/troubleshooting.html>`__ for common error messages, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/pl/default-ask-mattermost-community/>`_.

Add Users
---------

Next, add people to your team by sending them an invitation:

1. Click your username at the top left of the Navigation Panel.
2. Click **Invite People** and enter the email addresses of the people you want to add.
3. Click **Invite Members**.

When the invitee receives the email with the link, it’s a single click to join your server, chat to you in the channel you’ve created, or create their own channels. More information about adding users is available `here <https://docs.mattermost.com/help/getting-started/managing-members.html#managing-members>`_. 

Create a Notifications Hub
--------------------------

Create a `“heartbeat” channel <https://community.mattermost.com/core/channels/community-heartbeat>`_ and integrate your most-used apps and plugins with Mattermost to send status updates and critical notifications in one place. 

You can find and install integrations and plugins via **Main Menu > Plugin Marketplace**. 

Get started with GitHub, Jira, and Jenkins:

* Connect your GitHub organization to Mattermost using a slash command, to manage your reviews, pull requests, comments, and merges. GitHub is pre-packaged in Mattermost. Follow the `configuration steps <https://github.com/mattermost/mattermost-plugin-github#configuration>`_, and then let your team know to run /github connect so they can receive notifications.
* Connect your Jira account to Mattermost and set up a channel for the bot to post issues so your team is always up to date. Visit the `configuration guide <https://mattermost.gitbook.io/plugin-jira/setup/configuration>`_ to get started. Once configured, share the `end user documentation <https://mattermost.gitbook.io/plugin-jira/end-user-guide/getting-started>`_ with your team so they can start receiving notifications.
* Connect your Jenkins server to Mattermost to centralize your workflows and manage builds. Visit the `installation guide <https://github.com/mattermost/mattermost-plugin-jenkins#installation>`_ to get started. Share the `features list <https://github.com/mattermost/mattermost-plugin-jenkins#features>`_ with your team so they can ramp up quickly.

**Next:** `Learn more about organizing conversations <https://docs.mattermost.com/help/getting-started/organizing-conversations.html>`_ and setting up `Mattermost on your mobile device <https://docs.mattermost.com/mobile/mobile-overview.html>`_.
