Invite people to your workspace
================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Anyone can invite people to Mattermost teams and channels, unless your system admin has :doc:`disabled </administration-guide/onboard/advanced-permissions>` your ability to do so.

.. tab:: Web/Desktop

  1. Select the team name at the top of the channel sidebar, and then select **Invite People**.

    .. image:: ../../images/invite-people.png
      :alt: Select the team name in the sidebar and select Invite People.

  2. Choose how to invite people:

    - **Copy invite link**: Share an invitation link with others using apps on your mobile device.
    - **Invite as member**: Send an invitation by email to people who don't have an account on your Mattermost workspace by specifying their email address and selecting **Invite**. 
    - **Add existing users**: Add existing workspace users as members of the current team by specifying their username and selecting **Invite**.
    - **Invite as guest**: Invite a guest temporarily with limited workspace access. Specify their email address, select the channels they can access, and optionally add a custom message. See the :doc:`guest accounts </administration-guide/onboard/guest-accounts>` documentation to learn more about guest accounts.

      - **Use magic link**: Invite guests to log in without a password using a magic link when :ref:`enabled by your system admin <administration-guide/onboard/guest-accounts:configure magic links for guests>`. See the :ref:`magic link login for guests <end-user-guide/access/access-your-workspace:magic link login for guests>` documentation for login details.

    .. image:: ../../images/web-desktop-invite-people-to-the-team.png
      :alt: You can invite users through the web or desktop app in a number of ways.

.. tab:: Mobile

  1. Tap the |plus| icon in the top right corner of the screen and tap **Invite people to the team**.

    .. image:: ../../images/mobile-invite-people-to-the-team.png
      :alt: When you select +, you can access more options from the popup window.
      :scale: 30

  2. Choose how to invite people:

    - **Share link**: Share an invitation link with others using apps on your mobile device.
    - **Invite as member**: Send an invitation by email to people who don't have an account on your Mattermost workspace by specifying their email address and tap **Send**. 
    - **Add existing users**: Add existing workspace users as members of the current team by specifying their username and tap **Send**.
    - **Invite as guest**: Invite a guest temporarily with limited workspace access. See the :doc:`guest accounts </administration-guide/onboard/guest-accounts>` documentation to learn more about guest accounts. Specify their email address, select the channels they can access, and optionally add a custom message.  Tap **Send** when ready.

      - **Use magic link**: Invite guests to log in without a password using a magic link when :ref:`enabled by your system admin <administration-guide/onboard/guest-accounts:configure magic links for guests>`. See the :ref:`magic link login for guests <end-user-guide/access/access-your-workspace:magic link login for guests>` documentation for login details.

    .. image:: ../../images/mobile-send-invite-to.png
      :alt: You can invite users through the mobile app in a number of ways.
      :scale: 30

.. note::

  - Can't share invitation links? Contact your Mattermost system admin for assistance. An :doc:`SSL certificate (or a self-signed certificate) </administration-guide/onboard/ssl-client-certificate>` may be required for link-based invitations to work.
  - When inviting guests, you must select at least one channel they can access. Guests are limited to the channels you specify and cannot discover other channels.
  - An invite link can be used by anyone and doesn’t change unless it’s re-generated or revoked by a system admin or team admin via **Team Settings > Access > Invite Code**.
  - Your system admin must :ref:`enable email invitations <administration-guide/configure/authentication-configuration-settings:enable email invitations>` and configure :ref:`email <administration-guide/configure/environment-configuration-settings:smtp>` for Mattermost to send email-based invitations.
    - Invitation links sent by email expire after 48 hours and can only be used once.
  - Your system admin can :ref:`cancel all email invitations <administration-guide/configure/authentication-configuration-settings:invalidate pending email invites>` that haven't yet been accepted within the System Console.