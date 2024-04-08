Collaborate within Microsoft Teams (Pilot)
==========================================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |plus-icon| image:: ../images/plus_F0415.svg
  :alt: Open menus using the plus icon.
  :class: theme-icon

The :doc:`Mattermost for Microsoft Teams plugin </about/mattermost-for-microsoft-teams>` integration enables you to collaborate with Microsoft Teams users without leaving Mattermost.

.. include:: ../_static/badges/academy-msteams.rst
  :start-after: :nosearch:

Connect your Mattermost account to your Microsoft Teams account
---------------------------------------------------------------

To use the Microsoft Teams plugin, you must connect your Mattermost user account to your Microsoft Teams account. You only need to complete this step once.

1. Log into Mattermost using your credentials. 
2. When you log in, you’ll be prompted to enter your Microsoft Teams user information, including your Microsoft Teams email address and your Microsoft Teams password.

.. note::

  - To change which accounts are linked, in Mattermost, disconnect the current account by running the slash command ``/msteams disconnect`` within the Mattermost message text box. Then, re-connect a new Mattermost account to a new Microsoft Teams account by running the Mattermost slash command ``/msteams connect``.
  - If your Microsoft Teams user account is removed from Microsoft Teams, your linked Mattermost user account will also be removed the next time user accounts are synchronized across the two platforms.

Mattermost will confirm when your account is connected, and prompt you to select your primary platform.

Select your preferred platform
-------------------------------

Once you've connected your Mattermost account to your Microsoft Teams account, Mattermost prompts you to choose which platform you'll use more often: `Mattermost <#mattermost-is-your-preferred-platform>`_ or `Microsoft Teams <#microsoft-teams-is-your-preferred-platform>`_. Mattermost optimizes your experience based on the platform you prefer to use.

.. note::

  - If you're not prompted to connect your accounts, run the Mattermost slash command ``/msteams connect`` within the Mattermost message text box to display the prompt in a browser window. Follow the link to connect your accounts.
  - If you select **Skip for now**, Mattermost is selected as your primary platform. You can change this preference any time by selecting your profile picture and going to **Settings > MS Teams Settings**.

Mattermost is your preferred platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Mattermost is preferred, you'll receive Microsoft Teams messages and notifications in Mattermost.

We recommend that you disable notifications in Microsoft Teams. If you don't, you'll receive duplicate message notifications in both platforms. See the `Microsoft Teams notifications documentation <https://support.microsoft.com/en-us/office/manage-notifications-in-microsoft-teams-1cc31834-5fe5-412b-8edb-43fecc78413d>`__ for details.

Microsoft Teams is your preferred platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Microsoft Teams is preferred, you'll receive messages from Mattermost in Microsoft Teams. Mattermost notifications are automatically muted for you to prevent duplicate notifications.

Setup complete
--------------

Setup is complete! You're ready to collaborate across your organization. Interact with colleagues in Microsoft Teams without having to leave Mattermost.

Get started
-----------

You can start a direct or group message between Mattermost and Microsoft Teams users unless your Mattermost administrator has :ref:`disabled the ability to do so in the System Console <configure/plugins-configuration-settings:sync direct and group messages>`. 

- Within Mattermost select the |plus-icon| icon next to **Direct Messages** in the left pane, then search for the user you want to message. Your direct or group conversation is visible in both Mattermost and Microsoft Teams.

- Within Microsoft Teams, select **Chat > New chat**, and select the users you want to chat with. Your conversation is visible in both Mattermost and Microsoft Teams for all users who have connected their Mattermost user account to their Microsoft Teams user account.

.. image:: ../images/ms-teams-dm-sync-feb-2024.gif
   :alt: An example of a Mattermost direct message (DM) that is synced with a DM on Microsoft Teams.
