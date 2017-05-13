Configuring Mattermost Server
=============================

1. Navigate to ``https://mattermost.example.com`` and create a team and user.

  The first user in the system is automatically granted the ``system_admin`` role, which gives you access to the System Console.

2. Open the System Console. Click your username at the top left of navigation panel. In the menu that opens, click **System Console**.

3. You must set the `Site URL <https://docs.mattermost.com/administration/config-settings.html#site-url>`_:
  a. In the System Console, click **General > Configuration**.
  b. In the **Site URL** field, set the URL that users point their browsers at. For example, ``https://example.com``.

4. Setup an SMTP email service. Click **Notifications > Email** and make the following changes. The example below assumes AmazonSES.

    a. Set **Enable Email Notifications** to ``true``
    b. Set **Notification Display Name** to ``No-Reply``
    c. Set **Notification From Address** to ``mattermost@example.com``
    d. Set **SMTP Server Username** to ``[YOUR_SMTP_USERNAME]``
    e. Set **SMTP Server Password** to ``[YOUR_SMTP_PASSWORD]``
    f. Set **SMTP Server** to ``email-smtp.us-east-1.amazonaws.com``
    g. Set **SMTP Server Port** to ``465``
    h. Set **Connection Security** to ``TLS``
    i. Save the Settings

5. Click **Files > Storage** and change **Local Storage Directory** from ``./data/`` to ``/opt/mattermost/data``

6. Click **General > Logging** and set **Output logs to console** to ``false``

7. Feel free to modify other settings.
8. Restart the Mattermost Service.

  On Ubuntu 14.04 and RHEL 6.6: ``sudo service mattermost restart``
  
  On Ubuntu 16.04 and RHEL 7.1: ``sudo systemctl restart mattermost``
